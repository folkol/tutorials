import pandas as pd
from altair import Chart

data = pd.DataFrame({'a': list('CCCDDDEEE'),
                     'b': [2, 7, 4, 1, 2, 6, 8, 4, 7]})
chart = Chart(data).mark_circle().encode(
    x='a',
    y='average(b)',
)

print(chart.to_json(indent=2, data=False))
#chart.serve()
