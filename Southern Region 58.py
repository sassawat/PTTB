import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('sasawat17', 'l6zvgkrnkl')

fig = {'data': [{'labels': ['Personal computer', 'Notebook', 'Tablet', 'PDA', 'Smart Phone'],\
                 'values': [2341471, 1085371, 893134, 124095, 2602347], 'type': 'pie'}], \
       'layout': {'title': 'Southern Region'}}

url = py.plot(fig, filename='Southern Region 58')
