from lib.multiplesizes import *
from lib.single import *
class youthsizes:

    def enumerateyouth():
        print("\n" + "_YOUTH SIZES_" + "\n")
        print("Following sizes are accepted: " + "\n" + "S->XL")
        smalsize = str(input("What is the smallest size in your stack?: "))
        larsize = str(input("What is the largest size in your stack?: "))
        
        if smalsize.lower() == larsize.lower():
            print("// Performing same size enumeration...")
            size = smalsize.upper()
            count = int(input(size + " (amt): "))
            single.singlesize(size, count)
        elif smalsize.lower() == str("xs"): #XSMALL is out of bounds.
            yn = str(input("// S is the smallest size available for youth," + "\n" + "// (LARGEST SIZE IS LIMITED TO 5XL)" + "\n" +  "would you like to enumerate still?: "))
        
            if yn.lower() == str("y") or yn.lower() == str("yes"): #Enumerate as normal
                    multiplesizes.multiple(smalsize,larsize) 
            elif yn.lower() == str("n") or yn.lower() == str("no"): #Input a new small size
                    newsmalsize = str(input("Please enter a new small size: "))
                    smalsize = newsmalsize
                    newlarsize = str(input("Please enter a new large size: "))
                    larsize = newlarsize
                    multiplesizes.multiple(smalsize,larsize)
            else: #assume yes
                    print("// Invalid Input, assuming 'yes'.")
                    multiplesizes.multiple(smalsize, larsize) #Enumerate

        elif smalsize.lower() == str("xl") or larsize.lower() == str("2xl") or larsize.lower() == str("xxl") or larsize.lower() == str("3xl") or larsize.lower() == str("xxxl") or larsize.lower() == str("4xl") or larsize.lower() == str("xxxxl") or larsize.lower() == str("5xl") or larsize.lower() == str("xxxxxl"):
            yn = str(input("// XL is the largest size available for youth," + "\n" + "// (LARGEST SIZE IS LIMITED TO 5XL)" + "\n" + "would you like to enumerate still?: "))
            if yn.lower() == str("y") or yn.lower() == str("yes"): #Enumerate as normal
                multiplesizes.multiple(smalsize,larsize) 
            elif yn.lower() == str("n") or yn.lower() == str("no"): #Input a new large size
                newsmalsize = str(input("Please enter a new small size: "))
                smalsize = newsmalsize
                newlarsize = str(input("Please enter a new large size: "))
                larsize = newlarsize
                multiplesizes.multiple(smalsize,larsize)
            else: #assume yes
                print("// Invalid Input, assuming 'yes'.")
                multiplesizes.multiple(smalsize, larsize) #Enumerate
#    def enumerateinfant:
#        print
#    def enumeratetoddler:
#        print

    
