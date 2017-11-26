/*function ShowHide_apk(){
	if (document.getElementById('btnMenuLateral').checked == true){	
		document.getElementById("menu_left").style.display = "block";
		
	}
	else{
		document.getElementById("menu_left").style.display = "none";

	}

}*/
function ShowHide_apk(){
	if (document.getElementById('btnMenuLateral').checked == true){	
		document.getElementById("menu_left").style.marginLeft = "0px";
		
	}
	else{
		document.getElementById("menu_left").style.marginLeft = "-500px";

	}

}