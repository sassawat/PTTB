import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('sasawat17', 'l6zvgkrnkl')

fig = {'data': [{'labels': ['Personal computer', 'Notebook', 'Tablet', 'PDA', 'Smart Phone'],\
                 'values': [4609847, 2178955, 1482747, 173288, 3727486], 'type': 'pie'}], \
       'layout': {'title': 'Northeastern Region'}}

url = py.plot(fig, filename='Northeastern Region 58')
