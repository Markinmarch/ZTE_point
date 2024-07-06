// AJAX, который отправляет параметры товара
// $(document).on("submit", "#itemBuy", function(event){
//     event.preventDefault();
//     var itemIndex = $(this).attr("itemIndex")
//     $.ajax({
//         type: "POST",
//         url: "/bascket",
//         data: {id: $("#itemId" + itemIndex).val()}
//     });
    // Добавляем стиль кнопке, при добавлении в корзину
    // $(".bascket").addClass("before-click-buy-button");
// });

$(".plus").click(
    function(event){
        event.preventDefault();
        var itemIndex = $(this).attr("itemIndex");
        var itemCount =  $("#itemCount" + itemIndex).val();
        var plusOne = parseInt(itemCount) + 1;
        $("#itemCount" + itemIndex).val(plusOne);
        var itemPrice = $(this).attr("itemPrice");
        $("#itemPrice" + itemIndex).text(parseFloat(plusOne * itemPrice).toFixed(2) + " руб.");
    }
);

$(".minus").click(
    function(event){
        event.preventDefault();
        var itemIndex = $(this).attr("itemIndex");
        var itemCount =  $("#itemCount" + itemIndex).val();
        if (itemCount == 1) {
            return false;
        }
        minusOne = parseInt(itemCount) - 1;
        $("#itemCount" + itemIndex).val(minusOne);
        var itemPrice = $(this).attr("itemPrice");
        $("#itemPrice" + itemIndex).text(parseFloat(minusOne * itemPrice).toFixed(2) + " руб.");
    }
);

// $("#totalPrice").text(
//     function(){
//         var sum = 0;
//         $(".itemPrice").each(function(){
//             sum += parseFloat($(this).attr("amount")).toFixed(2)*1;
//         })
//         return parseFloat(sum).toFixed(2);
//     }
// );
    