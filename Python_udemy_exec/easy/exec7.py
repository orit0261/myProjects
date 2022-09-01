def reverse(input: str) -> str:
    es = ''
    if input:
      for i in range(len(input), 0,-1):
          es += input[i-1]
      return es

    return 'You Have Inputted an Out of Bound Value'

print(reverse('abc1כגדכג'))
