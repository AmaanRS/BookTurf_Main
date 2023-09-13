//Form data
window.addEventListener("load", function () {
  function updateHiddenForm() {
    const selectedSport = document
      .getElementById("selected-sport-heading")
      .textContent.trim();
    const selectedLocation = document
      .querySelector(".search-list-item.active")
      .textContent.trim();
    const selectedDate = document
      .querySelector(".date-toggle")
      .textContent.trim();
    const selectedTimeslot = document
      .querySelector(".tabs-box .tab.active")
      .textContent.trim();

    document.getElementById("hidden-sport").value = selectedSport;
    document.getElementById("hidden-location").value = selectedLocation;
    document.getElementById("hidden-date").value = selectedDate;
    document.getElementById("hidden-timeslot").value = selectedTimeslot;
    console.log("Hidden Form Data:");
    console.log(`Sport: ${selectedSport}`);
    console.log(`Location: ${selectedLocation}`);
    console.log(`Date: ${selectedDate}`);
    console.log(`Timeslot: ${selectedTimeslot}`);
  }

  // Simulate form submission when the page loads
  window.addEventListener("load", function () {
    updateHiddenForm();
    document.getElementById("hidden-form").submit();
  });
});
//value in button
/*
function updateSelectedSport(button) {
  const selectedSportButton = document.getElementById("selected-sport-heading");
  selectedSportButton.value = button.value;
}*/
