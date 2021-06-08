from questions import QUESTIONS


def isAnswerCorrect(question, answer):
    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''
    if question["answer"] == answer:
        return True
    else:
        return False


def lifeLine(ques):#working on it
    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''


def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''

    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks

    print("Welcome to KBC!!!")
    for i in range(0,15):
        print(f'\tQuestion {i + 1}: {QUESTIONS[i]["name"]}')
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[i]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[i]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[i]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[i]["option4"]}')
        ans = input('Your choice ( 1-4 ) : ')
        money=0
        min_reward = 0
        last_reward = 0
        # check for the input validations
        while (len(ans) != 1 or ans == "quit"):
            if (ans == "quit"):
                money = last_reward
                break
            else:
                print("INVALID INPUT")
            ans = input('Your choice ( 1-4 ) : ')

        if isAnswerCorrect(QUESTIONS[i], int(ans)):
            # print the total money won.
            # See if the user has crossed a level, print that if yes
            last_reward = QUESTIONS[i]["money"]
            if (i == 4):
                min_reward = QUESTIONS[i]["money"]
            elif (i == 9):
                min_reward = QUESTIONS[i]["money"]
            print('\tYay! You gave a right answer!')

        else:
            # end the game now.-
            # also print the correct answer
            print('\nOh we are sorry! The answer is wrong!')
            print('The correct answer is : ', QUESTIONS[i]["answer"])
            money = min_reward
            break

        # print the total money won in the end.
    if money<1: print("Sorry!")
    else: print("Yay! You played well :D")
    print("You won Rs.", money)


kbc()
