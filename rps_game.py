import random

computer_choices = ['R', 'P', 'S']


def winner(pc, cc):
    if (pc.lower() == 'r' and cc.lower() == 'p') or (pc.lower() == 'p' and cc.lower() == 's') or (pc.lower() == 's' and cc.lower() == 'r'):
        return 'computer'
    elif (cc.lower() == 'r' and pc.lower() == 'p') or (cc.lower() == 'p' and pc.lower() == 's') or (cc.lower() == 's' and pc.lower() == 'r'):
        return 'player'
    else:
        return 'tie'


def comp_choice():
    return random.choice(computer_choices)[0]


def sps():
    game_on = True
    player_score = 0
    computer_score = 0
    win = ''
    while game_on:
        player_choice = input('Rock(R) Paper(P) Scissor(S) ? : ')[0].lower()
        if player_choice in ['r', 's', 'p']:
            computer_choice = comp_choice()
            win = winner(player_choice, computer_choice)
            if win == 'player':
                player_score += 1
                print(win + ' won')
            elif win == 'computer':
                computer_score += 1
                print(win + ' won')
            else:
                print(win)
            print("Player  | Computer")
            print("{}       | {}      ".format(player_score, computer_score))
            if player_score == 5 or computer_score == 5:
                game_on = False
                win = 'Player' if player_score == 5 else 'Computer'
            prev_pc = player_choice
            prev_cc = computer_choice
            prev_win = win[0].lower()
        else:
            print('Please enter one of the correct options')
    print('Game won by {}'.format(win))


game_started = True
new_game = 'y'
while game_started:
    if new_game == 'y':
        sps()
    new_game = input('Start a new game ? (y/n): ')
    if new_game == 'y':
        continue
    elif new_game == 'n':
        game_started = False
    else:
        print('Please enter "y" for a new game or "n" to quit')
