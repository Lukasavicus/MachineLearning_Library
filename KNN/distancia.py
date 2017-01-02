import math
#function D = distancia(x, X)
def distancia(x, X):
	"""
	DISTANCIA calcula a distancia entre a amostra x e todos as amostras da 
	base X.
	D = DISTANCIA (x, X) retorna um vetor de distancias entre a amostra x 
	e todos as amostras da base X. Cada posicao Di = dist(x, Xi).
	"""

	#  Inicializa a variavel de retorno e algumas variaveis uteis
	#m = len(X[1]);  # Quantidade de objetos em X
	#D = zeros(m,1); # Inicializa a matriz de distancias D

	m = len(X[1])
	D = [0 for i in X[1]]

	# ====================== ESCREVA O SEU CODIGO AQUI ======================
	# Instrucoes: Implemente a funcao de similaridade. Teoricamente, voce pode 
	#             usar qualquer funcao de distancia. Porem, para este exercicio
	#             eh necessario usar a distancia Euclidiana (funcao norm).
	#
	# Obs: use um loop-for para calcular a distancia entre o objeto x e cada
	#      amostra Xi de X. O vetor D devera ter o mesmo numero de linhas de X.
	#

	D = [math.sqrt(sum(map(lambda n1, n2: (n1 - n2) ** 2, x, xi))) for xi in X ]

	return D