import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('sasawat17', 'l6zvgkrnkl')

fig = {'data': [{'labels': ['Personal computer', 'Notebook', 'Tablet', 'PDA', 'Smart Phone'],\
                 'values': [5494933, 2433960, 2295878, 167094, 7631985], 'type': 'pie'}], \
       'layout': {'title': 'Central Region'}}

url = py.plot(fig, filename='Central Region 58')
