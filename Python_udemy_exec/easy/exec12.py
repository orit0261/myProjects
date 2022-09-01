def build_pyramid(height: int) -> str:
    # to-do
    if height > 9 or height < 1:
        return 'please enter number 1 and 9'

    pyramid = ''

    for row in range(0, height):
        blanks = ' ' * (height - (row + 1))
        hashs = (row + 1) * '#'
        pyramid += blanks + hashs+' '+hashs

        if ((row + 1) != height):
            pyramid += ("\n")

    return pyramid


print(build_pyramid(5))
