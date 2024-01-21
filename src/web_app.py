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
    untaxed_cost = np.zeros(years)
    total_medical_cost = np.zeros(years)

    for year in range(years):
        if year > 0:
            # Calculate the cash and invested parts of the HSA balance
            hsa_cash = min(1000, hsa_balance[year - 1])
            hsa_invested = max(0, hsa_balance[year - 1] - hsa_cash)

            # Calculate the new HSA balance
            hsa_balance[year] = hsa_cash * \
                (1 + 0.01) + hsa_invested * \
                (1 + hsa_return_rate) + hsa_contribution

            # If there's a withdrawal, subtract it from the invested part of the balance and add it to the taxable cost
            if hsa_withdrawal_rate > 0:
                hsa_balance[year] -= hsa_withdrawal_rate
                untaxed_cost[year] = untaxed_cost[year-1] + hsa_withdrawal_rate

            # Calculate the taxable cost for the current year
            taxable_cost[year] = taxable_cost[year-1] + \
                ((annual_medical_expense-untaxed_cost[year]) * (1 + tax_rate))

            total_medical_cost[year] = taxable_cost[year] + untaxed_cost[year]

    data = [
        go.Scatter(x=list(range(years)), y=hsa_balance,
                   mode='lines', name='HSA Account Balance'),
        go.Scatter(x=list(range(years)), y=taxable_cost,
                   mode='lines', name='Total Cost from Taxable Income'),
        go.Scatter(x=list(range(years)), y=total_medical_cost,
                   mode='lines', name='Total Cost To You Mixing HSA and Taxable Income')
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON


if __name__ == '__main__':
    app.run(debug=True)
