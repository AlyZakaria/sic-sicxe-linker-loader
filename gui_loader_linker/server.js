

const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 5000

app.use(bodyParser.json());

app.get('/', (_req, res) => {
    res.send('Home Page..')
})
app.post('/inputs' , (req, res) => {
    console.log(req.body)
})
app.listen(port, () => {
    console.log(`listening on port ${port}`)
})
