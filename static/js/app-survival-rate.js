// Function to display data
function showData (tableData, tbody) {
    tableData.forEach(rowData => {
        // Append one table row `tr` to the table body
        var rowTable = tbody.append("tr");
    
        Object.entries(rowData).forEach(([key, value]) => {
            // // Append one cell for the datetime m/d/yyyy
            var cellTable = rowTable.append("td")
            cellTable.text(value);
        });
    });    
};

// Initialize variables from data.js
var tableData = data;
// Use D3 to select the table
var table = d3.select("table");
// Use d3 to create a bootstrap striped table
// http://getbootstrap.com/docs/3.3/css/#tables-striped
table.attr("class", "table table-striped");
// Use D3 to select the table body
var tbody = d3.select("tbody");

// Display default dataset
showData (tableData, tbody);

// Select the button
var button = d3.select("#filter-btn");
// Select the form
var form = d3.select("#form");

// Create event handlers 
button.on("click", runFilter);
form.on("submit", runFilter);

// Complete the event handler function for the form
function runFilter() {
    // Clear the table
    tbody.html("");
    
    // Prevent the page from refreshing
    d3.event.preventDefault();
    
    // Default value to be displayed
    var filteredData = tableData;

    // Select the input elements and get the raw HTML node
    var inputDateTime = d3.select("#datetime");
    var inputCity = d3.select("#city");
    var inputState = d3.select("#state");
    var inputCountry = d3.select("#country");
    var inputShape = d3.select("#shape");

    // Create an array with input objects
    var inputArray = [ 
        {key: 'datetime', value: inputDateTime.property("value")},
        {key: 'city', value: inputCity.property("value").toLowerCase()},
        {key: 'state', value: inputState.property("value").toLowerCase()},
        {key: 'country', value: inputCountry.property("value").toLowerCase()},
        {key: 'shape', value: inputShape.property("value").toLowerCase()}
    ];

    // Filter for each input element
    inputArray.forEach(element => {
        if (element.value != ""){ // Only filter if current value is not blank
            filteredData = filteredData.filter(filteredRow => filteredRow[element.key]=== element.value);
        }
    });

    // Display filtered data
    showData (filteredData, tbody);
};
