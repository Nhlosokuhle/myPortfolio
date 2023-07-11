let menu = document.querySelector('#menu-icon');
let navlist = document.querySelector('.navlist');

menu.onclick = () => {
    menu.classList.toggle('bx-x');
    navlist.classList.toggle('open');
}

const sr = ScrollReveal ({
    distance: '65px',
    duration: '2600',
    delay: 450,
    reset: true,
});

sr.reveal('.col-md-8', {delay:200, origin:'top'});
sr.reveal('.col-md-4', {delay:450, origin:'bottom'});
sr.reveal('.col-md', {delay:350, origin: 'bottom'});