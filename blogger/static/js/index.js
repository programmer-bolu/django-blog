let toggle = document.getElementById('toggle-nav')
let nav = document.querySelector('header nav')
toggle.addEventListener('click', ()=>{
    if (nav.classList.contains('show')) {
        nav.classList.remove('show')
    }else[
        nav.classList.add('show')
    ]
})