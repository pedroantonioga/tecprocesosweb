/* Búsqueda del sitio (client-side, sin servidor).
   Usa window.BUSQUEDA_INDICE (definido en assets/js/indice.js).
   Devuelve resultados aproximados con tolerancia a errores de tecleo. */
(function () {
  'use strict';
  var INDICE = window.BUSQUEDA_INDICE || [];

  var overlay = document.getElementById('busqueda');
  var input = document.getElementById('busqueda-input');
  var caja = document.getElementById('busqueda-resultados');
  var btnAbrir = document.querySelector('.btn-busqueda');
  var btnCerrar = document.getElementById('busqueda-cerrar');
  if (!overlay || !input || !caja || !btnAbrir) return;

  // Normaliza: minúsculas, sin tildes, sin signos.
  function norm(s) {
    return (s || '').toLowerCase().normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '')
      .replace(/[^a-z0-9ñ ]+/g, ' ')
      .replace(/\s+/g, ' ').trim();
  }

  // Distancia de edición acotada (para tolerar erratas en palabras cortas).
  function lev(a, b) {
    if (a === b) return 0;
    var la = a.length, lb = b.length;
    if (Math.abs(la - lb) > 2) return 3;
    var prev = [], cur = [], i, j;
    for (j = 0; j <= lb; j++) prev[j] = j;
    for (i = 1; i <= la; i++) {
      cur[0] = i;
      for (j = 1; j <= lb; j++) {
        var cost = a.charAt(i - 1) === b.charAt(j - 1) ? 0 : 1;
        cur[j] = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + cost);
      }
      for (j = 0; j <= lb; j++) prev[j] = cur[j];
    }
    return prev[lb];
  }

  // Precalcula versiones normalizadas del índice.
  var IDX = INDICE.map(function (e) {
    var tn = norm(e.t);
    return { e: e, tn: tn, xn: norm(e.x), sn: norm(e.s), tw: tn.split(' ') };
  });

  function puntuar(entrada, tokens) {
    var sc = 0, hits = 0, k, t, best, w;
    for (k = 0; k < tokens.length; k++) {
      t = tokens[k];
      if (t.length < 2) continue;
      best = 0;
      if (entrada.tn.indexOf(t) !== -1) best = Math.max(best, 6);
      else {
        for (w = 0; w < entrada.tw.length; w++) {
          var pal = entrada.tw[w];
          if (pal === t) { best = Math.max(best, 6); break; }
          if (pal.length >= 3 && pal.indexOf(t) === 0) best = Math.max(best, 4);
          else if (t.length >= 4 && lev(pal, t) <= 1) best = Math.max(best, 3);
        }
      }
      if (entrada.xn.indexOf(t) !== -1) best = Math.max(best, 3);
      if (entrada.sn.indexOf(t) !== -1) best = Math.max(best, 1.5);
      if (best > 0) hits++;
      sc += best;
    }
    if (hits === 0) return 0;
    if (hits === tokens.length) sc += 3;          // todas las palabras aparecen
    if (entrada.e.u.indexOf('#') === -1) sc += 0.5; // leve preferencia a la página principal
    return sc;
  }

  function fragmento(texto, tokens) {
    var tn = norm(texto), pos = -1, k;
    for (k = 0; k < tokens.length && pos < 0; k++) pos = tn.indexOf(tokens[k]);
    var ini = pos > 40 ? pos - 40 : 0;
    var frag = texto.slice(ini, ini + 150).trim();
    return (ini > 0 ? '… ' : '') + frag + (texto.length > ini + 150 ? ' …' : '');
  }

  function buscar(q) {
    var tokens = norm(q).split(' ').filter(function (t) { return t.length >= 2; });
    if (!tokens.length) return [];
    var res = [];
    for (var i = 0; i < IDX.length; i++) {
      var sc = puntuar(IDX[i], tokens);
      if (sc > 0) res.push({ e: IDX[i].e, sc: sc });
    }
    res.sort(function (a, b) { return b.sc - a.sc; });
    return res.slice(0, 8);
  }

  function escapar(s) {
    return s.replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  function pintar(q) {
    var tokens = norm(q).split(' ').filter(function (t) { return t.length >= 2; });
    if (!tokens.length) {
      caja.innerHTML = '<p class="busqueda-vacia">Escriba una o más palabras para buscar en todo el sitio.</p>';
      return;
    }
    var r = buscar(q);
    if (!r.length) {
      caja.innerHTML = '<p class="busqueda-vacia">No se encontraron resultados para <strong>' +
        escapar(q) + '</strong>. Intente con otras palabras.</p>';
      return;
    }
    var html = '<ul class="busqueda-lista">';
    for (var i = 0; i < r.length; i++) {
      var e = r[i].e;
      html += '<li><a href="' + e.u + '">' +
        '<span class="br-tit">' + escapar(e.t) + '</span>' +
        (e.s ? '<span class="br-sec">' + escapar(e.s) + '</span>' : '') +
        '<span class="br-frag">' + escapar(fragmento(e.x, tokens)) + '</span>' +
        '</a></li>';
    }
    html += '</ul>';
    caja.innerHTML = html;
  }

  function abrir() {
    overlay.hidden = false;
    document.body.style.overflow = 'hidden';
    setTimeout(function () { input.focus(); }, 30);
    if (!input.value) pintar('');
  }
  function cerrar() {
    overlay.hidden = true;
    document.body.style.overflow = '';
    btnAbrir.focus();
  }

  btnAbrir.addEventListener('click', abrir);
  if (btnCerrar) btnCerrar.addEventListener('click', cerrar);
  overlay.addEventListener('click', function (ev) { if (ev.target === overlay) cerrar(); });
  document.addEventListener('keydown', function (ev) {
    if (ev.key === 'Escape' && !overlay.hidden) cerrar();
  });

  var temporiz;
  input.addEventListener('input', function () {
    clearTimeout(temporiz);
    var q = input.value;
    temporiz = setTimeout(function () { pintar(q); }, 120);
  });
  input.addEventListener('keydown', function (ev) {
    if (ev.key === 'Enter') {
      var primero = caja.querySelector('.busqueda-lista a');
      if (primero) window.location.href = primero.getAttribute('href');
    }
  });
})();
