var openButtons = Array.prototype.slice.call( document.getElementsByClassName("popupOpen") )

openButtons.forEach(element => {
    element.addEventListener("click", (event) => {
        document.getElementById("popupHolder").classList.remove("disabledPopup")
    }
)
})

document.getElementById("underlineRes").addEventListener("click", (event) => {
    document.getElementById("resources").classList.remove("disabledPopup")
})
document.getElementById("underlineAbout").addEventListener("click", (event) => {
    document.getElementById("about").classList.remove("disabledPopup")
})

document
    .getElementById("popupClose")
    .addEventListener("click", (event)=> {
        document
            .getElementById("popupClose")
            .parentElement
            .parentElement  
            .classList.add("disabledPopup")
        document.getElementById("about").classList.add("disabledPopup")
        document.getElementById("resources").classList.add("disabledPopup")
})


function playSound(url) {
    var a = new Audio(url);
    a.volume = 0.25
    a.play();
}