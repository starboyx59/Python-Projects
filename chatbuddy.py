def chatbot():
    print("Hi! I'm ChatBuddy ")
    print("You can talk to me about general things.")
    print("Type 'bye' to end the chat.")
    print("-" * 40)

    while True:
        user_input = input("You: ").lower()

       
        if "bye" in user_input:
            print("ChatBuddy: Bye! It was nice talking to you ")
            break

       
        elif "hello" in user_input or "hi" in user_input:
            print("ChatBuddy: Hello there! How are you today?")
        elif "how are you" in user_input:
            print("ChatBuddy: I'm just a program, but I'm doing great! How about you?")

       
        elif "school" in user_input:
            print("ChatBuddy: School is important! What’s your favorite subject?")
        elif "math" in user_input:
            print("ChatBuddy: Math is fun! Did you know 0 is the only number that can’t be represented in Roman numerals?")
        elif "science" in user_input:
            print("ChatBuddy: Science helps us understand how the world works!")
        elif "history" in user_input:
            print("ChatBuddy: History teaches us about the past so we can build a better future.")
        elif "english" in user_input:
            print("ChatBuddy: English is awesome! It connects people all around the world.")
        elif "favorite subject" in user_input:
            print("ChatBuddy: I like computer science — of course! ")

        
        elif "weather" in user_input:
            print("ChatBuddy: I can’t see outside, but I hope it’s sunny where you are ")

        
        elif "time" in user_input:
            from datetime import datetime
            print(f"ChatBuddy: It's currently {datetime.now().strftime('%I:%M %p')}.")

        
        elif "add" in user_input or "plus" in user_input:
            try:
                nums = [int(s) for s in user_input.split() if s.isdigit()]
                print(f"ChatBuddy: The answer is {sum(nums)}.")
            except:
                print("ChatBuddy: I can add numbers if you tell me clearly, like 'add 3 and 5'.")
        elif "multiply" in user_input:
            try:
                nums = [int(s) for s in user_input.split() if s.isdigit()]
                result = 1
                for n in nums:
                    result *= n
                print(f"ChatBuddy: The answer is {result}.")
            except:
                print("ChatBuddy: I can multiply numbers if you tell me clearly, like 'multiply 2 and 4'.")

        
        elif "fact" in user_input:
            import random
            facts = [
                "Honey never spoils — archaeologists found 3000-year-old honey that’s still good!",
                "Bananas are berries, but strawberries aren’t!",
                "Octopuses have three hearts!",
                "A group of flamingos is called a 'flamboyance'.",
                "Cats sleep for about 70% of their lives."
            ]
            print("ChatBuddy: " + random.choice(facts))

        
        elif "game" in user_input:
            print("ChatBuddy: I like guessing games! Do you play video games?")
        elif "music" in user_input:
            print("ChatBuddy: Music makes everything better! What kind of music do you like?")
        elif "sports" in user_input:
            print("ChatBuddy: Sports are great for staying healthy and having fun!")

        
        elif "name" in user_input:
            print("ChatBuddy: My name is ChatBuddy! What’s yours?")
        elif "who made you" in user_input or "who created you" in user_input:
            print("ChatBuddy: I was created by a student for a school project, just like you’re doing now!")
        elif "age" in user_input:
            print("ChatBuddy: I don’t age, but I was created not too long ago.")

        
        elif "joke" in user_input:
            import random
            jokes = [
                "Why did the computer go to therapy? Because it had a hard drive!",
                "Why was the math book sad? Because it had too many problems.",
                "Why did the student eat his homework? Because the teacher said it was a piece of cake!",
                "What do you call fake spaghetti? An impasta!"
            ]
            print("ChatBuddy: " + random.choice(jokes))

        
        else:
            print("ChatBuddy: Hmm... I’m not sure about that. Try asking me something else!")


chatbot()