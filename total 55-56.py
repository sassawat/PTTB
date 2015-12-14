import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('sasawat17', 'l6zvgkrnkl')

fig = {'data': [{'labels': ['Personal computer', 'Notebook', 'Tablet', 'PDA', 'Smart Phone'],\
                 'values': [119066200, 59460992, 42540310, 3600480, 105648315], 'type': 'pie'}], \
       'layout': {'title': 'Bangkok'}}

url = py.plot(fig, filename='Total 2555-2560')
