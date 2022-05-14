export function htmlToElement(html) {
    let template = document.createElement('template');
    html = html.trim();
    template.innerHTML = html;
    return template.content.firstChild;
}

export function sendPOST(data) {
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "http://localhost:20202/");
    xhr.setRequestHeader("Accept", "application/json");
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            console.log(`${new Date()} | addBook POST request ${xhr.status} status`);
            console.log(`${new Date()} | addBook POST request  response text: '${xhr.responseText}'`);
        }};

    xhr.send(data);
    console.log(`\`${new Date()} | New POST request has been sent\nData sent: ${data}`)
}