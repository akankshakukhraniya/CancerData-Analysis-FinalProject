var cancer_json = JSON.parse(cancer_data);
console.log(cancer_json);

var data = [
    {
      x: ['testing_data_score','training_data_score'],
      y: [cancer_json.testing_data_score, cancer_json.training_data_score],
      type: 'bar'
    }
  ];
  
  Plotly.newPlot('barchart', data);



var thead = d3.select('#table').append('thead').append('tr');
thead.append("th")
Object.keys(cancer_json.stats_dict).forEach(col=>{
    thead.append('th').text(col);
});

var tindex = d3.select('#table').append('tbody');
Object.keys(cancer_json.stats_dict.area_mean).forEach(th=>{
    tindex.append("tr").append("th").text(th)
});

Object.values(cancer_json.stats_dict).forEach((obj)=>{
    var col = d3.select('tbody').selectAll('tr')._groups[0];
    Object.values(obj).forEach((val,row)=>{
        d3.select(col[row]).append('td').text(val);
    });
});

// var graph= {
//         x:['Bening Cells', 'Malign Cells'],
//         y:[357,212],
//         type: 'bar'
//     };

// Plotly,newPlot('beningbar',graph);


// var thead = d3.select('#table').append('thead').append('tr');
// thead.append("th")
// Object.keys(cancer_json.classification_report).forEach(col=>{
//     thead.append('th').text(col);
// });

// var tindex = d3.select('#table').append('tbody');
// Object.keys(cancer_json.classification_report).forEach(th=>{
//     tindex.append("tr").append("th").text(th)
// });

// Object.values(cancer_json.classification_report).forEach((obj)=>{
//     var col = d3.select('tbody').selectAll('tr')._groups[0];
//     Object.values(obj).forEach((val,row)=>{
//         d3.select(col[row]).append('td').text(val);
//     });
// });