const all_books = Array.from(document.getElementsByClassName("book"))

function search() {
	// check if search query is empty
	if (document.getElementById("search_input").value === "") { return }

	const inp = document.getElementById("search_input").value.toLowerCase()
	let result = []

	// delete all existing books
	let curr_books = Array.from(document.getElementsByClassName("book"))
	curr_books.forEach(book => {book.remove()})

	// filter all existing books
	for (let i = 0; i < all_books.length; i++){
		const title = all_books[i].getElementsByClassName("book-title")[0].innerHTML
		const author = all_books[i].getElementsByClassName("book-author")[0].innerHTML
		if (title.toLowerCase().includes(inp) ||
			author.toLowerCase().includes(inp)) {
				result.push(all_books[i])
			}
		}

	// show filtered books
	if (result.length === 0) {
		// nothing was found
		let b = document.createElement("div")
		b.className = "book"
		let bta = document.createElement("div")
		bta.className = "book-title-author"
		let bt = document.createElement("div")
		bt.className = "book-title"
		bt.innerHTML = "Sadly, nothing was found"
		bta.appendChild(bt)
		b.appendChild(bta)
		document.getElementById("book-list").appendChild(b)
	} else {
		// show results
		for (let i = 0; i < result.length; i++){
			document.getElementById("book-list").appendChild(result[i])
		}
	}
}