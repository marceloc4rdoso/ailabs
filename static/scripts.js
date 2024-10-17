document.getElementById('formulario').onsubmit = async function (e) {
    e.preventDefault();
    const formData = new FormData(this);
    const response = await fetch('/gerar_ideia', {
        method: 'POST',
        body: formData
    });
    const data = await response.json();
    document.getElementById('resultado').innerText = data.ideia || data.error;
}
