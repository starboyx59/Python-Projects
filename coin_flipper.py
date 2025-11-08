import random
import time

print("Welcome to the Virtual Coin Flipper with AI Prediction!\n")
print("I'm your friendly AI predictor. Let's see if I can guess your coin flips correctly.\n")

ai_memory = {"Heads": 0, "Tails": 0}
ai_correct = 0
total_flips = 0

while True:
    print("\nAI is analyzing past flips...")
    time.sleep(1)

    if ai_memory["Heads"] > ai_memory["Tails"]:
        ai_prediction = "Heads"
        confidence = random.randint(60, 95)
    elif ai_memory["Tails"] > ai_memory["Heads"]:
        ai_prediction = "Tails"
        confidence = random.randint(60, 95)
    else:
        ai_prediction = random.choice(["Heads", "Tails"])
        confidence = random.randint(50, 70)

    print(f"My AI prediction: {ai_prediction} (Confidence: {confidence}%)")

    input("\nPress Enter to flip the coin... ")
    flip_result = random.choice(["Heads", "Tails"])
    print("\nFlipping", end="")
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.6)

    print(f"\n The coin landed on: {flip_result}!")

    total_flips += 1
    ai_memory[flip_result] += 1

    if flip_result == ai_prediction:
        ai_correct += 1
        print(random.choice([
            "I was right again!",
            "Nailed it!",
            "My prediction model is improving!"
        ]))
    else:
        print(random.choice([
            "Oops, not this time.",
            "I’ll analyze the pattern better next time.",
            "Interesting... I’ll remember that result."
        ]))

    accuracy = round((ai_correct / total_flips) * 100, 2)
    print(f"\nAI Accuracy so far: {accuracy}% after {total_flips} flips.")

    choice = input("\nFlip again? (y/n): ").strip().lower()
    if choice != 'y':
        print("\nThanks for playing!")
        print(f"Final AI accuracy: {accuracy}%")
        break
