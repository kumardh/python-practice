from pandas.io.json import json_normalize
data = [{'id': 1,
          'name': "Cole Volk",
          'fitness': {'height': 130, 'weight': 60}},
         {'name': "Mose Reg",
          'fitness': {'height': 130, 'weight': 60}},
         {'id': 2, 'name': 'Faye Raker',
          'fitness': {'height': 130, 'weight': 60}}]
json_normalize(data, max_level=0)