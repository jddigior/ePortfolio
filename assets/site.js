(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  // Hero balloons and legend highlight each other
  $$('[data-b]').forEach(function (el) {
    var n = el.getAttribute('data-b');
    var on = function () { $$('[data-b="' + n + '"]').forEach(function (x) { x.classList.add('hl'); }); };
    var off = function () { $$('[data-b="' + n + '"]').forEach(function (x) { x.classList.remove('hl'); }); };
    el.addEventListener('mouseenter', on); el.addEventListener('mouseleave', off);
    el.addEventListener('focus', on); el.addEventListener('blur', off);
  });

  // Project index preview
  var pvs = $$('.pv');
  if (pvs.length) {
    var rows = $$('.row');
    var show = function (i) {
      pvs.forEach(function (p) { p.classList.toggle('on', p.getAttribute('data-i') === i); });
      rows.forEach(function (r) { r.classList.toggle('on', r.getAttribute('data-i') === i); });
    };
    rows.forEach(function (r) {
      var i = r.getAttribute('data-i');
      r.addEventListener('mouseenter', function () { show(i); });
      r.addEventListener('focus', function () { show(i); });
    });
    show('0');
  }

  // Axon subsystem explorer
  var subs = $$('.sub');
  if (subs.length) {
    var pick = function (n, scroll) {
      subs.forEach(function (s) { s.classList.toggle('on', s.getAttribute('data-sub') === n); });
      $$('.tab').forEach(function (t) { t.setAttribute('aria-selected', t.getAttribute('data-sub') === n ? 'true' : 'false'); });
      $$('.spot').forEach(function (t) { t.classList.toggle('on', t.getAttribute('data-sub') === n); });
      if (scroll && window.innerWidth < 900) { $('.ex-panels').scrollIntoView({ block: 'start' }); }
    };
    $$('.tab, .spot').forEach(function (b) {
      b.addEventListener('click', function () {
        var n = b.getAttribute('data-sub');
        pick(n, true);
        if (history.replaceState) history.replaceState(null, '', '#sub-' + n);
      });
    });
    $$('.tab').forEach(function (t, i, all) {
      t.addEventListener('keydown', function (e) {
        var d = e.key === 'ArrowDown' || e.key === 'ArrowRight' ? 1 : e.key === 'ArrowUp' || e.key === 'ArrowLeft' ? -1 : 0;
        if (!d) return;
        e.preventDefault();
        var next = all[(i + d + all.length) % all.length];
        next.focus(); next.click();
      });
    });
    var m = location.hash.match(/^#sub-(\d)$/);
    pick(m ? m[1] : '1', false);
    if (m) { window.addEventListener('load', function () { $('#subsystems').scrollIntoView(); }); }
  }

  // Lightbox for figures
  var lb = $('.lightbox');
  var zooms = $$('a.zoom');
  if (lb && zooms.length && lb.showModal) {
    var lbImg = $('img', lb), lbCap = $('figcaption', lb), cur = 0;
    var open = function (i) {
      cur = (i + zooms.length) % zooms.length;
      var a = zooms[cur];
      lbImg.src = a.getAttribute('href');
      lbImg.alt = ($('img', a) || {}).alt || '';
      lbCap.textContent = (a.getAttribute('data-caption') || '').replace(' Click to enlarge.', '');
      if (!lb.open) lb.showModal();
    };
    zooms.forEach(function (a, i) {
      a.addEventListener('click', function (e) { e.preventDefault(); open(i); });
    });
    var single = zooms.length < 2;
    $('.lb-prev', lb).hidden = single; $('.lb-next', lb).hidden = single;
    $('.lb-prev', lb).addEventListener('click', function () { open(cur - 1); });
    $('.lb-next', lb).addEventListener('click', function () { open(cur + 1); });
    $('.lb-close', lb).addEventListener('click', function () { lb.close(); });
    lb.addEventListener('click', function (e) { if (e.target === lb || e.target.tagName === 'FIGURE') lb.close(); });
    lb.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') open(cur + 1);
      if (e.key === 'ArrowLeft') open(cur - 1);
    });
    lb.addEventListener('close', function () { lbImg.removeAttribute('src'); });
  }
})();
