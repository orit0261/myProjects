d = {}
s = 'dabaxyddab'

for i in range(1, int(len(s))):
    if s[i] not in d:
        d[str(i)]=s[i]

for k,v in d.items():
    print(k,v)


