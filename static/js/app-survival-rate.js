var cancer_json = JSON.parse(cancer_data);
console.log(cancer_json);

var race_originObj = {
    0: 'Non-Hispanic White',
    1: 'Hispanic (All Races)',
    2: 'Non-Hispanic Asian or Pacific Islander',
    3: 'Non-Hispanic Black',
    4: 'Non-Hispanic Unknown Race',
    5: 'Non-Hispanic American Indian/Alaska Native'
};

// Use D3 to select csr
var csr = d3.select("#csr").select("h1");
// Assign value from data
var valueStr = cancer_json.csr;
var csr_text = "You may have " + valueStr + " chance to survive !";
csr.html(csr_text);

// Select the button
var button = d3.select("#csr-btn");
// Select the form
var form = d3.select("#form");

// Create event handlers 
button.on("click", runCalculation);
form.on("submit", runCalculation);

// Complete the event handler function for the form
function runCalculation() { // This is run only when hit enter or the button
    // Clear the table
    csr.html("");
    
    // Prevent the page from refreshing
    d3.event.preventDefault();

    var URL="http://"
    var host_port = location.host;
    console.log("host_port: " + host_port);

    // Use D3 to select the dropdown menu
    var dropdownMenu = d3.select("#race_origin");
    // Assign the value of the dropdown menu option to a variable
    var input_race_origin = dropdownMenu.property("value");
    console.log("race_origin:"+ input_race_origin);
    var input_survival_months = d3.select("#survival_months").property("value");
    var input_tumor_size = d3.select("#tumor_size").property("value");

    if ((input_race_origin) && (input_survival_months) && (input_tumor_size)) {
        URL = URL + host_port + "/" + input_race_origin + "/" + input_survival_months + "/" + input_tumor_size;
    }
    else {
        URL = URL + host_port + "/99/0/0"; // Default dummy URL
    }
    console.log("URL: " + URL);

    window.open(URL,"_self");
};
