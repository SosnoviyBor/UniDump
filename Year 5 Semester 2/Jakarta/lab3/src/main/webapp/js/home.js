document.getElementById("new-queue-button").addEventListener("click", () => {
    const body = {
        name: document.getElementById("new-queue-name").value,
        password: document.getElementById("new-queue-password").value
    }

    fetch("/create/queue", {
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