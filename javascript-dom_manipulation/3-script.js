const toggle = document.querySelector("header");
toggle.addEventListener("click", function() {
  if (toggle.classList.contains("green")) {
    toggle.classList.remove("green");
    toggle.classList.add("red");
  } else {
    toggle.classList.remove("red");
    toggle.classList.add("green");
  }
});
