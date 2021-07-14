const card = document.getElementById("cartao")
card.addEventListener("click",flipCard);

function flipCard(){
    card.classList.toggle("flipCard");
}