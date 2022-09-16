
def end(char, replys): # check if the answers end with ?

    for elem in replys:
        if elem.endswith(char):
            return True

    return False

def find(replyTrick, possibleReply): # check if the answer to the riddle is present in the set of possible answers

    for elem in possibleReply:
        if replyTrick.find(elem) != -1:
            return True

    return False

def main():
    with open('answers.txt', 'r') as f: #for open answers.txt without using close at the end
        for line in f:

            question = str(line).split('? ')
            possibleReply = question[1].split('|')
            possibleReply[len(possibleReply)-1] = possibleReply[len(possibleReply)-1].strip('\n') #delete the character \n from the last element of the list
            
            print("KEEPER : Stop! Who would cross the Bridge of Death must answer me these questions three, 'ere the other side he see.")
            
            replyName = input("What is your name? ").strip(' !.')
            replyQuest = input("KEEPER : What is your quest? ").strip(' !.')
            replyTrick = input("KEEPER : What is " + question[0] + "?").strip(' !.').lower()
        
            if find(replyTrick, possibleReply):
                print("KEEPER : Right. Off you go.") 
            
            elif end('?', [replyName, replyQuest, replyTrick]):
                print("KEEPER : Auuuuuuuugh!")

            else: 
                print(replyName.upper() + ": Auuuuuuuugh!")
    
if __name__ == '__main__':
    main()
