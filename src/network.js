//  Oridnal Scale 
const scale = d3.scaleOrdinal(d3.schemeCategory10)
const color = d => scale(d.group)

var svg =  d3.select("svg");
var width = svg.attr("width");
var height = svg.attr("height");

// import dataset
d3.json('network.json').then(function(graphData) {
    console.log("Printing nodes");
    console.log(graphData.nodes);

    // define simulation
    var simulation = d3
        .forceSimulation(graphData.nodes)
        .force("charge", d3.forceManyBody().strength(-100))
        .force("center", d3.forceCenter(width / 2, height / 2))
        .force("link", d3.forceLink(graphData.links).id(function(d)         {
                    return d.id;
                    }).distance(200))
        .force("collide",d3.forceCollide().strength(0).radius(0))
        .alphaTarget(1)
        .on("tick", ticked);

 // define nodes 
    var nodes = svg
    .append("g")
    .selectAll("circle")
    .data(graphData.nodes)
    .enter()
    .append("circle")
    .attr("r", 30)
    .attr("fill", color)
    .on("mouseover", tooltip_node_in)
    .on("mouseout", tooltip_node_out);
  


    // define links 
    var links = svg
    .append("g")
    .selectAll("line")
    .data(graphData.links)
    .enter()
    .append("line")
    .attr("stroke-width", function(d) {return (d.value) * (d.value)})
    
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

    // define tool tip
    let tooltip = d3
        .select("body")
        .append("div")
        .style("position", "absolute")
        .style("visibility", "hidden")
        .style("background-color", "grey")
        .style("color", "white")
        .style("text-shadow", "1px 1px 1px #000000")
        .attr("class", "tooltip");

    let tooltip_node = d3
        .select("body")
        .append("div")
        .style("position", "absolute")
        .style("visibility", "hidden")
        .style("background-color", "crimson")
        .style("text-shadow", "1px 1px 1px #000000")
        .attr("class", "tooltip_node");

    function tooltip_in(event, d) {
            return tooltip
                .html(
                `<h4>Source: ${d.source.id}</h4>
                 <h4>Target: ${d.target.id}</h4>
                 <br>
                 <h5> (Relation: source value, target value) </h5>
                 <h5> Rules: ${d.source.rules}, ${d.target.rules} </h5>
                `
                )
                .style("visibility", "visible")
                .style("top", event.pageY + "px")
                .style("left", event.pageX + "px");
          }

    function tooltip_out() {
            return tooltip
                    .transition()
                    .duration(20)
                    .style("visibility", "hidden");
        }

    function tooltip_node_in(event, d) {
            return tooltip_node
                    .html(
                        `<h4> Sample: ${d.id}</h4>
                         <h5> Rules: ${d.rules} </h5>
                        `
                     )
                     .style("visibility", "visible")
                     .style("top", event.pageY + "px")
                     .style("left", event.pageX + "px");
        }

    function tooltip_node_out() {
            return tooltip_node
                .transition()
                .duration(10)
                .style("visibility", "hidden");
        }

 
    function ticked(){
        texts
            .attr("x", (d)=>d.x)
            .attr("y", (d)=>d.y);
    
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

