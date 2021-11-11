ls1 = [1, 5, 6, 7, 8, 5, 5, 2, 2, 1, 1]


def dup_remove(lst1):
  new_set = set(lst1)
  return (list(new_set))

def dup_remove2(lst1):
  lst2=[]
  dict1={}
  dict1={k: v for v, k in enumerate(lst1)}
  print(dict1)
  return list(dict1.keys())
  # for i in lst1:
  #   if
  #   dict[i].app
  #   if not i in lst2:
  #     lst2.append(i)



print(dup_remove(ls1))
print(dup_remove2(ls1))