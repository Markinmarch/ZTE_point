// AJAX, который отправляет параметры товара
$(document).on("submit", "#itemBuy", function(event){
    event.preventDefault();
    var itemIndex = $(this).attr("itemIndex")
    $.ajax({
        type: "POST",
        url: "/items",
        data: {
            id: $("#itemId" + itemIndex).val(),
            count: $("#itemCount" + itemIndex).val()
        },
    });
    // Добавляем стиль кнопке, при добавлении в корзину
    $(".bascket").addClass("before-click-buy-button");
});

// AJAX, который устанавливает поиск при нажатии на Enter
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
