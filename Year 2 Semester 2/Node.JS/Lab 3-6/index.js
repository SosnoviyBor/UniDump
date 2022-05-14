const html_path = "/main_page.html"
const config_path = './config/db_login.json'
const port = 20202

const express = require("express");
const app = express();
// launch server
app.listen(port, () => {
    console.log(`${new Date()} | Application started and listening on port ${port}`);
});
// teach this dumb machine how to parse jsom http bodies
app.use(express.json());
// css styles
app.use(express.static(__dirname));
// html page
app.get("/", (req, res) => {
    console.log(`${new Date()} | Received GET request from ${req.hostname}`)
    /* connect to MySQL database */
    const mysql_config = require(config_path)
    const mysql = require('mysql');
    const con = mysql.createConnection(mysql_config);
    con.connect(function(err) {
        if (err) throw err;
        console.log(`${new Date()} | Connected to database`);
    });
    /* parse the data from database*/
    const fs = require("fs");
    const cheerio = require('cheerio').load(fs.readFileSync("." + html_path))
    con.query("SELECT * FROM books", (err, result) => {
        if (err) throw err;
        let books = ""
        for (let i = 0; i < result.length; i++) {
            books += `
            <div class="book" id="book${result[i]["id"]}">
                <div class="cross-close" id="${result[i]["id"]}" hidden>
                    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTV6UObWmfMzJE7M1Eo0BaRdGuAsrQIIz7bNw&usqp=CAU" onclick="" alt="Image is unavailable">
                </div>
                <div class="book-title-author">
                    <div class="book-title" id="title${result[i]["id"]}">${result[i]["name"]}</div>
                    <div class="book-author" id="author${result[i]["id"]}">${result[i]["author"]}</div>
                </div>
                <div class="book-description">
                    <div class="book-image">
                        <img src="${result[i]["img"]}" alt="Image not found">
                    </div>
                    <div class="book-text">
                        ${result[i]["desc"]}
                    </div>
                </div>
            </div>
            `;
        }
        cheerio("#placeholder").replaceWith(books)
        res.send(cheerio.root().html())
        console.log(`${new Date()} | Sent the response`)
    })
})

app.post('/', function (req, res) {
    console.log(`${new Date()} | POST request received`)
    const mysql_config = require(config_path)
    const mysql = require('mysql');
    const con = mysql.createConnection(mysql_config);

    const data = req.body
    con.connect(function(err) {
        if (err) throw err;
        console.log(`${new Date()} | Connected to database`);
        switch (data["command"]){

            case "add":
                con.query(`INSERT INTO books VALUES`+
                ` (DEFAULT, '${data["title"]}', '${data["author"]}', '${data["desc"]}', '${data["img"]}')`, (err, result) => {
                    if (err) throw err;
                    console.log(`${new Date()} | New book has been added to database`)
                })
                break

            case "delete":
                con.query(`DELETE FROM books WHERE id=${data["id"]}`, (err, result) => {
                    if (err) throw err;
                    console.log(`${new Date()} | Book id=${data["id"]}, title="${data["title"]}", author="${data["author"]}" has been deleted`)
                })
                break

            default:
                console.log(`${new Date()} | Unknown POST request command received`)
        }
    });
    res.sendStatus(200);
});