#Accurate Shirt Stacker (Method Printing)

 # Libraries
from lib.multiplesizes import *
from lib.youthsizes import *
from lib.single import *
#########################################################################

def main():  #Main function
    def multifunction():
        print("Following inputs are accepted:" + "\n" + "XS->5XL")
        smalsize = str(input("What is the smallest size in your stack?: ")) #Smallest Size
        larsize = str(input("What is the largest size in your stack?: ")) #Largest Size
        multiplesizes.multiple(smalsize,larsize)
    def singlefunction():
        print("\n"+"_SINGLE SIZE_"+"\n")
        print("ALL INPUTS ARE ACCEPTED" + "\n")
        size = str(input("What size are you enumerating?: "))
        count = int(input("How many " + size.upper() + "'s are you counting in?: " ))
        single.singlesize(size, count)
    ##################################################################
    multi = str(input("Are there multiple sizes? [y/n]: ")) #Program Begins


    #Multiple Size Enumeration

    if multi.lower() == str("yes") or multi.lower() == str("y"): 
        youth = str(input("Are there youth shirts? [y/n]: ")) #Checks if user has youth shirts
        if youth.lower() == str("yes") or youth.lower() == str("y"):
            youthsizes.enumerateyouth()
            print("=============")
            print("\n" + "_ADULT SIZES_" + "\n")
            multifunction()
        elif youth.lower() == str("no") or youth.lower() == str("n"):
            multifunction()
        else: #If the input has no valid inputs, assume no.
            print("// Invalid Input, assuming 'no'.")
            multifunction()
    
    #Single Size Enumeration

    elif multi.lower() == str("no") or multi.lower() == str("n"): 
        print("// Performing Single Size Enumeration.")
        singlefunction()
    else: #Assume no
        print ("// Invalid input, assuming 'no'.")
        singlefunction()
    print("// Enumeration Finished.")
# Loop

while (True):
    def loopbreaker(returnval):
        ask = str(input("Would you like to repeat the script? [y/n]: "))
        if ask.lower() == str("y") or ask.lower() == str("yes"):
            print("\n" + "// Repeating Script...")
            return True
        elif ask.lower() == str("n") or ask.lower() == str("no"):
            print("// Exiting script...")
            return False
        else:
            print("// Invalid input, assuming 'yes'.")
            return True
    main()
    returnval=1
    z=loopbreaker(returnval)
    if z == False:
        break
    elif z == True:
        continue



