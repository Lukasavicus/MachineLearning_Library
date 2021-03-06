function [X_norm, mu, sigma] = normalizar(X)
%NORMALIZAR normaliza os atributos em X
%   NORMALIZAR(X) retorna uma versao normalizada de X onde o valor da
%   media de cada atributo eh 0 e desvio padrao eh igual a 1. Trata-se de
%   um importante passo de pre-processamento quando trabalha-se com 
%   metodos de aprendizado de maquina.

%  Calcula a quantidade de amostra e de atributos
[m,n] = size(X); % m = qtde de objetos e n = qtde de atributos por objeto

% Incializa as variaves de saida
X_norm = zeros(m,n); % inicializa X_norm
mu = 0; % inicializa media
sigma = 1; % inicializa desvio padrao

% ====================== ESCREVA O SEU CODIGO AQUI ======================
% Instrucoes: Calcule a media de cada atributo de X e armazene em mu. Note
%             que se X for uma matriz (m x n), entao mu tera que ser um
%             vetor (1 x n), no qual cada coluna de mu devera conter o 
%             valor da media de cada um dos n atributos. O mesmo devera ser
%             feito para o desvio padrao, que devera ser armazenado em
%             sigma. 
%             Sugestao: use os comandos mean e std para calcular a media e 
%             o desvio padrao, respectivamente.
%             
%             Uma vez encontrados os valores de mu e de sigma, calcule o
%             valor do atributo X normalizado. Para isso, para cada amostra
%             x_i de X sera necessario calcular (x_i - mu)/sigma e
%             armazenar em X_norm (base de dados normalizada).
%
%
%Calcula a media (vetorizada, ou seja, a media de cada coluna)
mu = mean(X);
%Calcula a media (vetorizada)
sigma = std(X);
% Atribui os valores corrigidos
if(exist('OCTAVE_VERSION', 'builtin'))
    X_norm = (X - mu) ./ sigma;
else
    X_norm = bsxfun(@rdivide, bsxfun(@minus, X,mu), sigma);
end

% ============================================================

end