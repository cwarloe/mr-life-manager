/* Shared entry-page behavior: doing-mode + MailerLite tag/fallback.
   Per-page config via <html data-guide="…" data-completion-url="…">. */
(function () {
  var root = document.documentElement;
  var guide = root.getAttribute('data-guide') || '';
  var completionUrl = root.getAttribute('data-completion-url') || '';

  // Ad blockers often leave the embed empty — reveal mailto fallback if so.
  addEventListener('load', function () {
    setTimeout(function () {
      document.querySelectorAll('.signup').forEach(function (box) {
        var embed = box.querySelector('.ml-embedded');
        var fb = box.querySelector('.ml-fallback');
        if (embed && fb && embed.children.length === 0) fb.hidden = false;
      });
    }, 2500);
  });

  // ADR-015 — tag signup with the door they entered. Send both field names;
  // MailerLite accepts the one the form expects and ignores the other.
  if (guide) {
    (function () {
      var VALUE = guide;
      function tag(form) {
        ['fields[guide]', 'guide'].forEach(function (name) {
          if (form.querySelector('input[name="' + name + '"]')) return;
          var i = document.createElement('input');
          i.type = 'hidden'; i.name = name; i.value = VALUE;
          form.appendChild(i);
        });
      }
      var tries = 0;
      var t = setInterval(function () {
        var forms = document.querySelectorAll('.ml-embedded form');
        if (forms.length) { forms.forEach(tag); clearInterval(t); }
        if (++tries > 40) clearInterval(t);
      }, 250);
    })();
  }

  // Doing mode: one step at a time; why hidden until tapped; gone in print.
  (function () {
    var body = document.body;
    var steps = Array.prototype.slice.call(document.querySelectorAll('.step'));
    if (!steps.length) return;
    var i = 0;

    // Split .do into one sentence per line so looking up mid-step is easy.
    steps.forEach(function (s) {
      var d = s.querySelector('.do');
      if (!d || d.dataset.split) return;
      d.dataset.split = '1';
      var parts = d.innerHTML.split(/(?<=[.!?])\s+(?=[A-Z])/);
      if (parts.length > 1) {
        d.innerHTML = parts.map(function (t) {
          return '<span class="s">' + t + '</span>';
        }).join('');
      }
    });

    steps.forEach(function (s) {
      var why = s.querySelector('.why');
      if (!why) return;
      var b = document.createElement('button');
      b.type = 'button'; b.className = 'whybtn'; b.textContent = 'Why?';
      b.addEventListener('click', function () {
        var open = why.classList.toggle('open');
        b.textContent = open ? 'Hide' : 'Why?';
      });
      why.parentNode.insertBefore(b, why);
    });

    steps.forEach(function (s, k) {
      var head = s.querySelector('.step-head');
      if (head) head.setAttribute('data-n', k + 1);
    });

    var nav = document.createElement('div');
    nav.className = 'nav';
    nav.innerHTML =
      '<button type="button" class="back">Back</button>' +
      '<button type="button" class="next">Next step</button>' +
      '<span class="count"></span>' +
      '<button type="button" class="exit">Show the whole page again</button>';
    var done = document.createElement('div');
    done.className = 'done';
    var source = new URLSearchParams(window.location.search).get('from');
    if (/^[a-z0-9-]{1,40}$/.test(source || '')) completionUrl += '?from=' + encodeURIComponent(source);
    done.innerHTML = '<h2>That\u2019s everything.</h2>' +
      '<p>Whatever you got through is what there was time for. The order runs biggest ' +
      'difference first, so wherever you stopped is the right place to have stopped.</p>' +
      '<a class="complete" href="' + completionUrl + '">I finished \u2014 what\u2019s next?</a>' +
      '<button type="button" class="exit">Show the whole page again</button>';
    var list = document.querySelector('.steps');
    list.parentNode.insertBefore(nav, list.nextSibling);
    nav.parentNode.insertBefore(done, nav);

    function show(n) {
      i = n;
      steps.forEach(function (s, k) { s.classList.toggle('current', k === i); });
      var end = i >= steps.length;
      done.classList.toggle('show', end);
      nav.querySelector('.next').textContent = i === steps.length - 1 ? 'Done' : 'Next step';
      nav.querySelector('.back').disabled = i === 0;
      nav.querySelector('.count').textContent = end ? '' : (i + 1) + ' of ' + steps.length;
      nav.style.display = end ? 'none' : '';
      window.scrollTo(0, 0);
    }
    function start() { body.classList.add('doing'); show(0); }
    function stop() {
      body.classList.remove('doing');
      steps.forEach(function (s) { s.classList.remove('current'); });
      done.classList.remove('show');
      document.querySelector('.fork').scrollIntoView({block: 'center'});
    }

    var goDo = document.querySelector('.go-do');
    var goPrint = document.querySelector('.go-print');
    if (goDo) goDo.addEventListener('click', start);
    if (goPrint) goPrint.addEventListener('click', function () { window.print(); });
    nav.querySelector('.next').addEventListener('click', function () { show(i + 1); });
    nav.querySelector('.back').addEventListener('click', function () { show(i - 1); });
    Array.prototype.forEach.call(document.querySelectorAll('.exit'), function (b) {
      b.addEventListener('click', stop);
    });
  })();
})();
