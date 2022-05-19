
const express = require('express'); 
const app = express();             
const port = 5000;                  


app.get('webscraping/index.js', (req, res) => {        //get requests to the root ("/") will route here
    res.sendFile('index.js', {root: __dirname});      
                                                        
});

app.listen(port, () => {         
    console.log(`5000 ${port}`); 
});