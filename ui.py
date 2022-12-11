import plot
import time
import random
import csv
#The following is the array of questions associated with its question number and its chart type. The array of these 3 objects will be shuffled and shown to user in randomised order
#please update the third items with whatever map you intend to compare the bar with
questions = [["What is the plastic pollution produced by the most polluting country?", 1, "bar"],
            ["What is the plastic pollution produced by the most polluting country?", 1, "choro"],
            ["Which country pollutes the most plastic", 2, "bar"],
            ["Which country pollutes the most plastic", 2,"tree"],
            ["What is the plastic pollution produced by the least polluting country?", 3, "bar"],
            ["What is the plastic pollution produced by the least polluting country?", 3,"tree"],
            ["Which country pollutes the least plastic?", 4, "bar"],
            ["Which country pollutes the least plastic?", 4,"tree"],
            ["Which kind of plastic waste is most found in different countries?", 5, "bar"],
            ["Which kind of plastic waste is most found in different countries?", 5,"heat"],
            ["Which country has the best plastic pollution to emission ratio?", 6, "bar"],
            ["Which country has the best plastic pollution to emission ratio?", 6,"tree"],
            ["Which country pollutes the most?", 7, "bar"],
            ["Which country pollutes the most?", 7,"heat"],
            ["Which country has the best ratio of recyclable plastics to non-recyclable plastics?", 8, "bar"],
            ["Which country has the best ratio of recyclable plastics to non-recyclable plastics?", 8,"tree"],
            ["Which country generates the most plastic waste per person?", 9, "bar"],
            ["Which country generates the most plastic waste per person?", 9,"tree"],
            ["Which country spends the most money recycling plastic?", 10, "bar"],
            ["Which country spends the most money recycling plastic?", 10,"choro"],
]

#shuffles questions
random.shuffle(questions)




#initialses a 3D list datastructure to keep track of time taken and whether user has got right for each question.
#X axis are the 10 questions [0 to 9 possible values]
#Y axis is whether bar or map for the specific question [2 possible values - 0 or 1. 0 represents bar, 1 represents map]
#Z axis represents time or correctAnswer [2 possible values - 0 or 1]. 0 will be used to store time, 1 will be used to store whether user got it correct or not. 0 means he got it wrong, 1 means he got it correct.
#Example to help understand better - if user attempts q1 barchart wrong and took 10 seconds to answer, the program will do scores[0][0][0] = 10.00, and scores[0][0][1] = 0
scores = []
for i in range(10):
    scores.append([[0,0],[0,0]])


print("Welcome to our quiz, we will now be showing you 20 questions! try to answer these questions to the best of your ability!")
input("Press Enter To Start")

for i in range(20):
    print(questions[i][0])
    options = plot.return_options(questions[i][1], questions[i][2])
    start_time = time.time()
    plot.display_charts(questions[i][1],questions[i][2])
    print("The options are:")
    print("0. ", options[0][0])
    print("1. ", options[1][0])
    print("2. ", options[2][0])
    print("3. ", options[3][0])
    answer = input("Enter your answer below: Options are 0,1,2 or 3")
    while True:
        if answer != "0" and answer != "1" and answer != "2" and answer != "3":
            answer = input("Please enter options 0, 1, 2 or 3. Not anything else")
        else:
            break
    end_time = time.time()
    time_taken = end_time - start_time
    answer = int(answer)


    #adds to score
    if questions[i][2] == "bar":
        scores[questions[i][1]-1][0][0] = time_taken
        scores[questions[i][1]-1][0][1] = options[answer][1]
    else:
        scores[questions[i][1]-1][1][0] = time_taken
        scores[questions[i][1]-1][1][1] = options[answer][1]




data = []
data.append("Tester 1")

for i in range(40):
    if i<10:
        data.append(scores[i][0][1])
    elif i<20:
        data.append(scores[i-10][1][1])
    elif i<30:
        data.append(scores[i-20][0][0])
    else:
        data.append(scores[i-30][1][0])





with open('Results.csv', 'a', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)





