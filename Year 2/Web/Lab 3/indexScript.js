const blockX = document.getElementById('x_header');
const blockY = document.getElementById('y_header');
blockX.onclick = () => window.location.replace("view.html")
blockY.onclick = () => window.location.replace("view.html")

var sliderCounter = 0	// Нумерация слайдеров
var slideIndex = 1;		// Индекс слайда по умолчанию

function newSlider() {	
	var arrowLeft = document.createElement("a")
	arrowLeft.classList.add("prev")
	arrowLeft.setAttribute("onclick", `minusSlide(${sliderCounter})`)
	arrowLeft.innerHTML = "&#10094;"
	var arrowRight = document.createElement("a")
	arrowRight.classList.add("next")
	arrowRight.setAttribute("onclick", `plusSlide(${sliderCounter})`)
	arrowRight.innerHTML = "&#10095;"

	var sliderDiv = document.createElement("div")
	sliderDiv.classList.add("slider")
	sliderDiv.id = `slider${sliderCounter}`
	sliderDiv.append(arrowLeft)
	sliderDiv.append(arrowRight)

	sliderDiv.append( addItem("2Hyt1WT33vM.jpg", "sample text 1") )
	sliderDiv.append( addItem("alena-aenami-couple1k.jpg", "sample text 2") )

	document.getElementById("four").append(sliderDiv)
	showSlides(slideIndex = 1, sliderCounter);
	sliderCounter++
}

function addItem(filename, text) {
	var itemDiv = document.createElement("div")
	itemDiv.classList.add("sliderItem")

	var img = document.createElement("img")
	img.src = `media/${filename}`
	img.alt = "no pic found :/"
	itemDiv.append(img)
	
	var innerDiv = document.createElement("div")
	innerDiv.classList.add("slideText")
	innerDiv.innerHTML = `slide ${text}`
	itemDiv.append(innerDiv)
	return itemDiv
}

/* Функция увеличивает индекс на 1, показывает следующй слайд*/
function plusSlide(sliderId) {
	showSlides(slideIndex += 1, sliderId);
}
/* Функция уменьшяет индекс на 1, показывает предыдущий слайд*/
function minusSlide(sliderId) {
	showSlides(slideIndex -= 1, sliderId);  
}

/* Основная функция слайдера */
function showSlides(n,sliderId) {
	var slides = document.getElementById(`slider${sliderId}`).getElementsByClassName("sliderItem")
	if (n > slides.length) {
		slideIndex = 1
	}
	if (n < 1) {
		slideIndex = slides.length
	}
	for (var i = 0; i < slides.length; i++) {
		slides[i].style.display = "none";
	}
	slides[slideIndex - 1].style.display = "block";
}