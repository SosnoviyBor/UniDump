function writeToInput(text) {
	document.getElementById("inp").value += text
}

function clearInput() {
	document.getElementById("inp").value = ""
	document.getElementById("result").innerHTML = "Result goes here"
}

function clearEverything() {
	clearInput()
	document.getElementById("log").innerHTML = ""
}

async function calculate(deadInside=false) {
	inp = document.getElementById("inp").value
	try {
		result = eval(inp)
		document.getElementById("result").innerHTML = `Result: ${result}`
		document.getElementById("log").innerHTML += `<br>${inp} = ${result}`
	} catch (e) {
		document.getElementById("result").innerHTML = e
	}
	if (inp === "1000-7" || deadInside === true) {
		if (deadInside === false) {
			img = document.createElement("img")
			img.src = "zxcursed-dead-inside.gif"
			document.getElementById("calc").appendChild(img)
		}
		document.getElementById("inp").value = `${result}-7`
		await new Promise(r => setTimeout(r, 100));
		calculate(true)
	}
}
function sqrt(x) {return Math.sqrt(x)}