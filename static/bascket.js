$(".plus").click(
    function(event){
        event.preventDefault();
        var itemIndex = $(this).attr("itemIndex");
        var itemCount =  $("#itemCount" + itemIndex).val();
        var plusOne = parseInt(itemCount) + 1;
        $("#itemCount" + itemIndex).val(plusOne);
        var itemPrice = $(this).attr("itemPrice");
        $("#itemPrice" + itemIndex).text(parseFloat(plusOne * itemPrice).toFixed(2) + " руб.");
        // сразу же отправляются данные в backend для их измениея в БД
        $.ajax({
            type: "POST",
            url: "/bascket",
            data: {
                id: $(this).attr("itemId"),
                count: plusOne,
            },
        })
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
        // сразу же отправляются данные в backend для их измениея в БД
        $.ajax({
            type: "POST",
            url: "/bascket",
            data: {
                id: $(this).attr("itemId"),
                count: minusOne,
            },
        })
    }
);
