async function getData() {
  const url = "https://swapi-api.hbtn.io/api/people/5/?format=json";
  try {
    const reponse = await fetch(url);
    if (!reponse.ok) {
      throw new Error(`Statut de réponse : ${reponse.status}`);
    }

    const resultat = await reponse.json();
    const name = resultat.name;
    const character = document.querySelector("#character");
    character.textContent = name;
  } catch (erreur) {
    console.error(erreur.message);
  }
}
getData();