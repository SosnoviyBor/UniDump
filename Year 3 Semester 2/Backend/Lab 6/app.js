const express = require('express')
const bodyParser = require('body-parser')
const sqlite = require("sqlite3").verbose()

const utils = require("./utils.js")

const app = express()
const port = 3000
app.listen(port, () => {
    console.log(`App is listening on port ${port}`)
})
app.use(bodyParser.urlencoded({ extended: true }))

const db_address = 'db.db'
const table = "messages"



// INSERT
app.post("/post", (req,res) => {
    const body = req.body
    const expectedKeys = ["from", "to", "content"]
    if (!utils.allBodyKeysExist(expectedKeys, body, res)) { return }

    const db = new sqlite.Database(db_address);
    db.serialize(() => {
        db.run(`INSERT INTO ${table} ("from", "to", "content")
                VALUES ("${body.from}", "${body.to}", "${body.content}")`)
    })
    
    db.close()
    res.send(`Successfully added entry ${JSON.stringify(body)}`)
})

// SELECT
app.get("/get", (req,res) => {
    var output = []
    const db = new sqlite.Database(db_address);
    db.each(`SELECT * FROM ${table}`, (err, row) => {
        const tmp = {
            "id": row.id,
            "from": row.from,
            "to": row.to,
            "content": row.content
        }
        output.push(tmp)
    }, () => {
        res.json(output)
    })
    db.close()
})

// UPDATE
app.put("/put", (req,res) => {
    const body = req.body
    const expectedKeys = ["id", "from", "to", "content"]
    if (!utils.allBodyKeysExist(expectedKeys, body, res)) { return }

    const db = new sqlite.Database(db_address);
    db.serialize(() => {
        db.run(`UPDATE ${table}
                SET "from" = "${body.from}",
                    "to" = "${body.to}",
                    "content" = "${body.content}"
                WHERE "id" = ${body.id}`)
    })
    
    db.close()
    res.send(`Successfully updated entry ${JSON.stringify(body)}`)
})

// DELETE
app.delete("/delete", (req,res) => {
    const body = req.body
    const expectedKeys = ["id"]
    if (!utils.allBodyKeysExist(expectedKeys, body, res)) { return }

    const db = new sqlite.Database(db_address);
    db.serialize(() => {
        db.run(`DELETE FROM ${table}
                WHERE "id" = ${body.id}`)
    })
    
    db.close()
    res.send(`Successfully deleted entry ${JSON.stringify(body)}`)
})