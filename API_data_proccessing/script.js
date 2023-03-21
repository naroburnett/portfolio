const form = document.querySelector("form");
const pokemonData = document.querySelector("#pokemon-list");

let myPokemon = [];

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const searchName = document.querySelector("#search-input").value.trim();
  const searchType = document.querySelector("#search-type").value;
  const searchNumber = document.querySelector("#search-number").value;
  const searchGeneration = document.querySelector("#search-generation").value;
  getPokemon(searchName, searchType, searchNumber, searchGeneration);
});

async function getPokemon(
  searchName,
  searchType,
  searchNumber,
  searchGeneration
) {
  let url = "https://pokeapi.co/api/v2/";
  let pokemonData = [];
  let data = [];

  // Search by Name
  if (searchName.trim() !== "") {
    url += `pokemon/${searchName.trim().toLowerCase()}`;
    let response = await fetch(url);
    data = await response.json();
    pokemonData = pokemonData.concat(data);
  }

  // Search by Type
  if (searchType !== "") {
    url += `type/${searchType}`;
    let response = await fetch(url);
    data = await response.json();
    //for each pokemon in the data , get the pokemon data
    for (let i = 0; i < data.pokemon.length; i++) {
      let pokemon = data.pokemon[i];
      let response = await fetch(pokemon.pokemon.url);
      poke_data = await response.json();
      pokemonData = pokemonData.concat(poke_data);
    }
  }

  // Search by Number
  if (searchNumber !== "") {
    url += `id/${searchNumber}`;
    let response = await fetch(url);
    data = await response.json();
    pokemonData = pokemonData.concat(data);
  }

  // Search by Generation access the pokemon species go to url for each pokemon species then go to varieties go to url for each variety and get the pokemon data
  if (searchGeneration !== "") {
    url += `generation/${searchGeneration}`;
    let response = await fetch(url);
    data = await response.json();
    //for each pokemon species in the data , get the pokemon data
    for (let i = 0; i < data.pokemon_species.length; i++) {
      let pokemonSpecies = data.pokemon_species[i];
      let response = await fetch(pokemonSpecies.url);
      let poke_species_data = await response.json();
      //for the first variety in the pokemon species data , get the pokemon data
      let pokemonVariety = poke_species_data.varieties[0];
      response = await fetch(pokemonVariety.pokemon.url);
      let poke_data = await response.json();
      pokemonData = pokemonData.concat(poke_data);
    }
  }

  renderPokemon(pokemonData, 1);
}

function renderPokemon(pokemonData, page) {
  const pokemonContainer = document.getElementById("pokemon-list");
  pokemonContainer.innerHTML = "";

  const startIndex = (page - 1) * 25;
  const endIndex = startIndex + 25;

  pokemonData.slice(startIndex, endIndex).forEach((pokemon) => {
    // for each pokemon, create a item that will contain the pokemon data (name,image, types, and stats) and append it to the pokemon container (pokemon-list)
    const listItem = document.createElement("li");
    listItem.classList.add("pokemon-item");
    const pokemonName = document.createElement("h2");
    pokemonName.innerText = pokemon.name;
    const pokemonImage = document.createElement("img");
    pokemonImage.src = pokemon.sprites.front_default;
    const pokemonTypes = document.createElement("p");
    pokemonTypes.innerText = "Types: ";
    const pokemonStats = document.createElement("p");
    pokemonStats.innerText = "Stats: ";
    // for each type in the pokemon, create a span and append it to the pokemon types
    for (let i = 0; i < pokemon.types.length; i++) {
      const pokemonType = document.createElement("span");
      pokemonType.innerText = pokemon.types[i].type.name;
      pokemonTypes.appendChild(pokemonType);
    }
    // for each stat in the pokemon get its name and base, then create a span and append it to the pokemon stats (name: base)
    for (let i = 0; i < pokemon.stats.length; i++) {
      const pokemonStat = document.createElement("span");
      pokemonStat.innerText = `${pokemon.stats[i].stat.name}: ${pokemon.stats[i].base_stat}`;
      pokemonStats.appendChild(pokemonStat);
    }

    listItem.appendChild(pokemonName);
    listItem.appendChild(pokemonImage);
    listItem.appendChild(pokemonTypes);
    listItem.appendChild(pokemonStats);
    pokemonContainer.appendChild(listItem);

    //create a button that will add the pokemon to the my pokemon list
    const addPokemonButton = document.createElement("button");
    addPokemonButton.innerText = "Add to My Pokemon";
    addPokemonButton.addEventListener("click", () => {
      myPokemon.push(pokemon);
      console.log(myPokemon);
    });
    listItem.appendChild(addPokemonButton);
  });

  let buttonContainer = document.querySelector(".button-container");
  if (buttonContainer) {
    buttonContainer.parentNode.removeChild(buttonContainer);
  }

  buttonContainer = document.createElement("div");
  buttonContainer.classList.add("button-container");
  // if the page is greater than 1, create a previous button and add an event listener to it that will call the renderPokemon function with the previous page
  if (page > 1) {
    const prevButton = document.createElement("button");
    prevButton.innerText = "Previous";
    prevButton.addEventListener("click", () => {
      renderPokemon(pokemonData, page - 1);
    });
    buttonContainer.appendChild(prevButton);
  }
  // if the end index is less than the pokemon data length, create a next button and add an event listener to it that will call the renderPokemon function with the next page
  if (endIndex < pokemonData.length) {
    const nextButton = document.createElement("button");
    nextButton.innerText = "Next";
    nextButton.addEventListener("click", () => {
      renderPokemon(pokemonData, page + 1);
    });
    buttonContainer.appendChild(nextButton);
  }
  // append the button container to the search results
  const searchResults = document.getElementById("search-results");
  searchResults.appendChild(buttonContainer);
}

//add a function that will calculate the average stats of the pokemon in the my pokemon list
function calculateAverageStats() {
  let averageStats = {};
  let totalStats = {};
  let count = 0;
  for (let i = 0; i < myPokemon.length; i++) {
    let pokemon = myPokemon[i];
    for (let j = 0; j < pokemon.stats.length; j++) {
      let stat = pokemon.stats[j];
      if (totalStats[stat.stat.name]) {
        totalStats[stat.stat.name] += stat.base_stat;
      } else {
        totalStats[stat.stat.name] = stat.base_stat;
      }
      count++;
    }
  }
  for (let stat in totalStats) {
    averageStats[stat] = totalStats[stat] / count;
  }
  return averageStats;
}

//function to remove the pokemon from the my pokemon list
function removePokemon(pokemon) {
  const index = myPokemon.indexOf(pokemon);
  myPokemon.splice(index, 1);
}
