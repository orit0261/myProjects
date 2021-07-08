import json

x = {

  "taxs": [
      {"low_sum": 0, "upper_sum": 6000, "tax": 0},
      {"low_sum": 6000, "upper_sum": 8000, "tax": 10},
      {"low_sum": 8000, "upper_sum": 10000, "tax": 20},
      {"low_sum": 10000, "upper_sum": 99999, "tax": 30},
  ]
}

for i in x['taxs']:
    print(i['low_sum'])
    print(i['upper_sum'])
    print(i['tax'])