function switchForm(id) {
  var forms = document.getElementsByClassName("content__form");
  for (i = 0; i < forms.length; i++) {
    forms[i].style.display = "none";
  }
  document.getElementById(`content__form--${id}`).style.display = "block";
}
switchForm("login");

document
  .getElementById("content__form__btn--login")
  .addEventListener("click", (event) => {
    switchForm("register");
  });

document
  .getElementById("content__form__btn--register")
  .addEventListener("click", (event) => {
    switchForm("login");
  });
