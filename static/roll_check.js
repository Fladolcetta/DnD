function sendData() {
    let char_id = document.getElementById("char_id_div").textContent;
    char_id = char_id.trim();
    char_id = char_id.replaceAll("'", "");
    char_id = char_id.replaceAll("\"", "");
    let check_type = document.getElementById("check_type").value;
    if (check_type === "save") {
        check = document.getElementById("stat_select").value;
    } else if (check_type === "stat") {
        check = document.getElementById("stat_select").value;
    } else if (check_type === "skill") {
        check = document.getElementById("skill_select").value;
    } else {
        check = "";
    }
    $.ajax({
        url: '/roll_check',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ 'char_id': char_id , 'check_type': check_type, 'check': check}),
        success: function(response) {
            document.getElementById('roll_check').innerHTML = response.result;
        },
        error: function(error) {
            console.log(error);
        }
    });
}

function hide_stat_select(){
    document.getElementById('stat_select').style.display = "none";
}

function hide_skill_select(){
    document.getElementById('skill_select').style.display = "none";
}

function show_stat_select(){
    document.getElementById('stat_select').style.display = "block";
}

function show_skill_select(){
    document.getElementById('skill_select').style.display = "block";
}

function hide_all(){
    hide_stat_select();
    hide_skill_select();
}

function check_type_selection(select){
    let check_type = select.value;
    if(check_type === "save"){
        show_stat_select();
        hide_skill_select();
    }else if(check_type === "stat"){
        show_stat_select();
        hide_skill_select();
    }else if(check_type === "skill"){
        show_skill_select();
        hide_stat_select();
    }else{
        hide_all();
    }
}