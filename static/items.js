window.onload = searchItem;

function searchButton() {
    var buttonName = document.getElementById("itemSearchButton");
    buttonName.onclick = searchItem;
}

function searchItem() {
    var itemKwargs = document.getElementById("itemSearch");

    if (itemKwargs.value == "") {
        alert("Перед началом поиска введите хотя бы несколько букв.")
        return false;
    }
}