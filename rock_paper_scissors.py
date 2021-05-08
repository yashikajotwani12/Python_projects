import random

def play():
        user=input("What's your choice?' r ' for rock, ' p' for paper, ' s ' for scissors :::: ")
        computer = random.choice(['r','p','s'])
     
        if user == computer:
                    return 'Tie'

        if is_win(user, computer):
                  return f'{computer} was chosen by computer...You Won!'

        return f'{computer} was chosen by computer...You Lost!'

def is_win(player , opponent):
    if(player =='r' and opponent =='s') or(player=='s' and opponent=='p') or (player=='p' and opponent=='r'):
        return True


print(play())
