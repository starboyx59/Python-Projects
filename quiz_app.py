import random

questions = [
    ("What is the capital of France?", "Paris"),
    ("Which planet is known as the Red Planet?", "Mars"),
    ("What is the largest mammal in the world?", "Blue Whale"),
    ("Who wrote 'Romeo and Juliet'?", "William Shakespeare"),
    ("What gas do plants absorb from the atmosphere?", "Carbon Dioxide"),
    ("Which ocean is the largest?", "Pacific Ocean"),
    ("What is H2O commonly known as?", "Water"),
    ("Who painted the Mona Lisa?", "Leonardo da Vinci"),
    ("What is the fastest land animal?", "Cheetah"),
    ("How many continents are there on Earth?", "7"),
    ("Which country is known as the Land of the Rising Sun?", "Japan"),
    ("What is the hardest natural substance on Earth?", "Diamond"),
    ("Which planet is closest to the Sun?", "Mercury"),
    ("Who discovered gravity?", "Isaac Newton"),
    ("What is the boiling point of water in Celsius?", "100"),
    ("Which language has the most native speakers?", "Mandarin"),
    ("What is the largest desert in the world?", "Sahara"),
    ("What is the smallest prime number?", "2"),
    ("Which country gifted the Statue of Liberty to the USA?", "France"),
    ("What is the largest bone in the human body?", "Femur"),
    ("What is the chemical symbol for gold?", "Au"),
    ("What is the capital of Australia?", "Canberra"),
    ("How many planets are in our solar system?", "8"),
    ("Which animal is known as the King of the Jungle?", "Lion"),
    ("What color do you get when you mix red and white?", "Pink"),
    ("What is the square root of 64?", "8"),
    ("What is the largest internal organ in the human body?", "Liver"),
    ("Who is known as the Father of Computers?", "Charles Babbage"),
    ("Which planet has the most moons?", "Saturn"),
    ("Which is the largest ocean animal?", "Blue Whale"),
    ("What is the main gas found in the air we breathe?", "Nitrogen"),
    ("Who invented the light bulb?", "Thomas Edison"),
    ("What is the capital of Italy?", "Rome"),
    ("What is the freezing point of water in Celsius?", "0"),
    ("Which metal is liquid at room temperature?", "Mercury"),
    ("How many colors are there in a rainbow?", "7"),
    ("What is the tallest mountain in the world?", "Mount Everest"),
    ("Which continent is the Sahara Desert located on?", "Africa"),
    ("Who was the first man to step on the moon?", "Neil Armstrong"),
    ("Which country is famous for the pyramids?", "Egypt"),
    ("What is the chemical symbol for oxygen?", "O"),
    ("Which country has the maple leaf on its flag?", "Canada"),
    ("What is the capital of Germany?", "Berlin"),
    ("Which part of the plant conducts photosynthesis?", "Leaf"),
    ("Which bird can mimic human speech?", "Parrot"),
    ("Who is known as the Father of Modern Physics?", "Albert Einstein"),
    ("What is the smallest planet in our solar system?", "Mercury"),
    ("What is the process by which plants make their food?", "Photosynthesis"),
    ("Which animal is known for changing its color?", "Chameleon"),
    ("What is the chemical formula for table salt?", "NaCl"),
    ("What is the largest planet in our solar system?", "Jupiter"),
    ("Who invented the telephone?", "Alexander Graham Bell"),
    ("What is the capital of China?", "Beijing"),
    ("Which organ pumps blood throughout the body?", "Heart"),
    ("What is the main ingredient in bread?", "Flour"),
    ("Which animal is known to have a trunk?", "Elephant"),
    ("What is the process of water turning into vapor called?", "Evaporation"),
    ("Which festival is known as the Festival of Lights in India?", "Diwali"),
    ("What is the national sport of Japan?", "Sumo Wrestling"),
    ("What do bees collect from flowers?", "Nectar"),
    ("What is the capital city of Spain?", "Madrid"),
    ("Which natural satellite orbits the Earth?", "Moon"),
    ("Which animal lays eggs and can fly?", "Bird"),
    ("What is the largest island in the world?", "Greenland"),
    ("How many legs does a spider have?", "8"),
    ("What is the chemical symbol for iron?", "Fe"),
    ("Which famous scientist developed the theory of relativity?", "Albert Einstein"),
    ("What is the largest country by land area?", "Russia"),
    ("Which planet is known for its rings?", "Saturn"),
    ("Who was the first President of the United States?", "George Washington"),
    ("What is the capital of Russia?", "Moscow"),
    ("What is the national flower of Japan?", "Cherry Blossom"),
    ("Which language is spoken in Brazil?", "Portuguese"),
    ("What is the study of living organisms called?", "Biology"),
    ("Which is the longest river in the world?", "Nile"),
    ("What is the largest bird in the world?", "Ostrich"),
    ("Who discovered penicillin?", "Alexander Fleming"),
    ("What is the capital of Canada?", "Ottawa"),
    ("Which organ helps humans breathe?", "Lungs"),
    ("What is the capital of South Korea?", "Seoul"),
    ("What do we call a baby frog?", "Tadpole"),
    ("How many players are there in a football team?", "11"),
    ("What is the chemical symbol for silver?", "Ag"),
    ("Who was the first woman to fly solo across the Atlantic?", "Amelia Earhart"),
    ("Which instrument measures temperature?", "Thermometer"),
    ("What type of animal is a Komodo dragon?", "Lizard"),
    ("Which planet is known as the Blue Planet?", "Earth"),
    ("What is the largest ocean in the world?", "Pacific Ocean"),
    ("Who painted The Starry Night?", "Vincent van Gogh"),
    ("What is the capital of Mexico?", "Mexico City"),
    ("Which is the fastest bird in the world?", "Peregrine Falcon"),
    ("Which gas do humans exhale?", "Carbon Dioxide"),
    ("What is the main source of energy for the Earth?", "Sun"),
    ("Which shape has three sides?", "Triangle"),
    ("Which country is home to the kangaroo?", "Australia"),
    ("How many days are there in a leap year?", "366"),
    ("What is the largest continent?", "Asia"),
    ("Who is known as the Iron Man of India?", "Sardar Vallabhbhai Patel"),
    ("Which part of the body helps you see?", "Eyes"),
    ("What is the capital of Egypt?", "Cairo")
]

random.shuffle(questions)

score = 0
for i, (question, answer) in enumerate(questions, 1):
    print(f"Q{i}: {question}")
    user_answer = input("Your answer: ").strip().lower()
    if user_answer == answer.strip().lower():
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is {answer}\n")

print(f"You got {score} out of {len(questions)} questions correct.")
if score == len(questions):
    print("Perfect score! Excellent job!")
elif score > 80:
    print("Outstanding performance!")
elif score > 60:
    print("Great work! Keep it up!")
elif score > 40:
    print("Good effort! You’re improving.")
else:
    print("Keep practicing and try again.")
