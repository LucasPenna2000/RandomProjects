function clicar() {
	var clicou = document.querySelector("#main");
	clicou.innerText = "Clicou!";
}	
function entrou() {
	var entrar = document.querySelector("#main")
	entrar.innerText = "entrou!"
}
function saiu() {
	var sair = document.querySelector("#main")
	sair.innerText = "Saiu!"
}
//Configuração das cores

var main = document.querySelector("#main") //variável para trocar a cor da div pelos inputs
var titulo = document.querySelector("#titulo") //variável para trocar o titulo pelos inputs

function corpreta() {
	main.style.backgroundColor = "#000000"
	titulo.innerText = "Choose Another!"
}
function corazul() {
	main.style.backgroundColor = "#000080"
	titulo.innerText = "Choose Another!"
}
function corverde() {
	main.style.backgroundColor = "#008000"
	titulo.innerText = "Choose Another!"
}
