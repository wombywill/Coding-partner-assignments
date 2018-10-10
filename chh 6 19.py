def print_menu(usrStr):
    menuOp = ' '
    print("MENU")
    print("c - Number of non-whitespace characters")
    print("w - Number of words")
    print("f - Fix capitalization")
    print("r - Replace punctuation")
    print("s - Shorten spaces")
    print("q - Quit")
    print("")
    menuOp = input("Choose an option:")
    print('')

    if menuOp == 'c':

      num = get_num_of_non_WS_characters(usrStr)

      print("Number of non-whitespace characters:",num)

    elif menuOp == 'w':

      num = get_num_of_words(usrStr)

      print('Number of words:',num)

    elif menuOp == 'f':

      num, result = fix_capitilization(usrStr)

      print('Number of letters capitalized:',num)

      print('Edited text:',result)

    elif menuOp == 'r':

      modified = replace_punctuation(usrStr)

      print( 'Edited text:',modified)

    elif menuOp == 's':

      modified = shorten_space(usrStr)

      print( 'Edited text:',modified)

    return menuOp, usrStr


def get_num_of_non_WS_characters(usrStr):

    num_of_non_WS_characters = 0

    for i in usrStr:

        if i not in ' ':

            num_of_non_WS_characters = num_of_non_WS_characters + 1

    return num_of_non_WS_characters


def get_num_of_words(usrStr):

    return len(usrStr.split())



def fix_capitilization(usrStr):

    number_Capitalized = 0

    sentences = usrStr.split('.')

    for number in range(len(sentences ) ):

        sentence = sentences[number]

        if len( sentence ) > 0:

            for index in range(len(sentence) ):

                if not sentence[index].isspace():

                    if not sentence[index].isupper():

                        sentences[number] = sentence[:index] + sentence[index].upper() + sentence[index + 1:]

                        number_Capitalized += 1

                    break

    capitalizedString = ".".join(sentences)

    return numberOfSentencesCapitalized, capitalizedString



def replace_punctuation(usrStr, exclamationCount=0, semicolonCount=0):

    for i in range(len(usrStr)):

        if usrStr[i] == '!':

         usrStr = usrStr[0:i]+'.'+usrStr[i+1:len(usrStr)]

         exclamationCount +=1

    if usrStr[i] == ';':

      usrStr = usrStr[0:i]+','+usrStr[i+1:len(usrStr)]

      semicolonCount+=1

    print("Punctuation repalced")

    print("exclamationCount:",exclamationCount)

    print("semicolonCount:",semicolonCount)

    return usrStr



def shorten_space(usrStr):

    result = ""

    newstring = usrStr.split(" ")

    for ch in newstring:

        if len(ch)>0:

            result = result+ch+" "

    return result


if __name__ == "__main__":

   usrStr = input('Enter a sample text:\n\n')


print('You entered: %s\n' % usrStr)
print_menu(usrStr)
