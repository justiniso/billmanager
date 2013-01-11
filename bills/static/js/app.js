

function setup() {

	// make table rows clickable if they have a data-href attribute
	$('tr[data-href]').click(function() {
		var href = $(this).data('href');
		window.location = href;
	});

}





$(document).ready(function () {

	setup();

});


