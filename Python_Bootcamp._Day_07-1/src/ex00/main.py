from calculation import calculate_averages
from decision import make_decision
from json_reader import read_json
from user_interaction import prompt_user


def main():
    questions = read_json('questions.json')

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
