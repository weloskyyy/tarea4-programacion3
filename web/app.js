


// LOGIN (index.html)

const VALID_EMAIL = "a@a.com";
const VALID_PASSWORD = "welosky123";

// Intentamos obtener el formulario de login (solo existirá en index.html)
const loginForm = document.getElementById("loginForm");
const loginErrorLabel = document.getElementById("loginError");

if (loginForm) {
    loginForm.addEventListener("submit", function (e) {
        e.preventDefault();

        const email = document.getElementById("txtEmail").value.trim();
        const password = document.getElementById("txtPassword").value.trim();

        // Validaciones básicas (campos vacíos)
        if (!email || !password) {
            loginErrorLabel.textContent = "Por favor, completa todos los campos.";
            return;
        }

        // Credenciales válidas (camino feliz)
        if (email === VALID_EMAIL && password === VALID_PASSWORD) {
            // Podrías guardar algo en sessionStorage para simular sesión
            sessionStorage.setItem("isLoggedIn", "true");
            window.location.href = "crud.html";
        } else {
            // Caso negativo
            loginErrorLabel.textContent = "Credenciales incorrectas.";
        }
    });
}

// CRUD DE CONTACTOS (crud.html)


let contactos = []; // Array en memoria

const contactForm = document.getElementById("contactForm");
const contactErrorLabel = document.getElementById("contactError");
const tblContactosBody = document.getElementById("tblContactosBody");
const formTitle = document.getElementById("formTitle");
const btnCancelarEdicion = document.getElementById("btnCancelarEdicion");
const btnLogout = document.getElementById("btnLogout");

function verificarSesion() {
    const isLoggedIn = sessionStorage.getItem("isLoggedIn");
    if (!isLoggedIn && window.location.pathname.endsWith("crud.html")) {
        // Si no está logueado y está en crud.html, lo mandamos al login
        window.location.href = "index.html";
    }
}

if (window.location.pathname.endsWith("crud.html")) {
    verificarSesion();
}

if (btnLogout) {
    btnLogout.addEventListener("click", function () {
        sessionStorage.removeItem("isLoggedIn");
        window.location.href = "index.html";
    });
}

function limpiarFormulario() {
    document.getElementById("contactId").value = "";
    document.getElementById("txtNombre").value = "";
    document.getElementById("txtTelefono").value = "";
    document.getElementById("txtCorreo").value = "";
    contactErrorLabel.textContent = "";
    formTitle.textContent = "Crear contacto";
    btnCancelarEdicion.style.display = "none";
}

function renderizarTabla() {
    if (!tblContactosBody) return;

    tblContactosBody.innerHTML = ""; // Limpiamos tabla

    contactos.forEach((c, index) => {
        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${c.nombre}</td>
            <td>${c.telefono}</td>
            <td>${c.correo}</td>
            <td>
                <button type="button" class="btnEditar" data-index="${index}">Editar</button>
                <button type="button" class="btnEliminar" data-index="${index}">Eliminar</button>
            </td>
        `;

        tblContactosBody.appendChild(row);
    });

    // Eventos Editar / Eliminar
    document.querySelectorAll(".btnEditar").forEach(btn => {
        btn.addEventListener("click", function () {
            const index = this.getAttribute("data-index");
            cargarContactoEnFormulario(index);
        });
    });

    document.querySelectorAll(".btnEliminar").forEach(btn => {
        btn.addEventListener("click", function () {
            const index = this.getAttribute("data-index");
            eliminarContacto(index);
        });
    });
}

function cargarContactoEnFormulario(index) {
    const contacto = contactos[index];
    document.getElementById("contactId").value = index;
    document.getElementById("txtNombre").value = contacto.nombre;
    document.getElementById("txtTelefono").value = contacto.telefono;
    document.getElementById("txtCorreo").value = contacto.correo;
    formTitle.textContent = "Editar contacto";
    btnCancelarEdicion.style.display = "inline-block";
}

function eliminarContacto(index) {
    contactos.splice(index, 1);
    renderizarTabla();
}

// Manejador del formulario de contactos
if (contactForm) {
    contactForm.addEventListener("submit", function (e) {
        e.preventDefault();

        const nombre = document.getElementById("txtNombre").value.trim();
        const telefono = document.getElementById("txtTelefono").value.trim();
        const correo = document.getElementById("txtCorreo").value.trim();
        const id = document.getElementById("contactId").value;

        // Validaciones simples (puedes extenderlas para casos de límites)
        if (!nombre || !telefono || !correo) {
            contactErrorLabel.textContent = "Todos los campos son obligatorios.";
            return;
        }

        // Crear nuevo contacto
        if (id === "") {
            contactos.push({ nombre, telefono, correo });
        } else {
            // Editar contacto existente
            const index = parseInt(id, 10);
            contactos[index] = { nombre, telefono, correo };
        }

        limpiarFormulario();
        renderizarTabla();
    });
}

if (btnCancelarEdicion) {
    btnCancelarEdicion.addEventListener("click", function () {
        limpiarFormulario();
    });
}
