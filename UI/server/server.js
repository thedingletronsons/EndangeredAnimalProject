const express = require('express')
const app = express()

// if user types "localhost:5000/api" server the response with following json  
app.get("/api", (req,res) => (
    res.json({"users": ["userOne", "userTwo", "userThree", "userFour"]})
))

// start listening at port 5000
app.listen(5000, () => (console.log("Server started on port 5000")))