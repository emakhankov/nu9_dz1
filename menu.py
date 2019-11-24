def menu(caption, questions, answers):
    print(caption)
    for q in questions:
        print(q)
    while True:
        inp = input('Введите значение пункта: ')
        if inp in answers:
            return inp
        print('Неверный пункт, повторите заново')