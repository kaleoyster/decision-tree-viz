export function generateData(){
    var graphData = {
                  nodes: [
                            {"id":'Bridge 1', "group":1},
                            {"id":'Bridge 2', "group":2},
                            {"id":'Bridge 3', "group":3},
                            {"id":'Bridge 4', "group":2},
                            {"id":'Bridge 5', "group":1},
                            {"id":'Bridge 6', "group":1},
                            ],

                    links: [
                        {"source":'Bridge 1',
                         "target":'Bridge 2', 
                         "value": 5},

                        {"source":'Bridge 2', 
                         "target":'Bridge 3', 
                         "value": 7},

                        {"source":'Bridge 3', 
                         "target":'Bridge 5', 
                         "value": 8},

                        {"source":'Bridge 4', 
                         "target":'Bridge 5', 
                         "value": 2},

                        {"source":'Bridge 5', 
                         "target":'Bridge 6', 
                         "value": 15},

                        {"source":'Bridge 6', 
                         "target":'Bridge 1', 
                         "value": 10},
                    ]
                };
        return graphData;
    }
