# -*- coding: utf-8 -*-
"""Define el contenido de cada página y escribe el sitio completo."""
from generar import *  # noqa

# ==========================================================================
# PORTADA
# ==========================================================================
index_body = '''    <section class="hero">
      <div class="contenedor">
        <div class="hero-grid">
          <div class="hero-texto">
            <p class="eyebrow">Facultad de Ingeniería, Cúcuta, Norte de Santander</p>
            <h1>Tecnología en Procesos Industriales</h1>
            <p class="intro">Programa tecnológico de la Universidad Francisco de Paula Santander
              que forma profesionales integrales para la gestión y el mejoramiento de los procesos
              industriales de la región y el país, con fundamento humanístico, investigativo y
              vínculo permanente con el sector productivo.</p>
            <ul class="pildoras">
              <li class="pildora pildora--roja">Presencial</li>
              <li class="pildora">%(dur)s</li>
              <li class="pildora">%(cred)s créditos</li>
              <li class="pildora pildora--linea">SNIES %(snies)s</li>
            </ul>
            <div class="hero-acciones">
              <a class="boton boton--rojo" href="el-programa-plan-de-estudios.html">Ver plan de estudios</a>
              <a class="boton boton--linea" href="el-programa-perfil-de-ingreso.html">Cómo ingresar</a>
            </div>
          </div>
          <div class="foto-marco">
            <img src="assets/img/fotos/laboratorios.jpg"
                 alt="Estudiantes del programa en el laboratorio de automatización durante una práctica guiada">
          </div>
        </div>
      </div>
    </section>

    <section class="seccion seccion--roja" aria-label="Ficha técnica del programa">
      <div class="contenedor">
        <div class="ficha">
          <div class="dato"><span class="k">Título otorgado</span><span class="v">%(titulo)s</span></div>
          <div class="dato"><span class="k">Duración</span><span class="v">%(dur)s</span></div>
          <div class="dato"><span class="k">Modalidad</span><span class="v">%(mod)s</span></div>
          <div class="dato"><span class="k">Créditos</span><span class="v">%(cred)s</span></div>
          <div class="dato"><span class="k">Código SNIES</span><span class="v">%(snies)s</span></div>
          <div class="dato"><span class="k">Registro Calificado</span><span class="v">%(registro)s</span></div>
        </div>
      </div>
    </section>

    <section class="seccion">
      <div class="contenedor">
        <div class="doscolumnas">
          <div class="mv">
            <p class="eyebrow">Misión</p>
            <p>El programa de Tecnología en Procesos Industriales de la UFPS forma profesionales
              integrales comprometidos con la solución de los problemas de su entorno regional y
              nacional, con una sólida fundamentación humanística e investigativa y competencias
              orientadas al desarrollo y mejoramiento de los procesos industriales, aprovechando
              los beneficios del contexto binacional y la globalización de los mercados.</p>
            <a href="el-programa-pep.html" class="abrir">Conocer el Proyecto Educativo</a>
          </div>
          <div class="mv">
            <p class="eyebrow">Visión</p>
            <p>Ser reconocido en el ámbito local, regional y nacional por la formación de
              profesionales íntegros con capacidad de liderazgo, emprendimiento e innovación,
              promotores de la investigación, la gestión y la mejora de los procesos industriales,
              con responsabilidad social y compromiso con el desarrollo sostenible.</p>
            <a href="el-programa-historia.html" class="abrir">Ver la historia del programa</a>
          </div>
        </div>
      </div>
    </section>

    <section class="seccion seccion--suave">
      <div class="contenedor">
        <div class="centro">
          <h2 class="titulo-barra">Explora el programa</h2>
          <p class="medida" style="margin:0 auto 34px;">Toda la información académica, institucional
            y de comunidad, organizada en cuatro grandes áreas.</p>
        </div>
        <div class="tarjetas">
          <div class="tarjeta">
            <h3>El Programa</h3>
            <p>Historia, Proyecto Educativo, plan de estudios, perfiles, trabajos de grado e investigación.</p>
            <a href="el-programa.html" class="abrir">Abrir sección</a>
          </div>
          <div class="tarjeta">
            <h3>Institucional</h3>
            <p>Normatividad, trámites estudiantiles y de graduados, autoevaluación y formatos de descarga.</p>
            <a href="institucional.html" class="abrir">Abrir sección</a>
          </div>
          <div class="tarjeta">
            <h3>Comunidad</h3>
            <p>Consejo estudiantil y ANEIAP, equipo de trabajo, graduados e intermediación laboral.</p>
            <a href="comunidad.html" class="abrir">Abrir sección</a>
          </div>
          <div class="tarjeta">
            <h3>Vínculos</h3>
            <p>Redes académicas, proyección social, prácticas, convenios, movilidades y eventos.</p>
            <a href="vinculos.html" class="abrir">Abrir sección</a>
          </div>
        </div>
      </div>
    </section>

    <section class="seccion">
      <div class="contenedor">
        <h2 class="titulo-barra">Vida del programa</h2>
        <p class="medida">Prácticas de laboratorio, visitas industriales, sustentaciones de proyectos,
          cursos de formación complementaria y encuentros con graduados y empresas de la región.</p>
        <div class="tira-fotos">
          <img src="assets/img/fotos/visitas-industriales-1.jpg" alt="Visita industrial de estudiantes a una planta de procesamiento">
          <img src="assets/img/fotos/sustentaciones.jpg" alt="Sustentación de un proyecto de estudiantes ante docentes">
          <img src="assets/img/fotos/cursos.jpg" alt="Estudiantes en una feria de proyectos del programa">
          <img src="assets/img/fotos/egresados.jpg" alt="Entrega de certificados a estudiantes del programa">
        </div>
      </div>
    </section>''' % {"dur": D["duracion"], "titulo": D["titulo"], "mod": D["modalidad"],
                     "cred": D["creditos"], "snies": D["snies"], "registro": D["registro"]}

pagina("index.html",
       "Inicio",
       index_body,
       desc="Programa de Tecnología en Procesos Industriales de la UFPS, Facultad de Ingeniería, Cúcuta. Información académica, institucional y de comunidad.")

# ==========================================================================
# LANDINGS DE SECCIÓN
# ==========================================================================
def landing(slug, titulo, intro, tarjetas, foto=None):
    tj = "".join(
        '''          <div class="tarjeta">
            <h3>%s</h3>
            <p>%s</p>
            <a href="%s" class="abrir">Abrir página</a>
          </div>\n''' % (n, d, s) for n, d, s in tarjetas)
    foto_html = ""
    if foto:
        foto_html = '''    <section class="seccion seccion--suave">
      <div class="contenedor">
        <div class="foto-marco" style="max-width:760px;margin:0 auto;">
          <img src="%s" alt="%s">
        </div>
      </div>
    </section>''' % (foto[0], foto[1])
    cuerpo = '''%(encab)s
    <section class="contenido">
      <div class="contenedor">
        <div class="tarjetas">
%(tj)s        </div>
      </div>
    </section>
%(foto)s''' % {"encab": encab(titulo, migas((titulo, ""))), "tj": tj, "foto": foto_html}
    pagina(slug, titulo, cuerpo)

landing("institucional.html", "Institucional",
        "Información normativa y de gestión del programa: reglamentos, trámites para estudiantes y graduados, resultados de autoevaluación y formatos de uso frecuente.",
        [("Normatividad", "Calendario académico, estatuto estudiantil, compilación de normas de interés, protocolo de salidas académicas y resolución de registro calificado.", "institucional-normatividad.html"),
         ("Trámites", "Trámites estudiantiles y de graduados: certificaciones, constancias, cursos vacacionales, validaciones, reintegros y postulaciones.", "institucional-tramites.html"),
         ("Autoevaluación", "Informes de autoevaluación del programa y planes de mejoramiento en el marco del aseguramiento de la calidad.", "institucional-autoevaluacion.html"),
         ("Formatos y descargas", "Repositorio de formatos, plantillas y documentos oficiales para estudiantes, docentes y graduados.", "institucional-formatos-descargas.html")],
        foto=("assets/img/fotos/autoevaluacion.jpg", "Reunión de trabajo del comité del programa en sala de juntas"))

landing("el-programa.html", "El Programa",
        "Identidad académica de la Tecnología en Procesos Industriales: su historia, su Proyecto Educativo, la estructura curricular, los perfiles de formación y las apuestas de investigación.",
        [("Historia", "Origen y evolución del programa desde su creación en 2007 y su desarrollo curricular.", "el-programa-historia.html"),
         ("Registro Calificado", "Resoluciones y condiciones de calidad que respaldan la oferta del programa.", "el-programa-registro-calificado.html"),
         ("Proyecto Educativo (PEP)", "Misión, visión, objetivos, valores y líneas de profundización del programa.", "el-programa-pep.html"),
         ("Plan de Estudios", "Áreas de formación, distribución de créditos y organización por semestres.", "el-programa-plan-de-estudios.html"),
         ("Malla curricular", "Representación gráfica de las asignaturas y su secuencia por semestre.", "el-programa-malla-curricular.html"),
         ("Perfil de Ingreso", "Características y condiciones esperadas del aspirante al programa.", "el-programa-perfil-de-ingreso.html"),
         ("Perfiles de egreso", "Perfil profesional y perfil ocupacional del Tecnólogo en Procesos Industriales.", "el-programa-perfiles-de-egreso.html"),
         ("Trabajos de grado", "Modalidades, reglamento, requisitos, formatos y banco de directores y proyectos.", "el-programa-trabajos-de-grado.html"),
         ("Investigación", "Grupos y semilleros, líneas y proyectos de impacto, publicaciones y memorias.", "el-programa-investigacion.html")])

landing("comunidad.html", "Comunidad",
        "El programa es una comunidad de estudiantes, docentes, personal administrativo y graduados. Aquí se reúnen sus organizaciones, su equipo de trabajo y los servicios de conexión con el mundo laboral.",
        [("Consejo Estudiantil y ANEIAP", "Representación estudiantil y capítulo de la Asociación Nacional de Estudiantes de Ingeniería Industrial y afines.", "comunidad-consejo-aneiap.html"),
         ("Redes sociales del programa", "Canales oficiales del programa en Instagram y Facebook.", "comunidad-redes-sociales.html"),
         ("Equipo de Trabajo", "Comité curricular, coordinación, cuerpo docente y personal administrativo.", "comunidad-equipo-de-trabajo.html"),
         ("Graduados", "Encuentros, coloquios y directorios de emprendedores y consultores egresados.", "comunidad-graduados.html"),
         ("Intermediación Laboral", "Bolsa de empleo y conexión de estudiantes y graduados con el sector productivo.", "comunidad-intermediacion-laboral.html")],
        foto=("assets/img/fotos/egresados.jpg", "Grupo de estudiantes y graduados del programa con sus certificados"))

landing("vinculos.html", "Vínculos",
        "La proyección del programa hacia la región, la industria y otras instituciones: redes académicas, convenios, prácticas, cursos de extensión, movilidades y eventos.",
        [("Redes académicas", "Participación en ACOFI, Redin, COPNIA y RedColsi.", "vinculos-redes-academicas.html"),
         ("Proyección social / Extensión", "Convenios, prácticas, cursos, movilidades y eventos del programa.", "vinculos-proyeccion-social.html")],
        foto=("assets/img/fotos/visitas-industriales-2.jpg", "Estudiantes del programa durante una visita a una empresa de la región"))

# ==========================================================================
# HISTORIA
# ==========================================================================
historia = '''            <div class="foto-marco" style="max-width:560px;margin:0 0 30px;">
              <img src="assets/img/fotos/departamento-tpi.jpg"
                   alt="Entrada del Departamento de Procesos Industriales de la UFPS con el pendón del programa">
            </div>

            <h2>Origen del programa</h2>
            <p>El programa de Tecnología en Procesos Industriales fue creado mediante el
              <strong>Acuerdo 021 del 21 de marzo de 2007</strong> del Consejo Superior Universitario
              de la Universidad Francisco de Paula Santander. Inició labores en el primer semestre de
              2008, con Registro Calificado otorgado por la <strong>Resolución 3573 del 27 de junio de
              2007</strong> y Código SNIES 52956.</p>
            <p>El programa está adscrito a la Facultad de Ingeniería y ligado al Departamento de
              Procesos Industriales, unidad que imparte la mayor parte de su docencia. Su creación
              respondió a la necesidad de formar talento humano tecnológico para el medio industrial
              regional y nacional, en el marco de los planes de desarrollo del país.</p>

            <h2>Trayectoria y renovación</h2>
            <p>En 2012 se graduó la primera cohorte del programa. En el año 2014 se obtuvo la renovación
              del registro calificado por siete años, mediante la <strong>Resolución 1566 del 7 de
              febrero</strong>. En 2016 y 2018 el programa renovó su licencia interna de funcionamiento,
              al demostrar un desempeño favorable en los planes de mantenimiento propuestos, y en 2018
              se realizó el primer encuentro de graduados.</p>
            <p>A partir de 2019 se inició el plan de trabajo para la modernización curricular, de
              conformidad con los estudios de pertinencia y los resultados de autoevaluación, del cual
              surgió una nueva propuesta de Proyecto Educativo y de plan de estudios acorde con el
              Decreto 1330 de 2019. En 2020 se instaló el laboratorio de manufactura, se creó el
              semillero de investigación SEIPMA y se concretó la primera movilidad internacional del
              programa. Esa actualización se consolidó con la renovación del registro calificado
              otorgada por la <strong>Resolución MEN 021555 del 12 de noviembre de 2021</strong>.</p>

            <h2>Línea de tiempo</h2>
            <ol class="linea-tiempo">
              <li><span class="lt-anio">2007</span><span class="lt-hito">Creación interna del programa y otorgamiento del registro calificado.</span></li>
              <li><span class="lt-anio">2008</span><span class="lt-hito">Inicio del programa.</span></li>
              <li><span class="lt-anio">2012</span><span class="lt-hito">Primera cohorte de graduados.</span></li>
              <li><span class="lt-anio">2014</span><span class="lt-hito">Renovación del registro calificado.</span></li>
              <li><span class="lt-anio">2016</span><span class="lt-hito">Renovación de licencia interna.</span></li>
              <li><span class="lt-anio">2017</span><span class="lt-hito">Creación del semillero de investigación SIMECC.</span></li>
              <li><span class="lt-anio">2018</span><span class="lt-hito">Renovación de licencia interna y primer encuentro de graduados.</span></li>
              <li><span class="lt-anio">2019</span><span class="lt-hito">Estudio y propuesta de nuevo PEP y nuevo pénsum.</span></li>
              <li><span class="lt-anio">2020</span><span class="lt-hito">Semillero SEIPMA, laboratorio de manufactura y primera movilidad internacional.</span></li>
            </ol>

            <h2>El programa hoy</h2>
            <p>Actualmente la Tecnología en Procesos Industriales desarrolla procesos permanentes de
              autoevaluación y mejoramiento continuo, orientados a fortalecer sus condiciones de
              calidad de acuerdo con las necesidades de sus grupos de interés y del sector productivo
              de la frontera y el país.</p>'''

pagina("el-programa-historia.html", "Historia",
       encab("Historia", migas(("El Programa", "el-programa.html"), ("Historia", "")),
             "Recorrido del programa desde su creación en 2007 hasta su proceso actual de mejoramiento continuo.")
       + contenido_lateral(historia, lateral_datos()))

# ==========================================================================
# PROYECTO EDUCATIVO (PEP)
# ==========================================================================
pep = '''            <h2 id="mision">Misión</h2>
            <p>El programa de Tecnología en Procesos Industriales de la Universidad Francisco de Paula
              Santander forma profesionales integrales comprometidos con la solución de los problemas
              de su entorno regional y nacional, partícipes del desarrollo económico y social, con una
              sólida fundamentación humanística e investigativa y competencias orientadas al desarrollo
              y mejoramiento de los procesos industriales, aprovechando los beneficios que brinda el
              contexto binacional y la globalización de los mercados.</p>

            <h2 id="vision">Visión</h2>
            <p>El programa será reconocido en el ámbito local, regional y nacional por la formación de
              profesionales integrales, por su capacidad de liderazgo, emprendimiento, promoción de la
              innovación, investigación, gestión y mejora de los procesos industriales, por su
              apropiación de nuevas tecnologías y su sentido de responsabilidad social, dando respuesta
              a las necesidades del sector industrial y de servicios, comprometidos con el desarrollo
              sostenible de la región y el país.</p>

            <h2 id="objetivos">Objetivos del programa</h2>
            <h3>Objetivo general</h3>
            <p>Formar talento humano competente en la gestión y mejora de los procesos industriales,
              capaz de incorporarse al sector productivo y de servicios respondiendo a sus necesidades
              reales, contribuyendo a que las empresas de la región y el país alcancen su máxima
              productividad y competitividad en un entorno ambientalmente sostenible.</p>
            <h3>Objetivos específicos</h3>
            <ul>
              <li>Formar tecnólogos con capacidad de ejecutar, controlar, transformar y operar los
                medios y procesos para la solución de problemas de los sectores productivos.</li>
              <li>Desarrollar competencias cognitivas, socioafectivas y comunicativas para producir
                conocimiento tecnológico, coordinar actividades interdisciplinarias y emprender
                proyectos productivos innovadores.</li>
              <li>Profundizar en la formación integral, capacitando para cumplir funciones
                profesionales, investigativas y de servicio social que requieren la región y el país.</li>
              <li>Fomentar la producción de conocimiento mediante la investigación básica y aplicada,
                y la atención prioritaria a los problemas regionales.</li>
              <li>Realizar actividades de extensión y de servicio a la comunidad, y promover la
                preservación del medio ambiente y la cultura ecológica.</li>
            </ul>

            <h2 id="lineas">Líneas de profundización</h2>
            <p>Con base en las competencias que debe desarrollar el graduado, el programa plantea tres
              líneas de profundización:</p>
            <h3>Gestión de la producción y las operaciones</h3>
            <p>Profundiza en la dirección, programación y control de la producción, y en la integración
              de las operaciones de la cadena de suministro, mediante modelos de optimización y
              herramientas para la toma de decisiones orientadas a la calidad y la productividad.</p>
            <h3>Gestión organizacional</h3>
            <p>Busca incrementar la competitividad de la organización fortaleciendo su estructura
              interna: gestión del talento humano, mercadeo, direccionamiento estratégico,
              emprendimiento, y seguridad y salud en el trabajo.</p>
            <h3>Transformación y procesamiento de los materiales</h3>
            <p>Fortalece el conocimiento de los procesos de transformación física y química de los
              materiales de uso industrial, en especial cerámicos, polímeros y metales, e investiga
              nuevos materiales compuestos con valor agregado.</p>

            <h2 id="valores">Valores</h2>
            <p>El programa adopta los valores éticos que orientan a la Universidad, integrados de forma
              transversal en el currículo: responsabilidad, transparencia, compromiso con la verdad,
              puntualidad, sentido de pertenencia, honestidad, equidad, respeto, trabajo en equipo,
              calidad humana, lealtad, y enfoque investigativo y humanista.</p>

            <h2 id="competencias">Competencias</h2>
            <p>La formación del Tecnólogo en Procesos Industriales integra competencias genéricas y
              específicas. Entre las genéricas se encuentran la capacidad de comprender, analizar e
              interpretar la lógica de las ciencias y la tecnología, la competencia comunicativa para el
              trabajo interdisciplinario y el aprendizaje autónomo, el trabajo en equipo, la toma de
              decisiones y el compromiso ético. Las competencias específicas se orientan a la gestión de
              la producción y las operaciones, la gestión organizacional y la transformación y el
              procesamiento de materiales, en coherencia con las tres líneas de profundización.</p>

            <h2 id="resultados">Resultados de Aprendizaje</h2>
            <p>Los resultados de aprendizaje describen lo que el estudiante será capaz de hacer al
              finalizar su proceso formativo y se encuentran declarados en los contenidos programáticos
              de cada asignatura, alineados con el perfil profesional y las competencias del programa.
              El detalle por asignatura puede consultarse en los
              <a href="el-programa-plan-de-estudios.html#contenidos">contenidos programáticos</a>.</p>

            <div class="aviso">Puede consultar el documento completo del Proyecto Educativo del Programa
              en el portal de la Universidad.
              <a href="https://ww2.ufps.edu.co/public/archivos/oferta_academica/7ed0c42bfb51c2edd45215411ace6ed1.pdf" target="_blank" rel="noopener">Abrir el PEP (PDF)</a>.</div>
            <p><a class="boton boton--rojo" href="https://ww2.ufps.edu.co/public/archivos/oferta_academica/7ed0c42bfb51c2edd45215411ace6ed1.pdf" target="_blank" rel="noopener">Descargar el Proyecto Educativo (PDF)</a></p>'''

pep_indice = indice_lateral("En esta página", [
    ("Misión", "mision"), ("Visión", "vision"), ("Objetivos", "objetivos"),
    ("Líneas de profundización", "lineas"), ("Valores", "valores"),
    ("Competencias", "competencias"), ("Resultados de Aprendizaje", "resultados")])

pagina("el-programa-pep.html", "Proyecto Educativo (PEP)",
       encab("Proyecto Educativo del Programa", migas(("El Programa", "el-programa.html"), ("Proyecto Educativo (PEP)", "")),
             "El PEP orienta el accionar del programa: define su misión, visión, objetivos, valores y líneas de profundización.")
       + contenido_lateral(pep, pep_indice + lateral_datos()))

# ==========================================================================
# PLAN DE ESTUDIOS
# ==========================================================================
# --- Datos del plan de estudios (Resolución MEN 021555 de 2021) ---
PLAN = [
 ("Primer semestre", "19", "912", [
   ("1982101","Cálculo Diferencial","Ninguno","4","64","0","128","0","192"),
   ("1982102","Álgebra Lineal","Ninguno","3","48","0","96","0","144"),
   ("1982103","Química General","Ninguno","4","64","32","96","0","192"),
   ("1982104","Introducción a la Tecnología en Procesos Industriales","Ninguno","2","32","0","64","0","96"),
   ("1982105","Fundamentos de Programación","Ninguno","3","16","32","96","0","144"),
   ("1982106","Constitución Política y Civismo","Ninguno","2","32","0","64","0","96"),
   ("1982107","Introducción a la Vida Universitaria","Ninguno","1","16","0","32","0","48"),
 ]),
 ("Segundo semestre", "18", "864", [
   ("1982201","Cálculo Integral","1982101","4","64","0","128","0","192"),
   ("1982202","Física Mecánica","*13 créditos","4","48","16","128","0","192"),
   ("1982203","Química Industrial","1982103","3","64","16","64","0","144"),
   ("1982204","Materiales de Ingeniería","*13 créditos","3","32","16","96","0","144"),
   ("1982205","Dibujo de Ingeniería asistido por computadora","1982104","2","0","32","64","0","96"),
   ("1982206","Comunicación oral y escrita","*13 créditos","2","32","0","64","0","96"),
 ]),
 ("Tercer semestre", "17", "816", [
   ("1982301","Métodos, Tiempos y Movimientos","*29 créditos","3","32","16","80","16","144"),
   ("1982302","Física Electromagnética","1982202","4","48","16","128","0","192"),
   ("1982303","Termodinámica","1982203","3","64","0","80","0","144"),
   ("1982304","Estadística y Probabilidad","1982101","2","48","0","48","0","96"),
   ("1982305","Administración","*29 créditos","2","32","0","64","0","96"),
   ("1982306","Metodología de la Investigación","1982206","2","32","0","64","0","96"),
   ("1982307","Inglés I","1982206","1","32","0","16","0","48"),
 ]),
 ("Cuarto semestre", "17", "816", [
   ("1982401","Planeación de la Producción","1982301","3","64","0","80","0","144"),
   ("1982402","Costos Industriales","*46 créditos","3","64","0","48","32","144"),
   ("1982403","Procesos Industriales I","1982303","3","80","16","48","0","144"),
   ("1982404","Control Estadístico de Calidad en Procesos","1982304","2","48","0","48","0","96"),
   ("1982405","Gestión del Talento Humano","1982305","3","48","0","64","32","144"),
   ("1982406","Electiva Profesional I","*46 créditos","2","48","0","48","0","96"),
   ("1982407","Inglés II","1982307","1","32","0","16","0","48"),
 ]),
 ("Quinto semestre", "17", "816", [
   ("1982501","Programación y Control de la Producción","1982401","3","64","0","80","0","144"),
   ("1982502","Mantenimiento Industrial","1982403","3","48","0","96","0","144"),
   ("1982503","Procesos de Manufactura","1982403","3","48","16","80","0","144"),
   ("1982504","Profundización en Materiales y Procesos I","1982404","3","48","16","64","16","144"),
   ("1982505","Electiva Profesional II","*63 créditos","2","48","0","48","0","96"),
   ("1982506","Seguridad y Salud en el Trabajo","1982405","3","48","0","80","16","144"),
 ]),
 ("Sexto semestre", "15", "720", [
   ("1982601","Prácticas Industriales","*86 créditos","4","64","0","32","96","192"),
   ("1982602","Electiva Humanística","*63 créditos","2","32","0","64","0","96"),
   ("1982603","Ética","*77 créditos","2","32","0","64","0","96"),
   ("1982604","Profundización en Materiales y Procesos II","1982504","3","48","16","80","0","144"),
   ("1982605","Electiva Profesional III","*77 créditos","2","48","0","48","0","96"),
   ("1982606","Gestión Ambiental","*63 créditos","2","48","0","48","0","96"),
   ("1982607","Trabajo de Grado","*63 créditos","0","0","0","0","0","0"),
 ]),
]

def tabla_semestre(nombre, cr, hrs, filas):
    trs = ""
    for f in filas:
        trs += ('<tr><td>%s</td><td>%s</td><td>%s</td><td class="c">%s</td>'
                '<td class="c">%s</td><td class="c">%s</td><td class="c">%s</td>'
                '<td class="c">%s</td><td class="c">%s</td></tr>') % f
    return ('''            <h3>%s</h3>
            <div class="tabla-envoltura">
              <table class="datos tabla-plan">
                <thead><tr><th>Código</th><th>Asignatura</th><th>Prerrequisito</th>
                  <th class="c">Cr</th><th class="c">HT</th><th class="c">HP</th>
                  <th class="c">HTI</th><th class="c">HAP</th><th class="c">Horas</th></tr></thead>
                <tbody>%s</tbody>
                <tfoot><tr><td colspan="3">Total del semestre</td><td class="c">%s</td>
                  <td colspan="4"></td><td class="c">%s</td></tr></tfoot>
              </table>
            </div>''') % (nombre, trs, cr, hrs)

plan = '''            <h2 id="estructura">Estructura curricular</h2>
            <p>El plan de estudios vigente corresponde al pénsum aprobado mediante la Resolución MEN
              021555 de 2021. Se organiza en <strong>%(cred)s créditos académicos</strong> distribuidos
              en <strong>%(dur)s</strong> de formación presencial, e integra el sistema de créditos del
              Decreto 1330 de 2019. Se construyó a partir de los propósitos de formación, el perfil
              profesional y ocupacional, las necesidades del contexto regional y nacional, y el proceso
              de autoevaluación.</p>

            <h2 id="areas">Áreas de formación</h2>
            <p>El currículo se organiza en las siguientes áreas de conocimiento, base de la formación
              integral del estudiante:</p>
            <ul>
              <li><strong>Ciencias Básicas.</strong> Fundamentos teóricos, experimentales y
                metodológicos de las ciencias naturales y las matemáticas.</li>
              <li><strong>Ciencias Básicas Tecnológicas.</strong> Bases de la ingeniería aplicada que
                articulan la ciencia con la práctica tecnológica.</li>
              <li><strong>Formación Profesional.</strong> Asignaturas propias de la gestión de la
                producción, la gestión organizacional y la transformación de materiales.</li>
              <li><strong>Formación Humanística.</strong> Componente socio-humanístico y de formación
                en valores, transversal a todo el plan.</li>
            </ul>

            <h2 id="semestres">Asignaturas por semestre</h2>
''' % {"cred": D["creditos"], "dur": D["duracion"]} \
+ "\n".join(tabla_semestre(*s) for s in PLAN) + '''
            <p style="font-size:.9rem;color:var(--gris);margin-top:16px;">Convenciones: Cr, créditos;
              HT, horas teóricas; HP, horas prácticas; HTI, horas de trabajo independiente; HAP, horas
              de asesoría in situ. Un asterisco en el prerrequisito indica el número mínimo de créditos
              aprobados requerido.</p>

            <h2 id="malla">Malla curricular</h2>
            <p>La representación gráfica del plan por semestres está disponible en la página de
              <a href="el-programa-malla-curricular.html">Malla curricular</a>.</p>

            <h2 id="contenidos">Contenidos programáticos</h2>
            <p>Los contenidos programáticos de cada asignatura, con sus competencias y resultados de
              aprendizaje, pueden consultarse en el portal de la Universidad.</p>
            <p><a class="boton boton--linea" href="https://ww2.ufps.edu.co/oferta-academica/tecnologia-en-procesos-industriales/2302" target="_blank" rel="noopener">Ver contenidos programáticos</a></p>
            <div class="aviso">Si un estudiante o graduado requiere que se le <strong>certifiquen</strong>
              los contenidos programáticos vistos, debe realizar la solicitud en la sección de
              <a href="institucional-tramites.html#estudiantiles">Trámites</a>
              (Certificación de contenidos programáticos).</div>'''

plan_indice = indice_lateral("En esta página", [
    ("Estructura curricular", "estructura"), ("Áreas de formación", "areas"),
    ("Asignaturas por semestre", "semestres"), ("Malla curricular", "malla"),
    ("Contenidos programáticos", "contenidos")])

pagina("el-programa-plan-de-estudios.html", "Plan de Estudios",
       encab("Plan de Estudios", migas(("El Programa", "el-programa.html"), ("Plan de Estudios", "")),
             "Áreas de formación, distribución de créditos y organización por semestres del programa.")
       + contenido_lateral(plan, plan_indice + lateral_datos()))

# ==========================================================================
# PERFILES DE EGRESO
# ==========================================================================
perfiles = '''            <h2 id="profesional">Perfil profesional</h2>
            <p>Con base en la formación recibida, el Tecnólogo en Procesos Industriales de la UFPS está
              en capacidad de:</p>
            <ul>
              <li>Planear, programar y controlar la producción según los requerimientos y las
                especificaciones técnicas del proceso.</li>
              <li>Aplicar conceptos y técnicas de gestión y control estadístico de la calidad de los
                productos y las operaciones.</li>
              <li>Adaptar nuevas tecnologías para desarrollar procesos industriales de manera eficiente
                y eficaz, preservando el medio ambiente.</li>
              <li>Desarrollar soluciones creativas e innovadoras a problemas reales y proyectos de
                desarrollo.</li>
              <li>Asistir en la planeación, organización, dirección y control de proyectos de
                ingeniería para el mejoramiento de las organizaciones.</li>
              <li>Aplicar herramientas de gestión de mantenimiento y de análisis de costos del proceso
                productivo.</li>
              <li>Apoyar el diseño e implementación de programas de seguridad y salud en el trabajo.</li>
              <li>Gestionar proyectos emprendedores que generen nuevas opciones laborales y mercados.</li>
              <li>Interactuar en equipos interdisciplinarios y comprometerse con la ética y la
                responsabilidad profesional, social y ambiental.</li>
            </ul>

            <h2 id="ocupacional">Perfil ocupacional</h2>
            <p>Según las competencias adquiridas, el egresado puede desempeñarse, entre otros, en los
              siguientes campos y cargos:</p>
            <ul>
              <li>Jefe de producción.</li>
              <li>Analista de proceso de producción.</li>
              <li>Analista de métodos y tiempos.</li>
              <li>Asistente de seguridad y salud en el trabajo.</li>
              <li>Supervisor de control y gestión de la calidad.</li>
              <li>Asistente en administración del recurso humano.</li>
              <li>Asistente de mantenimiento industrial.</li>
              <li>Asistente de costos de producción.</li>
              <li>Auxiliar de proyectos industriales.</li>
              <li>Jefe de almacén y materias primas.</li>
            </ul>''' 

perfiles_indice = indice_lateral("En esta página", [
    ("Perfil profesional", "profesional"), ("Perfil ocupacional", "ocupacional")])

pagina("el-programa-perfiles-de-egreso.html", "Perfiles de egreso",
       encab("Perfiles de egreso", migas(("El Programa", "el-programa.html"), ("Perfiles de egreso", "")),
             "Capacidades profesionales y campos de desempeño del Tecnólogo en Procesos Industriales.")
       + contenido_lateral(perfiles, perfiles_indice + lateral_datos()))

# ==========================================================================
# INVESTIGACIÓN
# ==========================================================================
investigacion = '''            <h2 id="apuesta">Apuesta investigativa</h2>
            <p>El programa promueve una cultura de investigación y proyección social entre docentes y
              estudiantes, orientada a la búsqueda de soluciones a las problemáticas de la industria y
              la academia. La investigación formativa se articula con las tres líneas de profundización del
              programa y se despliega a través de proyectos de aula, semilleros, grupos de investigación
              y trabajos de grado. El programa cuenta con el apoyo de dos grupos de investigación
              adscritos al Departamento de Procesos Industriales y a la Facultad de Ingeniería.</p>

            <h2 id="grupos">Grupos de investigación</h2>
            <div class="tabla-envoltura">
              <table class="datos">
                <thead><tr><th>Sigla</th><th>Grupo</th><th>Líneas</th></tr></thead>
                <tbody>
                  <tr><td>GIINGPRO</td><td>Grupo de investigación en innovación y gestión productiva</td>
                    <td>Gerencia organizacional; gestión productiva; innovación y competitividad.</td></tr>
                  <tr><td>GIPYC</td><td>Grupo de investigación en productividad y competitividad</td>
                    <td>Gestión estratégica de la calidad; producción, cadenas de suministro y simulación.</td></tr>
                </tbody>
              </table>
            </div>

            <h2 id="semilleros">Semilleros de investigación</h2>
            <p>El programa promueve la participación de los estudiantes en procesos de investigación
              formativa a través de sus semilleros, cuyas líneas temáticas corresponden a las líneas de
              profundización académica.</p>
            <div class="tabla-envoltura">
              <table class="datos">
                <thead><tr><th>Sigla</th><th>Semillero</th><th>Líneas</th></tr></thead>
                <tbody>
                  <tr><td>SIMECC</td><td>Semillero de investigación en manufactura esbelta y control estadístico de calidad en procesos</td>
                    <td>Lean manufacturing; control estadístico; cadenas de suministro; gestión gerencial.</td></tr>
                  <tr><td>SINDMAT</td><td>Semillero de investigación en desarrollo de materiales</td>
                    <td>Nuevos materiales; polímeros; materiales avanzados; innovación.</td></tr>
                </tbody>
              </table>
            </div>
            <p>En 2020 se creó, además, el semillero de investigación SEIPMA. %(pend)s (descripción y
              líneas por complementar).</p>

            <h2 id="investigadores">Investigadores categorizados</h2>
            <p>Relación de los docentes investigadores del programa y su categoría ante el Ministerio de
              Ciencia, Tecnología e Innovación. %(pend)s</p>

            <h2 id="lineas-proyectos">Líneas y proyectos de impacto</h2>
            <p>Las líneas de trabajo se alinean con las tres líneas de profundización del programa: gestión de
              la producción y las operaciones, gestión organizacional, y transformación y procesamiento
              de materiales. La relación de proyectos de impacto se incorporará a esta página. %(pend)s</p>

            <h2 id="publicaciones">Publicaciones</h2>
            <p>Producción académica de los docentes y estudiantes del programa. Puede consultar las
              revistas institucionales en el
              <a href="http://revistas.ufps.edu.co" target="_blank" rel="noopener">portal de publicaciones de la UFPS</a>. %(pend)s</p>

            <h2 id="memorias-eventos">Memorias de eventos</h2>
            <p>Memorias de congresos, encuentros y jornadas de investigación del programa. %(pend)s</p>''' % {"pend": PENDIENTE}

inv_indice = indice_lateral("En esta página", [
    ("Apuesta investigativa", "apuesta"), ("Grupos de investigación", "grupos"),
    ("Semilleros de investigación", "semilleros"), ("Investigadores categorizados", "investigadores"),
    ("Líneas y proyectos de impacto", "lineas-proyectos"), ("Publicaciones", "publicaciones"),
    ("Memorias de eventos", "memorias-eventos")])

pagina("el-programa-investigacion.html", "Investigación",
       encab("Investigación", migas(("El Programa", "el-programa.html"), ("Investigación", "")),
             "Grupos y semilleros, líneas y proyectos de impacto, publicaciones y memorias del programa.")
       + contenido_lateral(investigacion, inv_indice + lateral_datos()))

# ==========================================================================
# REGISTRO CALIFICADO
# ==========================================================================
registro = '''            <h2>Condiciones de calidad</h2>
            <p>La Tecnología en Procesos Industriales cuenta con Registro Calificado otorgado por el
              Ministerio de Educación Nacional, que acredita el cumplimiento de las condiciones de
              calidad para su oferta y desarrollo. Mediante la <strong>Resolución MEN 021555 del 12 de
              noviembre de 2021</strong> se renovó el registro calificado del programa por el término de
              siete años, en modalidad presencial, en Cúcuta, con 6 semestres y 103 créditos académicos,
              periodicidad de admisión semestral, y se aprobaron las modificaciones al plan de estudios.</p>
            <div class="tabla-envoltura">
              <table class="datos">
                <thead><tr><th>Acto administrativo</th><th>Descripción</th></tr></thead>
                <tbody>
                  <tr><td>Acuerdo 021 de 2007</td><td>Creación del plan de estudios (Consejo Superior Universitario).</td></tr>
                  <tr><td>Resolución 3573 de 2007</td><td>Registro Calificado inicial. Código SNIES %(snies)s.</td></tr>
                  <tr><td>Resolución 1566 de 2014</td><td>Renovación del registro calificado por siete años.</td></tr>
                  <tr><td>Resolución MEN 021555 de 2021</td><td>Renovación vigente del registro calificado por siete años y aprobación del nuevo plan de estudios.</td></tr>
                </tbody>
              </table>
            </div>
            <p><a class="boton boton--rojo" href="documentos/resolucion-021555-2021-registro-calificado.pdf" target="_blank" rel="noopener">Abrir la resolución (PDF)</a></p>''' % {
    "snies": D["snies"]}

pagina("el-programa-registro-calificado.html", "Registro Calificado",
       encab("Registro Calificado", migas(("El Programa", "el-programa.html"), ("Registro Calificado", "")),
             "Resoluciones y condiciones de calidad que respaldan la oferta del programa.")
       + contenido_lateral(registro, lateral_datos()))

# ==========================================================================
# MALLA CURRICULAR (imagen)
# ==========================================================================
malla = '''            <p>La malla curricular presenta la secuencia de asignaturas por semestre y su
              relación con las áreas de formación del programa. Para el detalle de créditos,
              intensidad horaria y prerrequisitos, consulte el
              <a href="el-programa-plan-de-estudios.html">Plan de Estudios</a>.</p>
            <figure>
              <img src="assets/img/fotos/malla-curricular.png"
                   alt="Malla curricular del programa de Tecnología en Procesos Industriales por semestres">
              <figcaption>Malla curricular del programa por semestres (I a VI). Las convenciones C, HT y HP
                corresponden a créditos, horas teóricas y horas prácticas.</figcaption>
            </figure>'''

pagina("el-programa-malla-curricular.html", "Malla curricular",
       encab("Malla curricular", migas(("El Programa", "el-programa.html"), ("Malla curricular", "")),
             "Representación gráfica de las asignaturas y su secuencia por semestre.")
       + contenido_lateral(malla, lateral_datos()))

# ==========================================================================
# PERFIL DE INGRESO
# ==========================================================================
ingreso = '''            <h2>Perfil del aspirante</h2>
            <p>El aspirante a la Tecnología en Procesos Industriales es una persona con interés por la
              industria, la producción de bienes y servicios y la solución de problemas del entorno,
              con disposición para el trabajo en equipo, el razonamiento lógico-matemático y el
              aprendizaje de nuevas tecnologías.</p>
            <h2>Inscripción y admisiones</h2>
            <p>El proceso de inscripción y admisión se realiza a través de la Oficina de Admisiones,
              Registro y Control Académico de la UFPS. Allí puede consultar fechas, requisitos, valores
              y resultados del proceso de admisión.</p>
            <p><a class="boton boton--rojo" href="https://ww2.ufps.edu.co/universidad/admisiones-registro-academico/2690" target="_blank" rel="noopener">Ir a Admisiones y Registro Académico</a></p>'''

pagina("el-programa-perfil-de-ingreso.html", "Perfil de Ingreso",
       encab("Perfil de Ingreso", migas(("El Programa", "el-programa.html"), ("Perfil de Ingreso", "")),
             "Características y condiciones esperadas del aspirante al programa.")
       + contenido_lateral(ingreso, lateral_datos()))

# ==========================================================================
# TRABAJOS DE GRADO (subsecciones)
# ==========================================================================
def descarga(nombre, tipo, meta, href="#", externo=False, accion="Abrir"):
    attr = ' target="_blank" rel="noopener"' if externo else ""
    return '''            <li class="descarga">
              <span class="icono" data-tipo="%s" aria-hidden="true"></span>
              <span class="info"><span class="nom">%s</span><span class="meta">%s</span></span>
              <a class="accion" href="%s"%s>%s</a>
            </li>''' % (tipo, nombre, meta, href, attr, accion)

grado = '''            <p>El trabajo de grado es una actividad de investigación o de aplicación tecnológica en
              la que el estudiante demuestra los conocimientos adquiridos y desarrolla una propuesta que
              resuelve un problema práctico de la industria. Es un requisito para optar al título de
              Tecnólogo en Procesos Industriales y se desarrolla en dos momentos: la aprobación del
              anteproyecto y la presentación del proyecto final para sustentación.</p>

            <h2 id="modalidades">Modalidades</h2>
            <p>El programa contempla tres modalidades principales de trabajo de grado, más una modalidad
              especial. Todas las modalidades requieren convenio interinstitucional con la empresa u
              organización.</p>
            <ul>
              <li><strong>Trabajo de investigación.</strong> Generación o aplicación de conocimiento
                mediante una actividad intelectual rigurosa, orientada al progreso del conocimiento y su
                aplicación en beneficio de la sociedad.</li>
              <li><strong>Pasantía.</strong> Rotación o permanencia del estudiante en una comunidad o
                institución donde, bajo la dirección de un profesional experto, realiza actividades
                propias de la profesión durante el periodo académico.</li>
              <li><strong>Trabajo dirigido.</strong> Desarrollo de un proyecto específico bajo la
                dirección de un profesional del área, siguiendo el plan establecido en el anteproyecto
                aprobado.</li>
              <li><strong>Modalidad especial.</strong> Curso de profundización en Gerencia de las
                Organizaciones Industriales.</li>
            </ul>

            <h2 id="requisitos">Requisitos</h2>
            <h3>Anteproyecto</h3>
            <p>Como prerrequisitos se exige el convenio con empresa vigente o previamente tramitado, y
              la afiliación a ARL activa o previamente tramitada, anexando la certificación. Para
              tramitar la ARL por la UFPS el estudiante remite la carta de aceptación de la empresa que
              indique la modalidad y el periodo, la fotocopia de la cédula ampliada al 150 por ciento y
              la certificación de afiliación a EPS. Los documentos del anteproyecto son:</p>
            <ol>
              <li>Hoja resumen del anteproyecto. <a class="req-plantilla" href="documentos/gac-f-04-resumen-anteproyecto.docx">descargar plantilla GAC-F-04</a></li>
              <li>Carta de los estudiantes presentando el anteproyecto, dirigida al comité curricular. <a class="req-plantilla" href="documentos/gac-f-01-carta-presentacion-anteproyecto-estudiantes.docx">descargar plantilla GAC-F-01</a></li>
              <li>Carta de aceptación del director, dirigida al comité curricular. <a class="req-plantilla" href="documentos/gac-f-03-carta-aval-director-anteproyecto.docx">descargar plantilla GAC-F-03</a></li>
              <li>Carta de aceptación de la empresa, dirigida al comité curricular. <a class="req-plantilla" href="documentos/gac-f-02-carta-aval-empresa-anteproyecto.docx">descargar plantilla GAC-F-02</a></li>
              <li>Constancia de matrícula de trabajo de grado.</li>
              <li>Hoja de vida del director. <span class="req-nota">Se requiere únicamente cuando el director no es docente de la UFPS.</span></li>
              <li>Soporte de los cursos de formación complementaria. <span class="req-nota">Se requiere cuando el proyecto trata sobre el diseño de sistemas de gestión de calidad o de sistemas de gestión de seguridad y salud en el trabajo.</span></li>
              <li>Archivo del anteproyecto en formato Word y PDF, según la <a href="#estructura">estructura mínima</a>.</li>
            </ol>
            <h3>Proyecto (informe final)</h3>
            <ol>
              <li>Carta de los estudiantes presentando el proyecto, dirigida al comité curricular. <a class="req-plantilla" href="documentos/gac-f-08-carta-presentacion-proyecto-estudiantes.docx">descargar plantilla GAC-F-08</a></li>
              <li>Carta del director sobre el cumplimiento de los objetivos. <a class="req-plantilla" href="documentos/gac-f-10-carta-aval-director-proyecto.docx">descargar plantilla GAC-F-10</a></li>
              <li>Carta de la empresa sobre el cumplimiento de los objetivos. <a class="req-plantilla" href="documentos/gac-f-09-carta-aval-empresa-proyecto.docx">descargar plantilla GAC-F-09</a></li>
              <li>Carta de aprobación del anteproyecto firmada por el Director del Programa, que
                demuestre el cumplimiento del cronograma de ejecución.</li>
              <li>Certificado de terminación de materias.</li>
              <li>Constancia de matrícula de trabajo de grado.</li>
              <li>Copia de los formatos de evaluación del anteproyecto de los tres docentes
                evaluadores.</li>
              <li>Certificados de los cursos de formación complementaria. <span class="req-nota">Se requieren cuando el proyecto trata sobre el diseño de sistemas de gestión de calidad o de sistemas de gestión de seguridad y salud en el trabajo.</span></li>
            </ol>
            <p>La entrega final se organiza en una carpeta ANTEPROYECTO, con el documento en Word, las
              cartas, los formatos de evaluación y la carta de aprobación, y una carpeta PROYECTO, con el
              documento en Word, los anexos, las cartas y la terminación de materias.</p>

            <div class="aviso"><strong>Único canal autorizado:</strong> la radicación se realiza al correo
              proyectosingindustrial@ufps.edu.co. Las fechas de comité curricular se publican en el
              Facebook del programa y se envían a los correos al inicio de cada semestre. La coordinación
              no recibe documentación fuera de esas fechas ni por otros medios.</div>

            <h2 id="estructura">Estructura mínima de las entregas</h2>
            <h3>Anteproyecto</h3>
            <p>Portada, contraportada, índice, índice de tablas, índice de figuras y lista de anexos.
              Introducción. 1. Problema (título, planteamiento, formulación, justificación a nivel de la
              empresa y del estudiante, objetivos general y específicos, alcances y limitaciones). 2.
              Marco referencial (antecedentes, marco contextual, teórico, conceptual y legal). 3. Diseño
              metodológico (tipo de investigación, población y muestra, instrumentos de recolección con
              fuentes primarias y secundarias, análisis de la información). 4. Aspectos administrativos
              (recursos humanos, institucionales, materiales y financieros, y cronograma en modelo Gantt
              y CPM). Bibliografía y anexos.</p>
            <h3>Proyecto</h3>
            <p>Conserva la misma estructura inicial hasta el diseño metodológico y continúa con 4.
              Desarrollo, con un apartado por cada objetivo específico enfocado a su solución, seguido de
              conclusiones, recomendaciones, bibliografía y anexos.</p>

            <h2 id="formatos">Formatos y plantillas</h2>
            <p>Plantillas oficiales para la elaboración del anteproyecto y del proyecto. Descargue el
              formato que necesite y complételo según las indicaciones del comité curricular.</p>
            <ul class="descargas">
%(desc)s
            </ul>

            <h2 id="directores">Banco de posibles directores</h2>
            <p>Todos los docentes del Departamento de Procesos Industriales y de la Facultad de
              Ingeniería poseen el perfil idóneo para dirigir trabajos de grado. Puede consultar el
              cuerpo docente en la página de <a href="comunidad-equipo-de-trabajo.html#docentes">Equipo
              de trabajo</a> o en los directorios institucionales.</p>
            <p>Las áreas temáticas para los proyectos incluyen: calidad; métodos y tiempos; seguridad y
              salud en el trabajo; procesos industriales y de manufactura; talento humano; mantenimiento
              industrial; logística e inventarios; simulación, modelado y optimización; estudios de
              factibilidad; producción y operaciones; materiales; gestión comercial; finanzas y costos;
              y dinámica de sistemas, entre otras relacionadas con el plan de estudios.</p>

            <h2 id="reglamento">Reglamento</h2>
            <p>El desarrollo del trabajo de grado se rige por el reglamento del programa y, en el caso de
              la pasantía, por el reglamento de pasantía de Ingeniería Industrial y Tecnología en
              Procesos Industriales. El convenio interinstitucional es obligatorio en todas las
              modalidades. %(pend)s (enlazar el reglamento cuando esté disponible).</p>

            <h2 id="banco">Banco de trabajos de grado</h2>
            <p>Repositorio de anteproyectos y proyectos desarrollados por los estudiantes del programa,
              disponible para consulta como referencia. %(pend)s</p>

            <h2 id="memorias">Memorias de sensibilizaciones</h2>
            <p>Presentaciones y materiales de las reuniones informativas de trabajo de grado realizadas
              por la coordinación del programa. %(pend)s</p>''' % {
    "pend": PENDIENTE,
    "desc": "\n".join([
        descarga("GAC-F-01 Cartas de presentación del anteproyecto (estudiantes)", "DOCX", "Momento anteproyecto",
                 "documentos/gac-f-01-carta-presentacion-anteproyecto-estudiantes.docx", accion="Descargar"),
        descarga("GAC-F-02 Carta de aval de la empresa (anteproyecto)", "DOCX", "Momento anteproyecto",
                 "documentos/gac-f-02-carta-aval-empresa-anteproyecto.docx", accion="Descargar"),
        descarga("GAC-F-03 Carta de aval del director (anteproyecto)", "DOCX", "Momento anteproyecto",
                 "documentos/gac-f-03-carta-aval-director-anteproyecto.docx", accion="Descargar"),
        descarga("GAC-F-04 Resumen del anteproyecto", "DOCX", "Momento anteproyecto",
                 "documentos/gac-f-04-resumen-anteproyecto.docx", accion="Descargar"),
        descarga("GAC-F-08 Cartas de presentación del proyecto (estudiantes)", "DOCX", "Momento proyecto",
                 "documentos/gac-f-08-carta-presentacion-proyecto-estudiantes.docx", accion="Descargar"),
        descarga("GAC-F-09 Carta de aval de la empresa (proyecto)", "DOCX", "Momento proyecto",
                 "documentos/gac-f-09-carta-aval-empresa-proyecto.docx", accion="Descargar"),
        descarga("GAC-F-10 Carta de aval del director (proyecto)", "DOCX", "Momento proyecto",
                 "documentos/gac-f-10-carta-aval-director-proyecto.docx", accion="Descargar"),
    ])}

grado_indice = indice_lateral("En esta página", [
    ("Modalidades", "modalidades"), ("Requisitos", "requisitos"),
    ("Estructura de las entregas", "estructura"), ("Formatos y plantillas", "formatos"),
    ("Banco de posibles directores", "directores"), ("Reglamento", "reglamento"),
    ("Banco de trabajos de grado", "banco"), ("Memorias de sensibilizaciones", "memorias")])

pagina("el-programa-trabajos-de-grado.html", "Trabajos de grado",
       encab("Trabajos de grado", migas(("El Programa", "el-programa.html"), ("Trabajos de grado", "")),
             "Modalidades, requisitos, estructura de las entregas, formatos y bancos de directores y proyectos.")
       + contenido_lateral(grado, grado_indice + lateral_datos()))

# ==========================================================================
# INSTITUCIONAL · NORMATIVIDAD (arquetipo de descargas)
# ==========================================================================
def descarga(nombre, tipo, meta, href="#", externo=False, accion="Abrir"):
    attr = ' target="_blank" rel="noopener"' if externo else ""
    return '''            <li class="descarga">
              <span class="icono" data-tipo="%s" aria-hidden="true"></span>
              <span class="info"><span class="nom">%s</span><span class="meta">%s</span></span>
              <a class="accion" href="%s"%s>%s</a>
            </li>''' % (tipo, nombre, meta, href, attr, accion)

normatividad = '''            <p>Documentos normativos de consulta para estudiantes, docentes y graduados del
              programa. Los enlaces marcados abren el documento oficial publicado por la Universidad;
              el calendario académico se actualiza cada semestre.</p>
            <ul class="descargas">
%s
            </ul>''' % (
    "\n".join([
        descarga("Calendario Académico", "PDF", "Publicado por la UFPS. Se actualiza cada semestre.",
                 "https://ww2.ufps.edu.co/public/archivos/calendarios/14b1b7721b0736c5b89b53e8b320f5b3.pdf", externo=True, accion="Abrir en UFPS"),
        descarga("Estatuto Estudiantil", "PDF", "Reglamentación institucional vigente.",
                 "https://ww2.ufps.edu.co/public/archivos/reglamentacion/6d04e1c9b1244df469317023a7699ce6.pdf", externo=True, accion="Abrir en UFPS"),
        descarga("Compilación de normas de interés", "WEB", "Portal de normatividad de la Universidad.",
                 "https://ww2.ufps.edu.co/universidad/normatividad", externo=True, accion="Ir al portal"),
        descarga("Protocolo para salidas académicas", "PÁG", "Resumen del reglamento de visitas empresariales y salidas de campo.",
                 "institucional-reglamento-salidas.html", accion="Ver resumen"),
        descarga("Resolución de Registro Calificado", "PDF", "Resolución MEN 021555 del 12 de noviembre de 2021.",
                 "documentos/resolucion-021555-2021-registro-calificado.pdf", accion="Abrir PDF"),
    ]))

pagina("institucional-normatividad.html", "Normatividad",
       encab("Normatividad", migas(("Institucional", "institucional.html"), ("Normatividad", "")),
             "Calendario académico, estatuto estudiantil, normas de interés, protocolo de salidas y registro calificado.")
       + '''    <section class="contenido"><div class="contenedor"><div class="prosa" style="max-width:820px;">'''
       + normatividad + '''</div></div></section>''')

# ==========================================================================
# INSTITUCIONAL · PROTOCOLO / REGLAMENTO DE SALIDAS ACADÉMICAS (resumen)
# ==========================================================================
reglamento = '''            <div class="aviso">Este es un resumen con fines informativos. En caso de duda prevalece
              el reglamento oficial adoptado por el Consejo Académico de la Universidad. %(pend)s</div>

            <h2 id="proposito">Propósito y alcance</h2>
            <p>El reglamento regula las visitas técnicas empresariales, las salidas de campo, las salidas
              pedagógicas y la participación en eventos académicos, deportivos, culturales, de
              investigación o de extensión que realiza la comunidad universitaria. Su fin es articular la
              teoría con la práctica y, al mismo tiempo, preservar la integridad de quienes participan.
              Aplica a estudiantes, docentes y personal administrativo que intervengan en estas
              actividades a nivel regional, nacional o internacional.</p>
            <p>Las visitas empresariales permiten conocer de cerca el funcionamiento y los procesos de una
              organización. Las visitas técnicas o salidas pedagógicas articulan los contenidos del plan de
              estudios con los procesos productivos de las empresas seleccionadas según el perfil del grupo.
              Las salidas de campo implican contacto directo con las personas, los lugares y los hechos
              relacionados con el objeto de estudio.</p>

            <h2 id="planificacion">Planificación y aprobación</h2>
            <p>La programación de las salidas del semestre debe presentarse en los formatos correspondientes
              dentro de las fechas del calendario académico, para organizar la logística. Para racionalizar
              los recursos de transporte se recomienda programar salidas con grupos de más de veinte
              estudiantes, unificando asignaturas cuando sea posible. El permiso académico otorgado por el
              Comité Curricular, el Consejo de Facultad y el Consejo Académico permite al estudiante cumplir
              con las evaluaciones practicadas durante su ausencia.</p>
            <p>El Comité Curricular verifica, evalúa y aprueba la salida de acuerdo con el pénsum y los
              contenidos de cada asignatura, y la remite al Consejo de Facultad para su aprobación final.
              La salida solo se desarrolla si cuenta con aval institucional, disponibilidad de recursos y
              carta de aceptación o invitación formal de la empresa por visitar. No se programan salidas
              durante las fechas de primeros previos, segundos previos y exámenes finales. Las salidas
              internacionales requieren autorización de la Rectoría, concepto previo del Comité Curricular y
              del Consejo de Facultad, y gestión ante la Oficina de Relaciones Internacionales.</p>

            <h2 id="documentacion">Documentación previa</h2>
            <p>Una vez aprobada la visita, y con al menos tres semanas de anticipación, la dirección del
              programa debe remitir a la Vicerrectoría Administrativa la documentación requerida para el
              trámite de transporte. Entre los documentos se incluyen el oficio de aceptación de la empresa
              con las fechas de la visita, el formato de salidas prácticas estudiantiles, el listado
              actualizado de estudiantes matriculados generado desde la plataforma, la autorización de
              salida institucional, la autorización de salida para menores de edad y los estudios previos de
              conveniencia y oportunidad. Solo se autorizan las salidas que cumplan la totalidad de los
              requisitos. Cuando la actividad exige pernoctar, se tramita además la solicitud de viáticos del
              docente responsable.</p>

            <h2 id="transporte">Requisitos del transporte</h2>
            <p>La empresa de transporte debe estar legalmente constituida y contar con la resolución de
              habilitación para prestar el servicio público de pasajeros en la modalidad de servicio
              especial, así como con antecedentes y documentación al día. Los vehículos deben tener tarjeta
              de propiedad, SOAT, revisión técnico-mecánica y de gases, tarjeta de operación y las pólizas de
              responsabilidad civil vigentes, y no superar los diez años de rodamiento. Los conductores deben
              contar con licencia de conducción para el servicio público vigente, con la categoría
              correspondiente al vehículo, y sin multas por prestación indebida del servicio.</p>

            <h2 id="viaje">Durante el viaje</h2>
            <p>Todos los pasajeros viajan sentados y ocupan un solo puesto, sin superar la capacidad
              autorizada del vehículo. El vehículo debe portar el equipo de prevención y seguridad de
              carretera, botiquín y extintor. Solo asisten los estudiantes y docentes reportados en el
              formato de la salida; no se autoriza el ingreso de otras personas, incluidos familiares.</p>

            <h2 id="deberes">Derechos y deberes de los participantes</h2>
            <p>El estudiante tiene derecho a beneficiarse plenamente de la actividad, recibir la debida
              inducción, estar amparado por el seguro estudiantil y estar afiliado al sistema de seguridad
              social en salud. Entre sus deberes están portar el documento de identidad y el carné de la
              UFPS, contar con la autorización firmada de los padres o tutores en caso de ser menor de edad,
              acatar las orientaciones del docente encargado, mantener buen comportamiento, cumplir los
              horarios, usar únicamente el transporte autorizado, emplear los elementos de protección
              personal indicados y hacer buen uso de las instalaciones visitadas.</p>
            <p>El docente a cargo es la máxima autoridad académica y disciplinaria durante toda la actividad.
              Entre sus obligaciones están gestionar la solicitud ante la dirección del programa, conseguir
              la empresa y los permisos, presentar el cronograma de trabajo, evitar desvíos de la ruta y
              vigilar el comportamiento del grupo.</p>

            <h2 id="prohibiciones">Prohibiciones para los estudiantes</h2>
            <ul>
              <li>Portar o consumir licor o sustancias psicoactivas.</li>
              <li>Ausentarse o separarse del grupo, o permanecer en sitios distintos a los establecidos.</li>
              <li>Portar cualquier tipo de arma.</li>
              <li>Realizar actos violentos o malos tratos a compañeros, transportistas, docentes o personal
                de la empresa visitada.</li>
              <li>Desobedecer las órdenes o los lineamientos del docente responsable de la salida.</li>
            </ul>''' % {"pend": PENDIENTE}

reglamento_indice = indice_lateral("En esta página", [
    ("Propósito y alcance", "proposito"), ("Planificación y aprobación", "planificacion"),
    ("Documentación previa", "documentacion"), ("Requisitos del transporte", "transporte"),
    ("Durante el viaje", "viaje"), ("Derechos y deberes", "deberes"),
    ("Prohibiciones", "prohibiciones")])

pagina("institucional-reglamento-salidas.html", "Protocolo para salidas académicas",
       encab("Protocolo para salidas académicas", migas(("Institucional", "institucional.html"),
             ("Normatividad", "institucional-normatividad.html"), ("Protocolo para salidas académicas", "")),
             "Resumen del reglamento de visitas técnicas empresariales, salidas de campo y salidas pedagógicas de la UFPS.")
       + contenido_lateral(reglamento, reglamento_indice))

# ==========================================================================
# INSTITUCIONAL · FORMATOS Y DESCARGAS
# ==========================================================================
formatos = '''            <p>Repositorio de formatos, plantillas y documentos oficiales de uso frecuente en el
              programa.</p>
            <ul class="descargas">
%s
            </ul>
''' % (
    "\n".join([
        descarga("Proyecto Educativo del Programa (PEP)", "PDF", "Documento oficial publicado por la UFPS.",
                 "https://ww2.ufps.edu.co/public/archivos/oferta_academica/7ed0c42bfb51c2edd45215411ace6ed1.pdf", externo=True, accion="Abrir"),
        descarga("Instructivo Estudiantil de la Facultad de Ingeniería", "PDF", "Guía de los trámites más frecuentes.",
                 "documentos/instructivo-estudiantil-facultad-ingenieria.pdf", accion="Abrir"),
        descarga("Reglamento de Prácticas Industriales", "PDF", "Programa de Tecnología en Procesos Industriales.",
                 "documentos/reglamento-practicas-industriales.pdf", accion="Abrir"),
        descarga("Formatos de trabajo de grado (GAC-F)", "DOCX", "Plantillas de anteproyecto y proyecto.",
                 "el-programa-trabajos-de-grado.html#formatos", accion="Ver"),
        descarga("Formato de hoja de vida para prácticas", "DOCX", "Plantilla editable para la práctica.",
                 "documentos/formato-hoja-de-vida-practica.docx", accion="Descargar"),
        descarga("Carta de autorización de cambio de pénsum", "DOCX", "Formato para el trámite de cambio de pénsum.",
                 "documentos/carta-autorizacion-cambio-de-pensum.docx", accion="Descargar"),
    ]))

pagina("institucional-formatos-descargas.html", "Formatos y descargas",
       encab("Formatos y descargas", migas(("Institucional", "institucional.html"), ("Formatos y descargas", "")),
             "Formatos, plantillas y documentos oficiales para estudiantes, docentes y graduados.")
       + '''    <section class="contenido"><div class="contenedor"><div class="prosa" style="max-width:820px;">'''
       + formatos + '''</div></div></section>''')

# ==========================================================================
# COMUNIDAD · EQUIPO DE TRABAJO (arquetipo directorio)
# ==========================================================================
def persona(nombre, rol, correo=""):
    iniciales = "".join([p[0] for p in nombre.split()[:2]]).upper()
    mail = '<div class="mail"><a href="mailto:%s">%s</a></div>' % (correo, correo) if correo else '<div class="mail">%s</div>' % PENDIENTE
    return '''            <div class="persona">
              <div class="avatar" aria-hidden="true">%s</div>
              <div class="nom">%s</div>
              <div class="rol">%s</div>
              %s
            </div>''' % (iniciales, nombre, rol, mail)

equipo = '''            <h2 id="coordinacion">Coordinación</h2>
            <div class="personas">
%s
            </div>
            <h2 id="comite">Comité Curricular</h2>
            <p>El comité curricular es el máximo ente de dirección académica del programa, liderado por
              la coordinación. Está conformado por representantes de los docentes, los estudiantes y los
              graduados. %s</p>
            <h2 id="docentes">Cuerpo docente</h2>
            <p>El detalle del cuerpo docente, con su formación y áreas de trabajo, se relaciona a
              continuación.</p>
            <div class="personas">
%s
            </div>
            <h2 id="administrativos">Personal administrativo</h2>
            <div class="personas">
%s
            </div>''' % (
    persona(D["coordinador"], "Coordinador del programa", D["correo"]),
    PENDIENTE,
    "\n".join([persona("Docente por definir", "Docente"), persona("Docente por definir", "Docente"),
               persona("Docente por definir", "Docente")]),
    persona("Por definir", "Apoyo administrativo"))

equipo_indice = indice_lateral("En esta página", [
    ("Coordinación", "coordinacion"), ("Comité Curricular", "comite"),
    ("Cuerpo docente", "docentes"), ("Personal administrativo", "administrativos")])

pagina("comunidad-equipo-de-trabajo.html", "Equipo de Trabajo",
       encab("Equipo de Trabajo", migas(("Comunidad", "comunidad.html"), ("Equipo de Trabajo", "")),
             "Comité curricular, coordinación, cuerpo docente y personal administrativo del programa.")
       + contenido_lateral(equipo, equipo_indice))

# ==========================================================================
# VÍNCULOS · PROYECCIÓN SOCIAL / EXTENSIÓN (subsecciones)
# ==========================================================================
proyeccion = '''            <h2 id="convenios">Convenios</h2>
            <p>Las prácticas, las pasantías y los trabajos de grado se desarrollan bajo la figura de un
              convenio interinstitucional vigente entre la empresa y la Universidad. El programa gestiona
              estos convenios con empresas e instituciones de la región, el país y el exterior.</p>
            <p><a class="boton boton--rojo" href="https://docs.google.com/spreadsheets/d/1SVUSM9iiXUk-kSnkfMKQLsq2ZBXrx_P2oW6q28LUGmA/edit?gid=1695155128#gid=1695155128" target="_blank" rel="noopener">Ver convenios vigentes de la Facultad de Ingeniería</a></p>

            <h3>Documentación para generar un convenio</h3>
            <ul>
              <li>Declaración compromisoria (formato firmado).</li>
              <li>Minuta del convenio editada y firmada (formato firmado).</li>
              <li>Copia del documento de identidad del representante legal.</li>
              <li>Copia de la Cámara de Comercio de la empresa (máximo 90 días de expedición).</li>
            </ul>
            <p>Envíe los documentos al correo
              <a href="mailto:practicasingindustrial@ufps.edu.co">practicasingindustrial@ufps.edu.co</a>
              si el convenio es para prácticas, o a
              <a href="mailto:proyectosingindustrial@ufps.edu.co">proyectosingindustrial@ufps.edu.co</a>
              si el convenio es para trabajo de grado o pasantía.</p>

            <h3>Plantillas de convenio</h3>
            <ul class="descargas">
%(desc_conv)s
            </ul>

            <h2 id="practicas">Prácticas</h2>
            <p>La práctica industrial es una asignatura del sexto semestre en la que el estudiante se
              vincula a una empresa pública o privada durante un semestre académico, por un periodo no
              inferior a dieciséis semanas ni superior a veinticuatro, con una intensidad mínima de 240
              horas en jornada diurna. El programa reconoce dos modalidades: práctica profesional y
              práctica investigativa. Toda práctica requiere convenio interinstitucional o contrato de
              aprendizaje, y la afiliación del estudiante a seguridad social en salud y a riesgos
              laborales.</p>
            <p><a class="boton boton--rojo" href="documentos/reglamento-practicas-industriales.pdf" target="_blank" rel="noopener">Reglamento de Prácticas Industriales (PDF)</a></p>

            <h3>Requisitos de legalización</h3>
            <p>Se entregan al inicio del semestre, en las fechas que indica el coordinador del programa
              según el calendario vigente:</p>
            <ol>
              <li>Formato de presentación de prácticas (lo entrega el profesor).</li>
              <li>Certificado de afiliación a ARL.</li>
              <li>Carta de aceptación de la empresa para el desarrollo de la práctica.</li>
              <li>Copia de la declaración compromisoria entregada en el convenio.</li>
              <li>Si es un convenio nuevo, anexar la minuta firmada (formato de convenio).</li>
            </ol>
            <p>El trámite de afiliación a riesgos laborales se explica en
              <a href="institucional-tramites.html#arl">Afiliación a ARL para práctica o trabajo de
              grado</a>.</p>

            <h3>Recursos</h3>
            <ul class="lista-enlaces">
              <li><a href="https://docs.google.com/spreadsheets/d/1XQp16ryso_C45Jmnel7uSaU0soOIdLVpu9MLVObXayY/edit?usp=sharing" target="_blank" rel="noopener">Repositorio de proyectos realizados</a></li>
              <li><a href="vinculos-vacantes.html">Vacantes activas de práctica</a></li>
              <li><a href="documentos/formato-hoja-de-vida-practica.docx">Modelo de hoja de vida para prácticas</a> (formato Word)</li>
            </ul>

            <h2 id="cursos">Cursos</h2>
            <p>Cursos de formación complementaria en temáticas propias de la profesión, con intensidad
              horaria certificable. %(pend)s</p>

            <h2 id="movilidades">Movilidades</h2>
            <p>Oportunidades de movilidad académica nacional e internacional para estudiantes y
              docentes del programa.</p>
            <ul class="lista-enlaces">
              <li><a href="#">Salidas nacionales</a></li>
              <li><a href="#">Movilidades internacionales</a></li>
            </ul>

            <h2 id="eventos">Eventos</h2>
            <p>Espacios académicos que conectan la academia con la industria:</p>
            <ul class="lista-enlaces">
              <li><a href="#">Congresos</a></li>
              <li><a href="#">ExpoIndustria</a></li>
              <li><a href="#">Semana de la Tecnología en Procesos Industriales</a></li>
            </ul>''' % {
    "pend": PENDIENTE,
    "desc_conv": "\n".join([
        descarga("Formato de convenio interinstitucional", "DOCX", "Minuta del convenio",
                 "documentos/formato-convenio-interinstitucional.docx", accion="Descargar"),
        descarga("Declaración compromisoria para convenio", "DOCX", "Formato para firmar",
                 "documentos/declaracion-compromisoria-convenio.docx", accion="Descargar"),
    ])}

proy_indice = indice_lateral("En esta página", [
    ("Convenios", "convenios"), ("Prácticas", "practicas"), ("Cursos", "cursos"),
    ("Movilidades", "movilidades"), ("Eventos", "eventos")])

pagina("vinculos-proyeccion-social.html", "Proyección social / Extensión",
       encab("Proyección social / Extensión", migas(("Vínculos", "vinculos.html"), ("Proyección social / Extensión", "")),
             "Convenios, prácticas, cursos de extensión, movilidades y eventos del programa.")
       + contenido_lateral(proyeccion, proy_indice))

# --- Vacantes activas de práctica (grilla editable por el administrador) ---
vacantes_cuerpo = '''            <p>Ofertas de práctica publicadas por las empresas. Cada recuadro corresponde a la pieza
              gráfica enviada por una empresa. Para postularse, siga las indicaciones de contacto que
              aparecen en cada pieza.</p>
            <div class="aviso"><strong>Para el administrador del sitio:</strong> las piezas gráficas se
              administran en el archivo <strong>vinculos-vacantes.html</strong>. Guarde cada imagen en la
              carpeta <strong>assets/img/vacantes/</strong> y copie un bloque de vacante por cada una;
              para retirar una oferta, borre su bloque. Hay instrucciones dentro del código, justo antes
              de la grilla.</div>

            <!-- ============================================================
                 GRILLA DE VACANTES
                 Para AÑADIR una vacante, copie este bloque y cambie la imagen,
                 el texto alternativo y, si aplica, el enlace de contacto:

                   <a class="vacante" href="ENLACE_O_CORREO">
                     <img src="assets/img/vacantes/NOMBRE-DE-LA-IMAGEN.jpg"
                          alt="Vacante de práctica en EMPRESA">
                   </a>

                 Si la pieza no lleva enlace, use un <div class="vacante"> en lugar del <a>.
                 Para QUITAR una vacante, borre su bloque completo.
                 ============================================================ -->
            <div class="vacantes-grid">
              <div class="vacante vacante--vacia">Espacio para la pieza gráfica de la empresa</div>
              <div class="vacante vacante--vacia">Espacio para la pieza gráfica de la empresa</div>
              <div class="vacante vacante--vacia">Espacio para la pieza gráfica de la empresa</div>
            </div>
            <p style="margin-top:22px;">%(pend)s (a la espera de las piezas gráficas de las empresas).</p>''' % {"pend": PENDIENTE}

pagina("vinculos-vacantes.html", "Vacantes activas de práctica",
       encab("Vacantes activas de práctica",
             migas(("Vínculos", "vinculos.html"),
                   ("Proyección social / Extensión", "vinculos-proyeccion-social.html"),
                   ("Vacantes activas", "")),
             "Ofertas de práctica publicadas por las empresas aliadas del programa.")
       + '''    <section class="contenido"><div class="contenedor"><div class="prosa">'''
       + vacantes_cuerpo + '''</div></div></section>''')

# ==========================================================================
# VÍNCULOS · REDES ACADÉMICAS
# ==========================================================================
redes_ac = '''            <p>El programa participa en redes y organismos que articulan la formación en
              ingeniería y tecnología con estándares nacionales e internacionales.</p>
            <div class="tarjetas">
              <div class="tarjeta" id="acofi"><h3>ACOFI / Redin</h3><p>Asociación Colombiana de Facultades de
                Ingeniería y Red de Ingeniería.</p><a class="abrir" href="https://www.acofi.edu.co/" target="_blank" rel="noopener">Visitar sitio</a></div>
              <div class="tarjeta" id="copnia"><h3>COPNIA</h3><p>Consejo Profesional Nacional de Ingeniería.</p>
                <a class="abrir" href="https://www.copnia.gov.co/" target="_blank" rel="noopener">Visitar sitio</a></div>
              <div class="tarjeta" id="redcolsi"><h3>RedColsi</h3><p>Red Colombiana de Semilleros de Investigación.</p>
                <a class="abrir" href="https://www.fundacionredcolsi.org/" target="_blank" rel="noopener">Visitar sitio</a></div>
            </div>
            <div class="aviso">Verifique la vigencia de la participación del programa en cada red. %s</div>''' % PENDIENTE

pagina("vinculos-redes-academicas.html", "Redes académicas",
       encab("Redes académicas", migas(("Vínculos", "vinculos.html"), ("Redes académicas", "")),
             "Participación del programa en ACOFI, Redin, COPNIA y RedColsi.")
       + '''    <section class="contenido"><div class="contenedor"><div class="prosa">'''
       + redes_ac + '''</div></div></section>''')

# ==========================================================================
# COMUNIDAD · REDES SOCIALES
# ==========================================================================
redes_soc = '''            <p>Sigue los canales oficiales del programa para enterarte de convocatorias,
              eventos, prácticas y noticias.</p>
            <div class="tarjetas">
              <div class="tarjeta"><h3>Instagram</h3><p>@tecprocesos_ufps</p>
                <a class="abrir" href="%s" target="_blank" rel="noopener">Abrir Instagram</a></div>
              <div class="tarjeta"><h3>Facebook</h3><p>Tecprocesos UFPS</p>
                <a class="abrir" href="%s" target="_blank" rel="noopener">Abrir Facebook</a></div>
            </div>''' % (D["instagram"], D["facebook"])

pagina("comunidad-redes-sociales.html", "Redes sociales del programa",
       encab("Redes sociales del programa", migas(("Comunidad", "comunidad.html"), ("Redes sociales del programa", "")),
             "Canales oficiales del programa en Instagram y Facebook.")
       + '''    <section class="contenido"><div class="contenedor"><div class="prosa">'''
       + redes_soc + '''</div></div></section>''')

# ==========================================================================
# PÁGINAS DE ANDAMIAJE (contenido por complementar)
# ==========================================================================
def scaffold(slug, titulo, padre_nombre, padre_slug, intro, secciones):
    bloques = ""
    for sec in secciones:
        h, texto = sec[0], sec[1]
        hid = (' id="%s"' % sec[2]) if len(sec) > 2 else ""
        bloques += '            <h2%s>%s</h2>\n            <p>%s</p>\n' % (hid, h, texto)
    bloques += '            <p>%s</p>' % PENDIENTE
    cuerpo = encab(titulo, migas((padre_nombre, padre_slug), (titulo, "")), intro) \
        + contenido_lateral(bloques, lateral_datos())
    pagina(slug, titulo, cuerpo)

# --- Trámites (con anclas y subtítulo por trámite; el paso a paso queda pendiente) ---
def bloque_tramites(titulo_grupo, ancla, items):
    h3s = ""
    for it in items:
        if isinstance(it, tuple):
            nom, cont = it[0], it[1]
            tid = (' id="%s"' % it[2]) if len(it) > 2 else ""
            h3s += '            <h3%s>%s</h3>\n%s\n' % (tid, nom, cont)
        else:
            h3s += '            <h3>%s</h3>\n            <p>Procedimiento por documentar. %s</p>\n' % (it, PENDIENTE)
    return '            <h2 id="%s">%s</h2>\n%s' % (ancla, titulo_grupo, h3s)

_arl_desc = '''            <p>Trámite para afiliar al estudiante al Sistema General de Riesgos Laborales (ARL)
              a través de la UFPS, requisito indispensable para iniciar la práctica o el trabajo de grado.
              Requisitos:</p>
            <ol>
              <li>Carta de aceptación de la empresa, donde se relacione el periodo en el que se realizará
                la práctica o el trabajo de grado, el área donde trabajará y el horario de trabajo.</li>
              <li>Fotocopia de la cédula del estudiante, ampliada al 150 por ciento.</li>
              <li>Certificación de afiliación a EPS del estudiante (no es válida la certificación de
                ADRES o Fosyga).</li>
            </ol>
            <p>Envíe los documentos al correo
              <a href="mailto:practicasingindustrial@ufps.edu.co">practicasingindustrial@ufps.edu.co</a>
              si la afiliación es para prácticas, o a
              <a href="mailto:proyectosingindustrial@ufps.edu.co">proyectosingindustrial@ufps.edu.co</a>
              si es para trabajo de grado o pasantía.</p>'''

_t_pensum = '''            <p>El cambio de pénsum es un procedimiento reglamentado por la Universidad que el
              estudiante realiza de manera individual, dentro de los plazos y fechas del calendario
              académico vigente. La solicitud se presenta ante el plan de estudios. Requisitos:</p>
            <ol>
              <li>Soporte del pago de los derechos de cambio de pénsum, según los derechos pecuniarios
                vigentes. El recibo se genera desde Divisist, en Recibos de Pago, opción Constancias,
                seleccionando CAMBIO DE PENSUM, y se paga en el banco indicado o en línea por PSE.</li>
              <li>Carta firmada por el estudiante en la que da su consentimiento para el cambio.</li>
            </ol>
            <ul class="descargas">
''' + descarga("Carta de autorización de cambio de pénsum", "DOCX", "Formato para diligenciar y firmar",
               "documentos/carta-autorizacion-cambio-de-pensum.docx", accion="Descargar") + '''
''' + descarga("Instructivo de pago del cambio de pénsum", "PDF", "Guía paso a paso en Divisist",
               "documentos/instructivo-pago-cambio-de-pensum.pdf", accion="Abrir") + '''
            </ul>'''

_t_cancel = '''            <p>La cancelación del semestre académico se solicita dentro de las seis primeras
              semanas de clase, sin que queden calificaciones en la hoja de vida académica. Dentro de ese
              plazo se tramita ante la División de Admisiones y Registro; pasado ese plazo se tramita de
              manera extemporánea ante la Facultad de Ingeniería.</p>
            <p><strong>Cancelación ordinaria</strong> (primeras seis semanas): presente la solicitud por
              escrito al Vicerrector Asistente de Estudios, al correo
              <a href="mailto:admisiones@ufps.edu.co">admisiones@ufps.edu.co</a>, para anular la matrícula
              académica sin registro de notas.</p>
            <p><strong>Cancelación extemporánea</strong> (por fuerza mayor o caso fortuito): solicite por
              escrito ante el Consejo de Facultad de Ingeniería exponiendo los motivos, y remita la
              solicitud y los soportes al formulario que indica la Facultad, al correo
              <a href="mailto:facuingenieria@ufps.edu.co">facuingenieria@ufps.edu.co</a>, adjuntando la
              fotocopia de la matrícula académica y el soporte del caso. El Consejo analiza y aprueba o no
              la solicitud.</p>
            <p>El detalle de este y otros trámites está en el Instructivo Estudiantil de la Facultad de
              Ingeniería, disponible en <a href="institucional-formatos-descargas.html">Formatos y
              descargas</a>.</p>'''

_t_contenidos = '''            <p>Proceso completo de certificación de contenidos programáticos.</p>
            <p><strong>A. Pagos.</strong> Genere los recibos en
              <a href="https://acceso.ufps.edu.co/" target="_blank" rel="noopener">acceso.ufps.edu.co</a>
              (previo registro) y cancele: el derecho de contenidos programáticos (programas técnicos y
              tecnológicos de pregrado), el certificado de notas en papel de seguridad, el certificado de
              buena conducta y la estampilla Pro-Hospital. La estampilla no se adquiere en la página de la
              UFPS, sino en la Secretaría de Hacienda Departamental de Norte de Santander (Gobernación).</p>
            <p><strong>B. Solicitud de certificados a Admisiones.</strong> Realizados los pagos, ingrese a
              <a href="https://divisist2.ufps.edu.co/solicitud" target="_blank" rel="noopener">divisist2.ufps.edu.co/solicitud</a>,
              opción Graduado, y solicite el certificado de notas y el certificado de buena conducta,
              adjuntando los soportes de pago. También puede enviar la solicitud a
              <a href="mailto:admisiones@ufps.edu.co">admisiones@ufps.edu.co</a>.</p>
            <p><strong>C. Envío de la solicitud de contenidos programáticos.</strong> Obtenidos los
              certificados de Admisiones, envíe su solicitud al correo del programa,
              <a href="mailto:ingindustrial@ufps.edu.co">ingindustrial@ufps.edu.co</a>, adjuntando en PDF
              el pago del derecho de contenidos programáticos, el certificado de notas en papel de
              seguridad, el certificado de buena conducta y la estampilla Pro-Hospital.</p>'''

_t_vacacional = '''            <p>El estudiante que a lo largo del semestre identifique la necesidad de cursar un
              vacacional debe presentar la solicitud ante el comité curricular antes de las fechas de
              segundos previos, para que el Comité estudie la posibilidad de ofertarlo al final del
              semestre.</p>
            <p>Cuando el calendario académico lo establezca, consulte el listado de cursos vacacionales
              autorizados por el plan de estudios en
              <a href="https://evaldocente.ufps.edu.co/admitidos/vacacionales/index.php" target="_blank" rel="noopener">el portal de vacacionales</a>
              y siga los pasos para la inscripción y el pago, siempre que acredite el cumplimiento de los
              prerrequisitos del curso.</p>'''

_t_valida = '''            <p>Los exámenes de validación se presentan en ocasiones extraordinarias, previa
              autorización del Consejo de Facultad, para reconocer cursos aprobados en otras universidades
              que no han sido aceptados, o para comprobar la idoneidad en materias en las que el estudiante
              tiene los conocimientos pero no los créditos. Condiciones:</p>
            <ul>
              <li>Se realizan antes de la matrícula académica del periodo.</li>
              <li>Solo se pueden validar dos asignaturas por semestre.</li>
              <li>Las asignaturas teóricas reprobadas y todas las asignaturas prácticas no se validan.</li>
              <li>No tienen habilitación ni supletorio.</li>
              <li>La prueba es oral y escrita; la nota mínima para aprobar es cuatro coma cero (4,0).</li>
            </ul>
            <p>Pasos:</p>
            <ol>
              <li>Enviar una comunicación escrita a la Facultad para concertar el día y la hora del
                examen.</li>
              <li>Diligenciar los formatos institucionales requeridos (formato de solicitudes de
                Admisiones y Registro).</li>
              <li>Presentar la prueba ante los docentes asignados como jurados, para el registro formal de
                la nota.</li>
            </ol>'''

_t_saber = '''            <p>Proceso de inscripción a las Pruebas Saber TyT. Todo el proceso está supeditado al
              calendario nacional que publique el ICFES.</p>
            <p><strong>Requisitos previos:</strong> haber aprobado al menos el 75 por ciento de los
              créditos del programa y ser estudiante activo.</p>
            <p>Paso a paso:</p>
            <ol>
              <li>Preregistro en Divisist 2.0: ingrese al portal, busque la inscripción a las pruebas y
                verifique que sus datos personales y de contacto estén actualizados.</li>
              <li>Preinscripción institucional: la Vicerrectoría Asistente de Estudios realiza la solicitud
                ante el ICFES con base en los datos de Divisist.</li>
              <li>Credenciales de acceso: recibirá un correo del ICFES con el usuario y la contraseña
                provisional para la plataforma Prisma.</li>
              <li>Inscripción en Prisma: ingrese, cambie la contraseña, complete el formulario de
                caracterización (información personal, académica, socioeconómica y de citación) y confirme
                la preinscripción.</li>
              <li>Pago del examen: genere la referencia de pago y pague dentro de las fechas establecidas,
                en banco o por PSE. La inscripción solo es válida tras registrar el pago.</li>
              <li>Citación y presentación: consulte la fecha, la hora y el lugar en Prisma y asista con su
                documento de identidad.</li>
            </ol>'''

_t_cartas = '''            <p>Las cartas de presentación se solicitan diligenciando el formulario dispuesto por el
              programa. Tienen un costo que debe pagarse previamente, con el recibo generado desde
              Divisist. En el formulario debe indicar si la carta la requiere para práctica o para trabajo
              de grado.</p>
            <p><a class="boton boton--rojo" href="https://docs.google.com/forms/d/e/1FAIpQLSfSonb2cYF063VtxnPSL2JS2DuV8JRl7PjAUBuBq22ycOkSg/viewform?usp=send_form" target="_blank" rel="noopener">Abrir el formulario de solicitud</a></p>'''

_t_constancias = '''            <p>Las constancias de estudio, el certificado de calificaciones y la actualización del
              documento de identidad se solicitan en
              <a href="https://divisist2.ufps.edu.co/solicitud" target="_blank" rel="noopener">divisist2.ufps.edu.co/solicitud</a>,
              y las atiende la Vicerrectoría Asistente de Estudios. Antes de solicitarlas, el estudiante
              debe generar y pagar el recibo correspondiente desde Divisist, según el tipo de constancia.</p>
            <p>El plan de estudios no expide constancias de estudio: únicamente Admisiones y Registro está
              facultada para ello.</p>'''

_t_reintegro = '''            <p>Se considera reintegro el retorno de un estudiante que se retiró de la Universidad sin
              reserva de cupo (Estatuto Estudiantil, Título II, Capítulo II). El procedimiento depende del
              tiempo que lleve sin estudiar.</p>
            <p><strong>Menos de un año sin estudiar:</strong> presente la solicitud de activación de
              código a la Vicerrectoría Asistente de Estudios, exponiendo los motivos. Tenga en cuenta la
              fecha límite del calendario académico.</p>
            <p><strong>Más de un año sin estudiar:</strong></p>
            <ol>
              <li>Consulte con el director del programa si necesita cambio de pénsum; de ser así,
                solicítelo al director.</li>
              <li>Presente la solicitud de reintegro al Consejo de Facultad de Ingeniería exponiendo los
                motivos (<a href="https://drive.google.com/uc?id=1lVIjcLEXP5zSjnaGJQu6i_qmYDHuI3F&amp;export=download&amp;authuser=0" target="_blank" rel="noopener">descargar formato de reintegro</a>).</li>
              <li>Tenga en cuenta la fecha límite del calendario académico y, si requiere cambio de
                pénsum, adjunte la solicitud con el recibo de pago.</li>
              <li>Solicite al correo <a href="mailto:facuingenieria@ufps.edu.co">facuingenieria@ufps.edu.co</a>
                el enlace al formulario de Google para adjuntar los documentos requeridos.</li>
            </ol>
            <p>Las solicitudes de reintegro se reciben a partir de un mes antes de la fecha límite del
              calendario académico. El procedimiento completo está en el Instructivo Estudiantil de la
              Facultad, disponible en <a href="institucional-formatos-descargas.html">Formatos y
              descargas</a>.</p>'''

_t_destacado = '''            <p>Los graduados interesados en mantener un vínculo permanente con el programa y exponer
              sus logros pueden unirse al grupo de WhatsApp del programa y, una vez allí, contactar al
              administrador del grupo, que es el director o coordinador del programa, para expresar su
              interés en ser publicados en la próxima convocatoria de graduado destacado, adjuntando una
              breve reseña de sus logros laborales y empresariales y su hoja de vida académica.</p>
            <p><a class="boton boton--rojo" href="https://chat.whatsapp.com/IPOpPHNvnOyHObD6foQYlM" target="_blank" rel="noopener">Unirse al grupo de graduados</a></p>'''

_t_constancias_grad = '''            <p>Para los graduados, la expedición de certificaciones, incluida la generación y el pago
              de los recibos, se canaliza por
              <a href="https://acceso.ufps.edu.co/" target="_blank" rel="noopener">acceso.ufps.edu.co</a>,
              y la solicitud se realiza desde
              <a href="https://divisist2.ufps.edu.co/solicitud" target="_blank" rel="noopener">divisist2.ufps.edu.co/solicitud</a>.</p>'''

tramites_cuerpo = '''            <p>Guía de los trámites académicos y administrativos del programa. Varios trámites se
              gestionan ante instancias de la Universidad (Admisiones y Registro, Vicerrectoría Asistente
              de Estudios o Facultad de Ingeniería) y a través de los portales institucionales. Realícelos
              dentro de las fechas del calendario académico vigente.</p>
''' + bloque_tramites("Trámites estudiantiles", "estudiantiles", [
    ("Cambio de pénsum", _t_pensum, "pensum"),
    ("Cancelación de semestre", _t_cancel, "cancelacion"),
    ("Certificación de contenidos programáticos", _t_contenidos, "contenidos"),
    ("Cursos vacacionales", _t_vacacional, "vacacionales"),
    ("Exámenes de validación", _t_valida, "validacion"),
    ("Inscripción a Pruebas Saber TyT", _t_saber, "saber-tyt"),
    ("Afiliación a ARL para práctica o trabajo de grado", _arl_desc, "arl"),
    ("Solicitud de cartas de presentación", _t_cartas, "cartas"),
    ("Solicitud de constancias y certificados", _t_constancias, "constancias"),
    ("Solicitud de reintegro y activación de código", _t_reintegro, "reintegro")]) \
+ bloque_tramites("Trámites de graduados", "graduados", [
    ("Certificación de contenidos programáticos", _t_contenidos, "contenidos-grad"),
    ("Postulación a Egresado de Calidad o Destacado", _t_destacado, "destacado"),
    ("Solicitud de constancias y certificados", _t_constancias_grad, "constancias-grad")])

pagina("institucional-tramites.html", "Trámites",
       encab("Trámites", migas(("Institucional", "institucional.html"), ("Trámites", "")),
             "Trámites académicos y administrativos para estudiantes y graduados del programa.")
       + contenido_lateral(tramites_cuerpo,
             indice_lateral("Trámites estudiantiles", [
                 ("Cambio de pénsum", "pensum"), ("Cancelación de semestre", "cancelacion"),
                 ("Contenidos programáticos", "contenidos"), ("Cursos vacacionales", "vacacionales"),
                 ("Exámenes de validación", "validacion"), ("Pruebas Saber TyT", "saber-tyt"),
                 ("Afiliación a ARL", "arl"), ("Cartas de presentación", "cartas"),
                 ("Constancias y certificados", "constancias"), ("Reintegro y activación", "reintegro")])
             + indice_lateral("Trámites de graduados", [
                 ("Contenidos programáticos", "contenidos-grad"),
                 ("Egresado de Calidad o Destacado", "destacado"),
                 ("Constancias y certificados", "constancias-grad")]) + lateral_datos()))

scaffold("institucional-autoevaluacion.html", "Autoevaluación", "Institucional", "institucional.html",
         "La autoevaluación es un proceso permanente, participativo y reflexivo orientado al mejoramiento continuo.",
         [("Informes de autoevaluación del programa", "Resultados del proceso de autoevaluación del programa y planes de mejoramiento derivados, en el marco del ciclo de calidad institucional.", "informes")])

scaffold("comunidad-consejo-aneiap.html", "Consejo Estudiantil y ANEIAP", "Comunidad", "comunidad.html",
         "Representación estudiantil del programa y capítulo de la Asociación Nacional de Estudiantes de Ingeniería Industrial y afines.",
         [("Consejo Estudiantil", "Órgano de representación de los estudiantes ante las instancias del programa y la Facultad."),
          ("ANEIAP", "Capítulo estudiantil orientado al liderazgo, la formación integral y la proyección profesional.")])

scaffold("comunidad-graduados.html", "Graduados", "Comunidad", "comunidad.html",
         "Los graduados son parte esencial del programa y reflejan la calidad de la formación ofrecida.",
         [("Encuentros y coloquios", "Encuentros de graduados y coloquios que mantienen el vínculo con la comunidad egresada."),
          ("Directorios", "Directorio de emprendedores y directorio de consultores egresados del programa.")])

scaffold("comunidad-intermediacion-laboral.html", "Intermediación Laboral", "Comunidad", "comunidad.html",
         "Servicios de conexión de estudiantes y graduados con las oportunidades del sector productivo.",
         [("Bolsa de empleo", "Publicación de vacantes y oportunidades laborales para estudiantes y graduados del programa, en articulación con las empresas de la región.")])

print("\\nSitio generado.")

# ==========================================================================
# ÍNDICE DE BÚSQUEDA (client-side, sin servidor)
# ==========================================================================
import re as _re, html as _html, json as _json, glob as _glob

def _limpiar(fragmento):
    h = _re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', fragmento, flags=_re.S | _re.I)
    h = _re.sub(r'<[^>]+>', ' ', h)
    h = _html.unescape(h)
    return _re.sub(r'\s+', ' ', h).strip()

_CAT = {"index.html": "Inicio"}
for _cat, _cs, _hijos in NAV:
    _CAT[_cs] = _cat
    for _l2 in _hijos:
        _CAT[_l2[1]] = _cat

_entradas = []
for _p in sorted(_glob.glob(os.path.join(RAIZ, "*.html"))):
    _slug = os.path.basename(_p)
    if _slug == "PLANTILLA-pagina-contenido.html":
        continue
    _raw = open(_p, encoding="utf-8").read()
    _m = _re.search(r'<main.*?>(.*?)</main>', _raw, flags=_re.S | _re.I)
    _body = _m.group(1) if _m else _raw
    _h1 = _re.search(r'<h1[^>]*>(.*?)</h1>', _raw, flags=_re.S)
    _tit = _limpiar(_h1.group(1)) if _h1 else _slug
    _cat = _CAT.get(_slug, "")
    _entradas.append({"t": _tit, "s": _cat, "u": _slug, "x": _limpiar(_body)[:1100]})
    # entradas por sección (encabezados con id)
    for _hm in _re.finditer(r'<h[23]\s+id="([^"]+)"[^>]*>(.*?)</h[23]>', _body, flags=_re.S):
        _hid = _hm.group(1)
        _htext = _limpiar(_hm.group(2))
        _rest = _body[_hm.end():]
        _nx = _re.search(r'<h[23][^>]', _rest)
        _seg = _rest[:_nx.start()] if _nx else _rest[:2600]
        _entradas.append({"t": _htext, "s": (_cat + " · " + _tit) if _cat else _tit,
                          "u": _slug + "#" + _hid, "x": (_htext + ". " + _limpiar(_seg))[:520]})

with open(os.path.join(RAIZ, "assets/js/indice.js"), "w", encoding="utf-8") as _f:
    _f.write("window.BUSQUEDA_INDICE = " + _json.dumps(_entradas, ensure_ascii=False) + ";")
print("Índice de búsqueda:", len(_entradas), "entradas")
