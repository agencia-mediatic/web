// ============================================================
//  ENLACES DE LOS BOTONES (para medir con UTM)
//  Pega aquí el enlace de cada botón. Si dejas '' el botón usa el destino por defecto.
//  Si el enlace empieza por http, se abre en una pestaña nueva.
// ============================================================
window.MEDIATIC = {
  DESTINO_POR_DEFECTO: 'index.html#contacto',

  ENLACES: {
    'cabecera':     'https://form.mediatic.io/?utm_source=web&utm_medium=home&utm_campaign=bt-sup-ag-lla',  // Botón de arriba a la derecha: "Agendar llamada" (sale en todas las páginas)
    'hero':         'https://form.mediatic.io/?utm_source=web&utm_medium=home&utm_campaign=bt-qro-resul',  // Botón del inicio: "Quiero conseguir estos resultados"
    'quienes-somos':'https://form.mediatic.io/?utm_source=web&utm_medium=home&utm_campaign=bt-qin-som',  // Botón de ¿Quiénes somos?: "Quiero que trabajemos juntos"
    'resultados':   'https://form.mediatic.io/?utm_source=web&utm_medium=home&utm_campaign=resul',  // Botón del bloque azul de reels: "Quiero estos resultados"
    'hablemos':     'https://form.mediatic.io/?utm_source=web&utm_medium=home&utm_campaign=hblms',  // Botón de la sección "Hablemos": "Rellenar el formulario"
    'pie':          '',  // Botón "Pedir presupuesto" del pie de página (sale en todas las páginas)
    'blog-lateral': '',  // Botón fijo del lateral de los artículos del blog: "Agendar diagnóstico"
    'blog-opciones-marketing-2026':'https://form.mediatic.io/?utm_source=web&utm_medium=blog&utm_campaign=opciones-marketing-2026',  // Enlace "hablemos" del artículo de opciones de marketing 2026
    'blog-de-profundis':'https://form.mediatic.io/?utm_source=web&utm_medium=blog&utm_campaign=web-blog-caso-exito-de-profundis',  // Enlace "contacta con Mediatic" del caso de éxito de De Profundis
    'blog-mitos-instagram':'https://form.mediatic.io/?utm_source=web&utm_medium=blog&utm_campaign=mitos-instagram',  // Enlace "contacta con Mediatic" del artículo de mitos de Instagram
    'blog-pmu-paradise':'https://form.mediatic.io/?utm_source=web&utm_medium=blog&utm_campaign=pmu-paradise',  // Enlace "contacta con Mediatic" del artículo de PMU Paradise
    'blog-caso-exito-mario-cozma':'https://form.mediatic.io/?utm_source=web&utm_medium=home&utm_campaign=caso-exito-mario',  // Enlace de contacto del caso de éxito de Mario Cozma (también el botón "Agendar diagnóstico" lateral)
    'blog-cumple-2-anos':'https://form.mediatic.io/?utm_source=web&utm_medium=blog&utm_campaign=2-anos',  // Enlace "contacta con el equipo" del artículo Mediatic cumple 2 años (y su botón "Agendar diagnóstico" lateral)
    'blog-caso-exito-marina-garrido':'https://form.mediatic.io/?utm_source=web&utm_medium=blog&utm_campaign=caso-exito-dra-marina-garrido',  // Enlace "cuéntanos tu proyecto" del caso de éxito de la Dra. Marina Garrido (y su botón lateral). Pendiente de enlace con UTM
    'blog-caso-exito-gisela-jorba':'https://form.mediatic.io/?utm_source=web&utm_medium=blog&utm_campaign=caso-exito-gisela-jorba',  // Enlace "cuéntanos tu proyecto" del caso de éxito de Gisela Jorba (y su botón lateral). Pendiente de enlace con UTM
    'ag-contenido-bcn':'https://form.mediatic.io/?utm_source=web&utm_medium=blog&utm_campaign=ag-contenido-bcn',  // Página «Agencia de creación de contenido en Barcelona»: todos sus botones al formulario
    'blog-guion-perfecto-instagram':'https://form.mediatic.io/?utm_source=web&utm_medium=blog&utm_campaign=guiones-instagram',  // Enlace "agendar una reunión" del artículo del guion perfecto para Instagram (y su botón lateral "Agendar diagnóstico")
    'blog-caso-exito-pedro-seo':'https://form.mediatic.io/?utm_source=web&utm_medium=blog&utm_campaign=caso-exito-pedro-seo',  // Enlace "hablemos" del caso de éxito de Pedro SEO
    'blog-caso-exito-la-school-of-dance':'https://form.mediatic.io/?utm_source=web&utm_medium=blog&utm_campaign=caso-school-of-dance',  // Enlace "cuéntanos tu proyecto" del caso de éxito de La School of Dance
    'blog-caso-exito-sosa-ingredients':'https://form.mediatic.io/?utm_source=web&utm_medium=blog&utm_campaign=caso-sosa-ingredients',  // Enlace "cuéntanos tu proyecto" del caso de éxito de Sosa Ingredients
    'blog-mejores-agencias-contenido-barcelona':'https://form.mediatic.io/?utm_source=web&utm_medium=blog&utm_campaign=mejores-agencias-contenido-barcelona',  // Enlace "cuéntanos qué necesitas" del artículo de las 5 mejores agencias de contenido en Barcelona
    'blog-articulo':''   // Enlace de texto dentro de los artículos del blog: "agenda una sesión de diagnóstico"
  },

  // Redes sociales del pie de página. Si dejas '' en LinkedIn, el enlace no lleva a ningún sitio.
  REDES: {
    instagram: 'https://www.instagram.com/mediatic.io/',
    youtube:   'https://www.youtube.com/@mediatic.agencia',
    linkedin:  ''
  },

  // Chat (Crisp). El chat de Crisp NO se carga hasta que la persona pulsa el botón "Chatea con Mediatic".
  // ID: el "Website ID" de Crisp (Ajustes > Chatbox > Instalación). Si lo dejas '' el botón del chat no aparece.
  // HORARIO: solo sirve para mostrar "En línea" (verde) dentro de ese horario; fuera sale "Te respondemos en cuanto podamos".
  CHAT: {
    ID: '',   // Chat DESACTIVADO hasta tenerlo configurado. Para reactivarlo, pon aquí el Website ID de Crisp: 48fefa74-f841-4915-9ae5-bff3c85c5c74
    TITULO: 'Habla con Roger y Esteve',
    BOTON: 'Chatea con Mediatic',
    HORARIO: { dias: [1, 2, 3, 4, 5], desde: '09:00', hasta: '18:00', zona: 'Europe/Madrid' }   // dias: 1 = lunes ... 7 = domingo
  },

  // Textos legales (pon aquí las URL completas). Se usan en el pie de página, en el aviso de cookies y en el formulario.
  LEGAL: {
    aviso:      'aviso-legal.html',  // Aviso legal
    privacidad: 'politica-privacidad.html',  // Política de privacidad
    cookies:    'politica-cookies.html'   // Política de cookies
  },

  // Formulario de cualificación que se abre en una pestaña nueva al enviar el formulario corto.
  // Cuando lo publiques, pon aquí su URL completa (por ejemplo https://forms.mediatic.io/).
  FORMULARIO: 'https://form.mediatic.io/',

  // Datos del formulario corto que viajan al formulario largo (nombre, email, teléfono...).
  // Ponlo en false si prefieres que solo viajen las UTM.
  PASAR_DATOS_AL_FORMULARIO: true,

  // Parámetros de UTM que se guardan y se reenvían al formulario.
  UTM: ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term']
};
