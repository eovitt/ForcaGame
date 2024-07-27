import random
from collections import Counter

algumasPalavras = '''maçã banana manga morango 
laranja uva abacaxi damasco limão coco melancia 
cereja mamão baga pêssego lichia melão'''

algumasPalavras = algumasPalavras.split(' ')
palavra = random.choice(algumasPalavras)

if __name__ == '__main__':
    print('Adivinhe a palavra!')

    for i in palavra:
        print('_', end=' ')
    print()

    jogando = True
    letrasAdivinhadas = ''
    chances = len(palavra) + 2
    correto = 0
    flag = 0

    try:
        while (chances != 0) and flag == 0:  
            print()
            chances -= 1

            try:
                palpite = str(input('Digite uma letra para adivinhar: '))
            except:
                print('Digite apenas uma letra!')
                continue
            if not palpite.isalpha():
                print('Digite apenas uma LETRA')
                continue
            elif len(palpite) > 1:
                print('Digite apenas UMA letra')
                continue
            elif palpite in letrasAdivinhadas:
                print('Você já adivinhou essa letra')
                continue
            if palpite in palavra:
                k = palavra.count(palpite)
                for _ in range(k):
                    letrasAdivinhadas += palpite  
            for char in palavra:
                if char in letrasAdivinhadas and (Counter(letrasAdivinhadas) != Counter(palavra)):
                    print(char, end=' ')
                    correto += 1
                elif (Counter(letrasAdivinhadas) == Counter(palavra)):
                   
                    print("A palavra é: ", end=' ')
                    print(palavra)
                    flag = 1
                    print('Parabéns, você venceu!')
                    break  
                else:
                    print('_', end=' ')
        if chances <= 0 and (Counter(letrasAdivinhadas) != Counter(palavra)):
            print()
            print('Você perdeu! Tente novamente..')
            print('A palavra era {}'.format(palavra))
    except KeyboardInterrupt:
        print()
        print('Tchau! Tente novamente.')
        exit()
