function gerarVideo() {
    const prompt = document.getElementById("prompt").value;
    const status = document.getElementById("status");

    if (prompt.trim() === "") {
        status.innerHTML = "⚠️ Escreva uma ideia para o vídeo.";
        return;
    }

    status.innerHTML = "⏳ A preparar o seu vídeo...";

    setTimeout(() => {
        status.innerHTML = "🎨 A criar as cenas...";
    }, 2000);

    setTimeout(() => {
        status.innerHTML = "🎬 A montar o vídeo de 30 segundos...";
    }, 5000);

    setTimeout(() => {
        status.innerHTML = "✅ Vídeo preparado!";
    }, 8000);
}
