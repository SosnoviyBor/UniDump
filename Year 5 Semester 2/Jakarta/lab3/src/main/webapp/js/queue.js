import * as utils from "./utils.js";

if (document.getElementById("data").dataset.isOpen === "false") {
    document.getElementById("new-user-name").disabled = true
    document.getElementById("new-user-submit").disabled = true
    document.getElementById("status").innerHTML = "закрита"
} else {
    document.getElementById("status").innerHTML = "відкрита"
}


document.getElementById("login-submit").addEventListener("click", () => {
    document.getElementById("login-submit").value = ""

    const body = {
        password: document.getElementById("login-password").value,
        queueId: document.getElementById("data").dataset.queueId
    }
    utils.postToNewTab(body, "/admin")
})


document.getElementById("new-user-submit").addEventListener("click", () => {
    const body = {
        name: document.getElementById("new-user-name").value,
        queueId: document.getElementById("queue-name").dataset.id
    }

    fetch("/create/user", {
        method: "POST",
        body: JSON.stringify(body),
        headers: { "Content-type": "application/json; charset=UTF-8" }
    })
        .then(response => {
            switch (response.status) {
                case 200:
                    location.reload()
            }
        })
})