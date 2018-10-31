def checkCommas(dataPoint):
     
     if ',' not in dataPoint:
          
          print('Error: No comma in string.')
          return False
     
     elif dataPoint.count(",") > 1:
         
          print('Error: Too many commas in input.')
          return False
     
     else:
          
          index = dataPoint.find(",")
          
          name = dataPoint.split(",")[0]
          integer = (dataPoint.split(",")[1]).strip()
          
          if not (integer.isdigit()):
               
               print('Error: Comma not followed by an integer.')
               return False
          else:
               return True


def table(title, header1, header2, nameList, numberList):
     
     print("\n\n %33s \n" %(title))
     
     print("\n %-20s %-10s %-23s \n" %(header1, "|", header2))
     print("----------------------------------------------------")
     
     for i in range(0, len( nameList)):
          print("%-20s %-10s %-23d " %(nameList[i], "|", numberList[i]))
     print("\n")


def histogram( nameList, numberList):
     
     for i in range(0, len( nameList)):
          print("\n %20s %-5s " %( nameList[i], " "), end = "")
          for j in range(0, numberList[i]):
               print("*", end="")
     print("\n")


def main():
     nameList = []   
     numberList = []   

     
     title = input('Enter a title for the data:\n')
     print("You entered: " + title)

     
     header1 = input('\nEnter the column 1 header:\n')
     print("You entered: " + header1)

     
     header2 = input('\nEnter the column 2 header:\n')
     print("You entered: " + header2)

     
     dataPoint = input("\nEnter a data point (-1 to stop input):\n")
     while dataPoint != "-1":
          
          commas = checkCommas(dataPoint)
          
          if commas:
               name = dataPoint.split(",")[0]
               integer = int((dataPoint.split(",")[1]).strip())
               
               print("Data string: " + name)
               print("Data integer: " + str(integer))
               
               nameList.append(name)
               numberList.append(integer)
          
          dataPoint = input("\nEnter a data point (-1 to stop input):\n")

     
     table(title, header1, header2, nameList, numberList)
      
     
     histogram(nameList, numberList)


main()
