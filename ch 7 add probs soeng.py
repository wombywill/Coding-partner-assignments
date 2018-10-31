#5. Alphabetic Telephone Number Translator
print ('Alphabetic Telephone Numeric Translator:')
print ('-----------------------------------------')
print ('')
def main():
    phone_number = input("Enter a 10 number format as XXX-XXX-XXXX: ")
    parse_number(phone_number)

def parse_number(phone_number):

    new_number = ''
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for digits in phone_number:
        if not digits.isdigit():

            if digits in alphabet[0:3]:
                digits = '2'

            elif digits in alphabet[3:6]:
                digits = '3'
        
            elif digits in alphabet[6:9]:
                digits = '4'
        
            elif digits in alphabet[9:12]:
                digits = '5'
        
            elif digits in alphabet[12:15]:
                digits = '6'
        
            elif digits in alphabet[15:19]:
                digits = '7'

            elif digits in alphabet[19:21]:
                digits = '8'
        
            elif digits in alphabet[21:26]:
                digits = '9'
        
            new_number += digits
        else:
            new_number += digits
    
    print(new_number)
    
main()

#9. Vowels and Consonants
print ('')
print ('Vowels and Consonants:')
print ('---------------------')
print ('')
string = input("Enter a phrase:")
vowels = 0
for i in string:
      if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
string = string.replace(' ','')
string = string.replace('.','')
length = 0
for char in string:
    length += 1
consanants = length - vowels
print("Number of vowels are:")
print(vowels)
print("Number of Consanants are:")
print(consanants)

#12. Pig Latin
print ('')
print ('Pig Latin OR Igpay Atinlay:')
print ('----------------------------')
print ('')
def main():
        
        sentence = input('What would you like to say in Pig Latin?: ')
        sentence = sentence.split()
        for k in range(len(sentence)):
                i = sentence[k]
                if i[0] in ['a', 'e', 'i', 'o', 'u']:
                        sentence[k] = i+'ay'
                elif i.isalpha() == False:
                        sentence[k] = i
                else:
                        sentence[k] = i[1:] + i[0]+'ay'
        return ' '.join(sentence)

def t(str):
        return str[0]+str[1]

if __name__ == "__main__":
        x = main()
        print(x)


#1. Initials
print ('')
print ('Initials:')
print ('---------')
print ('')
names = input('Enter your first, middle, and last name:\n')
names = names.replace(' ','')
names = names.split(',')

name1 = names[0]
name2 = names[1]
name3 = names[2]

initials = []
initials.append(name1[0])
initials.append(name2[0])
initials.append(name3[0])
print('.'.join(initials))
