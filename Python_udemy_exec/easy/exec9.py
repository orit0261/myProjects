def are_anagrams(a: str, b: str) -> bool:
    a = list(a.replace(' ','').lower())
    b = list(b.replace(' ','').lower())

    if  len(a) != len(b):
        return False
    return sorted(a)==sorted(b)



print(are_anagrams('Listaen', 'aSilent'))
print(are_anagrams('1wow', 'wow1'))