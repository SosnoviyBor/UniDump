const express = require("express");
const bodyParser = require("body-parser");
const path = require("path");
const axios = require("axios");
const { auth } = require("express-oauth2-jwt-bearer");
const cookieParser = require("cookie-parser");

const port = 3000;
const app = express();

app.use(cookieParser());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`);
});

app.get("/", (req, res) => {
    const token = req.get("Authorization");

    if (token) {
        return res.json({
            token: token,
            logout: "http://localhost:3000/logout",
        });
    }

    res.sendFile(path.join(__dirname + "/index.html"));
});

app.post("/api/login", async (req, res) => {
    const { login, password } = req.body;

    const getUserTokenData = {
        method: "post",
        url: `https://dev-oss8ohe4nbxa2vgu.us.auth0.com/oauth/token`,
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data: {
            grant_type: "password",
            username: login,
            password: password,
            audience: "https://dev-oss8ohe4nbxa2vgu.us.auth0.com/api/v2/",
            scope: "offline_access",
            client_id: "hIh1592k2ZaPY2vLltLWORo0gPc12XIL",
            client_secret:
                "Dq_LpMpNG0R6ObAwAhh29eHK90X1su7Kb_u9xb_B6B6XzgnQinV3RGbVS-k1JGrd",
        },
    };

    await axios
        .request(getUserTokenData)
        .then((response) => {
            console.log("login:", response.data);

            const currentDate = new Date();
            currentDate.setHours(currentDate.getHours() + 4);
            res.cookie("token", response.data.access_token, {
                expires: currentDate,
                httpOnly: true,
            });
            console.log(new Date());
            res.status(200).json({ token: response.data.access_token });
        })
        .catch((error) => {
            console.error("Error login:", error);
        });

    res.status(401).send();
});

app.get("/logout", function (req, res) {
    // console.log(req);

    res.cookie("token", "", {expires: new Date.now(), httpOnly:true})
    // res.cookie("token", "", {expires: 0})
    // res.clearCookie("token")
    
    res.send();
});

app.get("/api/public", function (req, res) {
    res.json({
        message: "Публічна сторінка",
    });
});

const setHeader = (req, res, next) => {
    console.log("Cookies:", req.cookies);

    if (req.cookies.token) {
        req.headers.authorization = `Bearer ${req.cookies.token}`;
    }

    next();
};

const checkJwt = auth({
    audience: "https://dev-oss8ohe4nbxa2vgu.us.auth0.com/api/v2/",
    issuerBaseURL: `https://dev-oss8ohe4nbxa2vgu.us.auth0.com/`,
});

app.get("/api/private", setHeader, checkJwt, function (req, res) {
    res.json({
        message: "Приватна сторінка",
    });
});
