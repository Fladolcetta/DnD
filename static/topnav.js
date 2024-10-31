var current = location.pathname;
if (current=="/load_character") {
    current = "/create_character"
}
var element = document.getElementById(current);
element.classList.add("active");