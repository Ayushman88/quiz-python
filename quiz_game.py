print("WELCOME TO THE GEO QUIZ GAME!")

while True:
    playing = input("Do you want to play? ")

    if playing.lower() != "yes":
        quit()
    else: print("Lets play the game!!")
    
    questions_and_answers = [
    ["What is the capital of India? ", "New Delhi"],
    ["What is the capital of Japan? ", "Tokyo"],
    ["What is the capital of Brazil? ", "Brasília"],
    ["What is the capital of Russia? ", "Moscow"],
    ["What is the capital of Australia? ", "Canberra"],
    ["What is the capital of Canada? ", "Ottawa"],
    ["What is the capital of Germany? ", "Berlin"],
    ["What is the capital of France? ", "Paris"],
    ["What is the capital of South Africa? ", "Cape Town"],
    ["What is the capital of Egypt? ", "Cairo"],
    ["What is the capital of Mexico? ", "Mexico City"],
    ["What is the capital of Argentina? ", "Buenos Aires"],
    ["What is the capital of Italy? ", "Rome"],
    ["What is the capital of Spain? ", "Madrid"],
    ["What is the capital of Nigeria? ", "Abuja"],
    ["What is the capital of Turkey? ", "Ankara"],
    ["What is the capital of Thailand? ", "Bangkok"],
    ["What is the capital of South Korea? ", "Seoul"],
    ["What is the capital of Saudi Arabia? ", "Riyadh"],
    ["What is the capital of Vietnam? ", "Hanoi"]
    ]
    
    score = 0
    
    
    for question, answer in questions_and_answers:
        user_answer = input(question).strip().lower()
        if user_answer == answer.lower():
            score += 1
            print("Correct answer!")
            print("Score: ", score)
        else:
            print("Wrong answer.")
            print("Correct answer:", answer)
            print("Score: ", score)
        
    print("your final score: ", score, "out of ", len(questions_and_answers))
    print("Thanks for playing the game!!")