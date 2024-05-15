// AJAX, который отправляет параметры товара
$(document).on("submit", "#itemBuy", function(event){
    event.preventDefault();
    $.ajax({
        type: "POST",
        url: "/items",
        data: {
            id: $("#itemId").val(),
            count: $("#itemCount").val()
        }
    })
});

// AJAX, который устанавилвает поиск при нажатии на Enter
$("#itemSearch").keypress(function(event) {
    if (event.keyCode == 13) {
        event.preventDefault();
        $("#itemSearchButton").click();
    }
});

// Блок функций, который выполняют перенаправление на поисковую страницу с товарами
window.onload = searchItem;

function searchItem() {
    var buttonName = document.getElementById("itemSearchButton");
    buttonName.onclick = getSearchItems;
}

function getSearchItems() {
    var keywords = document.getElementById("itemSearchInput");

    if (keywords.value == ""){
        alert("Введите ключевые слова, пожалуйста!");
        return false;
    }
    window.location.replace("http://localhost:5000/items/search?keywords=" + keywords.value);    
}

$("#itemBuyButton").click(function(){
    $(".bascket").addClass("before-click-buy-button");
});