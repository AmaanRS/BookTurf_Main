const searchInput = document.getElementById("search-input");
const searchList = document.getElementById("search-list");

const citiesAndTurfs = [
  "Mira Road",
  "Bhayandar",
  "Lush Turf, Mira road",
  "LLF , Mira road",
  "LLF , Bhayandar",
];

searchInput.addEventListener("input", () => {
  const searchTerm = searchInput.value.toLowerCase();
  const filteredCities = citiesAndTurfs.filter((city) =>
    city.toLowerCase().startsWith(searchTerm)
  );

  displaySearchResults(filteredCities);
});

function displaySearchResults(results) {
  searchList.innerHTML = "";

  if (results.length > 0) {
    results.forEach((result) => {
      const listItem = document.createElement("li");
      listItem.classList.add("search-list-item");
      listItem.textContent = result;
      listItem.addEventListener("click", () => {
        searchInput.value = result;
        searchList.style.display = "none";
      });

      searchList.appendChild(listItem);
    });

    searchList.style.display = "block";
  } else {
    searchList.style.display = "none";
  }
}

document.addEventListener("click", (event) => {
  if (!searchList.contains(event.target) && event.target !== searchInput) {
    searchList.style.display = "none";
  }
});
