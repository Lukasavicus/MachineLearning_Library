#function [theta, J_historico] = gradienteDescente(X, y, theta, alpha, num_iter)
def gradienteDescente(X, y, theta, alpha, num_iter):
"""
GRADIENTEDESCENTE Executa o gradiente descente para aprender e otimizar theta
   theta = GRADIENTEDESENTE(X, y, theta, alpha, num_iter) atualiza theta usando 
   num_iter passos do gradiente com taxa de aprendizado alpha
"""

# Initializa algumas variaveis uteis
    m = len(y); # numero de exemplos de treinamento
    #J_historico = zeros(num_iter, 1);
    J_historico = [0 for i in range(num_iter)]

    for iterator in range(m)

        # ====================== ESCREVA O SEU CODIGO AQUI ====================
        # Instrucoes: Execute um unico passo do gradiente para ajustar o vetor
        #             theta. 
        #
        # Dica: para verificar se a o gradiente esta correto, verifique se a 
        #       funcao de custo (computarCusto) nunca aumenta de valor no 
        #       decorrer das iteracoes. Para facilitar, em ex02.m ha uma funcao
        #       que plota o custo J no decorrer das iteracoes. A linha nunca
        #       pode ser crescente. Se for, reduza alpha.
        #

        X_times_T = [sum(map(lambda m1, m2: m1 * m2, theta, x)) for x in X]
        XT_minus_Y = map(lambda m1, m2: (m1 - m2), X_times_T, y)
        XTY_times_X = [sum(map(lambda m1, m2: m1 * m2, XT_minus_Y, x)) for x in X]

        # ============================================================

        # Armazena o custo J obtido em cada iteracao do gradiente    
        J_historico(iter) = computarCusto(X, y, theta);
