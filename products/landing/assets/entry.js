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
        }).join(' ');
      }
    });

    steps.forEach(function (s) {
      var why = s.querySelector('.why');
      if (!why) return;
      var b = document.createElement('button');
      b.type = 'button'; b.className = 'whybtn'; b.textContent = 'Why?';
      b.addEventListener('click', function () {
        var open = why.classList.toggle('open');
        b.textContent = open ? 'Hide explanation' : 'Why?';
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
      '<div class="stepper-track"></div>' +
      '<button type="button" class="back">Back</button>' +
      '<button type="button" class="next">Next step</button>' +
      '<span class="count"></span>' +
      '<button type="button" class="exit">Show the whole page again</button>';

    var stepper = nav.querySelector('.stepper-track');
    for (var p = 0; p < steps.length; p++) {
      var pip = document.createElement('span');
      pip.className = 'stepper-pip';
      stepper.appendChild(pip);
    }

    var done = document.createElement('div');
    done.className = 'done';
    var source = new URLSearchParams(window.location.search).get('from');
    var params = new URLSearchParams(window.location.search);
    var resuming = params.get('resume') === '1';
    var completionQuery = [];
    if (/^[a-z0-9-]{1,40}$/.test(source || '')) completionQuery.push('from=' + encodeURIComponent(source));
    // Which path the reader took, so completions can be compared (ADR-021).
    if (root.getAttribute('data-defer') === 'on') completionQuery.push('path=' + (resuming ? 'appointment' : 'now'));
    if (completionQuery.length) completionUrl += '?' + completionQuery.join('&');
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
      var pips = stepper.querySelectorAll('.stepper-pip');
      for (var pIdx = 0; pIdx < pips.length; pIdx++) {
        pips[pIdx].classList.toggle('complete', pIdx < i);
        pips[pIdx].classList.toggle('active', pIdx === i);
      }
      nav.style.display = end ? 'none' : '';
      window.scrollTo(0, 0);
    }
    function startAt(n) { body.classList.add('doing'); show(n); }
    function start() { startAt(0); }
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

    // Deferred appointment (ADR-021): a reader who can't act where they are
    // picks an exact date and time, gets a calendar invite, and comes back to
    // the steps. Nothing is stored or sent; the reminder lives in their calendar.
    if (root.getAttribute('data-defer') === 'on') deferred();

    function deferred() {
      var MAX_MOVES = 2;
      var minutes = parseInt(root.getAttribute('data-minutes'), 10) || 40;
      var task = root.getAttribute('data-task') || document.title;
      var moved = Math.min(parseInt(params.get('moved'), 10) || 0, MAX_MOVES);
      var firstAtHome = 0;
      while (firstAtHome < steps.length && steps[firstAtHome].hasAttribute('data-portable')) firstAtHome++;
      if (firstAtHome >= steps.length) firstAtHome = 0;
      var fork = document.querySelector('.fork');
      var goLater = document.querySelector('.go-later');
      if (!fork || !goLater) return;

      function esc(t) {
        return String(t).replace(/[&<>"]/g, function (c) {
          return {'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;'}[c];
        });
      }
      function returnUrl(moves) {
        var q = ['resume=1'];
        if (moves) q.push('moved=' + moves);
        if (/^[a-z0-9-]{1,40}$/.test(source || '')) q.push('from=' + encodeURIComponent(source));
        return location.origin + location.pathname + '?' + q.join('&');
      }
      function at(d, h, m) { var x = new Date(d); x.setHours(h, m, 0, 0); return x; }
      function nextDay(dow, h, m) {
        var now = new Date(), x = at(now, h, m);
        var add = (dow - now.getDay() + 7) % 7;
        x.setDate(x.getDate() + add);
        if (x <= now) x.setDate(x.getDate() + 7);
        return x;
      }
      function choices() {
        var now = new Date(), list = [];
        var tonight = at(now, 19, 0);
        if (tonight - now < 30 * 60000) tonight = at(now, 20, 30);
        if (tonight - now >= 30 * 60000) list.push(['Tonight', tonight]);
        var tomorrow = at(now, 19, 0); tomorrow.setDate(tomorrow.getDate() + 1);
        list.push(['Tomorrow evening', tomorrow]);
        list.push(['Saturday morning', nextDay(6, 10, 0)]);
        list.push(['Monday evening', nextDay(1, 19, 0)]);
        var seen = {};
        return list.filter(function (c) {
          var k = c[1].getTime(); if (seen[k]) return false; seen[k] = 1; return true;
        });
      }
      function label(d) {
        return d.toLocaleString('en-US', {weekday: 'long', month: 'short', day: 'numeric',
          hour: 'numeric', minute: '2-digit'});
      }
      function stamp(d) { return d.toISOString().replace(/[-:]/g, '').replace(/\.\d{3}/, ''); }
      function icsText(t) { return String(t).replace(/\\/g, '\\\\').replace(/[,;]/g, '\\$&').replace(/\n/g, '\\n'); }
      function fold(line) {
        var out = [];
        while (line.length > 73) { out.push(line.slice(0, 73)); line = ' ' + line.slice(73); }
        out.push(line); return out.join('\r\n');
      }
      function invite(when, url) {
        var end = new Date(when.getTime() + minutes * 60000);
        var details = 'Time to start. Open this and pick up at the next step:\n' + url;
        var lines = ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:-//Mr. Life Manager//Appointment//EN',
          'CALSCALE:GREGORIAN', 'METHOD:PUBLISH', 'BEGIN:VEVENT',
          'UID:' + Date.now() + '-' + Math.random().toString(36).slice(2) + '@mrlifemanager.com',
          'DTSTAMP:' + stamp(new Date()), 'DTSTART:' + stamp(when), 'DTEND:' + stamp(end),
          'SUMMARY:' + icsText(task), 'DESCRIPTION:' + icsText(details), 'URL:' + url,
          'BEGIN:VALARM', 'ACTION:DISPLAY', 'DESCRIPTION:' + icsText(task), 'TRIGGER:-PT0M', 'END:VALARM',
          'END:VEVENT', 'END:VCALENDAR'];
        return lines.map(fold).join('\r\n') + '\r\n';
      }
      function googleUrl(when, url) {
        var end = new Date(when.getTime() + minutes * 60000);
        return 'https://calendar.google.com/calendar/render?action=TEMPLATE' +
          '&text=' + encodeURIComponent(task) +
          '&dates=' + stamp(when) + '/' + stamp(end) +
          '&details=' + encodeURIComponent('Time to start. Open this and pick up at the next step: ' + url);
      }

      // Panel shown after "Not right now".
      var later = document.createElement('section');
      later.className = 'later';
      later.hidden = true;
      var portable = steps.filter(function (s) { return s.hasAttribute('data-portable'); });
      var portableHtml = '';
      if (portable.length) {
        portableHtml = '<div class="later-now"><h2>Do this part now, from right here.</h2><ol>' +
          portable.map(function (s) {
            var h = s.querySelector('.step-head h2'), d = s.querySelector('.do');
            return '<li><b>' + (h ? h.innerHTML : '') + '</b> ' + (d ? d.innerHTML : '') + '</li>';
          }).join('') + '</ol><p>Done? Now pick the time for the rest.</p></div>';
      }
      later.innerHTML = portableHtml +
        '<h2>When will you do it?</h2>' +
        '<p class="later-sub">Pick a day and a time. \u201cLater\u201d isn\u2019t a time.</p>' +
        '<div class="when-picks"></div>' +
        '<p class="when-own"><label>Or pick your own: <input type="datetime-local" class="when-input"></label> ' +
        '<button type="button" class="when-use">Use this time</button></p>' +
        '<div class="decided" hidden></div>';
      fork.parentNode.insertBefore(later, fork.nextSibling);

      var picks = later.querySelector('.when-picks');
      choices().forEach(function (c) {
        var b = document.createElement('button');
        b.type = 'button';
        b.innerHTML = '<span class="when-name">' + c[0] + '</span><span class="when-time">' +
          esc(label(c[1])) + '</span>';
        b.addEventListener('click', function () { decide(c[1]); });
        picks.appendChild(b);
      });
      later.querySelector('.when-use').addEventListener('click', function () {
        var v = later.querySelector('.when-input').value;
        var d = v ? new Date(v) : null;
        if (!d || isNaN(d) || d <= new Date()) { later.querySelector('.when-input').focus(); return; }
        decide(d);
      });

      function decide(when) {
        var url = returnUrl(moved);
        var box = later.querySelector('.decided');
        var href = 'data:text/calendar;charset=utf-8,' + encodeURIComponent(invite(when, url));
        box.innerHTML = '<h2>That\u2019s decided.</h2>' +
          '<p class="decided-when">' + esc(label(when)) + '</p>' +
          '<p>Put it on your calendar now, so it comes back to you at that time with the steps ready.</p>' +
          '<p class="decided-btns">' +
          '<a class="cal-ics" download="mr-life-manager.ics" href="' + href + '">Add to my calendar</a>' +
          '<a class="cal-google" target="_blank" rel="noopener" href="' + googleUrl(when, url) + '">Google Calendar</a>' +
          '</p>' +
          '<p class="decided-share"><button type="button" class="share-checker">Send it to someone who\u2019ll check on you</button></p>' +
          '<p class="fine">Nothing is stored on this site. The reminder lives in your calendar.</p>';
        box.hidden = false;
        box.querySelector('.share-checker').addEventListener('click', function () {
          var text = 'I\u2019ve set aside ' + label(when) + ' to ' + task.charAt(0).toLowerCase() +
            task.slice(1) + '. Check on me after?';
          var page = location.origin + location.pathname;
          if (navigator.share) { navigator.share({title: task, text: text, url: page}).catch(function () {}); }
          else { location.href = 'mailto:?subject=' + encodeURIComponent(task) + '&body=' +
            encodeURIComponent(text + '\n\n' + page); }
        });
        box.scrollIntoView({block: 'start'});
      }

      function openLater() { later.hidden = false; later.scrollIntoView({block: 'start'}); }
      goLater.addEventListener('click', openLater);

      // Coming back from the calendar invite.
      if (!resuming) return;
      var card = document.createElement('section');
      card.className = 'resume';
      var where = firstAtHome ? 'Step ' + (firstAtHome + 1) + ' is ready.' : 'Step one is ready.';
      if (moved >= MAX_MOVES) {
        card.innerHTML = '<h2>This is the time you picked.</h2>' +
          '<p>You\u2019ve moved it twice already. Either start now, or let this one go.</p>' +
          '<p class="resume-btns"><button type="button" class="resume-start">Start now</button>' +
          '<button type="button" class="resume-drop">Let it go</button></p>';
      } else {
        card.innerHTML = '<h2>This is the time you picked.</h2>' +
          '<p>' + minutes + ' minutes, set aside for this. ' + where + '</p>' +
          '<p class="resume-btns"><button type="button" class="resume-start">Start</button>' +
          '<button type="button" class="resume-move">I can\u2019t right now</button></p>';
      }
      var top = document.querySelector('header.top');
      top.parentNode.insertBefore(card, top.nextSibling);
      card.querySelector('.resume-start').addEventListener('click', function () { startAt(firstAtHome); });
      var move = card.querySelector('.resume-move');
      if (move) move.addEventListener('click', function () {
        moved += 1;
        card.hidden = true;
        openLater();
      });
      var drop = card.querySelector('.resume-drop');
      if (drop) drop.addEventListener('click', function () {
        card.innerHTML = '<h2>Okay. It\u2019s let go.</h2>' +
          '<p>No more reminders will come from this. If it comes back to you, this page will still be here.</p>';
      });
    }
  })();
})();
