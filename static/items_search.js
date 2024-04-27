window.onload = searchItem;

function searchItem() {
    var buttonName = document.getElementById("itemSearchButton");
    buttonName.onclick = getItemsInDB;
}

function getItemsInDB() {
    var keywords = document.getElementById("itemSearch");

    var itemData = JSON.stringify({
        words : keywords.value
    });

    if (keywords.value == "") {
        return false;
    }

    var xhr = new XMLHttpRequest();
    xhr.open()
}


