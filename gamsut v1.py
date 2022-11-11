import random
while True:
    print('Mode Permainan:')
    print('1. VS Komputer')
    print('2. VS Player\n')
    mode = input('Pilih mode permainan: ')
    if mode == '1':
        player_name = input('Masukkan nama pemain: ')
        try:
            ronde = int(input('Masukkan jumlah ronde: '))
            my_list = ['Batu', 'Kertas', 'Gunting']
            K = 0
            AI = 0
            for x in range(ronde):
                x += 1
                kamu = input(f'Masukkan gerakan kamu ke {x}: ')
                ai = random.choice(my_list)
                print(f'Gerakan AI ke {x}: {ai}')
                if (kamu == 'Batu' or kamu == 'batu') and ai == 'Kertas':
                    AI += 1
                    print('Poin untuk lawan!')
                if (kamu == 'Kertas' or kamu == 'kertas') and ai == 'Batu' :
                    K += 1
                    print('Poin untuk kamu!')
                if (kamu == 'Batu' or kamu == 'batu') and ai == 'Gunting':
                    K += 1
                    print('Poin untuk kamu!')
                if (kamu == 'Gunting' or kamu == 'gunting') and ai == 'Batu':
                    AI += 1
                    print('Poin untuk lawan!')
                if (kamu == 'Kertas' or kamu == 'kertas') and ai == 'Gunting':
                    AI += 1
                    print('Poin untuk lawan!')
                if (kamu == 'Gunting' or kamu == 'gunting') and ai == 'Kertas':
                    K += 1
                    print('Poin untuk kamu!')
                if (kamu == 'Gunting' or kamu == 'gunting') and ai == 'Gunting':
                    print('Seri!')
                if (kamu == 'Kertas' or kamu == 'kertas') and ai == 'Kertas':
                    print('Seri!')
                if (kamu == 'Batu' or kamu == 'batu') and ai == 'Batu':
                    print('Seri!')
            if K > AI:
                print(f'\nSelamat {player_name}! Kamu adalah pemenangnya!.')
            elif K < AI:
                print(f'\nYahh.. {player_name} kamu kalah.')
            else:
                print('\nPermainan berakhir seri.')
        except ValueError:
            print('input only number plzz')

    if mode == '2':
        try:
            ronde = int(input('Masukkan jumlah ronde: '))
            P1 = 0
            P2 = 0
            for x in range(ronde):
                x += 1
                gerakan_p1 = input(f'Masukkan gerakan Player 1 ke {x}: ')
                gerakan_p2 = input(f'Masukkan gerakan Player 2 ke {x}: ')
                if (gerakan_p1 == 'Batu' or gerakan_p1 == 'batu') and (gerakan_p2 == 'Kertas' or gerakan_p2 == 'kertas'):
                    P2 += 1
                    print('Poin untuk Player 2!')
                if (gerakan_p1 == 'Kertas' or gerakan_p1 == 'kertas') and (gerakan_p2 == 'Batu' or gerakan_p2 == 'batu'):
                    P1 += 1
                    print('Poin untuk Player 1!')
                if (gerakan_p1 == 'Batu' or gerakan_p1 == 'batu') and (gerakan_p2 == 'Gunting' or gerakan_p2 == 'gunting'):
                    P1 += 1
                    print('Poin untuk Player 1!')
                if (gerakan_p1 == 'Gunting' or gerakan_p1 == 'gunting') and (gerakan_p2 == 'Batu' or gerakan_p2 == 'batu'):
                    P2 += 1
                    print('Poin untuk Player 2!')
                if (gerakan_p1 == 'Kertas' or gerakan_p1 == 'kertas') and (gerakan_p2 == 'Gunting' or gerakan_p2 == 'gunting'):
                    P2 += 1
                    print('Poin untuk Player 2!')
                if (gerakan_p1 == 'Gunting' or gerakan_p1 == 'gunting') and (gerakan_p2 == 'Kertas' or gerakan_p2 == 'kertas'):
                    P1 += 1
                    print('Poin untuk Player 1!')
                if (gerakan_p1 == 'Gunting' or gerakan_p1 == 'gunting') and (gerakan_p2 == 'Gunting' or gerakan_p2 == 'gunting'):
                    print('Seri!')
                if (gerakan_p1 == 'Kertas' or gerakan_p1 == 'kertas') and (gerakan_p2 == 'Kertas' or gerakan_p2 == 'kertas'):
                    print('Seri!')
                if (gerakan_p1 == 'Batu' or gerakan_p1 == 'batu') and (gerakan_p2 == 'Batu' or gerakan_p2 == 'batu'):
                    print('Seri!')
            if P1 > P2:
                print('\nPemenangnya adalah Player 1.')
            elif P1 < P2:
                print('\nPemenangnya adalah Player 2.')
            else:
                print('\nPermainan berakhir seri.')
        except ValueError:
            print('input only number plzz..')
    elif mode != 1 and mode != 2:
        print('Please chose between 1 or 2\n')
        pass
