function request_server(value) {
	var a = new XMLHttpRequest();
	a.open("POST","/", true);
	a.send(value);
}