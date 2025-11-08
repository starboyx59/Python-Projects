import random
import time
import os

def get_user_name():
    if os.path.exists("user_data.txt"):
        with open("user_data.txt", "r") as file:
            name = file.read().strip()
        print(f"Welcome back, {name}!")
        return name
    else:
        name = input("Hi! I'm your Study Assistant. What’s your name? ")
        with open("user_data.txt", "w") as file:
            file.write(name)
        print(f"Nice to meet you, {name}! Let's boost your learning!")
        return name


study_tips = [
    "Take short breaks every 25 minutes to recharge your brain.",
    "Teach what you learn — explaining helps you remember better.",
    "Avoid multitasking. Focus on one thing at a time.",
    "Use active recall — test yourself, don't just reread notes.",
    "Drink water and stretch! Your brain loves oxygen and movement."
]

motivational_quotes = [
    "“Push yourself, because no one else is going to do it for you.”",
    "“Don’t watch the clock; do what it does. Keep going.”",
    "“Success is the sum of small efforts repeated daily.”",
    "“You don’t have to be great to start, but you have to start to be great.”"
]

definitions = {
    "ai": "AI stands for Artificial Intelligence — machines that can 'think' or learn like humans.",
    "python": "Python is a programming language known for simplicity and power. Great for beginners!",
    "algorithm": "An algorithm is a set of steps to solve a problem — like a recipe for your computer.",
    "machine learning": "Machine Learning is a subset of AI where computers learn from data instead of rules."
}


def ai_response(user_input):
    user_input = user_input.lower()

    if "tip" in user_input:
        return random.choice(study_tips)
    elif "motivate" in user_input or "quote" in user_input:
        return random.choice(motivational_quotes)
    elif "define" in user_input or "what is" in user_input:
        for key in definitions:
            if key in user_input:
                return definitions[key]
        return "Hmm, I’m not sure about that term yet — but you can teach me later!"
    elif "bye" in user_input:
        return "Goodbye! Keep learning and stay curious!"
    elif "thanks" in user_input or "thank you" in user_input:
        return "You're very welcome!"
    elif "how are you" in user_input:
        return "I’m feeling extra helpful today! Ready to study?"
    else:
        return random.choice([
            "That’s interesting! Tell me more.",
            "Can you rephrase that?",
            "Hmm… I’ll try to learn that soon.",
            "Good question! Let’s think about that together."
        ])


def chat():
    name = get_user_name()
    print("\nType 'bye' to end the chat anytime.")
    print("Try asking for a 'study tip', a 'definition', or a 'motivation quote'.\n")

    while True:
        user_input = input(f"{name}: ")
        if user_input.strip().lower() == "bye":
            print("AI Assistant: Goodbye! Keep studying smart!")
            break

        time.sleep(0.5)
        response = ai_response(user_input)
        print(f"AI Assistant: {response}\n")


if __name__ == "__main__":
    chat()
