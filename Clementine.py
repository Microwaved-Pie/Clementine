from time import sleep
from colorama import colorama_text

# D = Decision
# ID = Important Decision
# S1D = Season 1 Decision
# S2D = Season 2 Decision
# S3D = Season 3 Decision
# S4D = Season 4 Decision

S1D1 = int(0)
S1D2 = int(0)
S2D1 = int(0)
S2D2 = int(0)
S3D1 = int(0)
S3D2 = int(0)
S4D1 = int(0)
S4D2 = int(0)
choicesimported = int(0)
cachoicesimported = int(0)


while True:
    print("CLEMENTINE & AJ")
    print("Episode 1: Where The Flowers Grow")

    D = ("0")
    while True:
        D1 = input("""
0: Info
1: Import Choices
2: 
3: Start
                

{: """)
        print("_________________________________________________________________________")
        print(" ")
        if D1  == ("3"):
            print("{:Start")
            print("")
            print("")
            print("Clementine And AJ are in a abandoned school.")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("_________________________________________________________________________")
            print(" ")
        if D1 == ("0"):
            print("{:Info")
            print("""
Clementine & AJ is a rewrite of the clementine comics. or more or less a rewrite of the events after season 4.
This is episode 1/4: Where The Flowers Grow""")
            print("_________________________________________________________________________")
            print(" ")
        if D1 == ("1"):
            print("{:Import Choices")


            print("_________________________________________________________________________")
            print(" ")
            while True:
                S1D1 = input("""In Season 1, did Lee grab christa or omids hand?
1: Omid
2: Christa
            
 
{: """)
                S1D1 = int(S1D1)
                if S1D1 == (1) or S1D1 == (2):
                    print(" ")
                    print("Correct")
                    print("_________________________________________________________________________")
                    break
                else:
                    print(" ")
                    print("Invalid Input")
                    print("_________________________________________________________________________")
            print("_________________________________________________________________________")
            print(" ")
            S1D2 = input("""Did you Shoot, or leave Lee?
1: Shoot
2: Leave
 
 
{: """)
 
            print("_________________________________________________________________________")
            print(" ")
            S2D1 = input("""Did you distract, or run away from the scavangers surronding Christa in Season 2?
1: Distract
2: Run Away
 
 
{: """)
            print("_________________________________________________________________________")
            print(" ")
            S2D2 = input("""What ending did you get in Season 2?
1: Wellington
2: Kenny
3: Jane
4: Alone
                         
                         
{: """)
            print("_________________________________________________________________________")
            print(" ")
            S3D1 = input("""Who lived at the end of Season 3?
1: Gabe
2: Kate
3: Gabe & David
4: Kate & David
                         
                         
{: """)
            print("_________________________________________________________________________")
            print(" ")
            S3D2 = input(""" Who survived in season 3?
1: Lingard & Max & Conrad
2: Lingard & Max
3: Lingard & Conrad
4: Max & Conrad
5: Max
6: Conrad
7: Lingard
8: Nobody

                         
{: """)
            print("_________________________________________________________________________")
            print(" ")
            S4D1 = input("""What did you teach Aj the best?
1:
2:
3:
4:
                         
                         
{: """)
            print("_________________________________________________________________________")
            print(" ")
            S4D2 = input("""Did Lilly live?
1: Yes.
2: No
                         
                         
{: """)
