// AJAX, который отправляет параметры товара
$(document).on("submit", "#joinInBascket", function(event){
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
    $(".bascket").addClass("before-click-in-bascket-button");
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

$(".plus").click(
    function(event){
        event.preventDefault();
        var itemIndex = $(this).attr("itemIndex")
        var plusOne =  $("#itemCount" + itemIndex).val();
        $("#itemCount" + itemIndex).val(parseInt(plusOne)+1);
    }
);

$(".minus").click(
    function(event){
        event.preventDefault();
        var itemIndex = $(this).attr("itemIndex");
        var minusOne =  $("#itemCount" + itemIndex).val();
        if (minusOne == 1) {
            return false;
        }
        $("#itemCount" + itemIndex).val(parseInt(minusOne)-1);
    }
);

// В строку input type = number нельзя прописывать матиематические операторы
$('.item-count').keypress(function (e) {
    var txt = String.fromCharCode(e.which);
    if (!txt.match(/[0-9]/)) {
        return false;
    }
});