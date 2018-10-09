def get_num_of_characters(inputStr):
    count=0
    for letter in inputStr: #prob specfically says u use a for loop
        count+=1
    return count
def output_without_whitespace(inputStr):
    output="";
    for letter in inputStr: #prob specfically says u use a for loop
        if letter!=" " and letter!="\t":
            output+=letter
    return output;
if __name__ == '__main__':
    inputStr=input("Enter a sentence or phrase:")
    print('') #needed for zybooks, i find this format works better
    print('') #needed for zybooks, than embedding the newlines, no idea y
    print("You entered:",inputStr)
    
    noOfChars=get_num_of_characters(inputStr);
    print("\nNumber of characters:",noOfChars)
    
    stringWithoutSpace=output_without_whitespace(inputStr);
    print("String with no whitespace:",stringWithoutSpace)
