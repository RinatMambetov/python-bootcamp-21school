from src.calculation import calculate_averages
from src.decision import make_decision
from src.json_reader import read_json
from src.user_interaction import prompt_user


def main():
    """Main function that runs the program."""
    
    questions = read_json('src/questions.json')

    responses = []
    variables = []
    for q in questions:
        response, var = prompt_user(q['question'], q['responses'])
        responses.append(response)
        variables.append(var)

    averages = calculate_averages(variables)

    decision = make_decision(averages)

    print("Based on the variable measurements, the responding subject is a", decision)


if __name__ == '__main__':
    main()
