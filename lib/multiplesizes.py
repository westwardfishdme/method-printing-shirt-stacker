#Multiple Sizes
#Enumerate Multiple sizes.
from lib.single import *
class multiplesizes:
    def multiple(smalsize,larsize): # Check user input if there are multiple stacks to be counted in
            #XS sizes
        def xsmall(larsize):
            if larsize.lower() == str("5xl") or larsize.lower() == str("xxxxxl"):
                #Input Sizes
                xs = int(input("XS (amt): "))
                s = int(input("S (amt): "))
                m = int(input("M (amt): "))
                l = int(input("L (amt): "))
                xl = int(input("XL (amt): "))
                xxl = int(input("2XL (amt): "))
                txl = int(input("3XL (amt): "))
                ivxl = int(input("4XL (amt): "))
                vxl = int(input("5XL (amt): "))
                
                #Output stacks ()
                print("==================" +"\n")
                print("\n" + "_XS_" + "\n" + str(int(xs/12)) + " total stacks of (12)" + "\n" + "Remainder stack size: " + str(int(xs%12)) +"\n")
                print("_S_" + "\n" + str(int(s/12)) + " total stacks of (12)" + "\n" + "Remainder stack size: " + str(int(s%12)) +"\n")
                print("_M_" + "\n" + str(int(m/12)) + " total stacks of (12)" + "\n" + "Remainder stack size: " + str(int(m%12)) +"\n")
                print("_L_" + "\n" + str(int(l/12)) + " total stacks of (12)" + "\n" + "Remainder stack size: " + str(int(l%12)) +"\n")
                print("_XL_" + "\n" + str(int(xl/12)) + " total stacks of (12)" + "\n" + "Remainder stack size: " + str(int(xl%12)) +"\n") 
                print("_2XL_" + "\n" + str(int(xxl/12)) + " total stacks of (12)" + "\n" + "Remainder stack size: " + str(int(xxl%12)) +"\n")
                print("_3XL_" + "\n" + str(int(txl/12)) + " total stacks of (12)" + "\n" + "Remainder stack size: " + str(int(txl%12)) +"\n")
                print("_4XL_" + "\n" + str(int(ivxl/12)) + " total stacks of (12)" + "\n" + "Remainder stack size: " + str(int(ivxl%12)) +"\n")
                print("_5XL_" + "\n" + str(int(vxl/12)) + " total stacks of (12)" + "\n" + "Remainder stack size: " + str(int(vxl%12)) +"\n")

        #XS-4XL
            elif larsize.lower() == str("4xl") or larsize.lower() == str("xxxxl"):
                #Input Sizes
                xs = int(input("XS (amt): "))
                s = int(input("S (amt): "))
                m = int(input("M (amt): "))
                l = int(input("L (amt): "))
                xl = int(input("XL (amt): "))
                xxl = int(input("2XL (amt): "))
                txl = int(input("3XL (amt): "))
                ivxl = int(input("4XL (amt): "))

                #Output stacks ()
                print("==================" +"\n")
                print("\n" + "_XS_" + "\n" + str(int(xs/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xs%12)) +"\n")
                print("_S_" + "\n" + str(int(s/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(s%12)) +"\n")
                print("_M_" + "\n" + " total stacks of (12) " + str(int(m/12)) + "\n" + "Remainder stack size: " + str(int(m%12)) +"\n")
                print("_L_" + "\n" + str(int(l/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(l%12)) +"\n")
                print("_XL_" + "\n" + str(int(xl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xl%12)) +"\n")
                print("_2XL_" + "\n" + str(int(xxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xxl%12)) +"\n")
                print("_3XL_" + "\n" + str(int(txl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(txl%12)) +"\n")
                print("_4XL_" + "\n" + str(int(ivxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(ivxl%12)) +"\n")

        #XS-3XL
            elif larsize.lower() == str("3xl") or larsize.lower() == str("xxxl"):
                #Input Sizes
                xs = int(input("XS (amt): "))
                s = int(input("S (amt): "))
                m = int(input("M (amt): "))
                l = int(input("L (amt): "))
                xl = int(input("XL (amt): "))
                xxl = int(input("2XL (amt): "))
                txl = int(input("3XL (amt): "))

                #Output stacks ()
                print("==================" +"\n")
                print("\n" + "_XS_" + "\n" + str(int(xs/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xs%12)) +"\n")
                print("_S_" + "\n" + str(int(s/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(s%12)) +"\n")
                print("_M_" + "\n" + str(int(m/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(m%12)) +"\n")
                print("_L_" + "\n" + str(int(l/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(l%12)) +"\n")
                print("_XL_" + "\n" + str(int(xl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xl%12)) +"\n")
                print("_2XL_" + "\n" + str(int(xxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xxl%12)) +"\n")
                print("_3XL_" + "\n" + str(int(txl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(txl%12)) +"\n")

        #XS-2XL
            elif larsize.lower() == str("2xl") or larsize.lower() == str("xxl"):
                #Input Sizes
                xs = int(input("XS (amt): "))
                s = int(input("S (amt): "))
                m = int(input("M (amt): "))
                l = int(input("L (amt): "))
                xl = int(input("XL (amt): "))
                xxl = int(input("2XL (amt): "))
                            
                #Output stacks ()
                print("==================" +"\n")
                print("\n" + "_XS_" + "\n" + str(int(xs/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xs%12)) +"\n")
                print("_S_" + "\n" + str(int(s/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(s%12)) +"\n")
                print("_M_" + "\n" + str(int(m/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(m%12)) +"\n")
                print("_L_" + "\n" + str(int(l/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(l%12)) +"\n")
                print("_XL_" + "\n" + str(int(xl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xl%12)) +"\n")
                print("_2XL_" + "\n" + str(int(xxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xxl%12)) +"\n")

        #XS-XL
            elif larsize.lower() == str("xl"):   
                #Input Sizes
                xs = int(input("XS (amt): "))
                s = int(input("S (amt): "))
                m = int(input("M (amt): "))
                l = int(input("L (amt): "))
                xl = int(input("XL (amt): "))
                   
                #Output stacks ()
                print("==================" +"\n")
                print("\n" + "_XS_" + "\n" + str(int(xs/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xs%12)) +"\n")
                print("_S_" + "\n" + str(int(s/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(s%12)) +"\n")
                print("_M_" + "\n" + str(int(m/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(m%12)) +"\n")
                print("_L_" + "\n" + str(int(l/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(l%12)) +"\n")
                print("_XL_" + "\n" + str(int(xl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xl%12)) +"\n")

        #XS-L
            elif larsize.lower() == str("l"):
                #Input Sizes
                xs = int(input("XS (amt): "))
                s = int(input("S (amt): "))
                m = int(input("M (amt): "))
                l = int(input("L (amt): "))
                  
                #Output stacks ()
                print("==================" +"\n")
                print("\n" + "_XS_" + "\n" + str(int(xs/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xs%12)) +"\n")
                print("_S_" + "\n" + str(int(s/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(s%12)) +"\n")
                print("_M_" + "\n" + str(int(m/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(m%12)) +"\n")
                print("_L_" + "\n" + str(int(l/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(l%12)) +"\n")

        #XS-M
            elif larsize.lower() == str("m"):
                #Input Sizes
                xs = int(input("XS (amt): "))
                s = int(input("S (amt): "))
                m = int(input("M (amt): "))
                            
                #Output stacks ()
                print("==================" +"\n")
                print("\n" + "_XS_" + "\n" + str(int(xs/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xs%12)) +"\n")
                print("_S_" + "\n" + str(int(s/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(s%12)) +"\n")
                print("_M_" + "\n" + str(int(m/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(m%12)) +"\n")

        #XS-S
            elif larsize.lower() == str("s") :
                #Input Sizes
                xs = int(input("XS (amt): "))
                s = int(input("S (amt): "))

                #Output stacks ()
                print("==================" +"\n")
                print("\n" + "_XS_" + "\n" + str(int(xs/12)) + " total XS stacks of (12) " +  "\n" + "Remainder XS stack size: " + str(int(xs%12)) +"\n")
                print("_S_" + "\n" + str(int(xs/12)) + " total XS stacks of (12) " +  "\n" + "Remainder XS stack size: " + str(int(xs%12)) +"\n")

            else:
                print("// Invalid input for largest size")
        #########################################################################

        #SMALL SIZES 
        def small(larsize):


        #S-5XL
            if larsize.lower() == str("5xl") or larsize.lower() == str("xxxxxl"):
                #Input Sizes
                s = int(input("S (amt): "))
                m = int(input("M (amt): "))
                l = int(input("L (amt): "))
                xl = int(input("XL (amt): "))
                xxl = int(input("2XL (amt): "))
                txl = int(input("3XL (amt): "))
                ivxl = int(input("4XL (amt): "))
                vxl = int(input("5XL (amt): "))
                
                #Output stacks ()
                print("==================" +"\n")
                print("\n" + "_S_" + "\n" + str(int(s/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(s%12)) +"\n")
                print("_M_" + "\n" + str(int(m/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(m%12)) +"\n")
                print("_L_" + "\n" + str(int(l/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(l%12)) +"\n")
                print("_XL_" + "\n" + str(int(xl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xl%12)) +"\n")
                print("_2XL_" + "\n" + str(int(xxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xxl%12)) +"\n")
                print("_3XL_" + "\n" + str(int(txl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(txl%12)) +"\n")
                print("_4XL_" + "\n" + str(int(ivxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(ivxl%12)) +"\n")
                print("_5XL_" + "\n" + str(int(vxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(vxl%12)) +"\n")

        #S-4XL
            elif larsize.lower() == str("4xl") or larsize.lower() == str("xxxxl"):
                #Input Sizes
                s = int(input("S (amt): "))
                m = int(input("M (amt): "))
                l = int(input("L (amt): "))
                xl = int(input("XL (amt): "))
                xxl = int(input("2XL (amt): "))
                txl = int(input("3XL (amt): "))
                ivxl = int(input("4XL (amt): "))

                #Output stacks ()
                print("==================" +"\n")
                print("\n" + "_S_" + "\n" + str(int(s/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(s%12)) +"\n")
                print("_M_" + "\n" + str(int(m/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(m%12)) +"\n")
                print("_L_" + "\n" + str(int(l/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(l%12)) +"\n")
                print("_XL_" + "\n" + str(int(xl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xl%12)) +"\n")
                print("_2XL_" + "\n" + str(int(xxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xxl%12)) +"\n")
                print("_3XL_" + "\n" + str(int(txl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(txl%12)) +"\n")
                print("_4XL_" + "\n" + str(int(ivxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(ivxl%12)) +"\n")

        #S-3XL
            elif larsize.lower() == str("3xl") or larsize.lower() == str("xxxl"):
                #Input Sizes        
                s = int(input("S (amt): "))
                m = int(input("M (amt): "))
                l = int(input("L (amt): "))
                xl = int(input("XL (amt): "))
                xxl = int(input("2XL (amt): "))
                txl = int(input("3XL (amt): "))

                #Output stacks ()
                print("==================" +"\n")
                print("\n" + "_S_" + "\n" + str(int(s/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(s%12)) +"\n")
                print("_M_" + "\n" + str(int(m/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(m%12)) +"\n")
                print("_L_" + "\n" + str(int(l/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(l%12)) +"\n")
                print("_XL_" + "\n" + str(int(xl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xl%12)) +"\n")
                print("_2XL_" + "\n" + str(int(xxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xxl%12)) +"\n")
                print("_3XL_" + "\n" + str(int(txl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(txl%12)) +"\n")

        #S-2XL
            elif larsize.lower() == str("2xl") or larsize.lower() == str("xxl"):
                #Input Sizes
                s = int(input("S (amt): "))
                m = int(input("M (amt): "))
                l = int(input("L (amt): "))
                xl = int(input("XL (amt): "))
                xxl = int(input("2XL (amt): "))
                            
                #Output stacks ()
                print("==================" +"\n")
                print("\n" + "_S_" + "\n" + str(int(s/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(s%12)) +"\n")
                print("_M_" + "\n" + str(int(m/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(m%12)) +"\n")
                print("_L_" + "\n" + str(int(l/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(l%12)) +"\n")
                print("_XL_" + "\n" + str(int(xl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xl%12)) +"\n")
                print("_2XL_" + "\n" + str(int(xxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xxl%12)) +"\n")
                
        #S-XL
            elif larsize.lower() == str("xl"):   
                #Input Sizes
                s = int(input("S (amt): "))
                m = int(input("M (amt): "))
                l = int(input("L (amt): "))
                xl = int(input("XL (amt): "))
                   
                #Output stacks () 
                print("==================" +"\n")
                print("\n" + "_S_" + "\n" + str(int(s/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(s%12)) +"\n")
                print("_M_" + "\n" + str(int(m/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(m%12)) +"\n")
                print("_L_" + "\n" + str(int(l/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(l%12)) +"\n")
                print("_XL_" + "\n" + str(int(xl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xl%12)) +"\n")

        #S-L
            elif larsize.lower() == str("l"):
                #Input Sizes
                s = int(input("S (amt): "))
                m = int(input("M (amt): "))
                l = int(input("L (amt): "))
                  
                #Output stacks () 
                print("==================" +"\n")
                print("\n" + "_S_" + "\n" + str(int(s/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(s%12)) +"\n")
                print("_M_" + "\n" + str(int(m/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(m%12)) +"\n")
                print("_L_" + "\n" + str(int(l/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(l%12)) +"\n")

        #S-M
            elif larsize.lower() == str("m"):
                #Input Sizes
                s = int(input("S (amt): "))
                m = int(input("M (amt): "))
                            
                #Output stacks ()
                print("==================" +"\n")
                print("\n" + "_S_" + "\n" + str(int(s/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(s%12)) +"\n")
                print("_M_" + "\n" + str(int(m/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(m%12)) +"\n")
            
        #########################################################################
        #MEDIUM SIZES

        def medium(larsize):

        #M-5XL
            if larsize.lower() == str("5xl") or larsize.lower() == str("xxxxxl"):

                #Input Sizes
                m = int(input("M (amt): "))
                l = int(input("L (amt): "))
                xl = int(input("XL (amt): "))
                xxl = int(input("2XL (amt): "))
                txl = int(input("3XL (amt): "))
                ivxl = int(input("4XL (amt): "))
                vxl = int(input("5XL (amt): "))
                
                #Output stacks ()
                print("==================" +"\n")
                print("\n" + "_M_" + "\n" + str(int(m/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(m%12)) +"\n")
                print("_L_" + "\n" + str(int(l/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(l%12)) +"\n")
                print("_XL_" + "\n" + str(int(xl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xl%12)) +"\n")
                print("_2XL_" + "\n" + str(int(xxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xxl%12)) +"\n")
                print("_3XL_" + "\n" + str(int(txl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(txl%12)) +"\n")
                print("_4XL_" + "\n" + str(int(ivxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(ivxl%12)) +"\n")
                print("_5XL_" + "\n" + str(int(vxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(vxl%12)) +"\n")

        #M-4XL
            elif larsize.lower() == str("4xl") or larsize.lower() == str("xxxxl"):

                #Input Sizes
                m = int(input("M (amt): "))
                l = int(input("L (amt): "))
                xl = int(input("XL (amt): "))
                xxl = int(input("2XL (amt): "))
                txl = int(input("3XL (amt): "))
                ivxl = int(input("4XL (amt): "))

                #Output stacks ()
                print("==================" +"\n")
                print("\n" + "_S_" + "\n" + str(int(s/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(s%12)) +"\n")
                print("_M_" + "\n" + str(int(m/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(m%12)) +"\n")
                print("_L_" + "\n" + str(int(l/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(l%12)) +"\n")
                print("_XL_" + "\n" + str(int(xl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xl%12)) +"\n")
                print("_2XL_" + "\n" + str(int(xxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xxl%12)) +"\n")
                print("_3XL_" + "\n" + str(int(txl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(txl%12)) +"\n")
                print("_4XL_" + "\n" + str(int(ivxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(ivxl%12)) +"\n")

        #M-3XL
            elif larsize.lower() == str("3xl") or larsize.lower() == str("xxxl"):

                #Input Sizes        
                m = int(input("M (amt): "))
                l = int(input("L (amt): "))
                xl = int(input("XL (amt): "))
                xxl = int(input("2XL (amt): "))
                txl = int(input("3XL (amt): "))

                #Output stacks ()
                print("==================" +"\n")
                print("\n" + "_M_" + "\n" + str(int(m/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(m%12)) +"\n")
                print("_L_" + "\n" + str(int(l/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(l%12)) +"\n")
                print("_XL_" + "\n" + str(int(xl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xl%12)) +"\n")
                print("_2XL_" + "\n" + str(int(xxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xxl%12)) +"\n")
                print("_3XL_" + "\n" + str(int(txl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(txl%12)) +"\n")

        #M-2XL
            elif larsize.lower() == str("2xl") or larsize.lower() == str("xxl"):

                #Input Sizes
                m = int(input("M (amt): "))
                l = int(input("L (amt): "))
                xl = int(input("XL (amt): "))
                xxl = int(input("2XL (amt): "))
                            
                #Output stacks ()
                print("==================" +"\n")
                print("\n" + "_M_" + "\n" + str(int(m/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(m%12)) +"\n")
                print("_L_" + "\n" + str(int(l/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(l%12)) +"\n")
                print("_XL_" + "\n" + str(int(xl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xl%12)) +"\n")
                print("_2XL_" + "\n" + str(int(xxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xxl%12)) +"\n")

        #M-XL
            elif larsize.lower() == str("xl"):   
                
                #Input Sizes
                m = int(input("M (amt): "))
                l = int(input("L (amt): "))
                xl = int(input("XL (amt): "))
                   
                #Output stacks () 
                print("==================" +"\n")
                print("\n" + "_M_" + "\n" + str(int(m/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(m%12)) +"\n")
                print("_L_" + "\n" + str(int(l/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(l%12)) +"\n")
                print("_XL_" + "\n" + str(int(xl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xl%12)) +"\n")
                
        #M-L
            elif larsize.lower() == str("l"):

                #Input Sizes
                m = int(input("M (amt): "))
                l = int(input("L (amt): "))
                  
                #Output stacks () 
                print("==================" +"\n")
                print("\n" + "_M_" + "\n" + str(int(m/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(m%12)) +"\n")
                print("_L_" + "\n" + str(int(l/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(l%12)) +"\n")
            
            else:
                print("// Invalid input for largest size")
        #########################################################################

        #LARGE SIZES
        def large(larsize):
        #L-5XL
            if larsize.lower() == str("5xl") or larsize.lower() == str("xxxxxl"):

                #Input Sizes
                l = int(input("L (amt): "))
                xl = int(input("XL (amt): "))
                xxl = int(input("2XL (amt): "))
                txl = int(input("3XL (amt): "))
                ivxl = int(input("4XL (amt): "))
                vxl = int(input("5XL (amt): "))
                
                #Output stacks ()
                print("==================" +"\n")
                print("\n" + "_L_" + "\n" + str(int(l/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(l%12)) +"\n")
                print("_XL_" + "\n" + str(int(xl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xl%12)) +"\n")
                print("_2XL_" + "\n" + str(int(xxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xxl%12)) +"\n")
                print("_3XL_" + "\n" + str(int(txl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(txl%12)) +"\n")
                print("_4XL_" + "\n" + str(int(ivxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(ivxl%12)) +"\n")
                print("_5XL_" + "\n" + str(int(vxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(vxl%12)) +"\n")

        #L-4XL
            elif larsize.lower() == str("4xl") or larsize.lower() == str("xxxxl"):

                #Input Sizes
                l = int(input("L (amt): "))
                xl = int(input("XL (amt): "))
                xxl = int(input("2XL (amt): "))
                txl = int(input("3XL (amt): "))
                ivxl = int(input("4XL (amt): "))

                #Output stacks ()
                print("==================" +"\n")
                print("\n" + "_L_" + "\n" + str(int(l/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(l%12)) +"\n")
                print("_XL_" + "\n" + str(int(xl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xl%12)) +"\n")
                print("_2XL_" + "\n" + str(int(xxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xxl%12)) +"\n")
                print("_3XL_" + "\n" + str(int(txl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(txl%12)) +"\n")
                print("_4XL_" + "\n" + str(int(ivxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(ivxl%12)) +"\n")

        #L-3XL
            elif larsize.lower() == str("3xl") or larsize.lower() == str("xxxl"):

                #Input Sizes        
                l = int(input("L (amt): "))
                xl = int(input("XL (amt): "))
                xxl = int(input("2XL (amt): "))
                txl = int(input("3XL (amt): "))

                #Output stacks ()
                print("==================" +"\n")
                print("\n" + "_L_" + "\n" + str(int(l/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(l%12)) +"\n")
                print("_XL_" + "\n" + str(int(xl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xl%12)) +"\n")
                print("_2XL_" + "\n" + str(int(xxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xxl%12)) +"\n")
                print("_3XL_" + "\n" + str(int(txl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(txl%12)) +"\n")

        #L-2XL
            elif larsize.lower() == str("2xl") or larsize.lower() == str("xxl"):

                #Input Sizes
                l = int(input("L (amt): "))
                xl = int(input("XL (amt): "))
                xxl = int(input("2XL (amt): "))
                            
                #Output stacks ()
                print("==================" +"\n")
                print("\n" + "_L_" + "\n" + str(int(l/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(l%12)) +"\n")
                print("_XL_" + "\n" + str(int(xl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xl%12)) +"\n")
                print("_2XL_" + "\n" + str(int(xxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xxl%12)) +"\n")
        #L-XL
            elif larsize.lower() == str("xl"):   
                
                #Input Sizes
                l = int(input("L (amt): "))
                xl = int(input("XL (amt): "))
                   
                #Output stacks () 
                print("==================" +"\n")
                print("\n" + "_L_" + "\n" + str(int(l/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(l%12)) +"\n")
                print("_XL_" + "\n" + str(int(xl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xl%12)) +"\n")

            else:
                print("// Invalid input for largest size")
        #########################################################################
            
        #X-LARGE SIZES
        def xlarge(larsize):
        #XL-5XL
            if larsize.lower() == str("5xl") or larsize.lower() == str("xxxxxl"):

                #Input Sizes
                xl = int(input("XL (amt): "))
                xxl = int(input("2XL (amt): "))
                txl = int(input("3XL (amt): "))
                ivxl = int(input("4XL (amt): "))
                vxl = int(input("5XL (amt): "))
                
                #Output stacks ()
                print("==================" +"\n")
                print("\n" + "_XL_" + "\n" + str(int(xl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xl%12)) +"\n")
                print("_2XL_" + "\n" + str(int(xxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xxl%12)) +"\n")
                print("_3XL_" + "\n" + str(int(txl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(txl%12)) +"\n")
                print("_4XL_" + "\n" + str(int(ivxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(ivxl%12)) +"\n")
                print("_5XL_" + "\n" + str(int(vxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(vxl%12)) +"\n")

        #XL-4XL
            elif larsize.lower() == str("4xl") or larsize.lower() == str("xxxxl"):

                #Input Sizes
                xl = int(input("XL (amt): "))
                xxl = int(input("2XL (amt): "))
                txl = int(input("3XL (amt): "))
                ivxl = int(input("4XL (amt): "))

                #Output stacks ()
                print("==================" +"\n")
                print("\n" + "_XL_" + "\n" + str(int(xl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xl%12)) +"\n")
                print("_2XL_" + "\n" + str(int(xxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xxl%12)) +"\n")
                print("_3XL_" + "\n" + str(int(txl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(txl%12)) +"\n")
                print("_4XL_" + "\n" + str(int(ivxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(ivxl%12)) +"\n")

        #XL-3XL
            elif larsize.lower() == str("3xl") or larsize.lower() == str("xxxl"):

                #Input Sizes        
                xl = int(input("XL (amt): "))
                xxl = int(input("2XL (amt): "))
                txl = int(input("3XL (amt): "))

                #Output stacks ()
                print("==================" +"\n")
                print("\n" + "_XL_" + "\n" + str(int(xl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xl%12)) +"\n")
                print("_2XL_" + "\n" + str(int(xxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xxl%12)) +"\n")
                print("_3XL_" + "\n" + str(int(txl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(txl%12)) +"\n")

        #XL-2XL
            elif larsize.lower() == str("2xl") or larsize.lower() == str("xxl"):

                #Input Sizes
                xl = int(input("XL (amt): "))
                xxl = int(input("2XL (amt): "))
                            
                #Output stacks ()
                print("==================" +"\n")
                print("\n" + "_XL_" + "\n" + str(int(xl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xl%12)) +"\n")
                print("_2XL_" + "\n" + str(int(xxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xxl%12)) +"\n")

            else:
                print("// Invalid input for largest size")
        #########################################################################
        #2XL SIZES(
        def xxlarge(larsize):
        #2XL-5XL
            if larsize.lower() == str("5xl") or larsize.lower() == str("xxxxxl"):

                #Input Sizes
                xxl = int(input("2XL (amt): "))
                txl = int(input("3XL (amt): "))
                ivxl = int(input("4XL (amt): "))
                vxl = int(input("5XL (amt): "))
                
                #Output stacks ()
                print("==================" +"\n")
                print("\n" + "_2XL_" + "\n" + str(int(xxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xxl%12)) +"\n")
                print("_3XL_" + "\n" + str(int(txl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(txl%12)) +"\n")
                print("_4XL_" + "\n" + str(int(ivxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(ivxl%12)) +"\n")
                print("_5XL_" + "\n" + str(int(vxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(vxl%12)) +"\n")

        #2XL-4XL
            elif larsize.lower() == str("4xl") or larsize.lower() == str("xxxxl"):

                #Input Sizes
                xxl = int(input("2XL (amt): "))
                txl = int(input("3XL (amt): "))
                ivxl = int(input("4XL (amt): "))

                #Output stacks ()
                print("==================" +"\n")
                print("\n" + "_2XL_" + "\n" + str(int(xxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(xxl%12)) +"\n")
                print("_3XL_" + "\n" + str(int(txl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(txl%12)) +"\n")
                print("_4XL_" + "\n" + str(int(ivxl/12)) + " total stacks of (12) " +  "\n" + "Remainder stack size: " + str(int(ivxl%12)) +"\n")

        #2XL-3XL
            elif larsize.lower() == str("3xl") or larsize.lower() == str("xxxl"):

                #Input Sizes        
                xxl = int(input("2XL (amt): "))
                txl = int(input("3XL (amt): "))

                #Output stacks ()
                print("==================" +"\n")
                print("\n" + "_2XL_" + "\n" + " total stacks of (12) " + str(int(xxl/12)) + "\n" + "Remainder stack size: " + str(int(xxl%12)) +"\n")
                print("_3XL_" + "\n" + " total stacks of (12) " + str(int(txl/12)) + "\n" + "Remainder stack size: " + str(int(txl%12)) +"\n")

        #3XL SIZES
        def xxxlarge(larsize):
        #3XL-5XL
            if larsize.lower() == str("5xl") or larsize.lower() == str("xxxxxl"):

                #Input Sizes
                txl = int(input("3XL (amt): "))
                ivxl = int(input("4XL (amt): "))
                vxl = int(input("5XL (amt): "))
                
                #Output stacks ()
                print("==================" +"\n")
                print("\n" + "_3XL_" + "\n" + str(int(txl/12)) + " total stacks of (12)"  + "\n" + "Remainder stack size: " + str(int(txl%12)) +"\n")
                print("_4XL_" + "\n" + str(int(ivxl/12)) + " total stacks of (12)" + "\n" + "Remainder stack size: " + str(int(ivxl%12)) +"\n")
                print("_5XL_" + "\n" + str(int(vxl/12)) + " total stacks of (12)" +  "\n" + "Remainder stack size: " + str(int(vxl%12)) +"\n")

        #3XL-4XL
            elif larsize.lower(larsize) == str("4xl") or larsize.lower() == str("xxxxl"):

                #Input Sizes
                txl = int(input("3XL (amt): "))
                ivxl = int(input("4XL (amt): "))

                #Output stacks ()
                print("==================" +"\n")
                print("\n" + "_3XL_" + "\n" + str(int(txl/12)) + " total stacks of (12)" + "\n" + "Remainder stack size: " + str(int(txl%12)) +"\n")
                print("_4XL_" + "\n" + str(int(ivxl/12)) + " total stacks of (12) " + "\n" + "Remainder stack size: " + str(int(ivxl%12)) +"\n")

            else:
                print("// Invalid input for largest size")
        #########################################################################
        #4XL-5XL

        def xxxxlarge(larsize):
        #4XL-5XL
            if larsize.lower() == str("5xl") or larsize.lower() == str("xxxxxl"):

                #Input Sizes
                ivxl = int(input("4XL (amt): "))
                vxl = int(input("5XL (amt): "))
                
                #Output stacks ()
                print("==================" +"\n")
                print("\n" + "_4XL_" + "\n" + str(int(ivxl/12)) + " total stacks of (12)" + "\n" + "Remainder stack size: " + str(int(ivxl%12)) +"\n")
                print("_5XL_" + "\n" + str(int(vxl/12)) + " Total stacks of (12) " + "\n" + "Remainder stack size: " + str(int(vxl%12)) +"\n")

            else:
                print("// Invalid input for largest size")
    #########################################################################
    #input smallest size variables 
        if smalsize.lower() == larsize.lower(): #Single Size is given...
            print("// Smallest size is the same size as the largest size.")
            print("// Performing single size enumeration...")
            size = smalsize.upper()
            count = int(input(size + " (amt): "))
            single.singlesize(size, count)
        elif smalsize.lower() == str("xs"):
            print("smallest size= xs")
            xsmall(larsize)
        elif smalsize.lower() == str("s"):
            print("smallest size= s")
            small(larsize)
        elif smalsize.lower() == str("m"):
            print("smallest size= m")
            medium(larsize)
        elif smalsize.lower() == str("l"):
            print("smallest size= l")
            large(larsize)
        elif smalsize.lower() == str("xl"):
            print("smallest size= xl")
            xlarge(larsize)
        elif smalsize.lower() == str("xxl") or smalsize.lower == str("2xl"):
            print("smallest size= 2xl")
            xxlarge(larsize)
        elif smalsize.lower() == str("xxxl") or smalsize.lower() == str("3xl"):
            print("smallest size= 3xl")
            xxxlarge(larsize)
        elif smalsize.lower() == str("xxxxl") or smalsize.lower() == str("4xl"):
            print("smallest size= 4xl")
            xxxxlarge(larsize)
        elif smalsize.lower() == str("xxxxxl") or smalsize.lower() == str("5xl"):
            print("\n"+"// 5XL is the largest available size. ")
            yn = str(input("Would you like to enumerate for a single size?: "))
            if yn.lower == str("yes") or yn.lower == str("y"):
                size = str("5XL")
                count = int(input(size + " (amt): "))
                single.singlesize(size, count)
            elif yn.lower() == str("no") or yn.lower() == str("n"):
                print("// Alright, cool") #Make separate library like youthsizes
        else:
                print("// Invalid input for the smallest size")
#class infant:
#    #INFANT SIZES: (0-3, 3-6, 6-9, K9-12, 12-18, 18-24)
#class toddler:
#    #TODDLER SIZES: (2T, 3T, 4T, 5T)
