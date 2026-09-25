questions = ( "1. Quelle est la capitale de l'australie ?",
              "2. Quel est le plus grand océan du monde ?",
              "3. En Machine Learning, lequel est un exemple de classification ?",
              "4. Quelle structure Python permet de stocker plusieurs éléments dans un ordre précis et accepte les doublons ?",
              "5. Si un modèle donne 95 prédictions correctes sur 100 exemples, quelle est son accuracy ?")

options = (("A) Sydney","B) Melbourne", "C) Canberra", "D) Perth"),
           ("A) Atlantique", "B) Indien", "C) Arctique", "D) Pacifique"),
           ("A) Prédire le prix d'une maison", "B) Prédire la température demain", "C) Déterminer si un email est spam ou non", "D) Prédire la vitesse d'une voiture"),
           ("A) Set", "B) Tuple", "C) List", "D) Dictionary"),
           ("A) 90 %", "B) 92 %" ,"C) 95 %" ,"D) 97 %"))

answers = ("B", "A", "C", "C", "C")
guesses = []
score = 0
questions_num = 0

for question in questions:
    print("-------------------")
    print(question)
    for option in options[questions_num]:
        print(option)

    guess = input("enter the option(A,B,C,D): ").upper()
    guesses.append(guess)
    if guess ==  answers[questions_num]:
        print("CORRECT !")
        score +=1
    else :
        print("INCORRECT !")
        print(f"the correct answer is {answers[questions_num]} ")

    questions_num += 1

print("----------------")
print("     RESULT     ")
print("----------------")

for answer in answers:
    print(answer, end=" ")
print()

for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"your score is {score} ")