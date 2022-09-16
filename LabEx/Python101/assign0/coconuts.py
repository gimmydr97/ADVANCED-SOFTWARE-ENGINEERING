

def birdsSplitCoconuts(birds, coconuts):
    
    if birds / coconuts >= 5.5:
        print("Yes! Carrying the coconuts is possible.")
    
    else: 
        print("No. Carrying the coconuts is impossible.")
        
def main():
    while True:

        birds = input("How many ounces of birds are carrying the coconuts?")
        coconuts = input("How many pounds of coconuts are there?")

        if birds != "" and coconuts != "": 
            birdsSplitCoconuts(float(birds), float(coconuts))
        else :
            break

if __name__ == '__main__':
    main()