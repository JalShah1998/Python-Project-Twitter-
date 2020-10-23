def strip_punctuation(str_word):
    new_str = ""
    for char in str_word:
        if char in punctuation_chars:
            print("")
        else:
            new_str = new_str + char
    return new_str


def get_pos(sentence):
    count = 0
    str1 = sentence.lower()

    for string in str1.split(" "):
        if strip_punctuation(string) in positive_words:
            count += 1

    return count


def get_neg(sentence):
    count = 0
    str_l = sentence.lower()
    for string in str_l.split(" "):
        if strip_punctuation(string) in negative_words:
            count += 1

    return count


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

fileref = open("project_twitter_data.csv", "r")
filecsv = open("resulting_data.csv", "w")


def writeInDataFile(filecsv):
    filecsv.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    filecsv.write("\n")

    linesPTDF = fileref.readlines()
    headerDontUsed = linesPTDF.pop(0)
    for linesTD in linesPTDF:
        listTD = linesTD.strip().split(',')
        filecsv.write(
            "{}, {}, {}, {}, {}".format(listTD[1], listTD[2], get_pos(listTD[0]), get_neg(listTD[0]),
                                        (get_pos(listTD[0]) - get_neg(listTD[0]))))
        filecsv.write("\n")


writeInDataFile(filecsv)
fileref.close()
filecsv.close()