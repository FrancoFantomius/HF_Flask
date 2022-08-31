const home = document.getElementById("link-home");
const apps = document.getElementById("link-apps")
const contact = document.getElementById("link-contact")
const about = document.getElementById("link-about")

const current_url = window.location.href
let url = new URL(current_url)
const path = url.pathname

window.onload = () => {
    if (path == "/"){
        home.classList.remove("link-available")
        home.classList.add("link-current")
    } else if (path == "/apps"){
        apps.classList.remove("link-available")
        apps.classList.add("link-current")
    } else if (path == "/contact"){
        contact.classList.remove("link-available")
        contact.classList.add("link-current")
    } else if (path == "/about"){
        about.classList.remove("link-available")
        about.classList.add("link-current")
    }
}