import computarCusto as cc

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
    for iterator in list(range(num_iter)):
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

        (m, n) = (len(X), len(X[0]));
        #for i in range(m):
        #    S = 0;
        #    for j in range(n):
        #        S += X[i][j] * theta[j];
        #    X_times_T[i] = S;

        X_times_T = [sum(map(lambda m1, m2: float(m1 * m2), theta, x)) for x in X]

        #for i in range(m):
        #    XT_minus_Y[i] = X_times_T[i] - y[i];

        XT_minus_Y = map(lambda m1, m2: float(m1 - m2), X_times_T, y)

        XTY_times_X = [0 for i in list(range(n))];
        
        for i in range(n):
            S = 0;
            for j in range(m):
                S += X[j][i] * XT_minus_Y[j];
            XTY_times_X[i] = theta[i] - (alpha * S / m);

        theta = XTY_times_X;

        # ============================================================
        # Armazena o custo J obtido em cada iteracao do gradiente    
        J_historico[iterator] = cc.computarCusto(X, y, theta);
    return (XTY_times_X, J_historico)