

function setup() {

	// TABLES

	// make table rows clickable if they have a data-href attribute
	$('tr[data-href]').click( function() {
		var href = $(this).data('href');
		window.location = href;
	});


	// FORMS & ACTIONS
	$('.confirm').click( function() {
		var conf = confirm('Are you sure?')
		return conf;
	});

	$('.confirm-delete').click( function() {
		var conf = confirm('Are you sure you want to delete this?')
		return conf;
	});

	$('.confirm-remove-friend').click( function() {
		var conf = confirm('Are you sure you want to remove this friend?')
		return conf;
	});

	$('.quickselect a').click( function() {
		$('.quickselect input').val(this.innerHTML);
		$(this).fadeOut();
		return false;
	});

}





$(document).ready(function () {

	setup();

});


