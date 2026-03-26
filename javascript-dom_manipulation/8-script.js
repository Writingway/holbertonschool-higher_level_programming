async function displayValues() {
  const url = "https://hellosalut.stefanbohacek.com/?lang=fr";
  try {
    const reponse = await fetch(url);
    if (!reponse.ok) {
      throw new Error(`Statut de réponse : ${reponse.status}`);
    }
    
    const resultat = await reponse.json();
    const displayText = resultat.hello;
    const listMovies = document.querySelector("#hello");
    listMovies.textContent = displayText;
  } catch (erreur) {
    console.error(erreur.message);
  }
}
displayValues();