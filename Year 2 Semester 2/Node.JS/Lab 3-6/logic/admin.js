if (cu.getCookie("isAdmin")) { drawAdminPage(cu.getCookie("username")) }

import * as templates from "./templatesHTML.js"
import * as cu from "./cookieUtils.js"
import * as ou from "./otherUtils.js"

export function login() {
    fetch("../config/admins.json")
        .then(response => response.json())
        .then(admins => {
            const inp_login = document.getElementById("login").value
            const inp_pword = document.getElementById("pword").value

            /* check if all fields are filled */
            let missing_input = false
            if (inp_login === "") {
                document.getElementById("login-text").style.color = "red"
                missing_input = true
            } else {
                document.getElementById("login-text").style.color = "black"
            }
            if (inp_pword === "") {
                document.getElementById("pword-text").style.color = "red"
                missing_input = true
            } else {
                document.getElementById("pword-text").style.color = "black"
            }
            if (missing_input) {
                let admin_text = document.getElementById("admin-text")
                admin_text.innerHTML = "You have to fill all the fields"
                admin_text.style.color = "red"
                return
            }

            /* search for all admin users */
            for (let i = 0; i < admins.length; i++) {
                if (inp_login === admins[i]["login"] && inp_pword === admins[i]["password"]) {
                    /* successful login */
                    cu.setCookie("isAdmin", true, "max-age=604800")
                    cu.setCookie("username", admins[i]["username"], "max-age=604800")
                    drawAdminPage(admins[i]["username"])
                    break
                } else {
                    /* incorrect login or password */
                    let admin_text = document.getElementById("admin-text")
                    admin_text.innerHTML = "Incorrect login or password"
                    admin_text.style.color = "red"
                    document.getElementById("pword").value = ""
                }
            }
        });
}

export function logout() {
    document.getElementById("admin-panel").remove()
    document.getElementById("admin-login-menu").remove()
    document.getElementById("menu").prepend(ou.htmlToElement(templates.login_menu))
    let crosses = document.getElementsByClassName("cross-close")
    for (let i = 0; i < crosses.length; i++) {
        crosses[i].hidden = true
        crosses[i].onclick = null
    }
    cu.deleteCookie("username")
    cu.deleteCookie("isAdmin")
}

export function drawAdminPage(username) {
    /* edit admin-login-menu */
    // edit welcome text
    let admin_text = document.getElementById("admin-text")
    admin_text.innerHTML = `Welcome, ${username}!`
    admin_text.style.color = "green"
    // delete inputs
    document.getElementById("admin-login").remove()
    document.getElementById("admin-password").remove()
    // edit button text and function
    let button = document.getElementById("login-button")
    button.value = "Logout"
    button.onclick = logout

    /* add crosses to books */
    let crosses = document.getElementsByClassName("cross-close")
    for (let i = 0; i < crosses.length; i++) {
        crosses[i].hidden = false
        crosses[i].setAttribute("onclick", `deleteBook('${crosses[i].id}')`)
    }

    /* draw admin panel */
    document.getElementById("book-list").prepend(ou.htmlToElement(templates.admin_panel))
}

export function addBook() {
    /* get data */
    const title = document.getElementById("inp-title").value
    const author = document.getElementById("inp-author").value
    const desc = document.getElementById("inp-desc").value
    const img = document.getElementById("inp-img").value

    /* check if all fields are filled */
    let missing_input = false
    if (title === "") {
        document.getElementById("text-title").style.color = "red"
        missing_input = true
    } else { document.getElementById("text-title").style.color = "black" }
    if (author === "") {
        document.getElementById("text-author").style.color = "red"
        missing_input = true
    } else { document.getElementById("text-author").style.color = "black" }
    if (desc === "") {
        document.getElementById("text-desc").style.color = "red"
        missing_input = true
    } else { document.getElementById("text-desc").style.color = "black" }
    if (img === "") {
        document.getElementById("text-img").style.color = "red"
        missing_input = true
    } else { document.getElementById("text-img").style.color = "black" }
    if (missing_input) { return }

    /* generate POST request */
    let data = `{
        "command": "add",
        "title": "${title}",
        "author": "${author}",
        "desc": "${desc}",
        "img": "${img}"
    }`;
    ou.sendPOST(data)

    alert(`The book with next parameters has been added to database:
    "title": "${title}",
    "author": "${author}",
    "desc": "${desc}",
    "img": "${img}"`+
    '\nTo see changes, please refresh the page')
}

export function deleteBook(id) {
    /* send POST request to nodejs file */
    console.log("Imagine that book was deleted")
    console.log(id)
    const title = document.getElementById(`title${id}`).innerHTML
    const author = document.getElementById(`author${id}`).innerHTML
    if (confirm(`Are you sure you want to delete ${title} by ${author}?`)) {
        let data = `{
            "command": "delete",
            "id": "${id}",
            "title": "${title}",
            "author": "${author}"
        }`
        ou.sendPOST(data)

        alert(`To see changes, refresh the page`)
    }
}