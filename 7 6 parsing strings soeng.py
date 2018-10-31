while True:

   input_string = input("Enter input string:")

   if input_string == "q" or input_string == "Q":      

       break

   input_as_bool="true"

   while(input_as_bool!="false"):

     if "," not in input_string:    

        input_as_bool="true"      

        print ("Error: No comma in string.\n")

        input_string = input("Enter input string:")

     if input_string == "q":              

                 exit(0)
     else:

      input_as_bool = "false"

   s_input = input_string.split(",")

   print ("First word:",s_input[0].strip())

   print ("Second word:",s_input[1].strip())

   print ("\n")
