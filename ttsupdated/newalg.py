from pydub import AudioSegment, silence
from modules.remove import remove_letter
from modules.file import classify, with_out_classify, divide, two_classify
from pydub.effects import speedup
# import important modules pydub and  our modules


def tts(text, voice):
    pure_letter, removed = remove_letter(text)
    words = with_out_classify(pure_letter)  # list included split by space include "/"
    pure_word = "".join(words).split("/")  # split by spaces
    pure_word.pop(-1)  # remove unnecessary parts
    main = AudioSegment.empty()
    for word in pure_word:  # for each word in  text word
        if "," in word:  # if word have comma
            if word == ",":  # if word have only comma without any word
                pass
            final_word = False
            dot = False
            comma_split = word.split(",")
            if comma_split[-1] == "":
                comma_split.pop(-1)
            if comma_split[0] == "":
                comma_split.pop(0)
            if word[0] == ",":
                main += AudioSegment.silent(60)
            print(comma_split)
            for comma_words in comma_split:
                mini = AudioSegment.empty()
                divided_word = divide(comma_words)
                if comma_split[-1] == comma_words:
                    final_word = True
                if "." in comma_words:  # if dot in comma word
                    dot = True
                for each_word in divided_word:  
                    if len(each_word) == 1:
                        each_classified = classify(each_word)
                        for folder_name, file_name in each_classified:
                            mini += AudioSegment.from_file(f"voice/{voice}/oneletter/{folder_name}/{file_name}.mp3")
                    if len(each_word) > 1:
                        each_classified = two_classify(each_word)
                        for folder_name, file_name in each_classified:
                            try:
                                mini += AudioSegment.from_file(f"voice/{voice}/mtone/{folder_name}/{file_name}.mp3")
                            except FileNotFoundError:
                                each_classified = classify(each_word)
                                for fn, fin in each_classified:
                                    mini += AudioSegment.from_file(f"voice/{voice}/oneletter/{fn}/{fin}.mp3")
                                break
                if dot:
                    mini += AudioSegment.silent(80)
                elif final_word and word[-1] != ",":
                    pass
                else:
                    mini += AudioSegment.silent(50)
                main += mini
        elif "." in word:
            if "." in word:
                if word == ".":
                    pass
                final_word = False
                comma_split = word.split(".")
                if comma_split[-1] == "":
                    comma_split.pop(-1)
                if comma_split[0] == "":
                    comma_split.pop(0)
                if word[0] == ".":
                    main += "i"
                print(comma_split)
                for comma_words in comma_split:
                    mini = AudioSegment.empty()
                    divided_word = divide(comma_words)
                    if comma_split[-1] == comma_words:
                        final_word = True
                    for each_word in divided_word:
                        if len(each_word) == 1:
                            each_classified = classify(each_word)
                            for folder_name, file_name in each_classified:
                                mini += AudioSegment.from_file(f"voice/{voice}/oneletter/{folder_name}/{file_name}.mp3")
                        if len(each_word) > 1:
                            each_classified = two_classify(each_word)
                            for folder_name, file_name in each_classified:
                                print(folder_name,file_name)
                                try:
                                    mini += AudioSegment.from_file(f"voice/{voice}/mtone/{folder_name}/{file_name}.mp3")
                                except FileNotFoundError:
                                    each_classified = classify(each_word)
                                    for fn, fin in each_classified:
                                        mini += AudioSegment.from_file(f"voice/{voice}/oneletter/{fn}/{fin}.mp3")
                                    break
                    if final_word and word[-1] != ".":
                        pass
                    else:
                        mini += AudioSegment.silent(120)
                    main += mini

        else:
            mini = AudioSegment.empty()
            divided_word = divide(word)
            for each_word in divided_word:
                if len(each_word) == 1:
                    each_classified = classify(each_word)
                    for folder_name, file_name in each_classified:
                        mini += AudioSegment.from_file(f"voice/{voice}/oneletter/{folder_name}/{file_name}.mp3")
                if len(each_word) > 1:
                    each_classified = two_classify(each_word)
                    for folder_name, file_name in each_classified:
                        try:
                            mini += AudioSegment.from_file(f"voice/{voice}/mtone/{folder_name}/{file_name}.mp3")
                        except FileNotFoundError:
                            each_classified = classify(each_word)
                            for fn, fin in each_classified:
                                mini += AudioSegment.from_file(f"voice/{voice}/oneletter/{fn}/{fin}.mp3")
                            break

            mini += AudioSegment.silent(30)
            main += mini
    main.export("result.mp3", format="mp3")


tts("ሰላም", "svoice")
