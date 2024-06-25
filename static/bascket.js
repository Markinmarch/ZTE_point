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
        var itemIndex = $(this).attr("itemIndex");
        var itemCount =  $("#itemCount" + itemIndex).val();
        var plusOne = parseInt(itemCount) + 1;
        $("#itemCount" + itemIndex).val(plusOne);
        var itemPrice = $(this).attr("itemPrice");
        $("#itemPrice" + itemIndex).text(parseFloat(plusOne * itemPrice).toFixed(2) + " руб.").val()
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
        minusOne = parseInt(minusOne) - 1;
        $("#itemCount" + itemIndex).val(minusOne);
        var itemPrice = $(this).attr("itemPrice");
        $("#itemPrice" + itemIndex).text(parseFloat(minusOne * itemPrice).toFixed(2) + " руб.").val()
    }
);