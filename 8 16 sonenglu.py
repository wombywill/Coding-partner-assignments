#need a list
weight_list= []

#enter weights/print list
for i in range(4):
   val = float(input("Enter weight " + str(i+1) + ": "))
   weight_list.append(val)
print("Weights:", weight_list)

#calculate total/average and print
total = 0.0
for i in range(len(weight_list)):
   total = total + weight_list[i]

average = total / len(weight_list);
print("Average weight:", average)

#find da maximum and print
maximum = weight_list[0]
for i in range(len(weight_list)):
   if weight_list[i] > maximum:
      maximum = weight_list[i]
print("Max Weight:", maximum)

#pick a number and convert
index = int(input("Enter a list index location (1 - 4): "))

if index < 1 or index > 4:
   print("Invalid index!")
else:
   print("Weight in pounds:", weight_list[index-1])
   print("Weight in kilograms:", (weight_list[index-1]/2.2))

#sort light to heavy
for i in range(len(weight_list)):
   minPos = i   
   for j in range(i + 1, len(weight_list)):
      if weight_list[j] < weight_list[minPos]:
         minPos = j

   if i != minPos:
      x = weight_list[i]
      weight_list[i] = weight_list[minPos]
      weight_list[minPos] = x
  
print("Sorted list:", weight_list)
