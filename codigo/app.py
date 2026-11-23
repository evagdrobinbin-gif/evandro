
// Mensagem do botão de contato
function falarConosco() {
    alert("🍫 Olá! Obrigado pelo interesse na ChocoFactory! Em breve entraremos em contato.");
}

// Botão para conhecer os produtos
function conhecerProdutos() {
    document.getElementById("produtos").scrollIntoView({
        behavior: "smooth"
    });
}

// Efeito de entrada dos produtos
const cards = document.querySelectorAll(".card");

const observador = new IntersectionObserver((entradas) => {
    entradas.forEach((entrada) => {
        if (entrada.isIntersecting) {
            entrada.target.style.opacity = "1";
            entrada.target.style.transform = "translateY(0)";
        }
    });
});

cards.forEach((card) => {
    card.style.opacity = "0";
    card.style.transform = "translateY(30px)";
    card.style.transition = "all 0.7s ease";
    observador.observe(card);
});

// Mensagem de boas-vindas
window.addEventListener("load", () => {
    console.log("Bem-vindo à ChocoFactory!");
});
