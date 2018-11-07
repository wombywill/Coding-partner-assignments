#Chapter 8 Additional Excercises
#1
print('Total Rainfall')
print('')
#input rainfall totals, make a list
#use float because might want decimals
year=[]
jan=float(input('Please enter January rainfall: \n'))
feb=float(input('Please enter February rainfall: \n'))
mar=float(input('Please enter March rainfall: \n'))
apr=float(input('Please enter April rainfall: \n'))
may=float(input('Please enter May rainfall: \n'))
jun=float(input('Please enter June rainfall: \n'))
jul=float(input('Please enter July rainfall: \n'))
aug=float(input('Please enter August rainfall: \n'))
sep=float(input('Please enter September rainfall: \n'))
octo=float(input('Please enter October rainfall: \n'))
nov=float(input('Please enter November rainfall: \n'))
dec=float(input('Please enter December rainfall: \n'))

year.extend((jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec))

#display total, average, low, and high
def total():
    print('The total rainfall was', sum(year))
total()

def average():
    print('The average rainfall was', float(sum(year))/len(year))
average()

def lowest():
    print('The lowest rainfall was', min(year))
lowest()

def highest():
    print('The highest rainfall was', max(year))
highest()



#2
print('')
print('Chapter 8 List Knowledge Display')
print('')


#3
print('')
print('Sentence Encrypt and Decryptor')
print('')
#make a cipher (could this be imported somehow?), made my own
enigma={'A' : '@', 'a' : '&', 'B': '%', 'b': '6', 'C' : '0', 'c' : '^', 'D' : '-', 'd' : '$',
        'E' : '3', 'e' : '4', 'F' : '*', 'f' : '#', 'G' : '~', 'g' : '9', 'H' : '5', 'h' : '7',
        'I' : '1', 'i' : '!', 'J' : '8', 'j' : '=', 'K' : '`', 'k' : '+', 'L' : '?', 'l' : '[',
        'M' : '>', 'm' : '<', 'N' : '♯', 'n' : '♫', 'O' : '♻', 'o' : '⚀', 'P' : '¶', 'p' : '⬠',
        'Q' : '⍺', 'q' : 'ᵹ', 'R' : '®', 'r' : '√', 'S' : 'ᵴ', 's' : '§', 'T' : '™', 't' : 'π',
        'U' : 'ú', 'u' : 'Ü', 'V' : '▼', 'v' : '▿', 'W' : 'Ϣ', 'w' : 'Ɯ', 'X' : '⊠', 'x' : '✖',
        'Y' : 'Ⓨ', 'y' : '¥', 'Z' : 'Ž', 'z' : '※'}
#need to input a sentence, encrypt, then decrypt
#would be more elegant with a menu?
while True:
   print('Menu')
   print('e - Encrypt a Sentence')
   print('d - Decrypt a Sentence')
   print('q - Quit')

   option = input('\n Choose an option: \n')
   
   if option == 'q':
       exit()

   elif option == 'e':
       print()
       print('Enter a sentence to encrypt: \n')
       #need function to encrypt
          print(#print)

   elif option == 'd':
       print()
       print('Enter a sentence to decrypt: \n')
       #need function to decrypt
          print(#result)



#4
print('')
print('Chapter 8 Dictionary Knowledge Display')
print('')
