const fs = require("fs");
const d3n = require("d3-node");

fs.readFile("./path.csv",(err, data) => {
    if (err){
        console.log(err);
    }
    console.log(data.toString());
});

console.log("last line");
console.log(d3n.version);

