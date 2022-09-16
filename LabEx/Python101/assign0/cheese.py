
def main():

    cheeses =["Muenster", "Cheddar", "Red Leicester"]
    questions = ["You... do have some cheese, don't you?", "Have you in fact got any cheese here at all?"]
    flag = 1

    print("Good morning. Welcome to the National Cheese Emporium!")
    
    while flag:

        reply = input("What would you like?")

        if reply in cheeses:

            flag = 0
            print("We have " + reply + ", yessir.")

        elif reply in questions:

            print("We have " + str(len(cheeses)) + " cheese(s)!")

            for cheese in cheeses:

                print(cheese)
        else: 

            print("I'm afraid we don't have any " + reply + ".")

if __name__ == '__main__':
    main()