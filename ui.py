import plot
#The following is the array of questions associated with its question number and its chart type. The array of these 3 objects will be shuffled and shown to user in randomised order
#please update the third items with whatever map you intend to compare the bar with
questions = [["What is the plastic pollution produced by the most polluting country?", 1, "bar"],
            ["What is the plastic pollution produced by the most polluting country?", 1, ""],
            ["Which country pollutes the most plastic", 2, "bar"],
            ["Which country pollutes the most plastic", 2,""],
            ["What is the plastic pollution produced by the least polluting country?", 3, "bar"],
            ["What is the plastic pollution produced by the least polluting country?", 3,""],
            ["Which country pollutes the least plastic?", 4, "bar"],
            ["Which country pollutes the least plastic?", 4,""],
            ["Which kind of plastic waste is most found in different countries?", 5, "bar"],
            ["Which kind of plastic waste is most found in different countries?", 5,""],
            ["Which country has the best plastic pollution to emission ratio?", 6, "bar"],
            ["Which country has the best plastic pollution to emission ratio?", 6,""],
            ["Which country pollutes the most?", 7, "bar"],
            ["Which country pollutes the most?", 7,""],
            ["Which country has the best ratio of recyclable plastics to non-recyclable plastics?", 8, "bar"],
            ["Which country has the best ratio of recyclable plastics to non-recyclable plastics?", 8,""],
            ["Which country generates the most plastic waste per person?", 9, "bar"],
            ["Which country generates the most plastic waste per person?", 9,"tree"],
            ["Which country spends the most money recycling plastic?", 10, "bar"],
            ["Which country spends the most money recycling plastic?", 10,"choro"],
]

print(questions)
print("Welcome to our quiz, we will now be showing you 20 questions! try to answer these questions to the best of your ability!")