$(document).ready(function() {
    $('input[name="name"]').autoComplete({
        minChars: 2,
        source: function(term, suggest){
            $.getJSON('https://api.opencagedata.com/geocode/v1/json', {
                q: term,
                key: 'b4b8c0c799df49ccb51391fd640cfc3a'
            }, function(data){
                var suggestions = [];
                $.each(data.results, function(i, val) {
                    suggestions.push(val.formatted);
                });
                suggest(suggestions);
            });
        }
    });
    formatWeatherData();
    monitorWeatherData();
});

function formatWeatherData() {
    var weatherItems = document.querySelectorAll('ul li');
    console.log("Weather items found:", weatherItems.length);

    if (weatherItems.length > 0) {
        var today = new Date().toISOString().split('T')[0]; 

        weatherItems.forEach(function(item, index) {
            var dateText = item.textContent.match(/(\d{4}-\d{2}-\d{2})/); 
            console.log("Found date in text:", dateText);

            if (dateText && dateText.length > 0) {
                var date = dateText[0];
                var formattedDate = date.replace(/^(\d{4})-(\d{2})-(\d{2})$/, '$3.$2.$1'); 
                console.log("Formatted date:", formattedDate);

                item.innerHTML = item.innerHTML.replace(date, formattedDate); 

                // Подсветка сегодняшней даты
                if (date === today && index === 0) { 
                    item.innerHTML = item.innerHTML.replace(formattedDate, 'Сегодня');
                    item.style.backgroundColor = '#e6e62d'; 
                    item.style.color = '#000080'; 
                }
            } else {
                console.log("No valid date format found in the text.");
            }
        });
    } else {
        console.log("No weather items found.");
    }
}