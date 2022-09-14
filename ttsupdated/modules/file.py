from modules.translate import trans
from modules.remove import remove_sym


def classify(word):
    result = []
    translated = trans(word)
    for i in translated:  # for each translated word
        if len(i) > 1:
            if i[1] == 'h' or i[1] == 'g' or i[1] == 's':  # classify folder and  file name if it has 2 consonant
                result.append([i[:2], i])
            else:  # classify folder and  file name if it has 1 consonant
                result.append([i[0], i])
        else:  # classify folder and  file name if it is space or if it is 1 digit alphabet
            result.append([i[0], i])
    return result


def with_out_classify(word):  # used to split words by space
    strtrans = ''.join(word).replace("__", " ")
    replaced = strtrans.split(" ")
    final = []
    for i in replaced:
        final.append(i)
        final.append("/")
    return final


def two_classify(word):
    word = remove_sym(word)
    word = trans(word)
    word = "".join(word)
    foldername = word[0]
    filename = word
    final = [[foldername, filename]]
    return final


def evenodd(inp):  # determine even or odd by the length of word
    inp = len(inp)
    return "eovdedn"[inp % 2::2]


def divide(word):
    reword = ""
    if len(word) == 1:
        reword = word
    elif len(word) == 2:
        reword = word
    elif len(word) == 3:
        reword = f"{word[0]} {word[-2:]}"
    elif len(word) == 4:
        reword = f"{word[:2]} {word[-2:]}"
    elif len(word) == 5:
        reword = f"{word[:2]} {word[2]} {word[-2:]}"
    elif len(word) == 6:
        reword = f"{word[:2]} {word[2:-2]} {word[-2:]}"
    elif len(word) == 7:
        reword = f"{word[:2]} {word[2:4]} {word[4]} {word[-2:]}"
    elif len(word) == 8:
        reword = f"{word[:2]} {word[2:4]} {word[4:6]} {word[-2:]}"
    elif len(word) == 9:
        reword = f"{word[:2]} {word[2:4]} {word[4]} {word[-4:-2]} {word[-2:]}"
    elif len(word) == 10:
        reword = f"{word[:2]} {word[2:4]} {word[4:-4]} {word[-4:-2]} {word[-2:]}"
    elif len(word) > 10:
        for i in word:
            reword += i + " "

    reword = reword.split(" ")

    return reword
