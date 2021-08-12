(()=>{
    var menu = document.getElementById('menu');
    window.addEventListener('scroll', ()=>{
        if (window.scrollY > 0) menu.classList.add('menuFixo');
        else menu.classList.remove('menuFixo');
    });
})();


// PQ N FUNCIONA

// let img = documen.getElementById('img');
// setTimeout(()=>{
//     if(img.classList !== "trocaHeader")
//     img.classList.add('trocaHeader')
// },5000)