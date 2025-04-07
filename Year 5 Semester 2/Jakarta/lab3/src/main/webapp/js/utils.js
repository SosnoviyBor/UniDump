export function postToNewTab(json, link) {
    const inp = document.createElement("input")
    inp.id = "result_middleman"
    inp.name = "result"
    inp.type = "hidden"
    inp.value = JSON.stringify(json)

    const form = document.createElement("form")
    form.action = link
    form.method = "post"
    form.target = "_blank"
    form.encoding = "UTF-8"
    form.hidden = true
    form.appendChild(inp)

    document.getElementById("wrapper").appendChild(form)
    form.submit()
    form.remove()
}