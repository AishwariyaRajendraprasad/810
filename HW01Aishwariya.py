import random

move = ['r','p','s']

'''For infinite number of games'''
while True:
        '''User Input'''
        print("**************ROCK***PAPER***SCISSOR**********************")
        Human = input("Please enter r,p,s for Rock, Paper, Scissors or q to quit:")

        '''quit'''
        if Human in ['quit','Quit','q','Q']:
                print ("Had fun!!!Goodbye!")
                exit()
        
        '''To check the input value'''
        if Human in move:

                '''Computer's choice'''
                Computer = random.choice(move)
                print("Computer's turn:", Computer)

                '''Conditions'''
                if Human =='r' and Computer == 'r':
                        print("It's a tie")

                elif Human == 'r' and Computer == 'p':
                        print("Paper beats Rock")
                        print("Computer wins, you looose")

                elif Human == 'r' and Computer == 's':
                        print("Rock beats Scissors")
                        print("You win!!")

                elif Human =='p' and Computer == 'p':
                        print("It's a tie")

                elif Human == 'p' and Computer == 's':
                        print("Scissor beats Paper")
                        print("Computer wins, you looose")

                elif Human == 'p' and Computer == 'r':
                        print("Paper beats Rock")
                        print("You win!!")

                elif Human =='s' and Computer == 's':
                        print("It's a tie")

                elif Human == 's' and Computer == 'r':
                        print("Rock beats Scissors")
                        print("Computer wins, you looose")

                elif Human == 's' and Computer == 'p':
                        print("Scissor beats Paper")
                        print("You win!!")

        
        else:
                print("Please check, your input is invalid")      
                      
        
        
        
        
 
