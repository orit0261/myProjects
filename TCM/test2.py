try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# to search
query = "black leather bag"

for j in search(query, tld="co.in", num=100, stop=100, pause=2):
    print(j)