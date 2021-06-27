


const toggleMobileNav = () =>{
    const navLinks = document.querySelectorAll('.nav-link');
    const nav = document.querySelector('.desk-nav');
    const navButton = document.querySelector('.bx-menu');


    // nav.style.display = 'block !important';
    nav.style.background = 'var(--white) !important'

    navButton.classList.toggle('bx-menu');
    navButton.classList.toggle('bx-plus');
    navButton.classList.toggle('text-dark');
    navButton.classList.toggle('text-light');

    console.log(navLinks)
    for (let i = 0; i < navLinks.length; i++){
        navLinks[i].classList.toggle('text-light');
        navLinks[i].classList.toggle('text-dark');
    }
}