const fs = require("fs");
const d3n = require("d3-node");
const d3 = require("d3");
fs.readFile("./path.csv",(err, data) => {
    if (err){
        console.log(err);
    }
    console.log(data.toString());
});

console.log("last line");
console.log(d3n.version);
console.log(d3);
