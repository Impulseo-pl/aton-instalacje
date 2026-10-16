(function(){
  var d=document.documentElement,pierwszy=d.classList.contains('pierwszy'),
      malo=window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ekran ładowania: min. 2,6 s przy pierwszym wejściu, potem tylko zasłona */
  var start=Date.now(),MIN=pierwszy&&!malo?2600:0;
  function gotowe(){
    if(d.classList.contains('gotowe'))return;
    setTimeout(function(){
      d.classList.add('gotowe');
      try{sessionStorage.setItem('aton_l','1')}catch(e){}
    },Math.max(0,MIN-(Date.now()-start)));
  }
  if(document.readyState==='complete')gotowe();else window.addEventListener('load',gotowe);
  setTimeout(gotowe,MIN+2500); /* awaryjnie, gdy coś się długo ładuje */

  /* przejścia między podstronami */
  document.addEventListener('click',function(e){
    var a=e.target.closest('a');
    if(!a||e.defaultPrevented||e.metaKey||e.ctrlKey||e.shiftKey||e.button!==0)return;
    if(a.target||a.hasAttribute('download')||a.classList.contains('fot'))return;
    var u=new URL(a.href,location.href);
    if(u.origin!==location.origin||!/^https?:/.test(u.protocol))return;
    if(u.pathname===location.pathname&&u.hash)return; /* kotwica na tej samej stronie */
    e.preventDefault();
    d.classList.add('wyjscie');
    setTimeout(function(){location.href=u.href},450);
  });
  window.addEventListener('pageshow',function(e){if(e.persisted){d.classList.remove('wyjscie');d.classList.add('gotowe')}});

  /* płynne przewijanie */
  var lenis=null;
  if(window.Lenis&&!malo){
    lenis=new Lenis({duration:1.25,easing:function(t){return Math.min(1,1.001-Math.pow(2,-10*t))},anchors:{offset:-90},smoothWheel:true});
    (function raf(t){lenis.raf(t);requestAnimationFrame(raf)})(performance.now());
  }
  window.atonLenis=lenis;

  /* menu chowa się przy przewijaniu w dół, wraca przy przewijaniu w górę */
  var top=document.querySelector('.top'),ostatni=0,hero=document.querySelector('.hero-in');
  function naScroll(){
    var y=window.scrollY;
    var chowaj=y>ostatni&&y>320&&!document.getElementById('menu').classList.contains('open');
    top.classList.toggle('schowany',chowaj);d.classList.toggle('bez-naglowka',chowaj);
    ostatni=y;
    if(hero&&!malo&&y<1000&&d.classList.contains('gotowe')){
      hero.style.transform='translate3d(0,'+(y*0.28)+'px,0)';
      hero.style.opacity=Math.max(0,1-y/650);
    }
  }
  window.addEventListener('scroll',naScroll,{passive:true});

  /* odsłanianie przy przewijaniu */
  var GRUPY=[
    ['.sekcja .t,.usluga .t',''],['.wstep',''],['.dwa-panele>.szklo','g'],['.kafel','g'],['.kat','g'],
    ['.porzadek>.szklo',''],['.kroki li','g'],['.faq details','g'],['.kontakt-uklad>.szklo','g'],
    ['.usluga-gora>.szklo','g'],['.rzad>.szklo',''],['.srodek',''],['.filtry',''],['.foto-szer',''],['.stopka-gora>div','g']
  ];
  var FOTO=['.kafel-foto','.kat-foto','.rzad-foto','.porzadek-foto img','.mur .fot'];
  var el=[];
  GRUPY.forEach(function(g){
    document.querySelectorAll(g[0]).forEach(function(x){
      if(x.closest('.naglowek'))return;
      x.classList.add('rv');
      if(g[1]){var i=Array.prototype.indexOf.call(x.parentNode.children,x);x.style.setProperty('--d',(Math.min(i,6)*0.09)+'s')}
      el.push(x);
    });
  });
  FOTO.forEach(function(s){
    document.querySelectorAll(s).forEach(function(x){
      x.classList.add('rv-foto');
      var sib=x.parentNode.children,i=Array.prototype.indexOf.call(sib,x);
      if(x.matches('.mur .fot'))i=i%4;
      x.style.setProperty('--d',(Math.min(i,6)*0.08)+'s');
      el.push(x);
    });
  });
  if('IntersectionObserver' in window&&!malo){
    var io=new IntersectionObserver(function(en){
      en.forEach(function(x){if(x.isIntersecting){x.target.classList.add('widac');io.unobserve(x.target)}});
    },{rootMargin:'0px 0px -8% 0px',threshold:0.08});
    el.forEach(function(x){io.observe(x)});
  }else el.forEach(function(x){x.classList.add('widac')});
})();
