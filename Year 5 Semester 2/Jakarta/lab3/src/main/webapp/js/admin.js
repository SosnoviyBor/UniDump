if (document.getElementById("data").dataset.isOpen === "false") {
    document.getElementById("status").innerHTML = "закрита"
} else {
    document.getElementById("status").innerHTML = "відкрита"
}


Array.from(document.getElementsByClassName("delete-user")).forEach(
    (button) => button.addEventListener("click", () => {
            if (button.parentElement.getElementsByClassName("confirmation")[0].checked) {
                const body = {
                    userId: button.id
                }

                fetch("/delete/user", {
                    method: "POST",
                    body: JSON.stringify(body),
                    headers: {"Content-type": "application/json; charset=UTF-8"}
                })
                    .then(response => {
                        switch (response.status) {
                            case 200:
                                location.reload()
                        }
                    })
            }
        }
    )
)


document.getElementById("delete-first").addEventListener("click", () => {
    const body = {
        queueId: document.getElementById("data").dataset.queueId
    }

    fetch("/delete/user/top", {
        method: "POST",
        body: JSON.stringify(body),
        headers: {"Content-type": "application/json; charset=UTF-8"}
    })
        .then(response => {
            switch (response.status) {
                case 200:
                    location.reload()
            }
        })
})


document.getElementById("update-queue-status").addEventListener("click", () => {
    const body = {
        queueId: document.getElementById("data").dataset.queueId,
        isOpen: document.getElementById("data").dataset.isOpen
    }

    fetch("/update/queue/status", {
        method: "POST",
        body: JSON.stringify(body),
        headers: {"Content-type": "application/json; charset=UTF-8"}
    })
        .then(response => {
            switch (response.status) {
                case 200:
                    location.reload()
            }
        })
})