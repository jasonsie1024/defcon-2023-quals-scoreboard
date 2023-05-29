# import requests
# import re
# import math
from time import time
from pprint import pprint
import plotly.graph_objects as go
import pickle
from datetime import datetime
# import minify_html

logs = dict()

try:
    with open('logs.p', 'rb') as f:
        logs: dict = pickle.load(f)
except:
    pass

## Getting current scoreboard from DEFCON offical website, commented sice it's offline now
# tick_log = dict()
# tick = datetime.now()
# res = requests.get('https://quals.2023.nautilus.institute/scoreboard/complete')
# res = re.findall("""<td>(.+)<\/td>
# <td>(.+)<\/td>
# <td>(.+)<\/td>""", res.text)
# res = list(map(lambda r: (r[1], int(r[2]), int(r[0])), res))


fig = go.Figure(layout=go.Layout(
        title=go.layout.Title(text="DEFCON 2023 Quals Scoreboard"),
        hovermode="x",
        hoverlabel=dict(font_size=10)
    ))

default_show = True # set default_show=True for teams with score >= score of 'TWN48'
ranklist = [(records[-1][0], tname) for (tname, records) in logs.items()]
ranklist = sorted(ranklist)[::-1]
# print(ranklist)

for (_, t_name) in ranklist:
    while logs[t_name] and logs[t_name][-1][1] > datetime.fromtimestamp(1685321343):
        logs[t_name] = logs[t_name][:-1]

    fig.add_trace(go.Scatter(x = list(map(lambda x: x[1], logs[t_name])), y = list(map(lambda x: x[0], logs[t_name])), name=t_name, line_shape='vh', connectgaps=True, visible= None if default_show else "legendonly"))
    if t_name == 'TWN48':
        default_show = False

# for (tname, records) in logs.items():
#     print(tname, records)
# for (t_name, score, rank) in res:
#     tick_log[t_name] = (score, tick)
#     if t_name not in logs:
#         logs[t_name] = []

#     if len(logs[t_name]) == 0 or tick_log[t_name][:-1] != logs[t_name][-1][:-1]:
#         logs[t_name].append(tick_log[t_name])
    
#     logs[t_name][-1] = (logs[t_name][-1][0], tick)

#     fig.add_trace(go.Scatter(x = list(map(lambda x: x[1], logs[t_name])), y = list(map(lambda x: x[0], logs[t_name])), name=t_name, line_shape='vh', connectgaps=True, visible= None if default_show else "legendonly"))
#     if t_name == 'TWN48':
#         default_show = False

fig.write_html('/home/dept/ta/jason/htdocs/defcon_quals/scoreboard.html', auto_open=False, include_plotlyjs='cdn')

# html = fig.to_html(include_plotlyjs='cdn')
# minified = minify_html.minify(html, minify_js=True, remove_processing_instructions=True)

# print(len(html), len(minified), len(minified) / len(html))

with open('logs.p', 'wb') as f:
    pickle.dump(logs, f)