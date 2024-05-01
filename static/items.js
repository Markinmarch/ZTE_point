window.onload = searchItem;

function searchButton() {
    var buttonName = document.getElementById("itemSearchButton");
    buttonName.onclick = searchItem;
}

function searchItem() {
    var itemKeywords = document.getElementById("itemSearch");

    if (itemKeywords.value == "") {
        alert("Перед началом поиска введите хотя бы несколько букв.")
        return false;
    }

    var searchItemData = JSON.stringify({searchWords: itemKeywords.value});

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/registration", true);
    xhr.setRequestHeader('content-type', 'application/json; charset=UTF-8');
    xhr.send(searchItemData);
}
