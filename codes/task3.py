import math

init = {'Лопахин':
            {'Должность': 'купец',
             'Возраст': 35,
             'Пол': 'Мужской'},
        'Фирс':
            {'Должность': 'лакей',
             'Возраст': None,
             'Пол': 'Мужской'},
        'Трофимов':
            {'Должность': 'Дворянин',
             'Возраст': 47,
             'Пол': 'Мужской'},
        'Яша': {'Должность': 'лакей',
                'Возраст': 28,
                'Пол': 'Мужской'},
        'Варя': {'Должность': 'воспитанница',
                 'Возраст': 24,
                 'Пол': 'Женский'},
        'Аня': {'Должность': 'дочь',
                'Возраст': 17,
                'Пол': 'Женский'},
        'Дуняшка': {'Должность': 'горничная',
                    'Возраст': None,
                    'Пол': 'Женский'},
        'Шарлотта': {'Должность': 'гувернантка',
                     'Возраст': 40,
                     'Пол': 'Женский'},
        'Раневская': {'Должность': 'Дворянка',
                      'Возраст': 32,
                      'Пол': 'Женский'}}


def main():
    age_males = 0
    age_females = 0
    count_males = 0
    count_females = 0
    for name, details in init.items():
        if details['Возраст'] is not None:
            if details['Пол'] == 'Женский':
                age_females += details['Возраст']
                count_females += 1
            if details['Пол'] == 'Мужской':
                age_males += details['Возраст']
                count_males += 1

    for name, details in init.items():
        if details['Возраст'] is None:
            if details['Пол'] == 'Женский':
                details['Возраст'] = int(age_females / count_females)
            if details['Пол'] == 'Мужской':
                details['Возраст'] = int(age_males / count_males)

    for name, details in init.items():
        if details['Пол'] == 'Мужской' and details['Возраст'] >= 30:
            print("{} {} {}".format(name, details['Возраст'], details['Должность']))
    for name, details in init.items():
        if details['Пол'] == 'Женский' and details['Возраст'] <= 24:
            print("{} {} {}".format(name, details['Возраст'], details['Должность']))

if __name__ == "__main__":
    main()
