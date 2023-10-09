// // JavaScript code to handle time slot selection
// const timeSlots = document.querySelectorAll(".time");
// const selectedTimeSlots = [];

// function handleTimeSlotClick(event) {
//   // Get the class name of the clicked time slot
//   const clickedSlotClass = event.target.classList.value;

//   // Check if the time slot is already selected
//   const isSelected = selectedTimeSlots.includes(clickedSlotClass);

//   if (isSelected) {
//     // If it's already selected, remove it from the selectedTimeSlots array
//     const index = selectedTimeSlots.indexOf(clickedSlotClass);
//     if (index !== -1) {
//       selectedTimeSlots.splice(index, 1);
//     }
//   } else {
//     // If it's not selected, add it to the selectedTimeSlots array
//     selectedTimeSlots.push(clickedSlotClass);
//   }

//   // Toggle "active" class for the clicked time slot
//   event.target.classList.toggle("active");
// }

// // Add click event listeners to each time slot
// timeSlots.forEach((slot) => {
//   slot.addEventListener("click", handleTimeSlotClick);
// });
// JavaScript code to handle time slot selection
const timeSlotContainers = document.querySelectorAll(".time-slot");
const selectedTimeSlots = [];

function handleTimeSlotClick(event) {
  const timeSlotContainer = event.currentTarget; // Get the clicked time slot container

  // Check if the time slot is already selected
  const isSelected = selectedTimeSlots.includes(timeSlotContainer);

  if (isSelected) {
    // If it's already selected, remove it from the selectedTimeSlots array
    const index = selectedTimeSlots.indexOf(timeSlotContainer);
    if (index !== -1) {
      selectedTimeSlots.splice(index, 1);
    }
  } else {
    // If it's not selected, add it to the selectedTimeSlots array
    selectedTimeSlots.push(timeSlotContainer);
  }

  // Toggle "selected" class for the clicked time slot container
  timeSlotContainer.classList.toggle("selected");
}

// Add click event listeners to each time slot container
timeSlotContainers.forEach((container) => {
  container.addEventListener("click", handleTimeSlotClick);
});
// const slider = document.querySelector(".image-slider");
// const arrLeft = document.querySelector(".arrow-left");
// const arrRight = document.querySelector(".arrow-right");

// const images = ["Component 1.png", "turf sample.jpeg", "turf sample.jpeg"];

// let id = 0;
// function slide(id) {
//   slider.style.backgroundImage = `url(/Frontend/src/assets/${images[id]})`;
//   slider.classList.add("image-fade");
//   setTimeout(() => {
//     slider.classList.remove("image-fade");
//   }, 500);
// }
// arrLeft.addEventListener("click", () => {
//   id--;
//   if (id < 0) {
//     id = images.length - 1;
//   }
//   slide(id);
// });

// arrRight.addEventListener("click", () => {
//   id++;
//   if (id > images.length - 1) {
//     id = 0;
//   }
//   slide(id);
// });

const slider = document.querySelector(".slider");
const leftArrow = document.querySelector(".arrow-left");
const rightArrow = document.querySelector(".arrow-right");

let currentIndex = 0;

function showSlide(index) {
  const slideWidth = slider.clientWidth;
  slider.style.transform = `translateX(-${index * slideWidth}px)`;
}

leftArrow.addEventListener("click", () => {
  if (currentIndex > 0) {
    currentIndex--;
    showSlide(currentIndex);
  }
});

rightArrow.addEventListener("click", () => {
  const numSlides = slider.children.length;
  if (currentIndex < numSlides - 1) {
    currentIndex++;
    showSlide(currentIndex);
  }
});

// Initialize slider with the first slide
showSlide(currentIndex);
