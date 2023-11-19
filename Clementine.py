from time import sleep
from colorama import colorama_text

# D = Decision
# ID = Important Decision
# S1D = Season 1 Decision
# S2D = Season 2 Decision
# S3D = Season 3 Decision
# S4D = Season 4 Decision

S1D1 = 1
S1D2 = 1
S2D1 = 1
S2D2 = 1
S3D1 = 1
S3D2 = 1
S4D1 = 1
S4D2 = 1


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
            S1D1 = input("""In Season 1, did Lee grab christa or omids hand?
1: Omid
2: Christa""")
            S1D2 = input("""Did you Shoot, or leave Lee?
1: Shoot
2: Leave""")
            S2D1 = input("""Did you distract, or run away from the scavangers surronding Christa in Season 2?
1: Distract
2: Run Away""")
            S2D2 = input("What ending did you get in Season 2?")
            S3D1 = input("Who lived at the end of Season 3?")
            S3D2 = input("What was characters ending personality in season 3?")
            S4D1 = input("What did you teach Aj the best?")
            S4D2 = input("Did Lilly live?")
