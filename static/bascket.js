// AJAX, который отправляет параметры товара
$(document).on("submit", "#itemBuy", function(event){
    event.preventDefault();
    var itemIndex = $(this).attr("itemIndex")
    $.ajax({
        type: "POST",
        url: "/bascket",
        data: {
            id: $("#itemId" + itemIndex).val(),
            count: $("#itemCount" + itemIndex).val()
        },
    });
    // Добавляем стиль кнопке, при добавлении в корзину
    $(".bascket").addClass("before-click-buy-button");
});

$(".plus").click(
    function(event){
        event.preventDefault();
        var itemIndex = $(this).attr("itemIndex")
        var plusOne =  $("#itemCount" + itemIndex).val();
        $("#itemCount" + itemIndex).val(parseInt(plusOne)+1);
        var itemPrice = $("#itemPrice" + itemIndex).val();
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