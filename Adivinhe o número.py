#Adivinhe o número:
#Tente adivinhar o número que estou pensando, eu lhe direi dicas até que ele seja acertado! Quanto menos dicas você usar mais pontos você ganha,você tem 10 chances de acertar!
from random import randint
x = randint(1,101)
scr = 100
loop = 1
while loop < 10:
	if loop == 1:
		val = int(input('Digite um número de 1 a 100: \n'))
		if val != x:
			scr -= 10
	if x != val:
		if val > x:
			val = int(input(f'O número que estou pensando é menor que {val}: \n'))
			scr -= 10
		if val < x:
			val = int(input(f'O número que estou pensando é maior que {val}: \n'))
			scr -= 10
	else:
		break
	loop += 1
if x == val:
	print(f'Parabéns, o número era {val}')
else:
	print('GAME OVER!')
print(f'SCORE: {scr}')
