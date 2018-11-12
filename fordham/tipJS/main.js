$(document).ready(function() {

	// calculate tip
	function calculateTip() {
		var billAmt = $("#billAmt").val();
		var tip = $("#serviceQual").val();
		var numOfPeople = $("#peopleAmt").val();

		// math time!
		// calculate total tip for the bill and divide by the guests
		var tipTotal =  (billAmt * tip) / numOfPeople;
		var mealTotal = billAmt / numOfPeople;
		var totalEach = tipTotal + mealTotal;
		// round the number to 2 decimal points
		totalEach.toFixed(2);
		$("#tip").html("$" + totalEach);
	}

	// when I click the calculate button, call my function
	$("#calculate").click(function() {
		calculateTip();
	});

})