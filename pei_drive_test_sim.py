import random

# List of sample questions and answers
questions = [
    {
        "q": "What does a flashing red traffic light mean?",
        "options": ["A) Proceed with caution", "B) Stop, then proceed when safe", "C) Yield only", "D) Ignore if no one is coming"],
        "answer": "B"
    },
    {
        "q": "When are you allowed to make a right turn at a red light in PEI?",
        "options": ["A) Never", "B) Only after stopping and ensuring it’s safe", "C) Only when signposted", "D) Anytime"],
        "answer": "B"
    },
    {
        "q": "What does this road sign indicate? (Yield Sign)",
        "options": ["A) Stop", "B) Yield", "C) No entry", "D) School zone"],
        "answer": "B"
    },
    {
        "q": "What is the minimum following distance recommended under ideal conditions?",
        "options": ["A) 1 second", "B) 2 seconds", "C) 3 seconds", "D) 5 seconds"],
        "answer": "C"
    },
    {
        "q": "If you’re approaching a school bus with flashing red lights, you must:",
        "options": ["A) Slow down and pass carefully", "B) Stop and do not pass until the lights are off", "C) Pass quickly", "D) Honk to warn children"],
        "answer": "B"
    }
]

random.shuffle(questions)
score = 0

for q in questions:
    print("\n" + q["q"])
    for opt in q["options"]:
        print(opt)
    ans = input("Your answer (A/B/C/D): ").strip().upper()
    if ans == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Incorrect. Correct answer: {q['answer']}")
print(f"\nYour final score: {score}/{len(questions)}")
