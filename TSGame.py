from random import randint
import TSLyrics as RL
from colorama import Fore

# Song names
Songs = ['Lavender Haze', 'Maroon', 'Anti-Hero', 'Snow on the Beach', 'Youre on your own, kid', 'Midnight Rain', 'Question...?', 'Vigilante Shit', 'Bejewelled', 'Labyrinth', 'Karma', 'Sweet Nothing', 'Mastermind']


def Main():
    # LL = length 0f lyrics
    LL = 0
    print('Bem vinda ao Joguinho da Taylor swift, aproveite sua estadia')

    # Start playing loop
    while True:
        s = randint(0, len(Songs))
        diff = str(input('Qual dificuldade Você quer jogar? [F/M/D]: '))
        if diff.upper() not in 'FMD':
            print('Você colocou algo errado aí')
            exit()

        # Checking difficulty and starting the code
        if diff.upper() == 'F':
            tries = 5
            print(Fore.GREEN)
            if s == 0:
                LL = len(RL.Zero())
                part = randint(0, LL)
                while 'oh'.upper() in RL.Zero()[part:part+20].upper() or part+50 > LL or ' ' not in RL.Zero()[part]  or ' ' not in RL.Zero()[part+50] :
                    part = randint(0, LL)
                print(RL.Zero()[part:part+50])
            if s == 1:
                LL = len(RL.One())
                part = randint(0, LL)
                while 'oh'.upper() in RL.One()[part:part+20].upper() or part+50 > LL or ' ' not in RL.One()[part]  or ' ' not in RL.Zero()[part+50]:
                    part = randint(0, LL)
                print(RL.One()[part:part+50])
            if s == 2:
                LL = len(RL.Two())
                part = randint(0, LL)
                while 'oh'.upper() in RL.Two()[part:part+20].upper() or part+50 > LL or ' ' not in RL.Two()[part]  or ' ' not in RL.Two()[part+50]:
                    part = randint(0, LL)
                print(RL.Two()[part:part+50])
            if s == 3:
                LL = len(RL.Three())
                part = randint(0, LL)
                while 'oh'.upper() in RL.Three()[part:part+20].upper() or part+50 > LL or ' ' not in RL.Three()[part]  or ' ' not in RL.Three()[part+50]:
                    part = randint(0, LL)
                print(RL.Three()[part:part+50])
            if s == 4:
                LL = len(RL.Four())
                part = randint(0, LL)
                while 'oh'.upper() in RL.Four()[part:part+20].upper() or part+50 > LL or ' ' not in RL.Four()[part]  or ' ' not in RL.Four()[part+50]:
                    part = randint(0, LL)
                print(RL.Four()[part:part+50])
            if s == 5:
                LL = len(RL.Five())
                part = randint(0, LL)
                while 'oh'.upper() in RL.Five()[part:part+20].upper() or part+50 > LL or ' ' not in RL.Five()[part]  or ' ' not in RL.Five()[part+50]:
                    part = randint(0, LL)
                print(RL.Five()[part:part+50])
            if s == 6:
                LL = len(RL.Six())
                part = randint(0, LL)
                while 'oh'.upper() in RL.Six()[part:part+20].upper() or part+50 > LL or ' ' not in RL.Six()[part]  or ' ' not in RL.Six()[part+50]:
                    part = randint(0, LL) 
                print(RL.Six()[part:part+50])
            if s == 7:
                LL = len(RL.Seven())
                part = randint(0, LL)
                while 'oh'.upper() in RL.Seven()[part:part+20].upper() or part+50 > LL or ' ' not in RL.Seven()[part]  or ' ' not in RL.Seven()[part+50]:
                    part = randint(0, LL)
                print(RL.Seven()[part:part+50])
            if s == 8:
                LL = len(RL.Eight())
                part = randint(0, LL)
                while 'oh'.upper() in RL.Eight()[part:part+20].upper() or part+50 > LL or ' ' not in RL.Eight()[part]  or ' ' not in RL.Eight()[part+50]:
                    part = randint(0, LL)
                print(RL.Eight()[part:part+50])
            if s == 9:
                LL = len(RL.Nine())
                part = randint(0, LL)
                while 'oh'.upper() in RL.Nine()[part:part+20].upper() or part+50 > LL or ' ' not in RL.Nine()[part]  or ' ' not in RL.Nine()[part+50]:
                    part = randint(0, LL)
                print(RL.Nine()[part:part+50])
            if s == 10:
                LL = len(RL.Ten())
                part = randint(0, LL)
                while 'oh'.upper() in RL.Ten()[part:part+20].upper() or part+50 > LL or ' ' not in RL.Ten()[part]  or ' ' not in RL.Ten()[part+50]:
                    part = randint(0, LL)
                print(RL.Ten()[part:part+50])
            if s == 11:
                LL = len(RL.Eleven())
                part = randint(0, LL)
                while 'oh'.upper() in RL.Eleven()[part:part+20].upper() or part+50 > LL or ' ' not in RL.Eleven()[part]  or ' ' not in RL.Eleven()[part+50]:
                    part = randint(0, LL)
                print(RL.Eleven()[part:part+50])
            if s == 12:
                LL = len(RL.Twelve())
                part = randint(0, LL)
                while 'oh'.upper() in RL.Twelve()[part:part+20].upper() or part+50 > LL or ' ' not in RL.Twelve()[part]  or ' ' not in RL.Twelve()[part+50]:
                    part = randint(0, LL)
                print(RL.Twelve()[part:part+50])


        elif diff.upper() == 'M':
            tries = 3
            print(Fore.YELLOW)
            if s == 0:
                LL = len(RL.Zero())
                part = randint(0, LL)
                while 'oh'.upper() in RL.Zero()[part:part+20].upper() or Songs[s] in RL.Zero()[part:part+30] or part+30 > LL:
                    part = randint(0, LL)
                print(RL.Zero()[part:part+30])
            if s == 1:
                LL = len(RL.One())
                part = randint(0, LL)
                while 'oh'.upper() in RL.One()[part:part+20].upper() or part+30 > LL or Songs[s] in RL.One()[part:part+30]:
                    part = randint(0, LL)
                print(RL.One()[part:part+30])
            if s == 2:
                LL = len(RL.Two())
                part = randint(0, LL)
                while 'oh'.upper() in RL.Two()[part:part+20].upper() or part+30 > LL or Songs[s] in RL.Two()[part:part+30]:
                    part = randint(0, LL)
                print(RL.Two()[part:part+30])
            if s == 3:
                LL = len(RL.Three())
                part = randint(0, LL)
                while 'oh'.upper() in RL.Three()[part:part+20].upper() or part+30 > LL or Songs[s] in RL.Three()[part:part+30]:
                    part = randint(0, LL)
                print(RL.Three()[part:part+30])
            if s == 4:
                LL = len(RL.Four())
                part = randint(0, LL)
                while 'oh'.upper() in RL.Four()[part:part+20].upper() or part+30 > LL or Songs[s] in RL.Four()[part:part+30]:
                    part = randint(0, LL)
                print(RL.Four()[part:part+30])
            if s == 5:
                LL = len(RL.Five())
                part = randint(0, LL)
                while 'oh'.upper() in RL.Five()[part:part+20].upper() or part+30 > LL or Songs[s] in RL.Five()[part:part+30]:
                    part = randint(0, LL)
                print(RL.Five()[part:part+30])
            if s == 6:
                LL = len(RL.Six())
                part = randint(0, LL)
                while 'oh'.upper() in RL.Six()[part:part+20].upper() or part+30 > LL or Songs[s] in RL.Six()[part:part+30]:
                    part = randint(0, LL)
                print(RL.Six()[part:part+30])
            if s == 7:
                LL = len(RL.Seven())
                part = randint(0, LL)
                while 'oh'.upper() in RL.Seven()[part:part+20].upper() or part+30 > LL or Songs[s] in RL.Seven()[part:part+30]:
                    part = randint(0, LL)
                print(RL.Seven()[part:part+30])
            if s == 8:
                LL = len(RL.Eight())
                part = randint(0, LL)
                while 'oh'.upper() in RL.Eight()[part:part+20].upper() or part+30 > LL or Songs[s] in RL.Eight()[part:part+30]:
                    part = randint(0, LL)
                print(RL.Eight()[part:part+30])
            if s == 9:
                LL = len(RL.Nine())
                part = randint(0, LL)
                while 'oh'.upper() in RL.Nine()[part:part+20].upper() or part+30 > LL or Songs[s] in RL.Nine()[part:part+30]:
                    part = randint(0, LL)
                print(RL.Nine()[part:part+30])
            if s == 10:
                LL = len(RL.Ten())
                part = randint(0, LL)
                while 'oh'.upper() in RL.Ten()[part:part+20].upper() or part+30 > LL or Songs[s] in RL.Ten()[part:part+30]:
                    part = randint(0, LL)
                print(RL.Ten()[part:part+30])
            if s == 11:
                LL = len(RL.Eleven())
                part = randint(0, LL)
                while 'oh'.upper() in RL.Eleven()[part:part+20].upper() or part+30 > LL or Songs[s] in RL.Eleven()[part:part+30]:
                    part = randint(0, LL)
                print(RL.Eleven()[part:part+30])
            if s == 12:
                LL = len(RL.Twelve())
                part = randint(0, LL)
                while 'oh'.upper() in RL.Twelve()[part:part+20].upper() or part+30 > LL or Songs[s] in RL.Twelve()[part:part+30]:
                    part = randint(0, LL)
                print(RL.Twelve()[part:part+30])
        elif diff.upper() == 'D':
            tries = 2
            print(Fore.RED)
            if s == 0:
                LL = len(RL.Zero())
                part = randint(0, LL)
                while Songs[s] in RL.Zero()[part:part+20] or part+20 > LL:
                    part = randint(0, LL)
                print(RL.Zero()[part:part+20])
            if s == 1:
                LL = len(RL.One())
                part = randint(0, LL)
                while Songs[s] in RL.One()[part:part+20] or part+20 > LL:
                    part = randint(0, LL)
                print(RL.One()[part:part+20])
            if s == 2:
                LL = len(RL.Two())
                part = randint(0, LL)
                while Songs[s] in RL.Two()[part:part+20] or part+20 > LL:
                    part = randint(0, LL)
                print(RL.Two()[part:part+20])
            if s == 3:
                LL = len(RL.Three())
                part = randint(0, LL)
                while Songs[s] in RL.Three()[part:part+20] or part+20 > LL:
                    part = randint(0, LL)
                print(RL.Three()[part:part+20])
            if s == 4:
                LL = len(RL.Four())
                part = randint(0, LL)
                while Songs[s] in RL.Four()[part:part+20] or part+20 > LL:
                    part = randint(0, LL)
                print(RL.Four()[part:part+20])
            if s == 5:
                LL = len(RL.Five())
                part = randint(0, LL)
                while Songs[s] in RL.Five()[part:part+20] or part+20 > LL:
                    part = randint(0, LL)
                print(RL.Five()[part:part+20])
            if s == 6:
                LL = len(RL.Six())
                part = randint(0, LL)
                while Songs[s] in RL.Six()[part:part+20] or part+20 > LL:
                    part = randint(0, LL)
                print(RL.Six()[part:part+20])
            if s == 7:
                LL = len(RL.Seven())
                part = randint(0, LL)
                while Songs[s] in RL.Seven()[part:part+20] or part+20 > LL:
                    part = randint(0, LL)
                print(RL.Seven()[part:part+20])
            if s == 8:
                LL = len(RL.Eight())
                part = randint(0, LL)
                while Songs[s] in RL.Eight()[part:part+20] or part+20 > LL:
                    part = randint(0, LL)
                print(RL.Eight()[part:part+20])
            if s == 9:
                LL = len(RL.Nine())
                part = randint(0, LL)
                while Songs[s] in RL.Nine()[part:part+20] or part+20 > LL:
                    part = randint(0, LL)
                print(RL.Nine()[part:part+20])
            if s == 10:
                LL = len(RL.Ten())
                part = randint(0, LL)
                while Songs[s] in RL.Ten()[part:part+20] or part+20 > LL:
                    part = randint(0, LL)
                print(RL.Ten()[part:part+20])
            if s == 11:
                LL = len(RL.Eleven())
                part = randint(0, LL)
                while Songs[s] in RL.Eleven()[part:part+20] or part+20 > LL:
                    part = randint(0, LL)
                print(RL.Eleven()[part:part+20])
            if s == 12:
                LL = len(RL.Twelve())
                part = randint(0, LL)
                while Songs[s] in RL.Twelve()[part:part+20] or part+20 > LL:
                    part = randint(0, LL)
                print(RL.Twelve()[part:part+20])
                        


        answer = 'Whatever'
        while answer.upper() != Songs[s].upper():
            print(Fore.MAGENTA +f'Você tem {tries} tentativas')
            answer = str(input(Fore.CYAN + 'Qual é a música? '))
            if answer.upper() != Songs[s].upper():
                tries -= 1
                print(Fore.RED + 'Errou!')
            elif answer.upper() == Songs[s].upper():
                print(Fore.GREEN + 'Acertou, muito bem!')
            if tries == 0:
                print(Fore.RED + 'Você perdeu, Muito poser')
                print(f'A resposta era {Songs[s]}')
                break
        yn = str(input(Fore.CYAN + 'Quer Jogar de novo? [S/N]: ').upper())
        if yn == 'N':
            print(Fore.CYAN + 'Obrigado por Jogar')
            print(Fore.RESET)
            break
        
        elif yn == 'S':
            pass
        else:
            print('Vou aceitar como um sim')
            pass
        print(Fore.RESET)

Main()
