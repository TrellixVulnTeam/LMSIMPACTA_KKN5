	
// ----------------- FUNÇÃO VALIDA-CHECKED ---------------------
function Condicional_cad(){
	if (document.getElementById('btnaplicativos').checked==true){
		document.getElementById('btnaplicativos').checked=false;
	}

}
function Condicional_apk(){
	if (document.getElementById('btncadastro').checked==true){
		document.getElementById('btncadastro').checked=false;
	}

}
// ----------------- FUNÇÃO SHOW-HIDE ---------------------
function ShowHide_apk(){

	if (document.getElementById('btnaplicativos').checked==true){
		document.getElementById("div_sub_apk").style.display = "block";
		document.getElementById("div_sub_cad").style.display = "none";

	}
	else if(document.getElementById('btnaplicativos').checked==false){
		document.getElementById("div_sub_apk").style.display = "none";	
	}
}function ShowHide_cad(){

	if (document.getElementById('btncadastro').checked==true){
		document.getElementById("div_sub_cad").style.display = "block";
		document.getElementById("div_sub_apk").style.display = "none";	

	}
	else if(document.getElementById('btncadastro').checked==false){
		document.getElementById("div_sub_cad").style.display = "none";	
	}
}