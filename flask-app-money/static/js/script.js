$('#sum-th').click(function () {
	window.location.href="/info/" + window.location.href.slice(27, 31) + "/sum";
})

$('#data-th').click(function () {
	window.location.href="/info/" + window.location.href.slice(27, 31) + "/data";
})

$('#add-button').click(function () {
	window.location.href="/form/" + window.location.href.slice(-9, -5);
})

