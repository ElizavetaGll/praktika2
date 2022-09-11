def test():
    group = {
        'dkmo-21': 'Технология разработки',
        'dkms-21': 'Разработка программных модулей',
        'dkmo -22': 'Разработка мобильных приложений',
        'dkmo -22/1': 'Тестирование программного обеспечения'
    }

    print(group['dkms-21'])

    for key in group.values():
        print(key)

    newGroup = 'dkmo -22/2'
    newDisciplineValue = 'Разработка баз данных'

    if newGroup in group:
        print('Ok')

    else:
        group[newGroup] = newDisciplineValue

    print(group)

    print(group.setdefault('dkems-21', 'Системы облачного хранения'))

    for key in group.values():
        print(key)


def example():

    states = {
        'Россия': 'RU',
        'Германия': 'DE',
        'Узбекистан': 'UZ',
        'Зимбабве': 'ZW',
        'Турция': 'TR'
    }

    cities = {
        'UZ': 'Газли',
        'TR': 'Сарыгерме',
        'DE': 'Мюнхен'
    }

    cities['ZW'] = 'Гверу'
    cities['RU'] = 'Москва'

    print(' - ' * 10)
    print(" B стране ZW есть город: ", cities['ZW'])
    print(" В стране RU есть город: ", cities['RU'])

    print(' - ' * 10)
    print("Аббревиатура Турции: ", states['Турция'])
    print("Аббревиатура Германии: ", states['Германия'])

    print('-' * 10)
    print("В Турции есть город: ", cities[states['Турция']])
    print("В Германии есть город: ", cities[states['Германия']])

    print('-' * 10)
    for state, abbrev in list(states.items()):
        print(f"{state} имеет аббревиатуру {abbrev}")

    print('-' * 10)
    for abbrev, city in list(cities.items()):
        print(f"B стране {abbrev} есть город {city}")

    print('-' * 10)
    for state, abbrev in list(states.items()):
        print(f"B стране {state} используется аббревиатура {abbrev}")
        print(f"И есть город {cities[abbrev]}")

    print('-' * 10)
    state = states.get('СССP')

    if not state:
        print("npoшу прощения, СССР распался.")

def resolve():

    states = {
        'Московская область': 'MSK',
        'Ростовская область': 'RV',
        'Краснодарская область': 'KR',
        'Томская область': 'TM',
        'Брянская область': 'BR'
    }

    cities = {
        'MSK': 'Москва',
        'RV': 'Ростов-на-Дону',
        'KR': 'Краснодар',
        'TM': 'Томск',
        'BR': 'Брянск'
    }

    print(' - ' * 10)
    print(" B области MSK есть город: ", cities['MSK'])
    print(" В области RV есть город: ", cities['RV'])

    print(' - ' * 10)
    print("Аббревиатура Московской области: ", states['Московская область'])
    print("Аббревиатура Ростовской области: ", states['Ростовская область'])

    print('-' * 10)
    print("В Московсковской области есть город: ", cities[states['Московская область']])
    print("В Ростовской области есть город: ", cities[states['Ростовская область']])

    print('-' * 10)
    for state, abbrev in list(states.items()):
        print(f"{state} имеет аббревиатуру {abbrev}")

    print('-' * 10)
    for abbrev, city in list(cities.items()):
        print(f"B области {abbrev} есть город {city}")

    print('-' * 10)
    for state, abbrev in list(states.items()):
        print(f"B области {state} используется аббревиатура {abbrev}")
        print(f"И есть город {cities[abbrev]}")

resolve()
