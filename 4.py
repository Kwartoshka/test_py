import json
import sys
from pprint import pprint


def count_questions(data: dict):
    questions_count = 0
    rounds = data['game']['rounds']
    for round in  rounds:
        for question in round['questions']:
            questions_count += 1
    print(questions_count)
    return questions_count


def print_right_answers(data: dict):
    # вывести все правильные ответы (correct_answer)
    correct_answers = []
    rounds = data['game']['rounds']
    for round in rounds:
        for question in round['questions']:
            correct_answers.append(question['correct_answer'])
    print(correct_answers)
    return correct_answers


def print_max_answer_time(data: dict):
    # вывести максимальное время ответа (time_to_answer)
    max_time_to_answer = 0
    times = []
    rounds = data['game']['rounds']
    for round in rounds:
        settings = round.get('settings')
        round_time = settings.get('time_to_answer')
        if round_time:
            max_time_to_answer = round_time if round_time > max_time_to_answer else max_time_to_answer

        for question in round['questions']:
            question_time = question.get('time_to_answer')
            if question_time:
                max_time_to_answer = question_time if question_time > max_time_to_answer else max_time_to_answer
    print(max_time_to_answer)
    return max_time_to_answer


def main(file):
    # загрузить данные из test.json файла
    with open(file) as f:
        data = json.load(f)
    count_questions(data)
    print_right_answers(data)
    print_max_answer_time(data)


if __name__ == '__main__':
    # передать имя файла из аргументов командной строки
    file = sys.argv[1]
    main(file)
