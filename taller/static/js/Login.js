document.getElementById("login-form").addEventListener("submit", function (event) {
  event.preventDefault();
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;
  var userType = "";

  if (email === "" || password === "") {
    var modal = document.getElementById("modal1");
    modal.showModal();   
    return;
  }

  var sanitizedEmail = email.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
  var sanitizedPassword = password.normalize("NFD").replace(/[\u0300-\u036f]/g, "");

  const users = ["mecanico@rmakween.cl", "admin@rmakween.cl"];
  const pass = ["mecanico", "admin"];

  if (sanitizedEmail === users[0] && sanitizedPassword === pass[0]) {
    userType = "mecanico";
  } else if (sanitizedEmail === users[1] && sanitizedPassword === pass[1]) {
    userType = "administrador";
  } else {
    var modal = document.getElementById("modal2");
    modal.showModal();
   
    return;
  }


  if (userType === "mecanico") {
    window.location.href = "Mecanico.html";
  } else if (userType === "administrador") {
    window.location.href = "Administrador.html";
  }
});
function cerrar() {
  var modal = document.getElementById("modal1");
  modal.close();
  var modal = document.getElementById("modal2");
  modal.close();
}