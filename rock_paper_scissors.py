from random import randint

def user_interface(options) -> int:
    '''
    Функция представления опций и запроса на выбор опции игроку
    Возвращает: int
    '''
    for index,option in enumerate(options):
        print(f'{index} = {option}')

    user_input = int(input('Что вы выбираете? '))
    return user_input


def computer_choice(content) -> int:
    '''
    Функция иметирует выбор компьютера, случайный выбор на основе доступных опреаций
    Возвращает: случайный int
    '''
    computer_chose = randint(0,len(content)-1)
    return computer_chose
    

def check_results(choices, player, computer) -> str:
    '''
    Функция которая проверяет кто выйграл
    Возвращает: str
    '''
    if player == computer:
        return 'Ничья'
    elif (player == 0 and computer == len(choices)-1) or (player>computer and not(player==len(choices)-1 and computer==0)):
        return 'Вы выйграли'
    return 'Вы проиграли'


def play():
    """
    Функция логики игры
    Возвращает: None
    """

    print('''
    ---------------------------------
    Сделайте выбор
    ''')

    #определите варианты и попросите участников выбрать один
    options_list = ['Камень', 'Бумага' , 'Ножници']
    player_result = user_interface(options_list)
    computer_result = computer_choice(options_list)
    
    #визуальное представление в терминале, чтобы мы могли видеть, что выбрали обе стороны
    print(f'      Вы выбрали: {options_list[player_result]}')
    print(f'Противник выбрал: {options_list[computer_result]}')

    #проверка результов между этими двумя и выведите победителя.
    results = check_results(options_list,player_result,computer_result)
    print (f'\n{results}')

def main():
    """
    Жизненный цикл игры
    """
    play_again = ''
    while play_again.lower() != 'n':
        play()
        print (f'Повторить игру?')
        play_again = input('\'y\' - да, \'n\' нет: ')

main()