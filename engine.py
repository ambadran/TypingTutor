import random
from random_words import *

paragraph_list_shown = []
paragraph = []
paragraph_list = []
paragraph_dict = {}
words_in_line = 0
lines = 0

def generate_paragraph(mode, complexity_level=0):
    global paragraph_list_shown
    global paragraph
    global paragraph_list
    global paragraph_dict
    global words_in_line
    global lines

    if mode == 'random':

        def generateWord():
            if complexity_level == 0:
                alphapet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                letter_list = random.choices(alphapet, k=random.randint(3, 6))
            elif complexity_level == 1:
                alphapet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
                letter_list = random.choices(alphapet,
                                             weights=[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                                                      3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], k=random.randint(3, 6))
            elif complexity_level == 2:
                alphapet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
                            '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+']
                letter_list = random.choices(alphapet,
                                             weights=[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                                                      5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                                      1, 1, 1, 1, 1, 1], k=random.randint(3, 6))
            word = "".join(letter_list)
            return word

        paragraph_list_shown = []
        x = 0

        words_in_line = 5
        lines = 5

        for i in range(lines):
            if x == 1:
                paragraph_list_shown.append("\n")  ### remove the \n because it makes me must type it in typing program
            for i in range(words_in_line):
                paragraph_list_shown.append("".join(generateWord()))
                x = 1

        paragraph = " ".join(paragraph_list_shown)

        paragraph_list = []

        for i in paragraph_list_shown:
            if i != "\n":
                paragraph_list.append(i)

        paragraph_dict = {}

        for i in paragraph_list:
            paragraph_dict[i] = True

    elif mode == 'normal':
        if complexity_level == 0:
            random_words = alphabetical_words

            paragraph_list_shown = []
            x = 0

            words_in_line = 5
            lines = 5

            for i in range(lines):
                if x == 1:
                    paragraph_list_shown.append("\n")  ### remove the \n because it makes me must type it in typing program
                for i in range(words_in_line):
                    paragraph_list_shown.append(random.choice(random_words))
                    x = 1

            paragraph = " ".join(paragraph_list_shown)

            paragraph_list = []

            for i in paragraph_list_shown:
                if i != "\n":
                    paragraph_list.append(i)

            paragraph_dict = {}

            for i in paragraph_list:
                paragraph_dict[i] = True

    elif mode == 'symbols':
        pass

if __name__ == '__main__':
    generate_paragraph('random')
    print(f"paragraph : {paragraph}\n")
    print(f"paragraph list : {paragraph_list}\n")
    print(f"paragraph list shown : {paragraph_list_shown}\n")
    print(f"paragraph dictionary : {paragraph_dict}\n")
