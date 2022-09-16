// 
const scale = d3.scaleOrdinal(d3.schemeCategory10)
const color = d => scale(d.group)

var svg =  d3.select("svg");
var width = svg.attr("width");
var height = svg.attr("height");

// import dataset
d3.json('network.json').then(function(graphData) {
    console.log("Printing nodes");
    console.log(graphData);

    // define simulation
    var simulation = d3
        .forceSimulation(graphData.nodes)
        .force("charge", d3.forceManyBody().strength(-30))
        .force("center", d3.forceCenter(width / 2, height / 2))
        .force("link", d3.forceLink(graphData.links).id(function(d){
                        return d.id;
                    }))
        .alphaTarget(1) 
        .on("tick", ticked);
    
   // define links 
    var links = svg
    .append("g")
    .selectAll("line")
    .data(graphData.links)
    .enter()
    .append("line")
    .attr("stroke-width", 3)
    .style("stroke", "black");
    
    // define nodes 
    var nodes = svg
    .append("g")
    .selectAll("circle")
    .data(graphData.nodes)
    .enter()
    .append("circle")
    .attr("r", 10)
    .attr("fill", color);
    
    // define texts
    var texts = svg
    .append("g")
    .selectAll("text")
    .data(graphData.nodes)
    .enter()
    .append("text")
    .text(d=>d.id);
    
    // define interaction
    var drag = d3
    .drag()
    .on("start", dragstarted)
    .on("drag", dragged)
    .on("end", dragended);
    
    nodes.call(drag);

    //define tool tip
    
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
    
});

