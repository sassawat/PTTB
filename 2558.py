import plotly.plotly as py
from plotly.graph_objs import *
#py.sign_in('sasawat17', '0868389886')

fig = {'data': [{'labels': ['Bangkok', 'Central region', 'Northern region', 'Northeastern region', 'Southern region'], \
        'values': [6338750, 5494933, 2927197, 4609847, 2341471], 'type': 'pie', 'name': 'Personal Computer', \
            'marker': {'colors': ['rgb(56, 75, 126)', \
                                  'rgb(18, 36, 37)', \
                                  'rgb(34, 53, 101)', \
                                  'rgb(36, 55, 57)', \
                                  'rgb(6, 4, 4)']}, \
                 'domain': {'x': [0, .48], 'y': [0, .49]}, \
            'hoverinfo':'label+percent+name', 'textinfo':'none'}, \
        {'labels': ['Bangkok', 'Central region', 'Northern region', 'Northeastern region', 'Southern region'], \
            'values': [1776846, 2295878, 1144309, 1482747, 893134], \
            'marker': {'colors': ['rgb(177, 127, 38)', \
                                  'rgb(205, 152, 36)', \
                                  'rgb(99, 79, 37)', \
                                  'rgb(129, 180, 179)', \
                                  'rgb(124, 103, 37)']}, \
            'type': 'pie', 'name': 'Tablet', 'domain': {'x': [.52, 1], 'y': [0, .49]}, \
            'hoverinfo':'label+percent+name', 'textinfo':'none'}, \
        {'labels': ['Bangkok', 'Central region', 'Northern region', 'Northeastern region', 'Southern region'], \
            'values': [2216706, 2433960, 1593301, 2178955, 1085371], \
            'marker': {'colors': ['rgb(33, 75, 99)', \
                                  'rgb(79, 129, 102)', \
                                  'rgb(151, 179, 100)', \
                                  'rgb(175, 49, 35)', \
                                  'rgb(36, 73, 147)']}, \
            'type': 'pie', 'name': 'Notebook', 'domain': {'x': [0, .48], 'y': [.51, 1]}, \
            'hoverinfo':'label+percent+name', 'textinfo':'none'}, \
        {'labels': ['Bangkok', 'Central region', 'Northern region', 'Northeastern region', 'Southern region'],
            'values': [83400, 60391, 45635, 62526, 51065], \
            'marker': {'colors': ['rgb(146, 123, 21)', \
                                  'rgb(177, 180, 34)', \
                                  'rgb(206, 206, 40)', \
                                  'rgb(175, 51, 21)', \
                                  'rgb(35, 36, 21)']}, \
            'type': 'pie', 'name':'PDA', 'domain': {'x': [.52, 1], 'y': [.51, 1]}, \
            'hoverinfo':'label+percent+name', 'textinfo':'none'}, \
        {'labels': ['Bangkok', 'Central region', 'Northern region', 'Northeastern region', 'Southern region'],
            'values': [1766136, 2782233, 1638714, 2091997, 1079145], 'type': 'pie', 'name': 'SmartPhone', \
            'marker': {'colors': ['rgb(70, 100, 126)', \
                                  'rgb(10, 86, 35)', \
                                  'rgb(46, 78, 105)', \
                                  'rgb(36, 55, 15)', \
                                  'rgb(6, 4, 4)']}, \
            'domain': {'x': [0, 100], 'y': [0, .51]}, 'hoverinfo':'label+percent+name', 'textinfo':'none'}], \
    'layout': {'title': 'Graph of information technology users used information technology devices 2558', \
               'showlegend': False}}

url = py.plot(fig, filename='Pie Chart Subplot Example')
