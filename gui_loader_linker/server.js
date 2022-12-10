

const express = require('express');
const bodyParser = require("body-parser")
var fileupload = require("express-fileupload");
const exec = require('child_process').exec;
const {resolve} = require('path');

const app = express();
const fs = require('fs');
const port = 5000

// app.use(bodyParser.json());
app.use(fileupload());
app.use(express.urlencoded({ extended: true }));

app.get('/', (_req, res) => {
    res.send('Home Page..')
})
app.post('/inputs' , (req, res) => {
    // console.log(req.body)
    if(req.body.type == 'SIC'){
        fs.writeFile('..\\rsc\\sic.txt', req.body.text, err => {
            if (err) {
              console.error(err);
            }
            // file written successfully
          });
    }
    else{
        fs.writeFile('..\\rsc\\sicxe.txt', req.body.text, err => {
            if (err) {
              console.error(err);
            }
            // file written successfully
          });
    }
    const absPath = resolve('../run.bat');
    exec(`"${absPath}" "${req.body.type}" "${req.body.address}"`, (err, stdout, stderr) => {
        if (err) {
            console.error(err);
            return;
        }   
        // console.log('here2',req.body.type);

    });
})
app.listen(port, () => {
    console.log(`listening on port ${port}`)
})


