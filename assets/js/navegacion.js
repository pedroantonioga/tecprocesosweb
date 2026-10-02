/* Navegación: menú móvil accesible y desplegables por toque.
   Sin dependencias externas. */
(function () {
  'use strict';
  var btn = document.querySelector('.btn-menu');
  var nav = document.querySelector('.nav-principal');

  if (btn && nav) {
    btn.addEventListener('click', function () {
      var abierto = nav.classList.toggle('abierto');
      btn.setAttribute('aria-expanded', abierto ? 'true' : 'false');
      document.body.style.overflow = abierto ? 'hidden' : '';
    });
  }

  /* En móvil, el enlace de una categoría con desplegable abre/cierra su submenú */
  var items = document.querySelectorAll('.nav-item');
  items.forEach(function (item) {
    var enlace = item.querySelector('.nav-enlace');
    var drop = item.querySelector('.nav-drop');
    if (!drop || !enlace) return;
    enlace.addEventListener('click', function (e) {
      if (window.matchMedia('(max-width:980px)').matches) {
        e.preventDefault();
        var abierto = item.classList.toggle('desplegado');
        enlace.setAttribute('aria-expanded', abierto ? 'true' : 'false');
      }
    });
  });

  /* Cerrar menú móvil al pasar a escritorio */
  window.addEventListener('resize', function () {
    if (!window.matchMedia('(max-width:980px)').matches && nav) {
      nav.classList.remove('abierto');
      document.body.style.overflow = '';
      if (btn) btn.setAttribute('aria-expanded', 'false');
    }
  });

  /* Resaltar la sección activa del índice lateral al desplazar */
  var enlacesIndice = document.querySelectorAll('.tarjeta-lateral .indice a[href^="#"]');
  if (enlacesIndice.length) {
    var objetivos = [];
    enlacesIndice.forEach(function (a) {
      var el = document.getElementById(a.getAttribute('href').slice(1));
      if (el) objetivos.push({ a: a, el: el });
    });
    var marcar = function () {
      var y = window.scrollY + 140;
      var activo = objetivos[0];
      objetivos.forEach(function (o) { if (o.el.offsetTop <= y) activo = o; });
      enlacesIndice.forEach(function (a) { a.classList.remove('activo'); });
      if (activo) activo.a.classList.add('activo');
    };
    window.addEventListener('scroll', marcar, { passive: true });
    marcar();
  }
})();
