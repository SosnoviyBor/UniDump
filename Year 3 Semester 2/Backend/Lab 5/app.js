const express = require('express')
const hbs = require("hbs")
const axios = require("axios")

const cities = require('./cities.json')
const secrets = require("./secrets.json")

const app = express()
app.set("view engine", "hbs")
hbs.registerPartials(__dirname + '/views/partials')

const port = 3000
app.listen(port, () => {
    console.log(`App is listening on port ${port}`)
})



app.get("/", (req,res) => {
    res.redirect("/weather/kyiv")
})

app.get("/weather", (req,res) => {
    res.redirect("/weather/kyiv")
})

app.get("/weather/:city", (req,res) => {
    const current_city = req.params["city"]
    if (cities[current_city] !== undefined) {
        // request lat and lon
        axios.get(`http://api.openweathermap.org/geo/1.0/direct?q=${cities[current_city]['en']}&limit=1&appid=${secrets['openweathermap_key']}`)
            .then(result => {
                const geo_data = result["data"][0]
                // request data
                axios.get(`https://api.openweathermap.org/data/2.5/weather?lat=${geo_data['lat']}&lon=${geo_data['lon']}&appid=${secrets['openweathermap_key']}`)
                    .then(result => {
                        // create context
                        const weather_data = result["data"]
                        const weather = {
                            city: cities[current_city]["ua"],
                            pressure: weather_data["main"]["pressure"],
                            humidity: weather_data["main"]["humidity"],
                            temp: Math.round(weather_data["main"]["temp"] - 273.15),    // Kelvin to Celsius
                            wind_speed: weather_data["wind"]["speed"],
                        }
                        res.render("weather.hbs", {weather})
                    })
                    .catch(error => {
                        console.log(error)
                    })
            })
            .catch(error => {
                console.log(error)
            })
    } else {
        res.send("There's no such city in app yet")
    }
})