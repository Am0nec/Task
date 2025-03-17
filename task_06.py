class WrongNumberOfPlayersError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NoSuchStrategyError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def rps_game_winner(array):
    if len(array) > 2:
        raise WrongNumberOfPlayersError('Количество игроков превышает 2-x')
    item1 = array[0][1]
    item2 = array[1][1]
    for i in range(0,2):
        if array[i][1] != 'S' and array[i][1] != 'P' and array[i][1] != 'R':
            raise NoSuchStrategyError('Нарушение правил игры')

    if item1 == item2:
        return array[0][0]
    elif (item1 == "R" and item2 == "S") or \
        (item1 == "S" and item2 == "P") or \
        (item1 == "P" and item2 == "R"):
        return array[0][0] + " " + array[0][1]
    else:
        return array[1][0] + " " + array[1][1]

try:
    started_list = [['player1', 'S'],['player2', 'P']]
    print(rps_game_winner(started_list))
except WrongNumberOfPlayersError as e:
    print(e)
except NoSuchStrategyError as e:
    print(e)
