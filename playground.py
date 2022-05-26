teststring = ["I", "have", "completely", "forgotten", "the", "symbolic", "assface", "mayhem", "tester3535", "howmuch",
              "apitester", "randomword", "Randomquote", "whereisthebeer", "finally", "enoughtext", "line5", "epaper",
              "display", "tester88", "letssee"]


def ass():
    target_string = ""
    chunk_start = 30
    max_lines_of_text = 5

    for i in teststring:
        if max_lines_of_text == 0:
            target_string += "..."
            break
        if len(target_string) + len(i) > chunk_start:
            target_string += "\n "
            target_string += "{} ".format(i)
            chunk_start += 30
            max_lines_of_text -= 1
        else:
            target_string += "{} ".format(i)
    return target_string

print(ass())