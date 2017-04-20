import math
#function [X_norm, mu, sigma] = normalizar(X)
def normalizar(X):

	"""
	NORMALIZAR normaliza os atributos em X
		NORMALIZAR(X) retorna uma versao normalizada de X onde o valor da
		media de cada atributo eh 0 e desvio padrao eh igual a 1. Trata-se de
		um importante passo de pre-processamento quando trabalha-se com 
		metodos de aprendizado de maquina.
	"""

	# Calcula a quantidade de amostra e de atributos
	#[m, n] = size(X); # m = qtde de objetos e n = qtde de atributos por objeto
	[m, n] = len(X), len(X[0])

	# Incializa as variaves de saida
	#X_norm = zeros(m,n); # inicializa X_norm

	mu = 0; # inicializa media

	sigma = 1; # inicializa desvio padrao


	# ====================== ESCREVA O SEU CODIGO AQUI ======================
	# Instrucoes: Calcule a media de cada atributo de X e armazene em mu. Note
	#             que se X for uma matriz (m x n), entao mu tera que ser um
	#             vetor (1 x n), no qual cada coluna de mu devera conter o 
	#             valor da media de cada um dos n atributos. O mesmo devera ser
	#             feito para o desvio padrao, que devera ser armazenado em
	#             sigma. 
	#             Sugestao: use os comandos mean e std para calcular a media e 
	#             o desvio padrao, respectivamente.
	#             
	#             Uma vez encontrados os valores de mu e de sigma, calcule o
	#             valor do atributo X normalizado. Para isso, para cada amostra
	#             x_i de X sera necessario calcular (x_i - mu)/sigma e
	#             armazenar em X_norm (base de dados normalizada).
	#
	#

	mu = map(lambda SUMS: SUMS/float(len(X)) , [sum(col) for col in zip(*X)])

	sigma = [math.sqrt(sum(deviations)/float(m-1)) for deviations in zip(*[map(lambda n1, n2: (n1 - n2) ** 2, mu, xi) for xi in X ])]

	X_norm = [map(lambda x_i, mu_i, sig_i: (x_i - mu_i)/float(sig_i), xii, mu, sigma)  for xii in [xi for xi in X]]

	return (X_norm, mu, sigma)
