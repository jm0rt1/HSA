from flask import Flask, render_template, request
import plotly
import plotly.graph_objs as go
import numpy as np
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/update_graph', methods=['POST'])
def update_graph():
    data = request.get_json()
    try:
        years = int(data['years'])
        annual_medical_expense = float(data['annual_medical_expense'])
        hsa_return_rate = float(data['hsa_return_rate'])
        tax_rate = float(data['tax_rate'])
        hsa_withdrawal_rate = float(data['hsa_withdrawal_rate'])
        hsa_contribution = float(data['hsa_contribution'])
    except KeyError as e:
        return f"Missing key: {e.args[0]}", 400
    except ValueError as e:
        return f"Invalid value for key: {e.args[0]}", 400

    # rest of your code...

    data = request.get_json()
    years = int(data['years'])
    annual_medical_expense = int(data['annual_medical_expense'])
    hsa_return_rate = float(data['hsa_return_rate'])
    tax_rate = float(data['tax_rate'])
    hsa_withdrawal_rate = int(data['hsa_withdrawal_rate'])
    hsa_contribution = int(data['hsa_contribution'])

    hsa_balance = np.zeros(years)
    taxable_cost = np.zeros(years)

    for year in range(years):
        if year > 0:
            hsa_balance[year] = hsa_balance[year - 1] * \
                (1 + hsa_return_rate) + hsa_contribution-hsa_withdrawal_rate
        taxable_cost[year] = ((annual_medical_expense) /
                              (1 - tax_rate)) * (year + 1)

    data = [
        go.Scatter(x=list(range(years)), y=hsa_balance,
                   mode='lines', name='HSA Account Balance'),
        go.Scatter(x=list(range(years)), y=taxable_cost,
                   mode='lines', name='Total Cost from Taxable Income')
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON


if __name__ == '__main__':
    app.run(debug=True)
