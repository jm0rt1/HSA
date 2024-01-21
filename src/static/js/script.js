$(document).ready(function () {
    $.ajax({
        url: '/update_graph',
        type: 'POST',
        data: {
            'years': 10,
            'annual_medical_expense': 5000,
            'hsa_return_rate': 0.07,
            'tax_rate': 0.24,
            'hsa_withdrawal_rate': 5000,
            'hsa_contribution': 3550
        },
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
});