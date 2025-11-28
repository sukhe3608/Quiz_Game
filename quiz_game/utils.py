import json
from quiz_game.question import Question

def load_questions(file_path: str) -> list:

    questions =[]
    
    try : 
        with open(file_path,'r') as file:
            data = json.load(file)
        for item in data:
            ques = Question(
                question = item['question'],
                options = item['options'],
                answer = item['answer']
            )

            questions.append(ques)

    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")

    return questions


def save_score(file_path: str, name: str, score: int):
    try:
        try:
            with open(file_path, 'r') as file:
                high_scores = json.load(file)
        except FileNotFoundError:
            high_scores = []

        high_scores.append({'name': name, 'score': score})
        high_scores = sorted(high_scores, key=lambda x: x['score'], reverse=True)[:10]

        with open(file_path, 'w') as file:
            json.dump(high_scores, file, indent=4)

    except Exception as e:
        print(f"Error saving score: {e}")


        