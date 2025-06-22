function enviarFormulario() {
  const nombre = document.getElementById('nombre').value;
  const email = document.getElementById('email').value;
  const mensaje = document.getElementById('mensaje').value;

  alert('Gracias ${nombre}, recibimos tu mensaje.');
  return false; // evita que la página se recargue
}