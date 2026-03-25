const toggle = document.querySelector("#add_item");
toggle.addEventListener("click", function() {
  const newItem = document.createElement("li");
  newItem.textContent = "Item";
  const list = document.querySelector("ul.my_list");
  list.appendChild(newItem);
});