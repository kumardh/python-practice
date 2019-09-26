from pandas.io.json import json_normalize

# Example 1: Flattening JSON objects : json_normalize does a pretty good job of flatting the object into a pandas dataframe.
sample_object = {'Name':'John', 'Location':{'City':'Los Angeles','State':'CA'}}
x = json_normalize(sample_object)
print(x)
# Result:
#    Name Location.City Location.State
# 0  John   Los Angeles             CA

# However flattening objects with embedded arrays is not as trivial.
sample_object = {'Name':'John', 'Location':{'City':'Los Angeles','State':'CA'}, 'hobbies':['Music', 'Running']}
x = json_normalize(sample_object)
print(x)
# Result:
#    Name           hobbies Location.City Location.State
# 0  John  [Music, Running]   Los Angeles             CA

# We can use record_path with meta properties to flatten as below.
x = json_normalize(sample_object, record_path='hobbies', meta=['Name'])
print(x)
# Result:
#          0  Name
# 0    Music  John
# 1  Running  John

# Example 2: making use of max_level.
data = [{'id': 1,
          'name': "Cole Volk",
          'fitness': {'height': 130, 'weight': 60}},
         {'name': "Mose Reg",
          'fitness': {'height': 130, 'weight': 60}},
         {'id': 2, 'name': 'Faye Raker',
          'fitness': {'height': 130, 'weight': 60}}]
x = json_normalize(data, max_level=0)
print(x)
# Result:
#     id        name                        fitness
# 0  1.0   Cole Volk  {'height': 130, 'weight': 60}
# 1  NaN    Mose Reg  {'height': 130, 'weight': 60}
# 2  2.0  Faye Raker  {'height': 130, 'weight': 60}

data = [{'id': 1,
          'name': "Cole Volk",
          'fitness': {'height': 130, 'weight': 60}},
         {'name': "Mose Reg",
          'fitness': {'height': 130, 'weight': 60}},
         {'id': 2, 'name': 'Faye Raker',
          'fitness': {'height': 130, 'weight': 60}}]
x = json_normalize(data, max_level=1)
print(x)
# Result:
#     id        name  fitness.height  fitness.weight
# 0  1.0   Cole Volk             130              60
# 1  NaN    Mose Reg             130              60
# 2  2.0  Faye Raker             130              60

# Example 3: Normalization from json string.
import json
json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
data = json.loads(json_string)
z  = json_normalize(sample_object)
print(z)
# Result:
#    Name           hobbies Location.City Location.State
# 0  John  [Music, Running]   Los Angeles             CA

# Example 4: Reading single quoted json data and normaliza
from pandas.io.json import json_normalize
f= open("singleQuote.txt","r")
x = f.read()
data = '{"values" :  ' + x.replace("'", '"') + '}'
sample_object = json.loads(data)
z  = json_normalize(sample_object)
print(z)
# Result:
#              values
# 0  [dog, cat, fish]

# Important Note: We see common error while working with json_normalize. AttributeError: 'str' object has no attribute 'values'
# The reason you are getting this error might be the data you are passing to json_normalize is a strand not a dict or list of dict with key/value pair.

# Below code will complain AttributeError: 'str' object has no attribute 'values'
#
# sample_object = ["dog","cat","fish"]
# z = json_normalize(sample_object)
# print(z)
#
# To make this work append all such instance with the Key or default value as appropriate like below -
#
# sample_object = {"values" : ["dog","cat","fish"]}
# z = json_normalize(sample_object)
# print(z)
#
# Now, this will work like a charm with below output -
# values
# 0 [dog, cat, fish]