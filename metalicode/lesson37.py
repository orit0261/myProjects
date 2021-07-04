def return_a_func(arg):
    def you_the_boss():
        print("boss!")

    def you_loser():
        print("loser!")

    if arg=='me':
        return you_the_boss
    else:
        return you_loser

func_from_func = return_a_func("me")
func_from_func()