import requests
import json
import re
import demjson3

def generate_questions_with_ollama(prompt, model="tinyllama"):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        text = response.json()['response']
        # Extract the first JSON list of questions (even with messy output)
        match = re.search(r'\[(.|\n)*\]', text)
        if match:
            json_str = match.group(0)
            json_str = json_str.replace('\n', '').replace('\r', '')
            try:
                # Use demjson3 for tolerant parsing
                questions = demjson3.decode(json_str)
                # Normalize options for each question (handles strings or dicts)
                for q in questions:
                    q["options"] = [
                        opt if isinstance(opt, str) else opt.get("text", "")
                        for opt in q.get("options", [])
                    ]
                return questions
            except Exception as e:
                print("Error parsing (demjson3) cleaned JSON string:", e)
                print(json_str)
                return None
        else:
            print("No JSON array found in model output.")
            return None
    else:
        print(f"Error: {response.status_code}")
        return None

ollama_prompt = """
You are an expert on Prince Edward Island (PEI) road rules and driver's license exams.
Generate a list of 3 new, intelligent multiple-choice questions to help someone practice for the PEI driver's license written exam.
Your answer MUST be in this exact JSON format, with no explanations or extra text:
[
  {
    "question": "Question text?",
    "options": ["A) ...", "B) ...", "C) ...", "D) ..."],
    "answer": "B"
  }
]
"""

def run_quiz():
    questions = generate_questions_with_ollama(ollama_prompt)
    if not questions:
        print("No valid questions generated.")
        return
    score = 0
    for idx, q in enumerate(questions, 1):
        print(f"\nQ{idx}: {q['question']}")
        for opt in q["options"]:
            print(opt)
        ans = input("Your answer (A/B/C/D): ").strip().upper()
        if ans == q["answer"].upper():
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer is: {q['answer']}")
    print(f"\nQuiz complete! Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()
