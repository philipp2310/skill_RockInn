(function () {

	function refreshRockInn() {
		$.ajax({
			url: '/home/widget/',
			data: JSON.stringify({
				skill: 'RockInn',
				widget: 'RockInnStatus',
				func: 'getNumbers',
				param: ''
			}),
			contentType: 'application/json',
			dataType: 'json',
			type: 'POST'
		}).done(function (answer) {
			$('#RockInn_FREE').html(answer['free']);
			$('#RockInn_VISITORS').html(answer['visitors']);
		});
	}

	refreshRockInn();
	setInterval(function () {
		refreshRockInn()
	}, 1000 * 20);
})();
