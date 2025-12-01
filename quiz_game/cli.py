from quiz_game.utils import load_questions, save_score
from quiz_game.game import QuizGame

def main_menu():
    print("\n====== Quiz Game Main Menu ======")
    print("1. Start Quiz")
    print("2. Exit")
    choice = input("Select an option (1-2): ")
    return choice

def run():
    while True:
        choice = main_menu()
        if choice == '1':
            questions = load_questions('data/questions.json')
            if not questions:
                print("No questions available to start the quiz.")
                continue

            game = QuizGame(questions)
            game.start()

            name = input("Enter your name for the high score list: ")
            save_score('high_scores.json', name, game.score)

        elif choice == '2':
            print("Thank you for playing! Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")




