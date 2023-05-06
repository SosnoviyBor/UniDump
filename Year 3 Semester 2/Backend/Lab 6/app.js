const express = require('express')
const bodyParser = require('body-parser')
const mysql = require('mysql')

const utils = require("./utils.js")
const secrets = require("./secrets.js")

const app = express()
const port = 3000
app.listen(port, () => {
    console.log(`App is listening on port ${port}`)
})
app.use(bodyParser.urlencoded({ extended: true }))

const conn = mysql.createConnection(secrets.mysqlConnectionDetails)
const table = "ads"


// INSERT
app.post("/post", (req,res) => {
    const body = req.body
    const expectedKeys = ["status_id", "address", "rooms", "cost_hrn"]
    if (!utils.allBodyKeysExist(expectedKeys, body, res)) { return }

    conn.query(`INSERT INTO ${table} (status_id, address, rooms, cost_hrn)
                VALUES ("${body.status_id}", "${body.address}", "${body.rooms}", "${body.cost_hrn}")`,
                (error, results, fields) => {
                    if (error) throw error
                })

    res.send(`Successfully added entry ${JSON.stringify(body)}`)
})

// SELECT
app.get("/get", (req,res) => {
    const query = req.query
    // select all if no "id" param
    if (query["id"] === undefined) SQLquery = `SELECT * FROM ${table}`
    // select by id if there is an "id" param
    else SQLquery = `SELECT * FROM ${table} WHERE id = ${query.id}`

    conn.query(SQLquery, (error, results, fields) => {
        if (error) throw error
        if (query["id"] === undefined) res.json(results)
        else res.json(results[0])
    })
})

// UPDATE
app.put("/put", (req,res) => {
    const body = req.body
    const expectedKeys = ["id", "status_id", "address", "rooms", "cost_hrn"]
    if (!utils.allBodyKeysExist(expectedKeys, body, res)) { return }

    conn.query(`UPDATE ${table}
                SET status_id = ${body.status_id},
                    address = "${body.address}",
                    cost_hrn = ${body.cost_hrn},
                    rooms = ${body.rooms}
                WHERE id = ${body.id}`,
                (error, results, fields) => {
                    if (error) throw error
                })

    res.send(`Successfully updated entry ${JSON.stringify(body)}`)
})

// DELETE
app.delete("/delete", (req,res) => {
    const body = req.body
    const expectedKeys = ["id"]
    if (!utils.allBodyKeysExist(expectedKeys, body, res)) { return }

    conn.query(`DELETE FROM ${table}
                WHERE id = ${body.id}`,
                (error, results, fields) => {
                    if (error) throw error
                })

    res.send(`Successfully deleted entry ${JSON.stringify(body)}`)
})