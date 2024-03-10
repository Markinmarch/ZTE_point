window.onload = joinUser;

function joinUser() {
    var buttonName = document.getElementById("joinUser");
    buttonName.onclick = getUserJoin;
}

function getUserJoin() {
    var userEmail = document.getElementById("userEmail").value;
    var userPassword = document.getElementById("userPassword").value;\
    
    var userData = JSON.stringify({
        email: userEmail,
        password: userPassword
    });

    if (userEmail == "" || userPassword == "") {
        alert("Введите параметры, пожалуйста!");
        return false;
    }

    var xhr = new XMLHttpRequest();
    // ...
}