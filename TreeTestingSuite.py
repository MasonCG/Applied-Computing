from Tree import *

tree = DecisionTree()

tree.addQuestion("Is your animal a mammal?")
tree.cur.yes = Node("Giraffe")
tree.cur.no = Node("Lizard")


def playAgain():
    print("\nWould you like to play again?")
    ans = input().upper()

    if ans == 'Y':
        tree.restart()
        return True
    
    return False


while(True):

    print(tree.cur.text) 
    print("Answer Y/N: ")
    ans = input().upper()
    print("\n")


    if ans == "Y":
        guessed = tree.nextNode(ans)
    elif ans == 'N':
        guessed = tree.nextNode(ans)
    else:
        continue

    if not guessed:
        continue


    # ===== ANIMAL GUESSED =====

    # asking if animal is right
    print(f"Is your animal a {guessed}?")
    print("Answer Y/N: ")
    ans = input().upper()

    if ans == "Y":
        print("\nyay! I win!!!")
        if playAgain():
            continue
        else:
            break

    # adding animal and question if it was not guessed
    print("\nDrats!!! I'll get it next time. Y")
    print("\nType your animal: ")
    newAnimal = input()
    print("\nGive me a question that distinguishes your animal from the one I guessed? Please make it a YES or NO question")
    newQuestion = input()
    print("\nWhat is the answer to your question?")
    print("Answer Y/N: ")
    newAns = input().upper()
    tree.addQuestion(newQuestion, newAns, newAnimal, guessed)
    
    if playAgain():
        continue
    else:
        break


