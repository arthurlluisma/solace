function createPets() {
  var pet = document.createElement("img");
  pet.src = "{% static 'solace/Pet-Alice-Happy.gif' %}";
  pet.className = "pet-middle-base";
  var randNum = Math.floor(Math.random() * (45 - 40)) + 40;
  var randRotate = Math.floor(Math.random() * 360);
  var randHue = Math.floor(Math.random() * 360);
  var randPet = Math.floor(Math.random() * 6);
  pet.style = `transform: rotate(${randRotate}deg) translate(0, -${randNum}vw); filter: hue-rotate(${randHue}deg)`;
  document.getElementById("earth-container").append(pet);
}

for (i = 0; i < 10; i++) {
  createPets();
}
