import re,glob
import time
V=str(int(time.time()))
import os
OUT='/Users/mediaticmac/landing-page/web'
NAV=[('index.html','Home',''),('resultados.html','Casos de éxito',''),('opiniones.html','Opiniones',''),('blog.html','Blog','')]
SITE='https://www.mediatic.io'   # <-- dominio definitivo de la web (sin barra final). Cámbialo aquí si es otro.
IG='https://www.instagram.com/mediatic.io/'
YT='https://www.youtube.com/@mediatic.agencia'
SEO={
 'index.html':('Agencia de contenido viral en Barcelona | Mediatic','Agencia de contenido viral en Barcelona. Multiplicamos por 5 tus visitas y leads en Instagram con menos de 5 horas al mes. Agenda tu llamada.',True),
 'equipo.html':('Equipo de expertos en contenido viral | Mediatic','Conoce al equipo de Mediatic: fundadores, guionistas, filmmakers y editores especializados en crear contenido viral para negocios y marcas personales.',True),
 'clientes.html':('Clientes y casos de éxito en redes sociales | Mediatic','Más de 100 clientes satisfechos y más de 30 nichos viralizados. Mira con quién trabajamos y los resultados que conseguimos con contenido orgánico.',True),
 'blog.html':('Noticias y artículos de contenido orgánico | Mediatic','Noticias y artículos de Mediatic: novedades sobre contenido orgánico para que aprendas y apliques en tu negocio, y logros de la agencia y su equipo.',False),
 'opiniones.html':('Opiniones de clientes sobre Mediatic | Agencia de contenido','Opiniones de clientes de Mediatic: charlas en vídeo y reseñas de negocios y marcas personales que han crecido en Instagram con contenido viral.',True),
 'resultados.html':('Casos de éxito de contenido viral | Mediatic','Casos de éxito de Mediatic: negocios y marcas personales que generan más negocio con contenido orgánico en Instagram. Más de 300 millones de views.',True),
 'aviso-legal.html':('Aviso Legal | Mediatic','Aviso legal de Mediatic Studios SL: identificación del titular, condiciones de uso, medidas de seguridad y propiedad intelectual.',True),
 'politica-privacidad.html':('Política de Privacidad | Mediatic','Política de privacidad de Mediatic Studios SL: cómo tratamos tus datos personales, tus derechos y cómo ejercerlos.',True),
 'politica-cookies.html':('Política de Cookies | Mediatic','Política de cookies de Mediatic Studios SL: qué cookies usamos, para qué sirven y cómo gestionarlas.',True),
 '404.html':('Página no encontrada | Mediatic','La página que buscas no existe. Vuelve al inicio de Mediatic, agencia de contenido viral en Barcelona.',False),
}
# En SEO[...][2]: True = se indexa; False = noindex (blog hasta tener artículos reales, 404 siempre)
CRUMBS={'equipo.html':'Equipo','clientes.html':'Clientes','blog.html':'Blog','resultados.html':'Casos de éxito','opiniones.html':'Opiniones','aviso-legal.html':'Aviso Legal','politica-privacidad.html':'Política de Privacidad','politica-cookies.html':'Política de Cookies'}

from seguir_leyendo import seguir
ART_META={'mitos-de-instagram.html':dict(
 title='Mitos de Instagram: 6 falsas verdades que frenan tu negocio',
 desc='Descubre los 6 mitos de Instagram que frenan a tu negocio: hora, hashtags, viralidad y ventas. Te contamos qué funciona de verdad. Lee la guía completa.',
 h1='Mitos de Instagram: 6 falsas verdades que frenan a tu negocio',
 cat='Consejos',date='2026-04-21',fecha='21 de abril de 2026',mins=11,yt='kX7RTLibXrs',
 thumb='img/blog/mitos-de-instagram.jpg',
 excerpt='La hora, los hashtags, la viralidad y las ventas: repasamos los seis mitos de Instagram que más escuchamos y qué funciona de verdad.')}

ART_META['gamma-pmu-congress-2026.html']=dict(
 title='Gamma PMU Congress 2026: Mediatic, ponente en San Sebastián',
 desc='Roger y Esteve, fundadores de Mediatic, explicaron en el Gamma PMU Congress 2026 cómo vender con contenido en redes sociales. Así fue la ponencia.',
 h1='Mediatic, ponente en el Gamma PMU Congress 2026',
 cat='Noticias',date='2026-11-01',fecha='1 de noviembre de 2026',mins=3,
 thumb='img/blog/gamma-pmu-congress-2026.jpg',
 excerpt='Roger y Esteve, fundadores de Mediatic, presentaron su ponencia sobre cómo convertir el contenido de Instagram en ventas ante más de 100 asistentes en San Sebastián.')
ART_META['mediatic-cumple-2-anos.html']=dict(
 title='Mediatic cumple 2 años | Agencia de contenido para redes',
 desc='Roger y Esteve fundaron Mediatic en 2024. Dos años después: más de 30 clientes, más de 8 personas en el equipo y 300 millones de reproducciones.',
 h1='Mediatic cumple 2 años',
 cat='Noticias',date='2026-07-12',fecha='12 de julio de 2026',mins=5,
 thumb='img/blog/mediatic-cumple-2-anos-thumb.jpg',
 excerpt='Repasamos cómo nacieron Roger y Esteve con Mediatic, cómo ha crecido la agencia en dos años y hacia dónde quiere ir.')
ART_META['opciones-marketing-2026.html']=dict(
 title='Opciones de marketing para este 2026: cuál elegir',
 desc='Descubre las opciones de marketing para este 2026: SEO, publicidad, radio, influencers y redes sociales. Ventajas, inconvenientes y cuál elegir.',
 h1='Opciones de marketing para este 2026: cuál conviene a tu empresa',
 cat='Consejos',date='2026-03-31',fecha='31 de marzo de 2026',mins=10,
 thumb='img/blog/opciones-de-marketing-2026.jpg',
 excerpt='SEO, publicidad, prensa, radio, email, influencers, ferias y redes sociales: repasamos sus ventajas e inconvenientes para que decidas dónde invertir en 2026.')
ART_META['pmu-paradise.html']=dict(
 title='Mediatic en PMU Paradise 2026: nuestra ponencia en Tenerife',
 desc='Roger y Esteve, fundadores de Mediatic, impartieron «Revive tu Instagram» en PMU Paradise 2026, en Tenerife: una ponencia con taller de guiones incluido.',
 h1='PMU Paradise 2026: la primera ponencia de Mediatic, en Tenerife',
 cat='Noticias',date='2026-05-31',fecha='31 de mayo de 2026',mins=4,
 thumb='img/blog/mediatic-pmu-paradise-2026-ponencia.jpg',
 excerpt='Roger y Esteve impartieron «Revive tu Instagram», su primera ponencia en un congreso, con un taller de guiones, ante unos 50 asistentes en Tenerife.')
ART_META['de-profundis.html']=dict(
 title='Caso de éxito en Instagram: De Profundis y el buceo técnico',
 desc='Así pasó De Profundis de menos de 1.000 seguidores a más de 6.200 y clientes diarios por Instagram, con menos de 6 horas cada tres meses. Descubre cómo.',
 h1='Caso de éxito: De Profundis',
 sub='Recibe clientes cada día desde Instagram con menos de 2 horas al mes',
 cat='Resultados',date='2026-04-14',fecha='14 de abril de 2026',mins=6,
 thumb='img/blog/de-profundis-portada-v2.jpg',
 excerpt='Recibe clientes cada día desde Instagram con menos de 2 horas al mes.')
def _draft(f,h1,cat,desc,date=None,fecha=None):
    d=dict(title=h1+' | Mediatic',desc=desc,h1=h1,cat=cat,draft=True,thumb='img/blog/%s.jpg'%f[:-5],excerpt='Próximamente.')
    if date: d.update(date=date,fecha=fecha)
    return d
ART_META.update({

 'caso-exito-marina-garrido.html':dict(
  title='Caso de éxito: Clínica Dra. Marina Garrido (1,2M de views en 3 meses)',
  desc='Así llevamos a la Clínica Dra. Marina Garrido a más de 1,2 millones de visualizaciones en tres meses, con 12 vídeos y menos de dos horas al mes.',
  h1='Caso de éxito: Clínica Dra. Marina Garrido',
  sub='Capta clientes para su clínica a través de redes con menos de 2 horas al mes',
  cat='Resultados',date='2026-08-02',fecha='2 de agosto de 2026',mins=7,
  thumb='img/blog/caso-exito-marina-garrido-portada.jpg',
  excerpt='Capta clientes para su clínica a través de redes con menos de 2 horas al mes.'),
 'caso-exito-manuel-costina.html':_draft('caso-exito-manuel-costina.html','Caso de éxito: Manuel Costiña','Resultados','Caso de éxito: Manuel Costiña.','2026-11-20','20 de noviembre de 2026'),
 'caso-exito-gisela-jorba.html':dict(
  title='Caso de éxito: Gisela Jorba (de 6.000 a 24.400 seguidores)',
  desc='Así llevamos a Gisela Jorba de 6.000 a 24.400 seguidores dentro de su nicho, duplicamos su lista de espera y lanzamos su formación con más de 50 ventas.',
  h1='Caso de éxito: Gisela Jorba',
  sub='Ha duplicado su lista de espera en su centro, pasando de 6 meses a 1 año',
  cat='Resultados',date='2026-09-15',fecha='15 de septiembre de 2026',mins=7,
  thumb='img/blog/caso-exito-gisela-jorba.jpg',
  excerpt='Ha duplicado su lista de espera en su centro, pasando de 6 meses a 1 año.'),
 'caso-exito-mario-cozma.html':dict(
  title='Caso de éxito: Mario Cozma (+44.000 seguidores)',
  desc='De 34.000 a 77.700 seguidores: así convertimos a Mario Cozma en el referente del transporte en redes sociales, junto a su podcast Rutas de Éxito.',
  h1='Caso de éxito: Mario Cozma',
  sub='De 34.000 a más de 77.000 seguidores en Instagram y posicionado como referente del transporte en redes',
  cat='Resultados',date='2026-06-30',fecha='30 de junio de 2026',mins=9,
  thumb='img/blog/caso-exito-mario-cozma.jpg',
  excerpt='De 34.000 a más de 77.000 seguidores en Instagram y posicionado como referente del transporte en redes.'),

 'caso-exito-pedro-seo.html':dict(
  title='Caso de éxito: Pedro SEO (+900.000 visualizaciones)',
  desc='Así trabajamos el contenido de Pedro SEO: vídeos de más de 900.000 visualizaciones y una estrategia de nicho que atrae clientes con 6 horas al mes.',
  h1='Caso de éxito: Pedro SEO',
  sub='Capta más clientes para su agencia y más alumnos para su formación gracias a nuestro contenido',
  cat='Resultados',date='2026-07-12',fecha='12 de julio de 2026',mins=8,
  thumb='img/blog/caso-exito-pedro-seo.jpg',
  excerpt='Capta más clientes para su agencia y más alumnos para su formación gracias a nuestro contenido, con solo 6 horas al mes.'),
 'caso-exito-sosa-ingredients.html':dict(
  title='Caso de éxito: Sosa Ingredients (+10.000 seguidores)',
  desc='Así cambiamos la comunicación corporativa de Sosa Ingredients por vídeos que aportan valor y la llevamos de 90.000 a 100.000 seguidores en tres meses.',
  h1='Caso de éxito: Sosa Ingredients',
  sub='Dejamos atrás la comunicación corporativa y crecimos +10.000 seguidores en 3 meses',
  cat='Resultados',date='2026-06-16',fecha='16 de junio de 2026',mins=7,
  thumb='img/blog/caso-exito-sosa-ingredients.jpg',
  excerpt='Dejamos atrás la comunicación corporativa y crecimos +10.000 seguidores en 3 meses.'),
 'caso-exito-la-school-of-dance.html':dict(
  title='Caso de éxito: La School of Dance (+8 millones de visitas)',
  desc='Así llevamos el contenido de La School of Dance, escuela de baile de Manresa, a más de 8 millones de visualizaciones en dos meses en Instagram y TikTok.',
  h1='Caso de éxito: La School of Dance',
  sub='Consiguimos +8 millones de visualizaciones en los primeros 2 meses',
  cat='Resultados',date='2026-06-17',fecha='17 de junio de 2026',mins=8,
  thumb='img/blog/caso-exito-la-school-of-dance.jpg',
  excerpt='Consiguimos +8 millones de visualizaciones en los primeros 2 meses.'),
 'guion-perfecto-instagram.html':dict(
  title='Cómo escribir el guion perfecto para Instagram: el proceso paso a paso',
  desc='Aprende a escribir el guion perfecto para Instagram: cómo encontrar ideas, validarlas, elegir el formato y adaptar tu guion para que funcione. Paso a paso.',
  h1='Cómo escribir el guion perfecto para Instagram: el proceso paso a paso',
  cat='Consejos',date='2026-07-14',fecha='14 de julio de 2026',mins=9,
  thumb='img/blog/guion-perfecto-instagram.jpg',
  excerpt='El proceso que seguimos en Mediatic para escribir guiones para Instagram: de las dudas de tus clientes a un guion propio que retenga la atención.'),
 'servicios.html':dict(
  title='Agencia de creación de contenido en Barcelona | Mediatic',
  desc='Agencia de creación de contenido viral en Barcelona para Instagram y TikTok. Estrategia, guiones, grabación y edición sin permanencia. Pide tu diagnóstico.',
  h1='Agencia de creación de contenido en Barcelona: para empresas que quieren clientes, no likes',
  cat='Servicios',date='2026-08-25',fecha='25 de agosto de 2026',mins=7,
  thumb='img/blog/servicios-portada.jpg',
  excerpt='Qué hacemos, cómo trabajamos y para quién es nuestro servicio de creación de contenido para redes sociales.'),
})
GAL_ALTS={'img/blog/sosa-ingredients-videos-ahora':['Vídeo de Sosa Ingredients en Instagram con 238 mil visualizaciones: azúcares','Vídeo de Sosa Ingredients en Instagram con 61 mil visualizaciones: la inulina','Vídeo de Sosa Ingredients en Instagram con 49,2 mil visualizaciones: qué hace cada ingrediente','Vídeo de Sosa Ingredients en Instagram con 33 mil visualizaciones: tus croquetas','Vídeo de Sosa Ingredients en Instagram con 20,8 mil visualizaciones: la crema pastelera'],
'img/blog/la-school-of-dance-video-viral':['Captura en Instagram del vídeo del paso viral de La School of Dance, con 787 mil visualizaciones','Captura en TikTok del mismo vídeo de La School of Dance, con 3,2 millones de visualizaciones'],
'img/blog/la-school-of-dance-instagram':['Vídeo de La School of Dance en Instagram con 235 mil visualizaciones','Vídeo de La School of Dance en Instagram con 168 mil visualizaciones: gimnasio contra baile','Vídeo de La School of Dance en Instagram con 138 mil visualizaciones: un muy buen bailarín','Vídeo de La School of Dance en Instagram con 112 mil visualizaciones','Vídeo de La School of Dance en Instagram con 63 mil visualizaciones: hábitos para mejorar como bailarín'],
'img/blog/la-school-of-dance-tiktok':['Vídeo de La School of Dance en TikTok con 153,7 mil visualizaciones: «No vas a bailar»','Vídeo de La School of Dance en TikTok con 114,8 mil visualizaciones: «iets frans»','Vídeo de La School of Dance en TikTok con 87,9 mil visualizaciones: un muy buen bailarín','Vídeo de La School of Dance en TikTok con 64,4 mil visualizaciones: gimnasio contra baile','Vídeo de La School of Dance en TikTok con 46 mil visualizaciones: aprende este truco'],
'img/blog/pedro-seo-videos-seo':['Vídeo de Pedro SEO con 163 mil visualizaciones en Instagram sobre el botón de buscar de Google','Vídeo de Pedro SEO con 89 mil visualizaciones en Instagram: así es como puedes posicionarte','Vídeo de Pedro SEO con 86 mil visualizaciones en Instagram: puedes robarle el SEO a tu competencia','Vídeo de Pedro SEO con 40,1 mil visualizaciones en Instagram: posicionarte primero en Google'],
'img/blog/pedro-seo-video-600000':['Captura en Instagram del vídeo de Pedro SEO «Si quieres que ChatGPT responda», con 125 mil visualizaciones','Captura en TikTok del mismo vídeo de Pedro SEO, con 775,9 mil visualizaciones'],
'img/blog/pedro-seo-primera-etapa':['Vídeo de Pedro SEO con 196 mil visualizaciones en Instagram','Vídeo de Pedro SEO con 172 mil visualizaciones en Instagram: «dependerá de ti»','Vídeo de Pedro SEO con 90,6 mil visualizaciones en Instagram: tres consejos','Vídeo de Pedro SEO con 47,8 mil visualizaciones en Instagram: escribir artículos o textos para la universidad'],
'img/blog/caso-exito-gisela-jorba-videos':['Reel de Gisela Jorba con 647 mil visualizaciones','Reel de Gisela Jorba con 274 mil visualizaciones','Reel de Gisela Jorba con 272 mil visualizaciones','Reel de Gisela Jorba con 79,8 mil visualizaciones','Reel de Gisela Jorba con 71,8 mil visualizaciones: los tres mejores eyeliners'],
'img/blog/caso-exito-marina-garrido-videos':['Vídeo de la clínica con 505,8 mil visualizaciones: dos siliconas que se acumulan en el cabello','Vídeo de la clínica con 176 mil visualizaciones: cosas que frenan la caída del pelo','Vídeo de la clínica con 138 mil visualizaciones: ranking de famosos','Vídeo de la clínica con 130,8 mil visualizaciones: un combinado que los una'],
'img/blog/caso-exito-mario-cozma-videos':['Reel de Mario Cozma con 3 millones de visualizaciones, grabado en las instalaciones de Iveco','Reel de Mario Cozma con 1,6 millones de visualizaciones: ¿necesitas dinero?','Reel de Mario Cozma con 1,5 millones de visualizaciones: preguntas y respuestas a un conductor experto','Reel de Mario Cozma con 1,3 millones de visualizaciones: con qué remolque se gana más dinero en España'],
'img/blog/caso-exito-mario-cozma-podcast':['Corte de Rutas de Éxito con 1,5 millones de visualizaciones: ¿qué estás cobrando actualmente?','Corte de Rutas de Éxito con 642 mil visualizaciones: en mi empresa todos cobramos lo mismo','Corte de Rutas de Éxito con 615 mil visualizaciones: precio desorbitado, lo urgente nunca es barato','Corte de Rutas de Éxito con 427 mil visualizaciones: ¿cuánto cobra un conductor de autocar?','Corte de Rutas de Éxito con 425 mil visualizaciones: así funciona la contabilidad en Alemania'],
'img/blog/caso-exito-mario-cozma':['Dos integrantes del equipo de Mediatic con chaleco rosa y una cámara con estabilizador, junto a las instalaciones de Mercedes-Benz en el Circuito del Jarama','Grabación de contenido junto a un camión Scania con bandera de España durante el Gran Premio de España de Camiones','Selfie junto a la pista del Circuito del Jarama con un camión de carreras al fondo'],
'img/blog/de-profundis-resultados-reels':[
 'Reel de De Profundis con 144 mil visualizaciones: cómo hacer una parada de descompresión paso a paso',
 'Reel de De Profundis con 143 mil visualizaciones: el nitrox sirve para bucear',
 'Reel de De Profundis con 98,2 mil visualizaciones: ranking de mejores lugares para buceo',
 'Reel de De Profundis con 199 mil visualizaciones: gas para buceo']}
RELATED={'caso-exito-sosa-ingredients.html':['de-profundis.html','caso-exito-mario-cozma.html','caso-exito-pedro-seo.html'],'caso-exito-la-school-of-dance.html':['de-profundis.html','caso-exito-gisela-jorba.html','caso-exito-pedro-seo.html'],'caso-exito-pedro-seo.html':['caso-exito-gisela-jorba.html','caso-exito-marina-garrido.html','caso-exito-mario-cozma.html'],'guion-perfecto-instagram.html':['mitos-de-instagram.html','pmu-paradise.html','servicios.html'],'pmu-paradise.html':['gamma-pmu-congress-2026.html','opciones-marketing-2026.html'],'opciones-marketing-2026.html':['mitos-de-instagram.html','de-profundis.html'],'mediatic-cumple-2-anos.html':['de-profundis.html','gamma-pmu-congress-2026.html'],'mitos-de-instagram.html':['de-profundis.html','gamma-pmu-congress-2026.html','guion-perfecto-instagram.html','servicios.html'],'de-profundis.html':['mitos-de-instagram.html','servicios.html'],'gamma-pmu-congress-2026.html':['mitos-de-instagram.html','servicios.html']}
ART_META=dict(sorted(ART_META.items(),key=lambda kv:kv[1].get('date',''),reverse=True))
def canon(file): return SITE+('/' if file=='index.html' else '/'+file)
def esc(t): return t.replace('&','&amp;').replace('"','&quot;').replace('<','&lt;')
def jsonld(file,title,desc):
    org={"@type":"ProfessionalService","@id":SITE+"/#organization","name":"Mediatic","legalName":"MEDIATIC STUDIOS SL","url":SITE+"/","logo":SITE+"/logo-mediatic-azul.png","image":SITE+"/img/og-image.jpg","description":"Agencia de contenido viral en Barcelona especializada en crear contenido orgánico para Instagram, para negocios y marcas personales.","email":"info@mediatic.io","slogan":"Agencia de contenido viral en Barcelona","address":{"@type":"PostalAddress","streetAddress":"Plaça Pau Casals, 96","addressLocality":"Sant Fruitós de Bages","addressRegion":"Barcelona","postalCode":"08272","addressCountry":"ES"},"areaServed":{"@type":"AdministrativeArea","name":"Barcelona"},"foundingDate":"2024","knowsAbout":["Contenido viral","Creación de contenido para redes sociales","Instagram","TikTok","Guiones para reels"],"contactPoint":{"@type":"ContactPoint","contactType":"sales","email":"info@mediatic.io","availableLanguage":"es"},"founder":[{"@type":"Person","@id":SITE+"/#roger-gaona","name":"Roger Gaona Boixader","jobTitle":"Fundador","worksFor":{"@id":SITE+"/#organization"},"sameAs":["https://www.instagram.com/roggaona/"]},{"@type":"Person","@id":SITE+"/#esteve-gaona","name":"Esteve Gaona Boixader","jobTitle":"Fundador","worksFor":{"@id":SITE+"/#organization"},"sameAs":["https://www.instagram.com/esteve.gaona/"]}],"sameAs":[IG,YT]}
    site={"@type":"WebSite","@id":SITE+"/#website","url":SITE+"/","name":"Mediatic","inLanguage":"es-ES","publisher":{"@id":SITE+"/#organization"}}
    pg={"@type":"WebPage","@id":canon(file)+"#webpage","url":canon(file),"name":title,"description":desc,"inLanguage":"es-ES","isPartOf":{"@id":SITE+"/#website"},"about":{"@id":SITE+"/#organization"}}
    graph=[org,site,pg]
    if file in CRUMBS:
        graph.append({"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Inicio","item":SITE+"/"},{"@type":"ListItem","position":2,"name":CRUMBS[file],"item":canon(file)}]})
    if file in ART_META:
        a=ART_META[file]
        graph.append({"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Inicio","item":SITE+"/"},{"@type":"ListItem","position":2,"name":"Blog","item":canon('blog.html')},{"@type":"ListItem","position":3,"name":a['h1'],"item":canon(file)}]})
        if file=='servicios.html':
            graph[-1]={"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Inicio","item":SITE+"/"},{"@type":"ListItem","position":2,"name":"Servicios","item":canon(file)}]}
            graph.append({"@type":"Service","name":"Creación de contenido para redes sociales","serviceType":"Agencia de creación de contenido","provider":{"@id":SITE+"/#organization"},"areaServed":[{"@type":"City","name":"Barcelona"},{"@type":"Country","name":"España"},{"@type":"Country","name":"Andorra"}],"description":"Estrategia, ideas, guiones, grabación, edición, publicación y análisis de vídeos para Instagram y TikTok.","url":canon(file)})
        elif not a.get('draft'): graph.append({"@type":"BlogPosting","@id":canon(file)+"#article","mainEntityOfPage":{"@id":canon(file)+"#webpage"},"headline":a['h1'],"description":a['desc'],"datePublished":a['date'],"dateModified":a['date'],"inLanguage":"es-ES","author":{"@id":SITE+"/#organization"},"publisher":{"@id":SITE+"/#organization"},"image":SITE+("/"+a['thumb'] if os.path.exists(os.path.join(OUT,a['thumb'])) else "/img/og-image.jpg"),"articleSection":a['cat']})
        if file=='guion-perfecto-instagram.html': graph.append({"@type":"HowTo","name":"Cómo escribir el guion perfecto para Instagram","step":[{"@type":"HowToStep","position":i+1,"name":n} for i,n in enumerate(["Encuentra ideas de contenido","Valida las ideas","Elige el formato","Escribe la primera versión del guion","Adapta y personaliza el guion"])]})
        _q=re.findall(r'<details><summary>(.*?)</summary><p>(.*?)</p></details>',open(os.path.join(OUT,'_build','servicios_page.html' if file=='servicios.html' else 'articulos/'+file),'r').read())
        if _q and not a.get('draft'): graph.append({"@type":"FAQPage","mainEntity":[{"@type":"Question","name":re.sub('<[^>]+>','',q),"acceptedAnswer":{"@type":"Answer","text":re.sub('<[^>]+>','',a2)}} for q,a2 in _q]})
    if file=='index.html':
        exec(open('/Users/mediaticmac/landing-page/web/_build/faq_data.py').read(),globals())
        graph.append({"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ_DATA]})
    def _vid(vid,name,desc,thumb,date,dur=None):   # ficha de vídeo (VideoObject)
        v={"@type":"VideoObject","name":name,"description":desc.strip(),"thumbnailUrl":SITE+"/"+thumb,"uploadDate":date,"embedUrl":"https://www.youtube.com/embed/"+vid,"contentUrl":"https://www.youtube.com/watch?v="+vid,"inLanguage":"es-ES","publisher":{"@id":SITE+"/#organization"}}
        if dur: v["duration"]=dur
        return v
    def _vid_ent(t):
        ds='Entrevista en vídeo con %s%s sobre su experiencia trabajando con Mediatic. %s'%(t['name'],(' (%s)'%t['niche']) if t.get('niche') else '',t.get('context',''))
        return _vid(t['id'],'%s: %s'%(t['name'],t['headline'].strip('“”"')),ds,'img/entrevistas/%s.jpg'%t['id'],t['uploadDate'],t.get('duration'))
    if file=='opiniones.html':   # una ficha de vídeo por cada entrevista de YouTube
        graph+= [_vid_ent(t) for t in _E if t.get('uploadDate')]
    elif file in ART_META and not ART_META[file].get('draft'):   # vídeos incrustados en los artículos
        _ap=os.path.join(OUT,'_build','articulos',file)
        for _i in (re.findall(r'<!--VIDEO:([\w-]{11})',open(_ap,'r').read()) if os.path.exists(_ap) else []):
            _t=next((x for x in _E if x['id']==_i and x.get('uploadDate')),None)
            if _t: graph.append(_vid_ent(_t))
        if file=='mitos-de-instagram.html': graph.append(_vid('kX7RTLibXrs','Desmintiendo mitos sobre redes sociales','Vídeo del canal de Mediatic en el que respondemos, según nuestra experiencia, a los mitos y falsas verdades sobre Instagram y redes sociales que más se han extendido.','img/blog/mitos-de-instagram.jpg','2026-04-21T11:56:44-07:00','PT14M26S'))
    return json.dumps({"@context":"https://schema.org","@graph":graph},ensure_ascii=False,separators=(',',':')).replace('</','<\\/')

from PIL import Image as _Img
_lw,_lh=_Img.open(os.path.join(OUT,'logo-mediatic-azul.png')).size
def header(cur):
    items=''.join('<li><a href="%s"%s%s%s>%s</a></li>'%(h,' class="on"' if h==cur else '',' aria-current="page"' if h==cur else '',(' data-link="%s"'%k) if k else '',n) for h,n,k in NAV)
    drawer=''.join('<a href="%s"%s>%s</a>'%(h,(' data-link="%s"'%k) if k else '',n) for h,n,k in NAV)
    return f'''<header>
  <nav class="drawer" aria-label="Menú móvil">{drawer}</nav>
  <a class="brand" href="index.html" aria-label="Mediatic, ir al inicio"><img src="logo-mediatic-azul.png" alt="Mediatic" width="{_lw}" height="{_lh}"></a>
  <nav class="menu" aria-label="Principal"><ul>{items}</ul></nav>
  <a class="btn sm hdr-cta" href="index.html#contacto" data-link="cabecera"><span class="long">Agendar llamada</span><span class="short">Agendar</span> <i>→</i></a>
  <button class="burger" aria-label="Abrir menú" aria-expanded="false"><span></span><span></span><span></span></button>
</header>'''
FOOT='''<footer><div class="wrap">
  <nav class="flinks" aria-label="Páginas de interés"><a href="index.html">Home</a><a href="resultados.html">Casos de éxito</a><a href="opiniones.html">Opiniones</a><a href="blog.html">Blog</a></nav>
  <div class="fbot"><small>Mediatic Studios SL ©2026</small><div class="fsocial"><a data-social="instagram" href="https://www.instagram.com/mediatic.io/" target="_blank" rel="noopener" aria-label="Instagram de Mediatic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.4" cy="6.6" r="1.1" fill="currentColor" stroke="none"/></svg></a><a data-social="youtube" href="https://www.youtube.com/@mediatic.agencia" target="_blank" rel="noopener" aria-label="YouTube de Mediatic"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M21.6 7.2a2.5 2.5 0 0 0-1.8-1.8C18.2 5 12 5 12 5s-6.2 0-7.8.4A2.5 2.5 0 0 0 2.4 7.2C2 8.8 2 12 2 12s0 3.2.4 4.8a2.5 2.5 0 0 0 1.8 1.8C5.8 19 12 19 12 19s6.2 0 7.8-.4a2.5 2.5 0 0 0 1.8-1.8c.4-1.6.4-4.8.4-4.8s0-3.2-.4-4.8zM10 15V9l5.2 3z"/></svg></a><a data-social="linkedin" href="#" aria-label="LinkedIn de Mediatic"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.4 20.5h-3.6v-5.6c0-1.3 0-3-1.8-3s-2.1 1.4-2.1 2.9v5.7H9.3V9h3.4v1.6c.5-.9 1.6-1.8 3.4-1.8 3.6 0 4.300 2.4 4.3 5.5v6.2zM5.3 7.4a2.1 2.1 0 1 1 0-4.2 2.1 2.1 0 0 1 0 4.2zM7.1 20.5H3.6V9h3.5v11.5z"/></svg></a></div></div>
  <nav class="flegal" aria-label="Legal"><a data-legal="aviso" href="aviso-legal.html">Aviso legal</a><a data-legal="privacidad" href="politica-privacidad.html">Política de privacidad</a><a data-legal="cookies" href="politica-cookies.html">Política de cookies</a><button type="button" data-open-cookies>Configurar cookies</button></nav>
</div>
<div class="fplanes" aria-hidden="true" role="presentation"><svg viewBox="0 -14 1600 274" preserveAspectRatio="xMidYMid meet"><defs><symbol id="mtp" viewBox="342 590 1203 865"><polygon points="1545,590 342,942 648,1060 681,1180 826,1082 921,1455" fill="#F0F0EF"/><polygon points="648,1060 681,1180 826,1082" fill="#1B1BCB" fill-opacity=".38"/></symbol></defs><path d="M-20 123.8 L0 128.0 L20 132.2 L40 136.3 L60 140.4 L80 144.4 L100 148.2 L120 151.9 L140 155.4 L160 158.8 L180 161.8 L200 164.7 L220 167.2 L240 169.5 L260 171.4 L280 173.0 L300 174.3 L320 175.2 L340 175.8 L360 176.0 L380 175.8 L400 175.3 L420 174.4 L440 173.2 L460 171.6 L480 169.7 L500 167.5 L520 165.0 L540 162.2 L560 159.2 L580 155.9 L600 152.4 L620 148.7 L640 144.9 L660 140.9 L680 136.8 L700 132.7 L720 128.5 L740 124.4 L760 120.2 L780 116.1 L800 112.1 L820 108.3 L840 104.5 L860 101.0 L880 97.7 L900 94.5 L920 91.7 L940 89.1 L960 86.8 L980 84.8 L1000 83.2 L1020 81.8 L1040 80.9 L1060 80.3 L1080 80.0 L1100 80.1 L1120 80.6 L1140 81.4 L1160 82.6 L1180 84.1 L1200 86.0 L1220 88.2 L1240 90.6 L1260 93.4 L1280 96.4 L1300 99.7 L1320 103.2 L1340 106.8 L1360 110.6 L1380 114.6 L1400 118.6 L1420 122.8 L1440 126.9 L1460 131.1 L1480 135.2 L1500 139.3 L1520 143.4 L1540 147.2 L1560 151.0 L1580 154.6 L1600 157.9 L1620 161.1 L1640 164.0" fill="none" stroke="#F0F0EF" stroke-opacity=".55" stroke-width="5" stroke-linecap="round" stroke-dasharray="1 17"/><g class="pb" style="animation-delay:-0.0s"><g transform="rotate(44.8 90 146.3)" opacity="0.9"><use href="#mtp" x="15" y="92.4" width="150" height="107.9"/></g></g><g class="pb" style="animation-delay:-0.9s"><g transform="rotate(37.0 300 174.3)" opacity="1"><use href="#mtp" x="240" y="131.2" width="120" height="86.3"/></g></g><g class="pb" style="animation-delay:-1.8s"><g transform="rotate(26.3 520 165.0)" opacity="0.55"><use href="#mtp" x="425" y="96.7" width="190" height="136.6"/></g></g><g class="pb" style="animation-delay:-2.7s"><g transform="rotate(22.1 740 124.4)" opacity="1"><use href="#mtp" x="670" y="74.0" width="140" height="100.7"/></g></g><g class="pb" style="animation-delay:-3.6s"><g transform="rotate(26.5 930 90.3)" opacity="0.85"><use href="#mtp" x="875" y="50.8" width="110" height="79.1"/></g></g><g class="pb" style="animation-delay:-4.5s"><g transform="rotate(36.3 1130 81.0)" opacity="0.6"><use href="#mtp" x="1042" y="18.0" width="175" height="125.8"/></g></g><g class="pb" style="animation-delay:-5.4s"><g transform="rotate(44.3 1330 105.0)" opacity="1"><use href="#mtp" x="1262" y="56.4" width="135" height="97.1"/></g></g><g class="pb" style="animation-delay:-6.3s"><g transform="rotate(45.1 1520 143.4)" opacity="0.8"><use href="#mtp" x="1457" y="98.4" width="125" height="89.9"/></g></g></svg></div></footer>'''
CHAT='''<aside class="mtchat" id="mtchat" aria-label="Chat con Mediatic" hidden>
<div class="mtc-card" role="dialog" aria-label="Chat con Mediatic" aria-hidden="true">
<button type="button" class="mtc-x" aria-label="Cerrar el chat"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3.5 3.5l9 9M12.5 3.5l-9 9" stroke="#fff" stroke-width="2" stroke-linecap="round"/></svg></button>
<div class="mtc-top"><div class="mtc-who"><b>Habla con Roger y Esteve</b><span class="mtc-st"><i></i><em>En línea</em></span></div><div class="mtc-av"><img src="img/equipo/roger-gaona-avatar.jpg" alt="Roger Gaona" width="44" height="44" loading="lazy"><img src="img/equipo/esteve-gaona-avatar.jpg" alt="Esteve Gaona" width="44" height="44" loading="lazy"></div></div>
<button type="button" class="mtc-go" data-chat-open><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M4 4h16a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H9l-4.2 3.6A.8.8 0 0 1 3.5 20V17H4a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2zm4 5.2a1.2 1.2 0 1 0 0 2.4 1.2 1.2 0 0 0 0-2.4zm4 0a1.2 1.2 0 1 0 0 2.4 1.2 1.2 0 0 0 0-2.4zm4 0a1.2 1.2 0 1 0 0 2.4 1.2 1.2 0 0 0 0-2.4z"/></svg><span>Chatea con Mediatic</span></button>
<p class="mtc-note">Al abrir el chat se carga Crisp, nuestro proveedor de chat. <a data-legal="privacidad" href="politica-privacidad.html">Privacidad</a></p>
</div>
<button type="button" class="mtc-fab" aria-label="Abrir el chat con Mediatic"><img src="img/equipo/roger-gaona-avatar.jpg" alt="" width="60" height="60" loading="lazy"><i></i></button>
</aside>'''
def page(file,title,body):
    st,desc,index=SEO.get(file,(title,'',True))
    robots='index,follow,max-image-preview:large' if index else 'noindex,follow'
    cls=' class="mfaq"' if 'faq-blue' in body[-12000:] and body.rstrip().endswith('</section>') else ''
    html=f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(st)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="{robots}">
{"" if file=="404.html" else '<link rel="canonical" href="'+canon(file)+'">'}
<meta name="theme-color" content="#1B1BCB">
<link rel="icon" href="favicon.svg" type="image/svg+xml"><link rel="icon" href="favicon-32.png" sizes="32x32" type="image/png"><link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta property="og:type" content="website"><meta property="og:site_name" content="Mediatic"><meta property="og:locale" content="es_ES">
<meta property="og:title" content="{esc(st)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{canon(file)}">
<meta property="og:image" content="{SITE}/img/og-image.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Mediatic, agencia de contenido viral en Barcelona">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(st)}"><meta name="twitter:description" content="{esc(desc)}"><meta name="twitter:image" content="{SITE}/img/og-image.jpg">
<link rel="preload" href="assets/fonts/SFProDisplay-Bold.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="styles.css?v={V}">
<script type="application/ld+json">{jsonld(file,st,desc)}</script>
</head>
<body>
<a class="skip" href="#contenido">Saltar al contenido</a>
{header(file)}
<main id="contenido"{cls}>
{body}
</main>
{FOOT}
{CHAT}
<script src="enlaces.js?v={V}"></script>
<script src="site.js?v={V}"></script>
<script src="cookies.js?v={V}"></script>
<script src="chat.js?v={V}"></script>
</body></html>'''
    open(os.path.join(OUT,file),'w').write(html)

CLIENTES_ORDEN=[1, 2, 3, 5, 4, 8, 7, 9, 10, 16, 11, 12, 20, 13, 14, 21, 15, 17, 23, 18, 19, 24, 22, 25, 26, 27, 28, 30, 29, 31, 6, 32, 33]
CLIENTES_NOMBRES={1: 'Manuel Costiña', 2: 'UPC', 3: 'Holcim', 4: 'Condis', 5: 'Adrià Solà Pastor', 6: 'Tengo un Plan', 7: 'Cenando con Pablo', 8: 'Làctics La Torre', 9: 'Banc de Sang', 10: 'Laboratorios SVR', 11: 'Vilà Vila', 12: 'Port Calella', 13: 'Sencor', 14: 'Sistach Security', 15: 'Cafès del Bages', 16: 'Oscar RGB', 17: 'SD Finance', 18: 'ICO', 19: 'IMP', 20: 'Pedro SEO', 21: 'Gisela Jorba', 22: 'De Profundis', 23: 'Mario Cozma', 24: 'Karoma', 25: 'Claudia&Julia', 26: 'Pol Corominas', 27: 'Sosa', 28: 'La School of Dance', 29: 'PrintDossier', 30: 'Peter Lead', 31: 'Centre Enric Pintado', 32: 'LC Lasers', 33: 'Jack Beds'}
CLIENTES_FRASES={1: 'Chef', 2: 'Universidad politécnica pública', 3: 'Soluciones de construcción', 4: 'Supermercados desde 1961', 5: 'Creador con +1M en YouTube', 6: 'Podcast de emprendimiento', 7: 'Creador gastro, +500K en YouTube', 8: 'Productos lácteos', 9: 'Banco de sangre de Catalunya', 10: 'Dermocosmética francesa', 11: 'Grupo empresarial', 12: 'Inmobiliaria', 13: 'Electrónica y electrodomésticos', 14: 'Sistemas de seguridad', 15: 'Tostadores de café', 16: 'Creador de contenido', 17: 'Asesoría financiera', 18: 'Instituto de comunicación', 19: 'Instituto de marca personal', 20: 'Experto SEO, +500K seguidores', 21: 'Experta en micropigmentación', 22: 'Buceo técnico', 23: 'Transporte y logística, +70K', 24: 'Peluquería en Manresa', 25: 'Tienda online de cocina', 26: 'Marca personal', 27: 'Ingredientes para gastronomía', 28: 'Escuela de baile', 29: 'Impresión online', 30: 'Agencia SEO en Barcelona', 31: 'Clínica dental', 32: 'Soluciones láser industriales', 33: 'Marca de colchones'}
def card(n,dup=False):
    nm=CLIENTES_NOMBRES[n].replace('&','&amp;')
    return ('<div class="cl"%s><div class="ph"><img src="img/clientes/c%02d.jpg" alt="%s" width="320" height="320" decoding="async"></div><p class="cn">%s</p><p>%s</p></div>'
            %(' aria-hidden="true"' if dup else '',n,'' if dup else nm,nm,CLIENTES_FRASES[n]))
r1=''.join(card(n) for n in CLIENTES_ORDEN)
r1d=''.join(card(n,True) for n in CLIENTES_ORDEN)
MARQ='<div class="marquee"><div class="track">%s%s</div></div>'%(r1,r1d)
SERV='''<div class="cards3">
 <div class="card"><div class="ico"></div><span class="chip">Done for you</span><h3>Servicio 1</h3><p class="d">[Descripción corta del servicio completo.]</p><ul><li>Beneficio 1</li><li>Beneficio 2</li><li>Beneficio 3</li><li>Beneficio 4</li></ul><a class="btn" href="index.html#contacto" data-link="servicios-1">Quiero saber más <i>→</i></a></div>
 <div class="card"><div class="ico"></div><span class="chip">Consultoría</span><h3>Servicio 2</h3><p class="d">[Descripción corta del servicio de estrategia.]</p><ul><li>Beneficio 1</li><li>Beneficio 2</li><li>Beneficio 3</li></ul><a class="btn" href="index.html#contacto" data-link="servicios-2">Quiero saber más <i>→</i></a></div>
 <div class="card hl"><div class="ico"></div><span class="chip">Diagnóstico 1:1</span><h3>Sesión de diagnóstico</h3><p class="d">[Descripción corta de la sesión de diagnóstico.]</p><ul><li>Beneficio 1</li><li>Beneficio 2</li><li>Beneficio 3</li></ul><a class="btn" href="index.html#contacto" data-link="servicios-3">Reserva tu sesión <i>→</i></a></div>
</div>'''
CASES='''<div class="cards2">
 <div class="case"><div class="vid"><div class="play">▶</div></div><h3>[Cliente A] consiguió <u>[resultado]</u> en [tiempo] con Mediatic.</h3><ul><li>Llegó a Mediatic con [punto de partida].</li><li>Diseñamos la estrategia y operamos [qué hicimos].</li><li>[Resultado destacado].</li></ul></div>
 <div class="case"><div class="vid"><div class="play">▶</div></div><h3>[Cliente B] consiguió <u>[resultado]</u> con Mediatic.</h3><ul><li>Llegó a Mediatic con [punto de partida].</li><li>Operamos su cuenta con [qué hicimos].</li><li>[Resultado destacado].</li></ul></div>
</div>'''
TESTI='''<section class="testi"><div class="wrap"><blockquote>“[Testimonio de cliente: 2–4 líneas contando cómo Mediatic cambió su resultado.]”</blockquote>
<div class="n">Nombre cliente</div><div class="s">00K Seguidores</div>
<div class="avs"><div class="av on"></div><div class="av"></div><div class="av"></div><div class="av"></div><div class="av"></div><div class="av"></div></div></div></section>'''
def head(tag,h1,sub): return f'<section class="page-head"><div class="wrap"><div class="tag">{tag}</div><h1>{h1}</h1><p class="sub">{sub}</p></div></section>'

ABOUT=open('/Users/mediaticmac/landing-page/web/_build/about.html').read()
import json,html as _h
_E=json.load(open('/Users/mediaticmac/landing-page/web/_build/entrevistas.json'))
def _card(t):
    name=_h.escape(t['name']);vid=t['id']
    if t.get('avatar'): av='<img src="%s" alt="%s" width="64" height="64" loading="lazy">'%(t['avatar'],name)
    else: av='<span class="rinit" aria-hidden="true">%s</span>'%_h.escape(t.get('iniciales','')[:2])
    return ('<article class="rcard"><div class="rthumb" data-yt="%s" data-kind="h" role="button" tabindex="0" aria-label="Ver charla con %s"><img src="img/entrevistas/%s.jpg" alt="Charla con %s: vídeo de la entrevista" width="640" height="360" loading="lazy" decoding="async"><span class="rplay">&#9654;</span></div>'
      '<div class="rauth">%s<b>%s</b>%s</div>'
      '<h3>%s</h3>%s</article>')%(vid,name,vid,name,av,name,('<span>%s</span>'%_h.escape(t['niche'])) if t.get('niche') else '',_h.escape(t['headline']),('<p>%s</p>'%_h.escape(t['context'])) if t.get('context') else '')
RESULTS=('<section class="results" id="opiniones"><div class="wrap"><div class="tag">Opiniones</div>'
 '<h2 class="sec-h"><span class="strike">No lo decimos nosotros</span><br><span class="hand">lo dicen ellos</span></h2>'
 '<p class="sub" style="max-width:700px">Charlas con nuestros clientes que revelan su opinión sobre el servicio.</p>'
 '<div class="rgrid">'+''.join(_card(t) for t in _E)+'</div></div></section>')
# --- HOME: solo 3 entrevistas (Marina, Mario, Gisela) + "Ver más" → opiniones.html ---
_HOME_ENT=[0,2,1]
RESULTS_HOME=('<section class="results" id="opiniones"><div class="wrap"><div class="tag">Opiniones</div>'
 '<h2 class="sec-h"><span class="strike">No lo decimos nosotros</span><br><span class="hand">lo dicen ellos</span></h2>'
 '<p class="sub" style="max-width:700px">Charlas con nuestros clientes que revelan su opinión sobre el servicio.</p>'
 '<div class="rgrid">'+''.join(_card(_E[i]) for i in _HOME_ENT)+'</div>'
 '<div class="more-cta"><a class="btn" href="opiniones.html">Ver más opiniones <i>→</i></a></div></div></section>')
_RES_ROWS=[[1, 37, 73, 34, 70, 31, 67, 28, 64, 25, 61, 22, 58, 19, 55, 16, 52, 13, 49, 10, 46, 7, 43, 4, 40], [26, 62, 23, 59, 20, 56, 17, 53, 14, 50, 11, 47, 8, 44, 5, 41, 2, 38, 74, 35, 71, 32, 68, 29, 65], [15, 51, 12, 48, 9, 45, 6, 42, 3, 39, 75, 36, 72, 33, 69, 30, 66, 27, 63, 24, 60, 21, 57, 18, 54]]
def _rrow(ids,rev):
    cards=''.join('<div class="rr"><img src="img/resultados/v%02d.jpg" alt="Vídeo de resultados de un cliente de Mediatic" width="300" height="469" loading="lazy" decoding="async"></div>'%i for i in ids)
    dup=''.join('<div class="rr" aria-hidden="true"><img src="img/resultados/v%02d.jpg" alt="" width="300" height="469" loading="lazy" decoding="async"></div>'%i for i in ids)
    return '<div class="rrow"><div class="rtrack%s">%s%s</div></div>'%(' rev' if rev else '',cards,dup)
RES2=('<section class="reels" id="resultados"><div class="wrap"><div class="reels-box">'
 '<div class="reels-head"><div class="tag">Resultados</div>'
 '<h2 class="sec-h">+300 millones de views, <span class="hand">y sumando</span></h2></div>'
 '<div class="reels-rows">'+_rrow(_RES_ROWS[0],False)+_rrow(_RES_ROWS[1],True)+_rrow(_RES_ROWS[2],False)+'</div>'
 '<div class="reels-cta"><a class="btn light" href="index.html#contacto" data-link="resultados">Quiero estos resultados <i>→</i></a></div>'
 '</div></div></section>')
# --- HOME: una sola tira con todos los vídeos rotando + "Ver más" → resultados.html ---
_ALL=[x for t in zip(*_RES_ROWS) for x in t]
_STATS=('<div class="stats">'
 '<div class="stat"><b><span class="pl">+</span><span class="cnt" data-to="100">100</span></b><span>Clientes satisfechos</span></div>'
 '<div class="stat"><b><span class="pl">+</span><span class="cnt" data-to="300" data-suf="M">300M</span></b><span>Millones de views</span></div>'
 '<div class="stat"><b><span class="pl">+</span><span class="cnt" data-to="30">30</span></b><span>Nichos viralizados</span></div></div>')
RES2_HOME=('<section class="reels reels-stats" id="resultados"><div class="wrap"><div class="reels-box">'
 '<div class="reels-rows">'+_rrow(_ALL,False).replace('class="rtrack','class="rtrack one')+'</div>'
 '</div>'+_STATS+'<div class="rs-cta"><a class="btn" href="index.html#contacto" data-link="hero">Quiero conseguir estos resultados <i>→</i></a><a class="btn light" href="resultados.html">Ver más resultados <i>→</i></a></div></div></section>')
# --- Página de resultados (3 tiras, sin cabecera interna) ---
RES2_PAGE=('<section class="reels" id="resultados"><div class="wrap"><div class="reels-box">'
 '<div class="reels-rows">'+_rrow(_RES_ROWS[0],False)+_rrow(_RES_ROWS[1],True)+_rrow(_RES_ROWS[2],False)+'</div>'
 '<div class="reels-cta"><a class="btn light" href="index.html#contacto" data-link="resultados">Quiero estos resultados <i>→</i></a></div>'
 '</div></div></section>')
_PEOPLE=[("Roger Gaona","Fundador"),("Esteve Gaona","Fundador"),("Betlem Boixader","Directora de edición"),("Anna Martínez","Copywriter"),("Mireia Sallés","Copywriter"),("Gerard Torres","Filmmaker"),("Juan Andrés","Editor"),("Juanjo","Editor")]
MTSVG='<svg viewBox="0 0 100 100" aria-hidden="true"><polygon fill="#fff" points="80,28.5 20,46.1 35.3,52 37,58 44.2,53.1 48.9,71.7"/></svg>'
import unicodedata
def _slug(n): return re.sub(r'[^a-z0-9]+','-',unicodedata.normalize('NFKD',n).encode('ascii','ignore').decode().lower()).strip('-')
def _member(i):
    n,r=_PEOPLE[i-1]
    sl=_slug(n)
    def ph(suffix,label):
        f='img/equipo/%s%s.jpg'%(sl,suffix)
        if os.path.exists(os.path.join(OUT,f)): return '<img src="%s" alt="%s" loading="lazy">'%(f,(n if not suffix else n+' (foto de broma)'))
        return '<span>%s</span>'%label
    return ('<div class="member" tabindex="0"><div class="mphoto main">'+ph('','Foto')+'</div><div class="mphoto joke">'+ph('-broma','¡Foto de broma!')+'</div>'
            '<div class="mlabel"><i class="in">'+MTSVG+'</i><div><b>%s</b><span>%s</span></div></div></div>')%(n,r)
TEAM_GRID='<div class="mgrid">'+''.join(_member(i) for i in range(1,9))+'</div>'
TEAM=('<section class="team-sec" id="equipo"><div class="wrap"><div class="tag">Equipo</div>'
 '<h2 class="sec-h">¿Quién está detrás de <span class="acc">Mediatic</span>?</h2>'
 '<p class="sub" style="margin-bottom:8px">Nuestro equipo de expertos en contenido</p>'+TEAM_GRID+'</div></section>')
_REV=[("Pedro SEO","+240.000 seguidores","Llevo tiempo trabajando con Roger y Steve y no puedo estar más contento con sus servicios. Son creativos, profesionales y siempre entregan contenido de calidad adaptado a lo que necesito. Si quieres crecer en redes sociales, pruébalos.","img/clientes/c20.jpg"),
("Tengo un Plan","+2.450.000 seguidores","Gente muy profesional!","img/clientes/c06.jpg"),
("Cenando con Pablo","+928.000 seguidores","Buen trabajo por su parte durante un evento gastronómico en Barcelona, ¡Muchas gracias!","img/clientes/c07.jpg"),
("Top Catalan Restaurants","+140.000 seguidores","Nos crearon un vídeo promocional para dar visibilidad a nuestro proyecto. Grandes profesionales, creativos y de trato cercano y ágil.","img/clientes/top-catalan-restaurants.jpg"),
("Sor Lucía Caram","+150.000 seguidores","Unos grandes profesionales. La calidad de su trabajo en redes, cuidando todos los detalles, los hace una opción importante para dar a conocer una marca, un proyecto, una idea. ¡Gracias!","img/clientes/sor-lucia-caram.jpg"),
("Mario Cozma","+77.400 seguidores","Llevamos trabajando con ellos más de 8 meses y muy contentos, son muy top. ¡Espero que sigan así muchos años!","img/clientes/c23.jpg"),
("Pol Corominas","+240.000 seguidores","Destaco su profesionalidad, su cercanía y la facilidad para trabajar con ellos. Un equipo creativo, resolutivo y muy alineado con lo que necesita cualquier negocio.","img/clientes/c26.jpg"),
("Instituto de Comunicación","+280.000 seguidores","Nos ha encantado trabajar juntos. La grabación fue súper efectiva: grabamos todo lo propuesto y los chicos hicieron incluso más de lo que se pedía. Un placer.","img/clientes/c18.jpg")]
def _gslide(i,n,sub,txt,img):
    return ('<figure class="gq%s%s" data-i="%d"><blockquote>“%s”</blockquote>'
            '<figcaption><b>%s</b><span>%s</span></figcaption></figure>')%(' on' if i==0 else '',(' long' if len(txt)>200 else (' mid' if len(txt)>140 else '')),i,txt,n,sub)
def _gav(i,n,img):
    inner=('<img src="%s" alt="%s" width="120" height="120">'%(img,n)) if img else '<span>%s</span>'%''.join(w[0] for w in n.split()[:2]).upper()
    return '<button class="gav%s" data-i="%d" aria-label="Reseña de %s">%s</button>'%(' on' if i==0 else '',i,n,inner)
REVIEWS=('<section class="greviews" id="resenas" aria-labelledby="h-resenas"><div class="wrap"><h2 class="sr-only" id="h-resenas">Reseñas de clientes en Google</h2>'
 '<div class="grate"><span class="stars">★★★★★</span><b>5,0</b><span>+150 reseñas en Google</span></div>'
 '<div class="gstage">'+''.join(_gslide(i,n,sub,txt,img) for i,(n,sub,txt,img) in enumerate(_REV))+'</div>'
 '<div class="gnav"><button class="garr" data-d="-1" aria-label="Anterior">←</button>'+''.join(_gav(i,n,img) for i,(n,sub,txt,img) in enumerate(_REV))+'<button class="garr" data-d="1" aria-label="Siguiente">→</button></div>'
 '</div></section>')
exec(open('/Users/mediaticmac/landing-page/web/_build/faq_data.py').read())
faq=''.join('<details><summary><h3>%s</h3></summary><p>%s</p></details>'%(q,a) for q,a in FAQ_DATA)
FAQ_BLUE='<section class="faq faq-blue" id="faq"><div class="wrap"><div class="tag">Por si te quedas con dudas</div><h2 class="sec-h">Preguntas frecuentes sobre contenido para redes sociales</h2><p class="sub">Resuelve todas las dudas que tengas.</p><div class="faq-list">'+faq+'</div></div></section>'
QUOTE=open('/Users/mediaticmac/landing-page/web/_build/quote.html').read()
# HOME
MARQ_HOME=MARQ.replace('class="track"','class="track rev"',1)   # la cinta de clientes va a la derecha; la de resultados a la izquierda
page('index.html','Mediatic | Agencia de contenido orgánico',f'''
<section class="hero"><div class="wrap hero-wrap">
 <h1>Agencia de <span class="acc">contenido viral</span><br>en Barcelona</h1>
 <p class="hero-sub">Multiplicamos <b class="hl">x5</b> tus <b class="hl">visitas</b> y <b class="hl">leads</b><br>en Instagram con menos de 5h al mes</p>
 </div><canvas id="fly"></canvas></section>
{RES2_HOME}
<section><div class="wrap"><div class="tag">Clientes</div><h2 class="sec-h" style="margin-bottom:28px">Estos son nuestros <span class="strike">clientes</span> <span class="hand">amigos</span></h2>{MARQ_HOME}</div></section>
{ABOUT}
{RESULTS_HOME}{TEAM}{REVIEWS}{QUOTE}
{FAQ_BLUE}''')

# PÁGINAS NUEVAS: opiniones y resultados (el menú de arriba apunta aquí)
page('opiniones.html','Opiniones | Mediatic','<section class="page-head ph-center ph-tight"><div class="wrap"><div class="tag">Opiniones de Mediatic</div><h1>Escucha a quienes ya <span class="pen">crecen con nosotros</span></h1><p class="sub">Entrevistas con nuestros clientes, donde son ellos mismos los que cuentan, con sus propias palabras, los beneficios de trabajar con Mediatic y cómo ha cambiado su negocio desde que lo hacen.</p></div></section><section class="results opi-sec" style="padding-top:0"><div class="wrap"><h2 class="sr-only">Opiniones de clientes de Mediatic: entrevistas en vídeo</h2><div class="rgrid opi-grid" style="margin-top:0">'+''.join(_card(t) for t in _E)+'</div></div><div class="flight" aria-hidden="true"><svg class="fl-path" viewBox="0 0 1000 392" preserveAspectRatio="none" focusable="false"><path d="M0 140 C 50 140 110 230 150 300 C 173 340 260 385 340 385 C 420 385 505 350 545 300 C 570 268 580 190 620 190 C 660 190 685 250 697 300 C 707 334 735 372 770 372 C 805 372 835 360 860 352" fill="none" stroke="#1B1BCB" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" vector-effect="non-scaling-stroke"/></svg><svg class="fl-plane" focusable="false"><g transform="rotate(17) scale(.12) translate(-718 -1107)"><polygon points="1545,590 342,942 648,1060 681,1180 826,1082 921,1455" fill="#1B1BCB"/><polygon points="648,1060 681,1180 826,1082" fill="#fff" fill-opacity=".35"/></g></svg></div></section><section class="rev-intro"><div class="wrap"><div class="casos-intro"><p class="ci-eyebrow">Clientes satisfechos</p><h2 class="sec-h">Clientes que confían en Mediatic</h2><p class="ci-sub">Más de 100 empresas y profesionales ya han confiado en nuestro equipo para hacer crecer sus redes sociales.<br>Descubre lo que opinan en Google sobre Mediatic.</p></div></div></section>'+REVIEWS+QUOTE)
# (la página resultados.html se genera más abajo, después de definir las tarjetas del blog)


page('equipo.html','Equipo | Mediatic',head('Equipo','El equipo de <span class="acc">Mediatic</span>: expertos en contenido viral','Nuestro equipo de expertos en contenido')+'<section style="padding-top:0"><div class="wrap"><h2 class="sr-only">Miembros del equipo de Mediatic</h2>'+TEAM_GRID+'</div></section>')

page('clientes.html','Clientes | Mediatic',head('Clientes','Estos son nuestros <span class="strike">clientes</span> <span class="hand">amigos</span>','Negocios, marcas y creadores que ya crecen en redes sociales con Mediatic.')+f'<section><div class="wrap">{MARQ}</div></section>{RESULTS}{RES2}{REVIEWS}')

BLOG_CATS=['Noticias','Consejos','Resultados','Servicios']
def _post(i):
    return f'<a class="post" href="#" data-cat="{BLOG_CATS[(i-1)%3]}"><div class="th"></div><div class="c">{BLOG_CATS[(i-1)%3]}</div><h3>[Título del artículo {i}]</h3><p class="sub" style="font-size:16px">[Resumen de 1–2 líneas del artículo.]</p></a>'
def _real(f,a):
    soon=' · Próximamente' if a.get('draft') else ''
    dt='<time class="pdate" datetime="%s">%s</time>'%(a['date'],a['fecha']) if a.get('date') else ''
    th='<div class="th" style="background:url(%s) center/cover"></div>'%a['thumb'] if os.path.exists(os.path.join(OUT,a['thumb'])) else '<div class="th"></div>'
    return f'<a class="post" href="{f}" data-cat="{a["cat"]}">{th}<div class="c">{a["cat"]}{soon}</div><h3>{a["h1"]}</h3><p class="sub" style="font-size:16px">{a["excerpt"]}</p>{dt}</a>'
posts=''.join(_real(f,a) for f,a in ART_META.items())
bfilter='<div class="bfilter" role="group" aria-label="Filtrar artículos por categoría"><button type="button" class="on" data-cat="">Todos</button>'+''.join(f'<button type="button" data-cat="{c}">{c}</button>' for c in BLOG_CATS)+'</div>'
page('blog.html','Blog | Mediatic',head('Blog','Blog de <span class="acc">contenido viral</span>: consejos, noticias y casos de éxito','Últimas noticias y novedades sobre el funcionamiento del contenido orgánico, para que aprendas y lo apliques en tu negocio. También verás las noticias y logros de la agencia.')+f'<section><div class="wrap">{bfilter}<h2 class="sr-only">Últimos artículos del blog</h2><div class="posts">{posts}</div><p class="bempty" hidden>Todavía no hay artículos en esta categoría. Muy pronto publicaremos novedades.</p></div></section>')

# ---- CASOS DE ÉXITO (menú «Casos de éxito»): cabecera + vídeos + casos del blog ----
# El avión llega por encima de la caja azul de vídeos, se "mete" en ella (queda tapado por la caja) y sale por debajo.
def _plane(x,y,rot,s=.11):
    # (x,y) = punto donde el camino llega al avión (la muesca de la cola); el avión sigue hacia delante
    return ('<g transform="translate(%s %s) rotate(%s) scale(%s) translate(-718 -1107)">'
     '<polygon points="1545,590 342,942 648,1060 681,1180 826,1082 921,1455" fill="#1B1BCB"/>'
     '<polygon points="648,1060 681,1180 826,1082" fill="#fff" fill-opacity=".35"/></g>')%(x,y,rot,s)
# Un solo avión: el camino entra desde la izquierda, se mete bajo la caja azul y sale por arriba a la derecha, donde termina el avión.
_PD_IN=('<svg class="pd pd-in" viewBox="0 0 800 140" aria-hidden="true" focusable="false">'
 '<path d="M0 138 C 140 52 300 10 460 54 C 580 86 660 126 740 148" fill="none" stroke="#1B1BCB" stroke-width="6" stroke-linecap="round"/></svg>')
_PD_OUT_S=('<svg class="pd pd-out-s" viewBox="0 0 260 130" aria-hidden="true" focusable="false">'
 '<path d="M26 140 C 90 135 140 120 190 72" fill="none" stroke="#1B1BCB" stroke-width="5" stroke-linecap="round"/>'
 +_plane(190,72,-12,.085)+'</svg>')
_PD_OUT=('<svg class="pd pd-out" viewBox="0 0 420 340" aria-hidden="true" focusable="false">'
 '<path d="M110 352 C 170 300 235 215 300 150" fill="none" stroke="#1B1BCB" stroke-width="6" stroke-linecap="round"/>'
 +_plane(300,150,-13,.12)+'</svg>')
_RES2_CASOS=RES2_PAGE.replace('<div class="wrap"><div class="reels-box">','<div class="wrap">'+_PD_IN+_PD_OUT+_PD_OUT_S+'<div class="reels-box"><div class="reels-head"><h2 class="sec-h">+300 millones de views, <span class="hand">y sumando</span></h2></div>')
# Tarjetas de casos de éxito (enlazan al artículo del blog). Pack = pendiente de definir por el cliente.
CASOS_CARD={
 'caso-exito-manuel-costina.html':('Manuel Costiña','Chef','**Próximamente**',''),
 'caso-exito-gisela-jorba.html':('Gisela Jorba','Micropigmentación','**Ha duplicado su lista de espera**',' en su centro, pasando de **6 meses a 1 año**.'),
 'caso-exito-marina-garrido.html':('Dra. Marina Garrido','Clínica de injertos capilares','**Capta clientes**',' para su clínica **a través de redes** con menos de 2 h al mes.'),
 'caso-exito-mario-cozma.html':('Mario Cozma','Transporte y logística','De 34.000 a **más de 77.000 seguidores** en Instagram',' y posicionado como **referente del transporte en redes**.'),
 'caso-exito-pedro-seo.html':('Pedro SEO','SEO y marketing','Capta **más clientes para su agencia** y más alumnos para su formación',' gracias a nuestro contenido, **con solo 6 horas al mes**.'),
 'caso-exito-sosa-ingredients.html':('Sosa Ingredients','Ingredientes para cocina','**Dejamos atrás la comunicación corporativa**',' y crecimos **+10.000 seguidores en 3 meses**.'),
 'caso-exito-la-school-of-dance.html':('La School of Dance','Escuela de baile','Consiguimos **+8 millones de visualizaciones**',' en los **primeros 2 meses**.'),
 'de-profundis.html':('De Profundis','Buceo técnico','**Recibe clientes** cada día desde Instagram',' **con menos de 2 horas al mes**.'),
}
CASOS_PACK={'caso-exito-sosa-ingredients.html':'Pack personalizado','caso-exito-la-school-of-dance.html':'Pack Básico','caso-exito-pedro-seo.html':'Pack personalizado','caso-exito-manuel-costina.html':'Pack Pro','caso-exito-gisela-jorba.html':'Pack Básico','caso-exito-marina-garrido.html':'Pack Starter','caso-exito-mario-cozma.html':'Pack Pro','de-profundis.html':'Pack Starter'}
CASOS_USER={'caso-exito-sosa-ingredients.html':'@sosaingredients','caso-exito-la-school-of-dance.html':'@laschoolofdance','caso-exito-pedro-seo.html':'@pedroseo_','caso-exito-gisela-jorba.html':'@giselajorba_micropigmentacion','caso-exito-marina-garrido.html':'@dra.marinagarrido','caso-exito-mario-cozma.html':'@mcozma1','de-profundis.html':'@de_profundis_ig'}   # Manuel Costiña: pendiente de usuario
CASOS_AVATAR={'caso-exito-sosa-ingredients.html':'img/testimonios/sosa.png','caso-exito-la-school-of-dance.html':'img/testimonios/laschool.png','caso-exito-pedro-seo.html':'img/testimonios/pedro.png','caso-exito-manuel-costina.html':'img/clientes/c01.jpg','caso-exito-gisela-jorba.html':'img/testimonios/gisela.png','caso-exito-marina-garrido.html':'img/testimonios/marina.png','caso-exito-mario-cozma.html':'img/testimonios/mario.png','de-profundis.html':'img/testimonios/deprofundis.png'}
def _ccard(f,a):
    n,nicho,hb,hr=CASOS_CARD[f]
    pk=CASOS_PACK.get(f,'Pack por definir')
    ph=('<img src="%s" alt="Foto de %s" width="640" height="400" loading="lazy" decoding="async">'%(a['thumb'],esc(n))) if os.path.exists(os.path.join(OUT,a['thumb'])) else ''
    av=CASOS_AVATAR.get(f,'')
    avh=('<img src="%s" alt="%s" width="64" height="64" loading="lazy">'%(av,esc(n))) if av and os.path.exists(os.path.join(OUT,av)) else '<span class="rinit" aria-hidden="true">%s</span>'%''.join(w[0] for w in n.split()[:2]).upper()
    return ('<a class="ccard" href="%s"><div class="cc-top"><div class="rauth">%s<div class="rwho"><h3>%s</h3>%s</div></div><span class="cc-pack">%s</span></div><div class="cc-photo">%s</div>'
            '<div class="cc-body"><span class="cc-niche">%s</span><p class="cc-hl">%s</p></div></a>')%(f,avh,esc(n),('<small>%s</small>'%esc(CASOS_USER[f])) if f in CASOS_USER else '',esc(pk),ph,esc(nicho),re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',esc(hb+hr)))
# Orden de las tarjetas de «Casos de éxito»: manual (no por fecha). Para cambiarlo, reordena esta lista; los casos que no estén aquí salen al final, por fecha.
CASOS_ORDEN=['caso-exito-manuel-costina.html','caso-exito-gisela-jorba.html','caso-exito-marina-garrido.html','caso-exito-mario-cozma.html','caso-exito-pedro-seo.html','de-profundis.html']
_casos_ord=sorted([(f,a) for f,a in ART_META.items() if f in CASOS_CARD],key=lambda fa:(CASOS_ORDEN.index(fa[0]) if fa[0] in CASOS_ORDEN else len(CASOS_ORDEN)))
_CASOS=''.join(_ccard(f,a) for f,a in _casos_ord)
page('resultados.html','Casos de éxito | Mediatic','<section class="page-head ph-center"><div class="wrap"><div class="tag">Casos de éxito de Mediatic</div><h1>Nuestros clientes generan <span class="pen">más negocio</span> con contenido viral</h1><p class="sub">Con estrategias de contenido personalizadas, guiones validados y vídeos virales que atraen público cualificado y convierten tus redes en una fuente constante de clientes.</p></div></section>'+_RES2_CASOS+'<section class="casos-sec"><div class="wrap"><div class="casos-intro"><p class="ci-eyebrow">Datos reales de nuestros clientes</p><h2 class="sec-h">Casos de éxito de Mediatic</h2><p class="ci-sub">Hemos ayudado a negocios y marcas personales a aumentar las ventas de su negocio, a multiplicar sus visitas, sus seguidores y sus clientes con contenido orgánico. Estos son algunos de los resultados.</p></div><div class="ccards">'+_CASOS+'</div><div class="more-cta ccards-more" hidden><button type="button" class="btn">Ver más casos <i>→</i></button></div></div></section>'+QUOTE)

# ---- artículos del blog ----
for _f,_a in ART_META.items():
    SEO[_f]=(_a['title'],_a['desc'],not _a.get('draft'))
    if _f=='servicios.html':   # página de servicios con diseño propio (_build/servicios_page.html)
        page(_f,_a['h1'],open(os.path.join(OUT,'_build','servicios_page.html')).read().replace('{{MARQ}}',MARQ).replace('{{REV}}',REVIEWS).replace('{{RES2}}',RES2.replace('data-link="resultados"','data-link="ag-contenido-bcn"')))
        _p=os.path.join(OUT,_f); _t=open(_p).read().replace('data-link="cabecera"','data-link="ag-contenido-bcn"'); open(_p,'w').write(_t)
        continue
    _body=open(os.path.join(OUT,'_build','articulos',_f)).read()
    _vid=('<div class="avid" data-vid="%s" role="button" tabindex="0" aria-label="Reproducir el vídeo: %s">%s<span class="rplay">&#9654;</span></div>'%(_a.get('yt',''),esc(_a['h1']),('<img src="%s" alt="Vídeo: %s" width="1280" height="720" loading="lazy" decoding="async">'%(_a['thumb'],esc(_a['h1']))) if os.path.exists(os.path.join(OUT,_a['thumb'])) else ''))+'<p class="vcap">Vídeo sobre los mitos de Instagram. Fuente: YouTube (canal de la agencia).</p>'
    _body=_body.replace('<!--VIDEO-->',_vid if _a.get('yt') else '')
    def _vid2(m):
        vid=m.group(1);th='img/entrevistas/%s.jpg'%vid
        im='<img src="%s" alt="Entrevista en vídeo" width="640" height="360" loading="lazy" decoding="async">'%th if os.path.exists(os.path.join(OUT,th)) else ''
        cap=m.group(2)
        return '<div class="avid" data-vid="%s" role="button" tabindex="0" aria-label="Reproducir la entrevista en vídeo">%s<span class="rplay">&#9654;</span></div>%s'%(vid,im,('<p class="vcap">%s</p>'%esc(cap)) if cap else '')
    _body=re.sub(r'<!--VIDEO:([\w-]+)(?:\|([^>]*?))?-->',_vid2,_body)
    def _photo(m):
        src,alt,cap,cred=m.group(1).split('|')
        base=src[:-4]
        _g=sorted(glob.glob(os.path.join(OUT,base+'-[0-9].jpg')))
        if _g:
            _alts=GAL_ALTS.get(base,[])
            _im=''.join('<img src="%s" alt="%s" loading="lazy" decoding="async">'%(os.path.relpath(p,OUT),esc(_alts[k] if k<len(_alts) else alt)) for k,p in enumerate(_g))
            return '<figure class="photo gal">%s%s</figure>'%(_im,('<figcaption>%s</figcaption>'%esc(cap)) if cap else '')
        if not os.path.exists(os.path.join(OUT,src)): return ''
        return '<figure class="photo%s"><img src="%s" alt="%s" loading="lazy" decoding="async">%s</figure>'%((' shot' if ('de-profundis-instagram-' in src or '-youtube' in src or '-antes' in src or '-comentarios' in src or '-vanguardia' in src or '-chat' in src) else ''),src,esc(alt),(('<figcaption>%s%s</figcaption>'%(esc(cap),('<br><span>Foto: %s</span>'%esc(cred)) if cred else ''))) if cap else '')
    _body=re.sub(r'<!--PROV:([^>]*?)-->',lambda m:'<figure class="photo prov" role="img" aria-label="%s"><div>Imagen provisional</div></figure>'%esc(m.group(1)),_body)
    _body=re.sub(r'<!--PHOTO:([^>]*?)-->',_photo,_body)
    _ks=list(ART_META);_i=_ks.index(_f)
    def _lk(k,lab):
        a2=ART_META[k];return '<a class="anx" href="%s"><small>%s</small><b>%s</b>%s%s</a>'%(k,lab,a2['h1'],('<span>%s</span>'%a2['sub']) if a2.get('sub') else '','<em>Próximamente</em>' if a2.get('draft') else '')
    _more=('<div class="acta nav"><span>Sigue leyendo</span>'+(_lk(_ks[_i-1],'← Más reciente') if _i>0 else '')+(_lk(_ks[_i+1],'Más antiguo →') if _i<len(_ks)-1 else '')+'</div>') if len(_ks)>1 else ''
    _aside=('<aside class="aside" aria-label="Contacto"><div class="aside-in">'
      '<div class="acta hl"><span>Crece con nosotros</span><h2>¿Hablamos de tu proyecto?</h2><p>Te decimos si podemos multiplicar por 5 tus visitas y leads con menos de 5 horas al mes.</p><a class="btn" href="index.html#contacto" data-link="blog-lateral">Agendar diagnóstico <i>→</i></a></div>'
      +_more+'</div></aside>')
    _head=('<section class="page-head art-head"><div class="wrap"><nav class="crumbs" aria-label="Migas de pan"><a href="index.html">Home</a><i>›</i><a href="blog.html">Blog</a><i>›</i><span aria-current="page">%s</span></nav><h1>%s</h1>%s<p class="byline">%s</p></div></section>'%(_a['h1'],_a['h1'],('<p class="art-sub">%s</p>'%_a['sub'] if _a.get('sub') else ''),(_a['cat']+' · Próximamente'+((' · '+_a['fecha']) if _a.get('fecha') else '')) if _a.get('draft') else '%s · Por el equipo de <b>Mediatic</b> · <time datetime="%s">%s</time> · %d min de lectura'%(_a['cat'],_a['date'],_a['fecha'],_a['mins'])))
    page(_f,_a['h1'],_head+'<section class="art"><div class="wrap art-grid"><article class="prose">'+_body+'</article>'+_aside+'</div></section>'+seguir(_f,ART_META,RELATED,OUT))


# ---- PÁGINAS LEGALES (texto copiado tal cual de legal.mediatic.io) ----
_LEG=[('aviso-legal.html','Aviso Legal'),('politica-privacidad.html','Política de Privacidad'),('politica-cookies.html','Política de Cookies')]
def _legal(file,title):
    body=open(SP_LEGAL+'/'+file).read()
    for a,b in (('/aviso-legal','aviso-legal.html'),('/politica-privacidad','politica-privacidad.html'),('/politica-cookies','politica-cookies.html')):
        body=body.replace('href="'+a+'"','href="'+b+'"')
    tabs=''.join('<a href="%s"%s>%s</a>'%(f,' class="on"' if f==file else '',t) for f,t in _LEG)
    page(file,title+' | Mediatic','<section class="page-head" style="padding-bottom:10px"><div class="wrap"><div class="tag">Información legal</div></div></section><section style="padding-top:0"><div class="wrap"><nav class="legal-tabs">'+tabs+'</nav><article class="legal">'+body+'</article></div></section>')
SP_LEGAL='/Users/mediaticmac/landing-page/web/_build/legal'
for _f,_t in _LEG: _legal(_f,_t)

# ---- CONTRATACIONES ----
JOBS='''<article class="job"><div class="jtop"><i class="jico"><svg viewBox="0 0 100 100" aria-hidden="true"><polygon fill="#fff" points="80,28.5 20,46.1 35.3,52 37,58 44.2,53.1 48.9,71.7"/></svg></i><span class="jbadge">Posición abierta</span></div><h3>Editor</h3><p>Conviertes vídeo en bruto en reels que retienen hasta el final. Buscamos a alguien con ojo para el ritmo, los subtítulos y el montaje pensado para redes sociales.</p><div class="jchips"><span>Reels</span><span>Montaje</span><span>Subtítulos</span><span>Retención</span></div><div class="jfoot"><span>Remoto · Jornada completa, media jornada o freelance</span><a class="btn sm" href="mailto:info@mediatic.io?subject=Candidatura%20Editor%20-%20Mediatic" data-link="aplicar-editor">Aplicar <i>→</i></a></div></article><article class="job"><div class="jtop"><i class="jico"><svg viewBox="0 0 100 100" aria-hidden="true"><polygon fill="#fff" points="80,28.5 20,46.1 35.3,52 37,58 44.2,53.1 48.9,71.7"/></svg></i><span class="jbadge">Posición abierta</span></div><h3>Filmmaker</h3><p>Buscamos a alguien con experiencia grabando y editando reels hablados a cámara para redes sociales. Si vives en España y crees que encajas, cuéntanos sobre ti.</p><div class="jchips"><span>Reels a cámara</span><span>Grabación</span><span>Edición</span></div><div class="jfoot"><span>Jornada completa, media jornada o freelance</span><a class="btn sm" href="../filmmakers/index.html" data-link="aplicar-filmmaker" target="_blank" rel="noopener">Aplicar <i>→</i></a></div></article><article class="job"><div class="jtop"><i class="jico"><svg viewBox="0 0 100 100" aria-hidden="true"><polygon fill="#fff" points="80,28.5 20,46.1 35.3,52 37,58 44.2,53.1 48.9,71.7"/></svg></i><span class="jbadge">Posición abierta</span></div><h3>Guionista</h3><p>Buscamos a alguien con experiencia guionizando reels virales para redes sociales. Si vives en España y crees que encajas, cuéntanos sobre ti.</p><div class="jchips"><span>Reels virales</span><span>Hooks</span><span>Copywriting</span></div><div class="jfoot"><span>Presencial · Jornada completa, media jornada o freelance</span><a class="btn sm" href="../guionistas/index.html" data-link="aplicar-guionista" target="_blank" rel="noopener">Aplicar <i>→</i></a></div></article>'''
_CONTRATACIONES_ELIMINADA=(  # página eliminada a petición del cliente (nov 2026); ya no se genera contrataciones.html
'<section class="page-head" style="padding-bottom:10px"><div class="wrap"><div class="tag">Posiciones abiertas</div><h1>Encuentra tu sitio en <span class="acc">Mediatic</span></h1><p class="sub">Buscamos gente que quiera hacer el mejor trabajo de su carrera. Estos son los roles que tenemos abiertos. Si no ves el tuyo pero crees que sumas, escríbenos igual.</p></div></section><section style="padding-top:20px"><div class="wrap"><h2 class="sr-only">Posiciones abiertas en Mediatic</h2><div class="jobs">'+JOBS+'</div><p class="jmore">¿No es un rol que encaje contigo, pero quieres trabajar con nosotros? <a href="mailto:info@mediatic.io?subject=Quiero%20trabajar%20en%20Mediatic" data-link="contrataciones-escribenos">Escríbenos igual →</a></p></div></section>'+FAQ_BLUE)

# ---- 404, robots.txt y sitemap.xml ----
page('404.html','Página no encontrada | Mediatic','<section class="page-head" style="min-height:62vh"><div class="wrap"><div class="tag">Error 404</div><h1>Esta página <span class="acc">no existe</span></h1><p class="sub" style="margin-bottom:30px">Puede que el enlace esté roto o que la página haya cambiado de sitio. Vuelve al inicio y te llevamos a donde quieras.</p><a class="btn" href="index.html">Ir al inicio <i>→</i></a></div></section>')
import datetime
_hoy=datetime.date.today().isoformat()
_urls=[f for f,(t,d,idx) in SEO.items() if idx and f!='404.html']
open(os.path.join(OUT,'sitemap.xml'),'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join('  <url><loc>%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>\n'%(canon(f),_hoy,'1.0' if f=='index.html' else ('0.3' if f.startswith(('aviso','politica')) else '0.8')) for f in _urls)+'</urlset>\n')
open(os.path.join(OUT,'robots.txt'),'w').write('User-agent: *\nAllow: /\nDisallow: /_build/\n\nSitemap: %s/sitemap.xml\n'%SITE)
print('ok')
