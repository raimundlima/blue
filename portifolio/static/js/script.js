
let inputNome = document.querySelector('#nome') /* Cria a variável inputNome e coloca nela o elemento que possui o id nome */
let inputEmail = document.querySelector('#email') /* Cria a variável inputEmail e coloca nela o elemento que possui o id email */
let textareaMensagem = document.querySelector('#mensagem') /* Cria a variável textareaMensagem e coloca nela o elemento que possui o id mensagem */
let btnEnviar = document.querySelector('#enviar')
/* Cria a variável btnEnviar e coloca nela o elemento que possui o id enviar */

function slide1(){
   document.getElementById('id').src="assets/img/back01.jpg";
   setTimeout("slide2()", 1000)
   }
   
   function slide2(){
   document.getElementById('id').src="assets/img/back02.jpg";
   setTimeout("slide3()", 1000)
   }
   
   function slide3(){
   document.getElementById('id').src="assets/img/back03.jpg";
   setTimeout("slide1()", 1000)
   } 

   array1 = new Array ("back01.jpg", "back02.jpg", "back03.jpg")

function comeco(){
document.getElementById('imgId').src = array1[0]
document.form.texto.value="0"
}

function mais(){
document.form.texto.value = Math.floor (1+ 1 - 2 + (document.form.texto.value) * 1 + 1)
if (document.form.texto.value > 2)
{document.form.texto.value = 0}
}

function menos(){
document.form.texto.value = Math.floor (1+ 1 - 2 + (document.form.texto.value) * 1 -1)
if (document.form.texto.value < 0)
{document.form.texto.value = 2}
}

function regular(){
document.getElementById('imgId').src = array1[document.form.texto.value];
setTimeout("regular()", 1)
}


/* Só posso utilziar a arrow function (=>) quando a função não tiver nome */

/* Adiciona um evento de keyup no inputNome e realiza a função */
inputNome.addEventListener('keyup', () => { 
   /* Verifica se o tamanho do valor do inputNome é menor que 2 */
   if(inputNome.value.length < 2){
      inputNome.style.borderColor = 'violet' /* Troca a cor da borda do input para red */
   } else {
      inputNome.style.borderColor = 'blue' /* Troca a cor da borda do input para green */
   }
})


/* Adiciona um evento de keyup no inputEmail e realiza a função */
inputEmail.addEventListener('keyup', () => {
   /* 
   O indexOf procura um caractere no valor do inputEmail, se esse valor não existir ele retorna -1. 
   Então essa expressão inputEmail.value.indexOf('@') == -1 é a mesmo coisa que:
   Se no valor de inputEmail não existir @, faça...

   || é o operador OU em JavaScript
   && é o operador E em JavaScript
   */
   if(inputEmail.value.indexOf('@') == -1 || inputEmail.value.indexOf('.') == -1){
      inputEmail.style.borderColor = 'red' /* Troca a cor da borda do input para red */
   } else {
      inputEmail.style.borderColor = 'green' /* Troca a cor da borda do input para green */
   }  
})

/* Adiciona um evento de keyup no textareaMensagem e realiza a função */
textareaMensagem.addEventListener('keyup', ()=>{
   /* Verifica se o tamanho do valor do textareaMensagem é maior que 100  */
   if(textareaMensagem.value.length > 100){
      textareaMensagem.style.borderColor = 'red' /* Troca a cor da borda do input para red */
   } else {
      textareaMensagem.style.borderColor = 'green' /* Troca a cor da borda do input para green */
   }
})

/* Adiciona um evento de click no btnEnviar e realiza a função */
btnEnviar.addEventListener('click', () => {
   alert('Formulário enviado com sucesso!') /* Mostra um alerta na tela com essa mensagem */
})


