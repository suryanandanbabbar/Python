# This prints the pascals triangle as given by sir.
def pascal(rows):
    
    for r in range(0, rows):
        for spaces in range(rows, r, -1):
            print(" ", end="")
        
        number = 1
        
        for col in range(0, r+1):
            print(number, end=" ")
            # Important formula
            number = number * (r - col) // (col + 1)
        print()

rows = int(input("rows: "))
pascal(rows)