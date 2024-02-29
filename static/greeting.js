window.onload = greetingUser;

function greetingUser() {
    var checkStatus = new URLSearchParams(window.location.search);
    var status = checkStatus.get("status");
    if (status == "ok") {
        alert("Поздравляем, регистрация успешно завершена!");
    }
}
