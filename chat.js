// ============================================================
//  CHAT DE LA WEB (Crisp)
//  - Muestra una tarjeta propia ("Habla con Roger y Esteve").
//  - Crisp NO se carga hasta que la persona pulsa "Chatea con Mediatic" (así no se instalan cookies de terceros antes).
//  - Si la persona ya abrió el chat antes (marca en su navegador), Crisp se carga solo para que no pierda la conversación.
//  La configuración (ID de Crisp, textos y horario) está en enlaces.js > CHAT.
// ============================================================
(function(){
  const C=(window.MEDIATIC||{}).CHAT||{};
  const root=document.getElementById('mtchat');
  if(!C.ID||!root)return;

  const KEY_ON='mt_chat_on', KEY_X='mt_chat_x', DIAS7=7*864e5, DIAS30=30*864e5;
  const rd=k=>{try{return JSON.parse(localStorage.getItem(k)||'null')}catch(e){return null}};
  const wr=(k,v)=>{try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}};

  const card=root.querySelector('.mtc-card'), fab=root.querySelector('.mtc-fab');
  const st=root.querySelector('.mtc-st'), stTxt=st.querySelector('em');
  if(C.TITULO)root.querySelector('.mtc-who b').textContent=C.TITULO;
  if(C.BOTON)root.querySelector('.mtc-go span').textContent=C.BOTON;

  // ¿Estamos dentro de horario? (hora de Madrid)
  function enHorario(){
    const h=C.HORARIO; if(!h)return true;
    try{
      const p=new Intl.DateTimeFormat('en-GB',{timeZone:h.zona||'Europe/Madrid',weekday:'short',hour:'2-digit',minute:'2-digit',hour12:false}).formatToParts(new Date());
      const g=t=>(p.find(x=>x.type===t)||{}).value;
      const dia={Mon:1,Tue:2,Wed:3,Thu:4,Fri:5,Sat:6,Sun:7}[g('weekday')];
      const min=(+g('hour')%24)*60+(+g('minute'));
      const tm=s=>{const a=s.split(':');return (+a[0])*60+(+a[1]||0)};
      return (h.dias||[]).indexOf(dia)>-1 && min>=tm(h.desde) && min<tm(h.hasta);
    }catch(e){return true}
  }
  const online=enHorario();
  st.classList.toggle('on',online);
  stTxt.textContent=online?'En línea':'Te respondemos en cuanto podamos';
  fab.classList.toggle('on',online);

  // Carga de Crisp (solo bajo petición)
  let cargado=false;
  function cargarCrisp(abrir){
    if(!cargado){
      cargado=true;
      window.$crisp=window.$crisp||[];
      window.CRISP_WEBSITE_ID=C.ID;
      const s=document.createElement('script');s.src='https://client.crisp.chat/l.js';s.async=true;document.head.appendChild(s);
    }
    if(abrir){window.$crisp.push(['do','chat:show']);window.$crisp.push(['do','chat:open'])}
    root.hidden=true;                       // Crisp ya pone su propio botón
  }

  // Si ya había abierto el chat hace menos de 30 días, lo cargamos para que vea las respuestas pendientes
  const on=rd(KEY_ON);
  if(on&&Date.now()-on<DIAS30){cargarCrisp(false);return}

  root.hidden=false;
  const cerrado=rd(KEY_X);
  const minimizada=cerrado&&Date.now()-cerrado<DIAS7;
  function mostrarTarjeta(){root.classList.remove('min');card.setAttribute('aria-hidden','false')}
  function minimizar(){root.classList.add('min');card.setAttribute('aria-hidden','true')}
  if(minimizada||matchMedia('(max-width:560px)').matches)minimizar();
  else{root.classList.add('min');setTimeout(mostrarTarjeta,3500)}   // aparece a los 3,5 s

  root.querySelector('.mtc-x').addEventListener('click',()=>{wr(KEY_X,Date.now());minimizar()});
  fab.addEventListener('click',mostrarTarjeta);
  root.querySelectorAll('[data-chat-open]').forEach(b=>b.addEventListener('click',()=>{
    wr(KEY_ON,Date.now());
    if(window.gtag&&window.__mtGA)window.gtag('event','chat_open',{pagina:location.pathname});
    cargarCrisp(true);
  }));
})();
