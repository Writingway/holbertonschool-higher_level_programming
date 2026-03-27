const toggle = document.querySelector("#update_header");
toggle.addEventListener("click", function() {
  const header = document.querySelector("header");
  header.textContent = "New Header!!!";
});