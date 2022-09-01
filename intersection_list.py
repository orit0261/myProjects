def FindIntersection(strArr):
  a=list(set(strArr[0].split(",")))
  b=list(set(strArr[1].split(",")))

  a = list(map(int, a))
  b = list(map(int, b))

  val =sorted(list(set(a) & set(b)))

  if len(val) == 0:
      return False
  else:
      return ",".join([str(i) for i in val])

print(FindIntersection(["1,-3,4,7,-13","1,-2,4,-13,15"]))
print(FindIntersection(["7,13","1,2,4,15"]))