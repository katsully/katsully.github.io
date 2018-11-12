$(document).ready(function() {

  //Calculate Tip
  function calculateTip() {
    var billAmt = $("#billamt").val();
    var serviceQual = $("#serviceQual").val();
    var numOfPeople = $("#peopleamt").val();

    //validate input
    if (billAmt === "" || serviceQual == 0) {
      alert("Please enter values");
      return;
    }
    //Check to see if this input is empty or less than or equal to 1
    if (numOfPeople === "" || numOfPeople <= 1) {
      numOfPeople = 1;
      $("#each").css('display', 'none');
    } else {
      $("#each").css('display', "block");
    }

    //Calculate tip
    var total = (billAmt * serviceQual) / numOfPeople;
    //round to two decimal places
    total = Math.round(total * 100) / 100;
    //next line allows us to always have two digits after decimal point
    total = total.toFixed(2);
    //Display the tip
    $("#totalTip").css('display', "block");
    $("#tip").html(total);

  }

  //Hide the tip amount on load
  $("#totalTip").css("display", "none");
  $("#each").css("display", "none");

  //click to call function
  $("#calculate").click( function() {
    calculateTip();

  });

});