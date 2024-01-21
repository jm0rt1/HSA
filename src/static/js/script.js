$(document).ready(function () {
    function updatePlot() {
        var years = $('#years').val();
        var annual_medical_expense = $('#annual_medical_expense').val();
        // get values of other sliders...

        $.ajax({
            url: '/update_graph',
            type: 'POST',
            data: JSON.stringify({
                'years': years,
                'annual_medical_expense': annual_medical_expense,
                // other data...
            }),
            contentType: 'application/json; charset=utf-8',
            dataType: 'json',
            async: false,
            success: function (data) {
                var layout = {
                    title: 'HSA Analysis',
                    xaxis: {
                        title: 'Year'
                    },
                    yaxis: {
                        title: 'Amount ($)'
                    }
                };
                Plotly.newPlot('graph', data, layout);
            }
        });
    }

    $('#years, #annual_medical_expense').on('input', function () {
        $('#' + this.id + '-value').text(this.value);
        updatePlot();
    });

    updatePlot();
});