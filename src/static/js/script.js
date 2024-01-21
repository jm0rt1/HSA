$(document).ready(function () {
    function updatePlot() {
        var years = $('#years').val();
        var annual_medical_expense = $('#annual_medical_expense').val();
        var hsa_return_rate = $('#hsa_return_rate').val();
        var tax_rate = $('#tax_rate').val();
        var hsa_withdrawal_rate = $('#hsa_withdrawal_rate').val();
        var hsa_contribution = $('#hsa_contribution').val();

        $.ajax({
            url: '/update_graph',
            type: 'POST',
            data: JSON.stringify({
                'years': years,
                'annual_medical_expense': annual_medical_expense,
                'hsa_return_rate': hsa_return_rate,
                'tax_rate': tax_rate,
                'hsa_withdrawal_rate': hsa_withdrawal_rate,
                'hsa_contribution': hsa_contribution
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

    $('#years, #annual_medical_expense, #hsa_return_rate, #tax_rate, #hsa_withdrawal_rate, #hsa_contribution').on('input', function () {
        $('#' + this.id + '-value').text(this.value);
        updatePlot();
    });

    updatePlot();
});