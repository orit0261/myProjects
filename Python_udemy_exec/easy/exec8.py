def is_palindrome(input: str) -> bool:
    if not input:
        return False

    input = input.lower()
    for i in range(int(len(input)//2)):
       k = len(input)-i-1
       if input[i]!=input[k]:
           return False
    return True

is_palindrome('wow1')