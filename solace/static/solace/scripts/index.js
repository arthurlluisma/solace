class Mission {
  constructor(title, description, improvement) {
    this.title = title;
    this.description = description;
    this.improvement = improvement;
  }
}

function removeMission(e) {
  const id = e.target.name;
  for (let i = 0; i < missions.length; i++) {
    if (missions[i].title == id) {
      missions.splice(i, 1);
    }
  }

  parent = document.querySelector(".missions");
  parent.innerHTML = "<h2>Missions</h2>";
  missions.forEach(createMissionBox);
  var model = ""
  petSrc = document.getElementById('petImg').src
  if (petSrc.includes("Bob")) {
    model = "Bob"
  } else {
    model = "Alice"
  }
  if (missions.length == 2) {
    const petArea = document.querySelector(".petArea");
    console.log(petArea);
    petArea.innerHTML = `
        <img id="petImg" src="./static/solace/sprites/Pet-${model}-Neutral.gif">
        <h2>${petname} is feeling alright.</h2>`;

    const pet = document.getElementById("petImg");
    console.log(petArea);
  }
  if (missions.length == 0) {
    parent.innerHTML = `
            <h2>Missions done!</h2> 
            <p>You made ${petname} happy.</p>
        `;

    const petArea = document.querySelector(".petArea");
    console.log(petArea);

    petArea.innerHTML = `
        <img id="petImg" src="./static/solace/sprites/Pet-${model}-Happy.gif">
        <h2>${petname} is feeling happy.</h2>`;

    const pet = document.getElementById("petImg");
    console.log(petArea);
  }
}
// document.getElementById('test').getParentElement
// document.getElementById('addFriend').addEventListener('click', function(e) {
//     document.getElementById('addFriend').dataset.username
//   })
function createMissionBox(mission) {
  parent = document.querySelector(".missions");
  div = document.createElement("div");
  div.setAttribute(
    "style",
    `
        display: flex;
        flex-direction: row;
        align-items: center;
    `
  )
  parent.appendChild(div);

  p = document.createElement("p");
  p.textContent = `${mission.title}, ${mission.description}`;
  p.setAttribute(
    "style",
    `
        position: relative;

    `
  );
  div.appendChild(p);

  check = document.createElement("img");
  check.setAttribute(
    "style",
    `
        position: relative;
        top: 0vh;
        width: 2rem;
        height: 2rem;
        justify-self: flex-end;
        margin-left: auto;
        margin-right: 0;
        cursor: pointer;
    `,
  );
  check.setAttribute("name", mission.title);
  check.src = "./solace/static/solace/images/check.svg"
  check.addEventListener("click", removeMission);
  div.appendChild(check);
}

// list of Missions; this is what you need to edit
const missions = [
  new Mission("Nutrition", "Grab a meal", 2),
  new Mission("Exercise", "Do some stretches or move around", 1),
  new Mission("Hydration", "Remember to drink water", 3),
  new Mission("Rest", "Take some time to slow down", 0),
  new Mission("Hygiene", "Brush your teeth after a meal", 2),
];

missions.forEach(createMissionBox);

var emotions = document.getElementById("emoteImages").children;
var curEmotion = null;
for (let i = 0; i < 5; i++) {
  emotions[i].addEventListener("click", (event) => {
    curEmotion = i;
    document.getElementById("emotionsPage").classList.add("pageDisabled");
    document.getElementById("journalPage").classList.remove("pageDisabled");
  });
}

function journalSubmit() {
  document.getElementById("daily-checkup-container").remove();
  document.getElementById("habits").classList.add("pageDisabled");
}
