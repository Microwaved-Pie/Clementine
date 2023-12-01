# Clementine
My Rewrite Of The Clementine Comics

# Loops until true
while True:
    # prompting user input 
    guess = int(input("Guess the number:"))
    # created a range.
    if 25 >= guess >= 20:
        print("Correct")
        # if matches comes out of the loop.
        break
        # code continues.
    else:
        print("Try again")