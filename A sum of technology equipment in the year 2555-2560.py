import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('sasawat17', 'l6zvgkrnkl')

trace1 = go.Bar(
    x=['Personal computer', 'Notebook', 'Tablet', 'PDA', 'Smart phone'],
    y=[119066200, 59460992, 42540310, 3600480, 105648315],
    name='A sum of technology equipment in the year 2555-2560'
)
data = [trace1]
layout = go.Layout(
    barmode='group'
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='grouped-bar')
