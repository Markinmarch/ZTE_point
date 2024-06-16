$('.plus').click(function(){
    var value =  $('#quantity').val();
   $('#quantity').val(parseInt(value)+1);
});
$('.minus').click(function(){
    var value =  $('#quantity').val();
   $('#quantity').val(parseInt(value)-1);
});