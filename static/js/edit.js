document.addEventListener('DOMContentLoaded', () => {

    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

    $navbarBurgers.forEach(el => {
        el.addEventListener('click', () => {

            const target = el.dataset.target;
            const $target = document.getElementById(target);

            el.classList.toggle('is-active');
            $target.classList.toggle('is-active');

        });
    });

    const txtImagen = document.querySelector('#txtImagen');
    const nombreImagen = document.querySelector('#nombreImagen');
    const preview = document.querySelector('#preview');
    txtImagen.addEventListener('change', (event) => {

        imagen = document.createElement('img');
        imagen.src = URL.createObjectURL(event.target.files[0]);
        imagen.width = 100;

        if (preview.firstChild) {
            preview.removeChild(preview.firstChild);
        }

        preview.appendChild(imagen);
        nombreImagen.innerHTML = event.target.files[0].name;

    });

});




