team={}

newteam={}

i=1

count=1


#input data
while count <= 5:

   jersey = int(input("Enter player %d's jersey number:\n" % count)) #jersey number

   rating = int(input("Enter player %d's rating:\n" % count)) #player rating

   team[jersey] = rating #create a dict

   roster = list(team.keys()) #make a list

   roster = sorted(roster) #Sort the new "list"

   count += 1

   print()#Print empty line

print("ROSTER")

for i in roster:

   print("Jersey number: %d, Rating: %d" % (i, team[i]))

while True:

   roster = list(team.keys()) #Turn dictionary keys into list

   roster = sorted(roster) #Sort the new "list"

   print()

   print("MENU") #Print menu

   print("a - Add player")

   print("d - Remove player")

   print("u - Update player rating")

   print("r - Output players above a rating")

   print("o - Output roster")

   print("q - Quit")

   option = input("\nChoose an option:\n")

   if option == "q": #If user enters "q"

      exit()

   elif option == "o": #If user enters "o"

      print()

      print("ROSTER")

      for i in roster:

         print("Jersey number: %d, Rating: %d" % (i, team[i]))

   elif option == "a": #If user enters "a"

      jersey2 = int(input("Enter a new player's jersey number:\n"))

      rating2 = int(input("Enter the player's rating:"))

      newteam[jersey2] = rating2

      team.update(newteam)

   elif option == "d": #If user enters "d"

      jerseyremove = int(input("Enter a jersey number:\n"))

      team.pop(jerseyremove)

   elif option == "u": #If user enters "u"

      jerseyupdate = int(input("Enter a jersey number:\n"))

      rateupdate = int(input("Enter a new rating for player:\n"))

      team[jerseyupdate] = rateupdate

   elif option == "r": #If user enters "r"

      rateabove = int(input("Enter a rating:\n"))

      print()

      print("ABOVE %d" % rateabove)

      for jersey, rating in team.items():

         if rating > rateabove:

            print("Jersey number: %d, Rating: %d" % (jersey, rating))

         if rating <= rateabove:

            continue

#enter q to quit when finished
