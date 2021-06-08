var cancer_json = JSON.parse(cancer_data);
console.log(cancer_json);

// Use D3 to select csr
var csr = d3.select("#csr").select("h1");
// Assign value from data
var csr_text = "You may have " + cancer_json.csr + " chance to survive !";
csr.html(csr_text);

// Select the button
var button = d3.select("#csr-btn");
// Select the form
var form = d3.select("#form");

// Create event handlers 
button.on("click", runCalculation);
form.on("submit", runCalculation);

// Complete the event handler function for the form
function runCalculation() {
    // Clear the table
    csr.html("");
    
    // Prevent the page from refreshing
    d3.event.preventDefault();
    
    // Select the input elements 
    var input_race_origin = d3.select("#race_origin").property("value");
    console.log(input_race_origin);

    if (input_race_origin) {
        var input_survival_months = d3.select("#survival_months").property("value");
        var input_tumour_classification= d3.select("#tumour_classification").property("value");
        var input_tumor_size = d3.select("#tumor_size").property("value");
        var URL = "https://cancer-data.herokuapp.com/" + input_race_origin + "/" + input_survival_months + "/" + input_tumour_classification + "/" + input_tumor_size;
    }
    else {
        var URL = "https://cancer-data.herokuapp.com/0/0/0/0";
    }
    console.log(URL);
   
    window.open(URL,"_self");

};
