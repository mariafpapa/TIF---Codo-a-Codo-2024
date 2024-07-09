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

    const exitButton = document.querySelector('#exit');
    exitButton.addEventListener('click', (event) => {
        event.preventDefault();
        window.localStorage.removeItem('clickToken');
        window.location.href = '/';
    });

    const clickToken = window.localStorage.getItem('clickToken');
    if (clickToken) {
        fetch('https://click-backend.onrender.com/user', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${clickToken}`
            }
        })
            .then(response => {
                if (!response.ok) {
                    window.localStorage.removeItem('clickToken');
                    return window.location.href = '/';
                }
                return response.json()
            })
            .then(data => {
                const user = document.querySelector('#user');
                const photo = document.querySelector('#photo');
                user.innerHTML = data.name;
                photo.src = data.imageProfile;
                if (data.message) {
                    window.localStorage.removeItem('clickToken');
                    window.location.href = '/';
                }
            })
    } else {
        window.location.href = '/';
    }


});




