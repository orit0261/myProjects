import re

data = {
    1: "Scandinavia includes Denmark Norway, and Sweden. I have been to Denmark",
    2: "Lord of the rings was filmed in New-Zealand",
    3: "The capital of Israel is Jerusalem",
    4: "Israel is the country I live in",
    5: "I have been to Washington"
}


data_to_find = {}
lst_words = []
for k, v in data.items():
    # k = 1, v = "Scandinavia includes Denmark, Norway, and Sweden. I have been to Denmark"
    res = re.sub(r'[^\w\s]', '', v) # remove all ,.{} signs

    words = set(res.split())
    for word in words:
        # check if the word exists
        if word in data_to_find:
            # this handles the case where the work ALREADY EXISTS in the dictionary
            data_to_find[word].append(k)
        else:
            data_to_find[word] = [k]


def get_word(input_str):
    return data_to_find.get(input_str)

print(get_word('have'))