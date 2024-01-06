// mobile navbar functionality

const nav_list = document.querySelector('.nav__lstcont');
const menu = document.querySelector('.nav__menubtn');
const close_menu = document.querySelector('.nav__close--menubtn');
const body = document.querySelector('body');

menu.addEventListener('click', () => {
    nav_list.classList.add('nav__list-visible');
    menu.classList.add('nav__menubtn--hide');
    close_menu.classList.add('close--show');
    body.classList.add('body-no-scroll');
})

close_menu.addEventListener('click', () => {
    nav_list.classList.remove('nav__list-visible');
    menu.classList.remove('nav__menubtn--hide');
    close_menu.classList.remove('close--show');
    body.classList.remove('body-no-scroll');
})

