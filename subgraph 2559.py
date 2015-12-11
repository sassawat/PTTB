import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('sasawat17', 'l6zvgkrnkl')

fig = {
    'data': [
        {
            'labels': ['Bangkok', 'Central region', 'Northern region', 'Northeastern region', 'Southern region'],
            'values': [4062790, 6091038, 2844636, 4157891, 2347765],
            'type': 'pie',
            'name': 'Personal Computer',
            'marker': {'colors': ['rgb(252, 133, 133)',
                                  'rgb(255, 51, 51)',
                                  'rgb(246, 68, 68)',
                                  'rgb(174, 5, 5)',
                                  'rgb(246, 4, 4)']},
            'domain': {'x': [0, .48],
                       'y': [0, .49]},
            'hoverinfo':'label+percent+name',
            'textinfo':'none'
        },
        {
            'labels': ['Bangkok', 'Central region', 'Northern region', 'Northeastern region', 'Southern region'],
            'values': [2345336, 3185157, 1650320, 2264018, 1334705],
            'marker': {'colors': ['rgb(175, 10, 246)',
                                  'rgb(128, 8, 179)',
                                  'rgb(219, 160, 245)',
                                  'rgb(204, 0, 204)',
                                  'rgb(122, 57, 149)']},
            'type': 'pie',
            'name': 'Tablet',
            'domain': {'x': [.52, 1],
                       'y': [0, .49]},
            'hoverinfo':'label+percent+name',
            'textinfo':'none'

        },
        {
            'labels': ['Bangkok', 'Central region', 'Northern region', 'Northeastern region', 'Southern region'],
            'values': [2555583, 3027591, 1822591, 2435251, 1268912],
            'marker': {'colors': ['rgb(0, 153, 0)',
                                  'rgb(102, 204, 0)',
                                  'rgb(178, 255, 153)',
                                  'rgb(0, 255, 0)',
                                  'rgb(153, 255, 51)']},
            'type': 'pie',
            'name': 'Notebook',
            'domain': {'x': [0, .48],
                       'y': [.51, 1]},
            'hoverinfo':'label+percent+name',
            'textinfo':'none'
        },
        {
            'labels': ['Bangkok', 'Central region', 'Northern region', 'Northeastern region', 'Southern region'],
            'values': [212855, 212624, 63621, 225857, 159904],
            'marker': {'colors': ['rgb(153, 204, 255)',
                                  'rgb(0, 128, 255)',
                                  'rgb(102, 178, 255)',
                                  'rgb(0, 102, 204)',
                                  'rgb(51, 153, 255)']},
            'type': 'pie',
            'name':'PDA',
            'domain': {'x': [.52, 1],
                       'y': [.51, 1]},
            'hoverinfo':'label+percent+name',
            'textinfo':'none'
        },
        {
            'labels': ['Bangkok', 'Central region', 'Northern region', 'Northeastern region', 'Southern region'],
            'values': [5987068, 9773874, 3754866, 4562502, 3309494],
            'type': 'pie',
            'name': 'SmartPhone',
            'marker': {'colors': ['rgb(204, 102, 0)',
                                  'rgb(255, 218, 30)',
                                  'rgb(255, 128, 0)',
                                  'rgb(255, 204, 153)',
                                  'rgb(255, 178, 102)']},
            'domain': {'x': [0, 100],
                       'y': [0, .90]},
            'hoverinfo':'label+percent+name',
            'textinfo':'none'
        }
    ],
    'layout': {'title': 'Graph of information technology users used information technology devices 2559',
               'showlegend': False}
}

url = py.plot(fig, filename='Pie Chart Subplot Example')
