function hide_stats() {
  document.getElementById("stats").style.display = "none";
}

function show_stats() {
  document.getElementById("stats").style.display = "block";
}

function check_type_selection(select) {
  let check_type = select.value;
  if (check_type === "roll") {
    hide_stats();
  } else {
    show_stats();
  }
}
