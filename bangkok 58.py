import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('sasawat17', 'l6zvgkrnkl')

fig = {'data': [{'labels': ['Personal computer', 'Notebook', 'Tablet', 'PDA', 'Smart Phone'],\
                 'values': [3638750, 2216706, 1776846, 171977, 4666129], 'type': 'pie'}], \
       'layout': {'title': 'Bangkok'}}

url = py.plot(fig, filename='Bangkok 58')
