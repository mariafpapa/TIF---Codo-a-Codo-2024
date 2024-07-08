const validationInput = (input, advice, text, type = 'input') => {
    const inputField = document.querySelector(`#${input}`);
    const adviceInputField = document.querySelector(`#${advice}`);

    inputField.addEventListener("input", function (event) {
        if (inputField.validity.valid) {
            inputField.className = `${type} is-success`;
            adviceInputField.innerHTML = "";
            adviceInputField.className = "help";
        } else {
            inputField.className = `${type} is-danger`;
            adviceInputField.innerHTML = text;
            adviceInputField.className = "help is-danger";
        }
    });

}

const findProducts = (category) => {
    // return fetch(`https://fakestoreapi.com/products/category/${category}`)
    //     .then(res => res.json())
    //     .then(json => {
    //         return json;
    //     });
}

const createCard = (product) => {
    return `<div class="cell m-2">
            <div class="box has-background-white has-text-centered">
              <p class="title is-6 has-text-black">${product.title.substring(0, 15)}</p>
              <figure class="image is-3by4">
                <img src="${product.image}" alt="${product.title}"/>
              </figure>
              <p>${product.description.substring(0, 40)}...</p>
              <span class="tag is-primary m-2">
                <i class="bx bx-star"></i> ${product.rating.rate}</span
              >
              <span class="tag is-primary m-2">
                <i class="bx bx-user-voice"></i> ${product.rating.count}</span
              >
              <p class="title is-5 has-text-black m-4">$${product.price}</p>
              <button class="button is-large is-primary is-rounded">Buy</button>
            </div>
          </div>`;

};

const preLoadProducts = () => {
    const electronicsProducts = document.querySelector('#electronicsProducts');
    let eProducts = findProducts('electronics');
    eProducts.then((products) => {
        products.forEach(product => {
            electronicsProducts.innerHTML += createCard(product);
        });
    });

    const jeweleryProducts = document.querySelector('#jeweleryProducts');
    let jProducts = findProducts('jewelery');
    jProducts.then((products) => {
        products.forEach(product => {
            jeweleryProducts.innerHTML += createCard(product);
        });
    });

    const mensclothingProducts = document.querySelector('#mensclothingProducts');
    let mcProducts = findProducts("men's clothing");
    mcProducts.then((products) => {
        products.forEach(product => {
            mensclothingProducts.innerHTML += createCard(product);
        });
    });

    const womensclothingProducts = document.querySelector('#womensclothingProducts');
    let wcProducts = findProducts("women's clothing");
    wcProducts.then((products) => {
        products.forEach(product => {
            womensclothingProducts.innerHTML += createCard(product);
        });
    });
};

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

    preLoadProducts();

    validationInput("inputName", "adviceName", "nombre no válido, es demasiado corto");
    validationInput("inputEmail", "adviceEmail", "correo electrónico no válido, por favor compruébelo");
    validationInput("inputPhone", "advicePhone", "teléfono no válido, por favor compruébelo");
    validationInput("inputMessage", "adviceMessage", "mensaje no válido, es demasiado corto", "textarea");


    const form = document.querySelector('#contactform');
    const clearFormResponse = document.querySelector('#clearFormResponse');
    const formResponse = document.querySelector('#formResponse');

    form.addEventListener('submit', (event) => {
        event.preventDefault();
        let confirmForm = document.querySelector('#confirmForm');
        // confirmForm.innerHTML = `Hi ${form.elements.inputName.value}, Thank you for contacting us. We have received your inquiry and our team is currently reviewing it. We will respond to all inquiries within 24 hours. In the meantime, if you have any questions or additional information, please feel free to email us. We thank you for your patience and look forward to assisting you. <br/>Best regards, Click Customer Support Team <br/> <a>info@Click.com</a>.`;
        confirmForm.innerHTML = `Hola ${form.elements.inputName.value}, gracias por ponerse en contacto con nosotros. Hemos recibido su consulta y nuestro equipo la está revisando en estos momentos. Responderemos a todas las consultas en un plazo de 24 horas. Mientras tanto, si tiene alguna pregunta o información adicional, no dude en enviarnos un correo electrónico. Le agradecemos su paciencia y esperamos poder ayudarle. <br/>Saludos cordiales, Equipo de Atención al Cliente de Click <br/> <a>info@click.com.</a>`;

        formResponse.className = 'grid is-visible';
        form.reset();
    });

    clearFormResponse.addEventListener('click', (event) => {
        event.preventDefault();
        confirmForm.innerHTML = '';
        formResponse.className = 'grid is-hidden';
    });

});




