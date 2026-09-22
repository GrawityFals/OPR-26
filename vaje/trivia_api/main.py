from random import shuffle
from requests import get, Response

def call_api() -> dict | None:
    url: str = "https://opentdb.com/api.php?amount=10&type=multiple"

    response: Response = get(url=url)

    if response.status_code == 200:
        return response.json()
    

def main() -> None:
    data: dict | None = call_api()
    questions: dict = data["results"]

    score: int = 0
    
    for question in questions:
        print("-"*50)
        print(f"[{question["difficulty"]}] {question["category"]}")
        print("-"*50)

        print(question["question"])
        answers: list[str] = question["incorrect_answers"] + [question["correct_answer"]]
        shuffle(answers)

        for i, answer in enumerate(answers):
            print([i], answer)

        if answers[int(input())] == question["correct_answer"]:
            score += 1
            print(f"CORRECT: {score}/10")
        else:
            print(f"WRONG correct answer was: {question["correct_answer"]}")

    print(f"You scored {score}/10")


if __name__ == "__main__":
    main()
