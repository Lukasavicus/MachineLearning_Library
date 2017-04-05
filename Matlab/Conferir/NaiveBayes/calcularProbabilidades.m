function [pAtrVitoria, pAtrDerrota] = calcularProbabilidades(X, Y)
%CALCULARPROBABILIDADES Computa a probabilidade de ocorrencia de cada 
%atributo por rotulo possivel. A funcao retorna dois vetores de tamanho n
%(qtde de atributos), um para cada classe.
%   [pAtrVitoria, pAtrDerrota] = CALCULARPROBABILIDADES(X, Y) calcula a 
%   probabilidade de ocorrencia de cada atributo em cada classe. 
%   Cada vetor de saida tem dimensao (n x 1), sendo n a quantidade de 
%   atributos por amostra.

% inicializa os vetores de probabilidades
pAtrVitoria = zeros(size(X,2),1);   %O valor size(Matriz, n), retorna o tamanho da n-esima dimensao (caso nao exista Ex.: Matriz bidimensional (size(X,3) == 1))
pAtrDerrota = zeros(size(X,2),1);

% ====================== ESCREVA O SEU CODIGO AQUI ======================
% Instrucoes: Complete o codigo para encontrar a probabilidade de
%               ocorrencia de um atributo para uma determinada classe.
%               Ex.: para a classe 1 (vitoria), devera ser computada um
%               vetor pAtrVitoria (n x 1) contendo n valores:
%               P(Atributo1=1|Classe=1), ..., P(Atributo5=1|Classe=1), e o
%               mesmo para a classe 0 (derrota):
%               P(Atributo1=1|Classe=0), ..., P(Atributo5=1|Classe=0).
%

s = size(X,1);
ss = size(X,2);
c1 = 0;
c0 = 0;

for i=1:s
    if(Y(i) == 1)
        c1 = c1 + 1;
    else
        c0 = c0 + 1;
    end
end

for j=1:ss
    for i = 1:s
        if(X(i,j) == 1 && Y(i) == 1)
            pAtrVitoria(j) = pAtrVitoria(j) + 1;
        end
        if(X(i,j) == 1 && Y(i) == 0)
            pAtrDerrota(j) = pAtrDerrota(j) + 1;
        end
    end
end

for j=1:ss
    pAtrVitoria(j) = pAtrVitoria(j) / c1;
    pAtrDerrota(j) = pAtrDerrota(j) / c0;
end
% =========================================================================

end