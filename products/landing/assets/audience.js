/* Audience landing pages: color-scheme switcher and QR source tag.
   The page's buttons carry data-look-pick="<family>-<scheme>"; the choice is
   kept on the door links (?look=) so the checklist and finish page match,
   and in this page's URL so a shared link opens in the same colors.
   Umami counts picks through the buttons' data-umami-event attributes. */
(function () {
  var root = document.documentElement;
  var picks = Array.prototype.slice.call(document.querySelectorAll('[data-look-pick]'));
  var allowed = picks.map(function (b) { return b.getAttribute('data-look-pick'); });
  var params = new URLSearchParams(location.search);
  var from = params.get('from') || '';
  if (!/^[a-z0-9-]{1,40}$/.test(from)) from = '';

  function apply(look) {
    root.setAttribute('data-look', look);
    picks.forEach(function (b) {
      b.setAttribute('aria-pressed', String(b.getAttribute('data-look-pick') === look));
    });
    Array.prototype.forEach.call(document.querySelectorAll('a.door'), function (a) {
      var u = new URL(a.getAttribute('href'), location.origin);
      u.searchParams.set('look', look);
      if (from) u.searchParams.set('from', from);
      a.setAttribute('href', u.pathname + u.search);
    });
  }

  var start = params.get('look');
  apply(allowed.indexOf(start) >= 0 ? start : root.getAttribute('data-look'));
  picks.forEach(function (b) {
    b.addEventListener('click', function () {
      var look = b.getAttribute('data-look-pick');
      apply(look);
      var u = new URL(location.href);
      u.searchParams.set('look', look);
      history.replaceState(null, '', u.pathname + u.search + u.hash);
    });
  });
})();
