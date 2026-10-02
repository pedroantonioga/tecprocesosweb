# Sitio web · Programa de Tecnología en Procesos Industriales (UFPS)

Sitio estático (HTML + CSS + JavaScript, sin framework) para el Programa de Tecnología
en Procesos Industriales de la Facultad de Ingeniería de la Universidad Francisco de
Paula Santander. Diseño alineado al Manual de Identidad Visual UFPS.

## Cómo ver el sitio

Abra el archivo `index.html` con doble clic en cualquier navegador (Chrome, Edge,
Firefox). No requiere instalación ni servidor. Todos los enlaces son relativos, de modo
que el sitio funciona igual desde una USB, desde el disco o publicado en internet.

## Estructura de carpetas

```
sitio/
├── index.html                     Portada
├── institucional*.html            Sección Institucional y sus páginas
├── el-programa*.html              Sección El Programa y sus páginas
├── comunidad*.html                Sección Comunidad y sus páginas
├── vinculos*.html                 Sección Vínculos y sus páginas
├── assets/
│   ├── css/estilos.css            Hoja de estilos única (colores, tipografía, componentes)
│   ├── js/navegacion.js           Menú móvil y desplegables
│   └── img/
│       ├── logos/                 Logo del programa, logo UFPS y favicon
│       └── fotos/                 Fotografías y malla curricular
├── documentos/                    Coloque aquí los PDF y formatos descargables
├── generar.py / build.py          Generadores opcionales (ver más abajo)
└── README.md
```

Todas las páginas están en la raíz con nombres descriptivos (estructura plana). Esto
mantiene los enlaces simples y evita rutas rotas al mover o publicar el sitio.

## Cómo editar los textos

Cada página es un archivo `.html`. Abra el que desee con un editor de texto (por
ejemplo el Bloc de notas, o Visual Studio Code) y modifique el texto que está entre las
etiquetas. Los marcadores `Información por complementar` señalan el contenido que falta
por definir; reemplácelos por la información oficial.

El **encabezado (menú)** y el **pie de página** se repiten en cada archivo. Si edita un
dato de contacto o un enlace del menú, hágalo en todos los archivos para mantener la
coherencia. Si prefiere no repetir el cambio a mano, use el generador (siguiente punto).

## Cómo agregar documentos descargables

1. Copie el archivo (PDF, Word, etc.) dentro de la carpeta `documentos/`.
2. En la página de descargas correspondiente, ajuste el enlace `href` del elemento para
   que apunte al archivo, por ejemplo: `href="documentos/estatuto-estudiantil.pdf"`.

## Cómo reemplazar la malla curricular

Guarde la imagen oficial como `assets/img/fotos/malla-curricular.png` (mismo nombre).
Aparecerá automáticamente en las páginas de Plan de Estudios y Malla curricular.

## Generadores opcionales (avanzado)

Los archivos `generar.py` y `build.py` permiten regenerar todas las páginas de forma
automática, manteniendo un solo encabezado y un solo pie para todo el sitio. Requieren
Python 3. Para regenerar:

```
python3 build.py
```

Los datos del programa (correo, teléfono, coordinador, etc.) están centralizados en el
diccionario `D` dentro de `generar.py`. La estructura del menú está en la lista `NAV`.
Si edita allí, todas las páginas se actualizan al regenerar. Estos scripts son
opcionales: el sitio funciona sin ellos.

## Buscador

El sitio incluye un buscador que funciona sin conexión ni servidor. Se abre con el ícono
de lupa del encabezado. La persona escribe un tema (por ejemplo "trabajo de grado",
"calendario", "malla" o "semilleros") y el buscador muestra los resultados más cercanos,
con tolerancia a pequeños errores de tecleo, y lleva directo a la página o a la sección
correspondiente. El índice de búsqueda está en `assets/js/indice.js` y se regenera
automáticamente al ejecutar `build.py`; no debe editarse a mano.

## Publicar en GitHub Pages

1. Cree un repositorio nuevo y suba el contenido de la carpeta del sitio.
2. En el repositorio, entre a Settings, luego Pages.
3. En Source elija la rama principal y la carpeta raíz. Guarde.
4. En pocos minutos el sitio quedará disponible en la URL que indique GitHub.

## Estado del avance

Secciones con contenido cargado: Institucional (normatividad con enlaces oficiales,
protocolo de salidas, trámites con su estructura, registro calificado) y El Programa
(historia con línea de tiempo, PEP, plan de estudios en tablas, malla, perfiles,
trabajos de grado y grupos y semilleros de investigación).

Pendientes por definir:

- Paso a paso de cada trámite (estudiantes y graduados).
- Investigación: investigadores categorizados, proyectos de impacto, publicaciones y memorias.
- Secciones Comunidad y Vínculos (contenido por trabajar).
- Versión del logo a una tinta blanca para fondos oscuros o rojos, en caso de requerirse.
