async function getMovies() {
  const url = "https://swapi-api.hbtn.io/api/films/?format=json";
  try {
    const reponse = await fetch(url);
    if (!reponse.ok) {
      throw new Error(`Statut de réponse : ${reponse.status}`);
    }
    
    const resultat = await reponse.json();
    const movies = resultat.results;
    const listMovies = document.querySelector("#list_movies");
    movies.forEach(movie => {
      const listItem = document.createElement("li");
      listItem.textContent = movie.title;
      listMovies.appendChild(listItem);
    });
  } catch (erreur) {
    console.error(erreur.message);
  }
}
getMovies();