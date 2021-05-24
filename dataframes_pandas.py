import pandas as pd

cites = ['austin','dallas','ashdod','tlv']
visitors = [100,200,300,400]
weekdays = ['sun','sun','mon','mon']
list_lables = ['city','visit','weekdays']
list_cols = [cites,visitors,weekdays]
# Zip the 2 lists together into one list of (key,value) tuples:
zipped = list(zip(list_lables,list_cols))
data = dict(zipped)
users = pd.DataFrame(data)
print(users)

# Inspect the list using print()
print(zipped)

# Build a dictionary with the zipped list: data
data = dict(zipped)

# Build and inspect a DataFrame from the dictionary: df
df = pd.DataFrame(data)
print(df)