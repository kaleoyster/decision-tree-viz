//d3.json('./network.json', function(data){
//    console.log('reading data');
//    console.log(data);
//});
//
function draw(){

    d3.json('./network.json', function(graphData){
    console.log('reading data');
    console.log(graphData);
    drawUtility(graphData)
});
        

 //   var graphData = dataForBridges();
  //  drawUtility(graphData);
    }

function drawUtility(graphData) {
    //simulation.stop();
    const scale = d3.scaleOrdinal(d3.schemeCategory10)
    const color = d => scale(d.group)

    var svg =  d3.select("svg");
    var width = svg.attr("width");
    var height = svg.attr("height");
   
    var simulation = d3
    .forceSimulation(graphData.nodes)
    .force("charge", d3.forceManyBody().strength(-30))
    .force("center", d3.forceCenter(width / 2, height / 2))
    .force("link", d3.forceLink(graphData.links).id(function(d){
                        return d.id;
                    }))
    .alphaTarget(1) 
    .on("tick", ticked);


    var links = svg
    .append("g")
    .selectAll("line")
    .data(graphData.links)
    .enter()
    .append("line")
    .attr("stroke-width", 3)
    .style("stroke", "orange");

    var nodes = svg
    .append("g")
    .selectAll("circle")
    .data(graphData.nodes)
    .enter()
    .append("circle")
    .attr("r", 10)
    .attr("fill", color);

    var texts = svg
    .append("g")
    .selectAll("text")
    .data(graphData.nodes)
    .enter()
    .append("text")
    .text(d=>d.id);

    var drag = d3
    .drag()
    .on("start", dragstarted)
    .on("drag", dragged)
    .on("end", dragended);

    nodes.call(drag);

    function ticked(){
        texts
            .attr("x", d=>d.x)
            .attr("y", d=>d.y);

        nodes
            .attr('cx', function(d){
                            return d.x;

                        })
            .attr('cy', function(d){
                            return d.y;

                        });
        links
            .attr('x1', function(d){
                            return d.source.x;
                        })

            .attr('y1', function(d){
                            return d.source.y;
                        })

            .attr('x2', function(d){
                            return d.target.x;
                        })

            .attr('y2', function(d){
                            return d.target.y;
                        });

 }

function dragstarted(event){
    if (!event.active) simulation.alphaTarget(0.3).restart();
        event.subject.fx = event.subject.x;
        event.subject.fy = event.subject.y;
 }

function dragged(event){
    event.subject.fx = event.x;
    event.subject.fy = event.y;
 }

function dragended(event){
    if (!event.active) simulation.alphaTarget(0);
        event.subject.fx = null;
        event.subject.fy = null;
  }
}

// TODO: This where the data will go
function redraw(){
    // redraw (update the visualization)
}

function dataForBridges(){
   var graphData = {
        nodes: [
                {"id":'Bridge 1', "group":1},
                {"id":'Bridge 2', "group":2},
                {"id":'Bridge 3', "group":3},
                {"id":'Bridge 4', "group":2},
                {"id":'Bridge 5', "group":1},
                {"id":'Bridge 6', "group":1},
                {"id":'Bridge 8', "group":2},
                ],

        links: [
            {"source":'Bridge 1',
             "target":'Bridge 2', 
             "value": 0},

            {"source":'Bridge 8',
             "target":'Bridge 2', 
             "value": 1},

            {"source":'Bridge 2', 
             "target":'Bridge 3', 
             "value": 1},

            {"source":'Bridge 3', 
             "target":'Bridge 5', 
             "value": 8},

            {"source":'Bridge 4', 
             "target":'Bridge 5', 
             "value": 2},

            {"source":'Bridge 5', 
             "target":'Bridge 2', 
             "value": 10},

            {"source":'Bridge 5', 
             "target":'Bridge 1', 
             "value": 2},
        ]
    };

    async function loadNames(){
        const response = await fetch('./network.json');
        let names = await response.json();
        names = JSON.stringify(names);
        names = JSON.parse(names);
        //console.log(names.nodes);
        return names;

    }
    //#loadNames();

    let names = loadNames();
    //console.log(names);

return graphData;
}
 
