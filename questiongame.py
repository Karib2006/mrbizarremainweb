import random

print('                                                 Question Answere Game')

questions = ['What is the capital of Bangladesh?', 'What is the capital of Brazil?', 'What is this Program written in?', 'Which club does Messi play for?', 'Who is PewDiePie?',
             'Who is Sundar Pichai?', 'Who is the CEO of Tesla?', 'Who is the founder of Amazon?', 'Who is the founder of Google?', 'Who is the founder of Microsoft?',
            'Who is the CEO of Microsoft ' ]

chance = 3

times= 6

while times > 1:
    times-=1
    final_question = random.sample(questions, k=1)
    if final_question == ['What is the capital of Bangladesh?']:
        answer = 'Dhaka'
    elif final_question == ['What is the capital of Brazil?']:
        answer = 'Brasilia'
    elif final_question == ['What is this Program written in?']:
        answer = 'Python'
    elif final_question == ['Which club does Messi play for?']:
        answer = 'Barcelona' or 'Barca'
    elif final_question == ['Who is PewDiePie?']:
        answer = 'Youtuber'
    elif final_question == ['Who is Sundar Pichai?']:
        answer = 'CEO of Google'
    elif final_question == ['Who is the CEO of Tesla?']:
        answer = 'Elon Musk'
    elif final_question == ['Who is the founder of Amazon?']:
        answer = 'Jeff Bezos'
    elif final_question == ['Who is the founder of Google?']:
        answer = 'Larry Page'
    elif final_question == ['Who is the founder of Microsoft?']:
        answer = 'Bill Gates'
    elif final_question == ['Who is the CEO of Microsoft?']:
        answer = 'Satya ela'
    else:
        pass


    print(f'>> {final_question}')
    usr_Ans = input('Answer: ').title()

    if usr_Ans == answer.title():
        print('Good Job Correct Answer !!!!')
    else:
        print(f'Sorry Your Answer is Wrong, The Correct Answere was {answer}')
        chance -= 1
        if chance == 2:
            print('2 more chances left')
        elif chance == 1:
            print('1 more chance left')
        else:
            pass

    if chance == 0:
        print('Game Over Try Again')
        break


    if times == 1:
        print('                                   Game Over Nice Game!!')
        a = input()















