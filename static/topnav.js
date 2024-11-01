var current = location.pathname;
if (current == "/load_character") {
  current = "/character_sheet";
}
var element = document.getElementById(current);
element.classList.add("active");
