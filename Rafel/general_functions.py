import config
import random
import string


def get_dic():
    return {"username": config.POSTGRES_USER,
            "port": config.POSTGRES_PORT,
            "database": config.POSTGRES_DB,
            "password": config.POSTGRES_PW,
            "host": config.POSTGRES_URL
            }


def qsort(inlist):
    if inlist == []:
        return []
    else:
        pivot = inlist[0]
        lesser = qsort([x for x in inlist[1:] if x < pivot])
        greater = qsort([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater


# generate random string len between max and min
def generate_random_string(min_len=5, max_len=15):
    num_char = random.randint(min_len, max_len)

    rand_string = ""
    for i in range(num_char):
        rand_string += random.choice(string.ascii_letters)

    return rand_string
