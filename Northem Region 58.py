import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('sasawat17', 'l6zvgkrnkl')

fig = {'data': [{'labels': ['Personal computer', 'Notebook', 'Tablet', 'PDA', 'Smart Phone'],\
                 'values': [2927197, 1593301, 1144309 ,55219 ,3056748], 'type': 'pie'}], \
       'layout': {'title': 'Northem Region'}}

url = py.plot(fig, filename='Northem Region 58')
