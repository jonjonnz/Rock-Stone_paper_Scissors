import random

computer_choices = ['R', 'P', 'S']
difficulty_level = ['Easy', 'Medium', 'Hard']


def winner(pc, cc):
    if (pc.lower() == 'r' and cc.lower() == 'p') or (pc.lower() == 'p' and cc.lower() == 's') or (pc.lower() == 's' and cc.lower() == 'r'):
        return 'computer'
    elif (cc.lower() == 'r' and pc.lower() == 'p') or (cc.lower() == 'p' and pc.lower() == 's') or (cc.lower() == 's' and pc.lower() == 'r'):
        return 'player'
    else:
        return 'tie'

# TODO
def comp_choice(dl, ppc, pcc, pw):
    if dl == 'e':
        cc = random.choice(computer_choices)[0]
    elif dl == 'm':
        cc = random.choice(computer_choices)[0]
        return cc
    elif dl == 'h':
        cc = random.choice(computer_choices)[0]


# set difficulty
def sps():
    for i in difficulty_level:
        print('1.' + i + '(' + i[0] + ')')
    dl = input('Select Difficulty level : ').lower()
    if dl in ['e', 'm', 'h']:
        game_on = True
        player_score = 0
        computer_score = 0
        win = ''
        prev_pc = None
        prev_cc = None
        prev_win = None
        while game_on:
            player_choice = input('Rock(R) Paper(P) Scissor(S) ? : ')[0].lower()
            if player_choice in ['r', 's', 'p']:
                computer_choice = comp_choice(dl, prev_pc, prev_cc, prev_win)
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
        return False
    else:
        return True


# game loop


game_started = True
new_game = 'y'
while game_started:
    if new_game == 'y':
        if sps():
            print('Please select the correct options')
            continue
    new_game = input('Start a new game ? (y/n): ')
    if new_game == 'y':
        continue
    elif new_game == 'n':
        game_started = False
    else:
        print('Please enter "y" for a new game or "n" to quit')

