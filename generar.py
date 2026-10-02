# -*- coding: utf-8 -*-
"""
Generador del sitio web del Programa de Tecnología en Procesos Industriales (UFPS).
Produce archivos HTML estáticos con encabezado, pie y estilos compartidos.
Ejecutar:  python3 generar.py
"""
import os

RAIZ = os.path.dirname(os.path.abspath(__file__))

# --------------------------------------------------------------------------
# DATOS DEL PROGRAMA (verificar y completar donde se indique)
# --------------------------------------------------------------------------
D = {
    "programa": "Tecnología en Procesos Industriales",
    "titulo": "Tecnólogo(a) en Procesos Industriales",
    "duracion": "6 semestres",
    "modalidad": "Presencial (Diurna)",
    "snies": "52956",
    "creditos": "103",
    "registro": "Resolución MEN 021555 de 2021",
    "coordinador": "Pedro Antonio Garzón Agudelo",
    "correo": "tecprocesos@ufps.edu.co",
    "tel": "(607) 5776655 Ext. 120",
    "ubicacion": "Edificio Fundadores 108",
    "direccion": "Avenida Gran Colombia No. 12E-96, Barrio Colsag, Cúcuta, Colombia",
    "web": "www.ufps.edu.co",
    "instagram": "https://www.instagram.com/tecprocesos_ufps/",
    "facebook": "https://www.facebook.com/Tecprocesosufps",
}

# --------------------------------------------------------------------------
# ESTRUCTURA DE NAVEGACIÓN (tal cual el mapa del sitio)
# --------------------------------------------------------------------------
NAV = [
    ("Institucional", "institucional.html", [
        ("Normatividad", "institucional-normatividad.html", [
            ("Calendario Académico", "https://ww2.ufps.edu.co/public/archivos/calendarios/14b1b7721b0736c5b89b53e8b320f5b3.pdf"),
            ("Compilación de normas de interés", "https://ww2.ufps.edu.co/universidad/normatividad"),
            ("Estatuto Estudiantil", "https://ww2.ufps.edu.co/public/archivos/reglamentacion/6d04e1c9b1244df469317023a7699ce6.pdf"),
            ("Protocolo para salidas académicas", "institucional-reglamento-salidas.html"),
            ("Resolución Registro Calificado", "documentos/resolucion-021555-2021-registro-calificado.pdf"),
        ]),
        ("Trámites", "institucional-tramites.html", [
            ("Trámites estudiantiles", "institucional-tramites.html#estudiantiles"),
            ("Trámites de graduados", "institucional-tramites.html#graduados"),
        ]),
        ("Autoevaluación", "institucional-autoevaluacion.html", [
            ("Informes de autoevaluación del programa", "institucional-autoevaluacion.html#informes"),
        ]),
        ("Formatos y descargas", "institucional-formatos-descargas.html", []),
    ]),
    ("El Programa", "el-programa.html", [
        ("Historia", "el-programa-historia.html", []),
        ("Registro Calificado", "el-programa-registro-calificado.html", []),
        ("Proyecto Educativo (PEP)", "el-programa-pep.html", [
            ("Misión", "el-programa-pep.html#mision"),
            ("Visión", "el-programa-pep.html#vision"),
            ("Líneas de Profundización", "el-programa-pep.html#lineas"),
            ("Competencias", "el-programa-pep.html#competencias"),
            ("Resultados de Aprendizaje", "el-programa-pep.html#resultados"),
        ]),
        ("Plan de Estudios", "el-programa-plan-de-estudios.html", []),
        ("Malla curricular", "el-programa-malla-curricular.html", []),
        ("Perfil de Ingreso", "el-programa-perfil-de-ingreso.html", []),
        ("Perfiles de egreso", "el-programa-perfiles-de-egreso.html", [
            ("Perfil profesional", "el-programa-perfiles-de-egreso.html#profesional"),
            ("Perfil ocupacional", "el-programa-perfiles-de-egreso.html#ocupacional"),
        ]),
        ("Trabajos de grado", "el-programa-trabajos-de-grado.html", [
            ("Modalidades", "el-programa-trabajos-de-grado.html#modalidades"),
            ("Reglamento de trabajos de grado", "el-programa-trabajos-de-grado.html#reglamento"),
            ("Requisitos del trabajo de grado", "el-programa-trabajos-de-grado.html#requisitos"),
            ("Formatos y plantillas", "el-programa-trabajos-de-grado.html#formatos"),
            ("Banco de posibles directores", "el-programa-trabajos-de-grado.html#directores"),
            ("Banco de trabajos de grado", "el-programa-trabajos-de-grado.html#banco"),
            ("Memorias de sensibilizaciones", "el-programa-trabajos-de-grado.html#memorias"),
        ]),
        ("Investigación", "el-programa-investigacion.html", [
            ("Grupos de Investigación", "el-programa-investigacion.html#grupos"),
            ("Semilleros de Investigación", "el-programa-investigacion.html#semilleros"),
            ("Investigadores categorizados", "el-programa-investigacion.html#investigadores"),
            ("Líneas y proyectos de impacto", "el-programa-investigacion.html#lineas-proyectos"),
            ("Publicaciones", "el-programa-investigacion.html#publicaciones"),
            ("Memorias de eventos", "el-programa-investigacion.html#memorias-eventos"),
        ]),
    ]),
    ("Comunidad", "comunidad.html", [
        ("Consejo Estudiantil y ANEIAP", "comunidad-consejo-aneiap.html", []),
        ("Redes sociales del programa", "comunidad-redes-sociales.html", []),
        ("Equipo de Trabajo", "comunidad-equipo-de-trabajo.html", [
            ("Comité Curricular", "comunidad-equipo-de-trabajo.html#comite"),
            ("Coordinador", "comunidad-equipo-de-trabajo.html#coordinacion"),
            ("Docentes", "comunidad-equipo-de-trabajo.html#docentes"),
            ("Administrativos", "comunidad-equipo-de-trabajo.html#administrativos"),
        ]),
        ("Graduados", "comunidad-graduados.html", [
            ("Encuentros de graduados", "comunidad-graduados.html#encuentros"),
            ("Coloquio de graduados", "comunidad-graduados.html#coloquio"),
            ("Directorio de Emprendedores", "comunidad-graduados.html#emprendedores"),
            ("Directorio de Consultores", "comunidad-graduados.html#consultores"),
        ]),
        ("Intermediación Laboral", "comunidad-intermediacion-laboral.html", [
            ("Bolsa de empleo", "comunidad-intermediacion-laboral.html#bolsa"),
        ]),
    ]),
    ("Vínculos", "vinculos.html", [
        ("Redes académicas", "vinculos-redes-academicas.html", [
            ("ACOFI / Redin", "vinculos-redes-academicas.html#acofi"),
            ("COPNIA", "vinculos-redes-academicas.html#copnia"),
            ("RedColsi", "vinculos-redes-academicas.html#redcolsi"),
        ]),
        ("Proyección social / Extensión", "vinculos-proyeccion-social.html", [
            ("Convenios", "vinculos-proyeccion-social.html#convenios"),
            ("Prácticas", "vinculos-proyeccion-social.html#practicas"),
            ("Cursos", "vinculos-proyeccion-social.html#cursos"),
            ("Movilidades", "vinculos-proyeccion-social.html#movilidades"),
            ("Eventos", "vinculos-proyeccion-social.html#eventos"),
        ]),
    ]),
]

# padre de cada slug (para resaltar la categoría activa)
PADRE = {}
for cat, cat_slug, hijos in NAV:
    PADRE[cat_slug] = cat_slug
    for h in hijos:
        PADRE[h[1]] = cat_slug

PENDIENTE = '<span class="pendiente">Información por complementar</span>'

def _es_externo(href):
    return href.startswith("http") or href.endswith(".pdf")

# --------------------------------------------------------------------------
# ENCABEZADO (mega-menú con vista previa hasta nivel 3)
# --------------------------------------------------------------------------
def header(activo):
    padre_activo = PADRE.get(activo, "")
    items = []
    for cat, cat_slug, hijos in NAV:
        aria = ' aria-current="page"' if cat_slug == padre_activo else ""
        grupos = []
        for l2 in hijos:
            l2_nom, l2_slug = l2[0], l2[1]
            l3 = l2[2] if len(l2) > 2 else []
            act2 = ' aria-current="page"' if l2_slug == activo else ""
            sub = ""
            if l3:
                lis = []
                for n3, h3 in l3:
                    ext = ' target="_blank" rel="noopener"' if _es_externo(h3) else ""
                    lis.append('<li><a href="%s"%s>%s</a></li>' % (h3, ext, n3))
                sub = '<ul class="drop-l3">%s</ul>' % "".join(lis)
            grupos.append(
                '<div class="drop-grupo"><a class="drop-l2" href="%s"%s>%s</a>%s</div>'
                % (l2_slug, act2, l2_nom, sub))
        ancho = ' nav-drop--ancho' if len(hijos) > 4 else ''
        items.append(
            '<li class="nav-item">'
            '<a class="nav-enlace" href="{cs}"{aria} aria-expanded="false" aria-haspopup="true">'
            '{cat}<span class="flecha" aria-hidden="true"></span></a>'
            '<div class="nav-drop{ancho}">{grupos}</div></li>'.format(
                cs=cat_slug, aria=aria, cat=cat, ancho=ancho, grupos="".join(grupos)))
    return (
'''<a class="marca-logo" href="index.html" aria-label="Inicio · Programa de Tecnología en Procesos Industriales, UFPS">
        <img src="assets/img/logos/ufps-programa-horizontal.png"
             alt="Universidad Francisco de Paula Santander · Programa de Tecnología en Procesos Industriales">
      </a>
      <div class="header-der">
        <nav class="nav-principal" id="menu" aria-label="Navegación principal">
          <ul class="nav-lista">
            ''' + "\n            ".join(items) + '''
          </ul>
        </nav>
        <button class="btn-busqueda" aria-label="Buscar en el sitio" aria-haspopup="dialog" aria-controls="busqueda">
          <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M10 2a8 8 0 1 0 5.29 14.01l4.35 4.35a1 1 0 0 0 1.42-1.42l-4.35-4.35A8 8 0 0 0 10 2zm0 2a6 6 0 1 1 0 12 6 6 0 0 1 0-12z"/></svg>
        </button>
        <button class="btn-menu" aria-label="Abrir menú" aria-controls="menu" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>
      </div>''')

# --------------------------------------------------------------------------
# PIE
# --------------------------------------------------------------------------
def footer():
    ig = D["instagram"]; fb = D["facebook"]
    return '''<footer class="sitio-footer">
    <div class="footer-top">
      <div class="contenedor">
        <div class="footer-grid">
          <div class="footer-marca">
            <img src="assets/img/logos/ufps-programa-horizontal.png"
                 alt="UFPS · Programa de Tecnología en Procesos Industriales">
            <p>Programa adscrito a la Facultad de Ingeniería de la Universidad Francisco
               de Paula Santander. Formación tecnológica con pertinencia regional,
               investigación aplicada y vínculo permanente con el sector productivo.</p>
          </div>
          <div class="footer-col">
            <h4>El Programa</h4>
            <ul>
              <li><a href="el-programa-historia.html">Historia</a></li>
              <li><a href="el-programa-pep.html">Proyecto Educativo</a></li>
              <li><a href="el-programa-plan-de-estudios.html">Plan de Estudios</a></li>
              <li><a href="el-programa-perfiles-de-egreso.html">Perfiles de egreso</a></li>
              <li><a href="el-programa-investigacion.html">Investigación</a></li>
            </ul>
          </div>
          <div class="footer-col">
            <h4>Servicios</h4>
            <ul>
              <li><a href="institucional-normatividad.html">Normatividad</a></li>
              <li><a href="institucional-tramites.html">Trámites</a></li>
              <li><a href="institucional-formatos-descargas.html">Formatos y descargas</a></li>
              <li><a href="vinculos-proyeccion-social.html">Prácticas y extensión</a></li>
              <li><a href="comunidad-intermediacion-laboral.html">Bolsa de empleo</a></li>
            </ul>
          </div>
          <div class="footer-col">
            <h4>Contacto</h4>
            <div class="footer-dato"><span class="k">Coordinación:</span><br>%(coord)s</div>
            <div class="footer-dato"><span class="k">Correo:</span><br><a href="mailto:%(correo)s">%(correo)s</a></div>
            <div class="footer-dato"><span class="k">Teléfono:</span><br>%(tel)s</div>
            <div class="footer-dato"><span class="k">Ubicación:</span><br>%(ubic)s</div>
          </div>
        </div>
      </div>
    </div>
    <div class="footer-base">
      <div class="contenedor">
        <div class="fila">
          <span class="legal">%(direccion)s</span>
          <div class="redes">
            <a href="%(ig)s" target="_blank" rel="noopener" aria-label="Instagram del programa">
              <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.2c3.2 0 3.6 0 4.9.07 1.17.05 1.8.25 2.23.41.56.22.96.48 1.38.9.42.42.68.82.9 1.38.16.42.36 1.06.41 2.23.06 1.27.07 1.65.07 4.86s0 3.6-.07 4.86c-.05 1.17-.25 1.8-.41 2.23-.22.56-.48.96-.9 1.38-.42.42-.82.68-1.38.9-.42.16-1.06.36-2.23.41-1.27.06-1.65.07-4.86.07s-3.6 0-4.86-.07c-1.17-.05-1.8-.25-2.23-.41-.56-.22-.96-.48-1.38-.9-.42-.42-.68-.82-.9-1.38-.16-.42-.36-1.06-.41-2.23C2.21 15.6 2.2 15.2 2.2 12s0-3.6.07-4.86c.05-1.17.25-1.8.41-2.23.22-.56.48-.96.9-1.38.42-.42.82-.68 1.38-.9.42-.16 1.06-.36 2.23-.41C8.4 2.21 8.8 2.2 12 2.2zm0 3.35A6.45 6.45 0 1 0 18.45 12 6.45 6.45 0 0 0 12 5.55zm0 10.64A4.19 4.19 0 1 1 16.19 12 4.19 4.19 0 0 1 12 16.19zm6.7-10.9a1.5 1.5 0 1 0 1.5 1.5 1.5 1.5 0 0 0-1.5-1.5z"/></svg>
            </a>
            <a href="%(fb)s" target="_blank" rel="noopener" aria-label="Facebook del programa">
              <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.5 21v-8.2h2.75l.41-3.2H13.5V7.55c0-.93.26-1.56 1.59-1.56h1.7V3.13A22.7 22.7 0 0 0 14.3 3c-2.46 0-4.15 1.5-4.15 4.26v2.38H7.4v3.2h2.75V21z"/></svg>
            </a>
            <a href="https://%(web)s" target="_blank" rel="noopener" aria-label="Sitio web UFPS">
              <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm6.9 6h-2.6a15.6 15.6 0 0 0-1.1-3.03A8 8 0 0 1 18.9 8zM12 4c.7 0 1.6 1.4 2.1 4H9.9C10.4 5.4 11.3 4 12 4zM4.3 14a7.9 7.9 0 0 1 0-4h3a20.7 20.7 0 0 0 0 4zm.8 2h2.6a15.6 15.6 0 0 0 1.1 3.03A8 8 0 0 1 5.1 16zm2.6-8H5.1a8 8 0 0 1 3.7-3.03A15.6 15.6 0 0 0 7.7 8zM12 20c-.7 0-1.6-1.4-2.1-4h4.2c-.5 2.6-1.4 4-2.1 4zm2.4-6H9.6a18.4 18.4 0 0 1 0-4h4.8a18.4 18.4 0 0 1 0 4zm.3 5.03A15.6 15.6 0 0 0 15.7 16h2.6a8 8 0 0 1-3.6 3.03zM17 14a20.7 20.7 0 0 0 0-4h3a7.9 7.9 0 0 1 0 4z"/></svg>
            </a>
          </div>
          <span class="footer-mas">Más información en <a href="https://%(web)s" target="_blank" rel="noopener">%(web)s</a></span>
        </div>
      </div>
    </div>
  </footer>''' % {
        "coord": D["coordinador"], "correo": D["correo"], "tel": D["tel"],
        "ubic": D["ubicacion"], "direccion": D["direccion"],
        "ig": ig, "fb": fb, "web": D["web"]}

# --------------------------------------------------------------------------
# PLANTILLA DE PÁGINA
# --------------------------------------------------------------------------
def pagina(slug, title, cuerpo, desc=""):
    html = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>%(title)s · Tecnología en Procesos Industriales · UFPS</title>
  <meta name="description" content="%(desc)s">
  <link rel="icon" type="image/png" href="assets/img/logos/favicon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700;800&family=Open+Sans:wght@400;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/estilos.css">
</head>
<body>
  <div class="barra-marca"></div>
  <header class="sitio-header">
    <div class="contenedor header-fila">
      %(header)s
    </div>
  </header>

  <div class="busqueda-overlay" id="busqueda" hidden>
    <div class="busqueda-panel" role="dialog" aria-modal="true" aria-label="Buscar en el sitio">
      <div class="busqueda-barra">
        <svg class="busqueda-lupa" viewBox="0 0 24 24" aria-hidden="true"><path d="M10 2a8 8 0 1 0 5.29 14.01l4.35 4.35a1 1 0 0 0 1.42-1.42l-4.35-4.35A8 8 0 0 0 10 2zm0 2a6 6 0 1 1 0 12 6 6 0 0 1 0-12z"/></svg>
        <input type="search" id="busqueda-input" placeholder="Buscar en el sitio: plan de estudios, trámites, trabajo de grado..." autocomplete="off" aria-label="Escriba su búsqueda">
        <button class="busqueda-cerrar" id="busqueda-cerrar" aria-label="Cerrar búsqueda">&times;</button>
      </div>
      <div class="busqueda-resultados" id="busqueda-resultados" aria-live="polite"></div>
    </div>
  </div>

  <main>
%(cuerpo)s
  </main>

  %(footer)s
  <script src="assets/js/indice.js"></script>
  <script src="assets/js/busqueda.js"></script>
  <script src="assets/js/navegacion.js"></script>
</body>
</html>''' % {"title": title, "desc": desc or (title + " · Programa de Tecnología en Procesos Industriales de la UFPS."),
              "header": header(slug), "cuerpo": cuerpo, "footer": footer()}
    with open(os.path.join(RAIZ, slug), "w", encoding="utf-8") as f:
        f.write(html)
    print("  escrito:", slug)

# migas de pan
def migas(*pares):
    partes = ['<a href="index.html">Inicio</a>']
    for i, (nombre, href) in enumerate(pares):
        if href and i < len(pares) - 1:
            partes.append('<a href="%s">%s</a>' % (href, nombre))
        else:
            partes.append('<span>%s</span>' % nombre)
    return '<nav class="migas" aria-label="Ruta">' + ' &rsaquo; '.join(partes) + '</nav>'

# encabezado de página interior
def encab(titulo, ruta, intro=""):
    return '''    <section class="encab-pagina">
      <div class="contenedor">
        %(migas)s
        <h1 class="titulo-barra">%(titulo)s</h1>
        %(intro)s
      </div>
    </section>''' % {"migas": ruta, "titulo": titulo,
                     "intro": ('<p class="medida">%s</p>' % intro) if intro else ""}

# página de contenido con barra lateral
def contenido_lateral(prosa, lateral):
    return '''    <section class="contenido">
      <div class="contenedor">
        <div class="contenido-grid">
          <div class="prosa">
%(prosa)s
          </div>
          <aside class="lateral">
%(lateral)s
          </aside>
        </div>
      </div>
    </section>''' % {"prosa": prosa, "lateral": lateral}

# tarjeta lateral de datos del programa (reutilizable)
def lateral_datos():
    return '''            <div class="tarjeta-lateral">
              <h4>Ficha del programa</h4>
              <div class="dato-lateral"><span class="k">Título</span><span class="v">%(titulo)s</span></div>
              <div class="dato-lateral"><span class="k">Nivel</span><span class="v">Tecnológico</span></div>
              <div class="dato-lateral"><span class="k">Duración</span><span class="v">%(dur)s</span></div>
              <div class="dato-lateral"><span class="k">Modalidad</span><span class="v">%(mod)s</span></div>
              <div class="dato-lateral"><span class="k">Créditos</span><span class="v">%(cred)s</span></div>
              <div class="dato-lateral"><span class="k">SNIES</span><span class="v">%(snies)s</span></div>
            </div>
            <div class="tarjeta-lateral">
              <h4>Coordinación</h4>
              <div class="dato-lateral"><span class="v">%(coord)s</span></div>
              <div class="dato-lateral"><a href="mailto:%(correo)s">%(correo)s</a></div>
              <div class="dato-lateral">%(tel)s</div>
            </div>''' % {"titulo": D["titulo"], "dur": D["duracion"], "mod": D["modalidad"],
                        "cred": D["creditos"], "snies": D["snies"], "coord": D["coordinador"],
                        "correo": D["correo"], "tel": D["tel"]}

def indice_lateral(titulo, enlaces):
    lis = "".join('<li><a href="#%s">%s</a></li>' % (i, t) for t, i in enlaces)
    return '''            <div class="tarjeta-lateral">
              <h4>%s</h4>
              <ul class="indice">%s</ul>
            </div>''' % (titulo, lis)

