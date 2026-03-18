Implemente as classes mat2, mat3 e mat4, destinadas à representação de matrizes quadradas de dimensões 2x2, 3x3 e 4x4, respectivamente.
A classe mat2 deverá possuir:

Quatro atributos do tipo float, correspondentes às posições da matriz, nomeados como: m00, m01, m10 e m11 (onde o primeiro índice representa a linha e o segundo a coluna).
Um método chamado toIdentity, que não recebe parâmetros e não retorna valor, e que deve definir os valores dos atributos m00, m01, m10 e m11 como uma matriz identidade 2x2 (valor 1 na diagonal principal e valor 0 nas demais posições).
Um construtor padrão, sem parâmetros, que obrigatoriamente chame o método toIdentity, garantindo que toda nova instância seja criada como matriz identidade.
Um método para adição de outra matriz mat2, que receba uma instância de mat2 como parâmetro e realize a soma com a matriz atual.
Um método para subtração de outra matriz mat2, que receba uma instância de mat2 como parâmetro e realize a subtração em relação à matriz atual.
Um método que receba um escalar do tipo float, chamado x, e multiplique todos os elementos da matriz (m00, m01, m10 e m11) por esse valor.
Um método que receba um escalar do tipo float, chamado x, e divida todos os elementos da matriz (m00, m01, m10 e m11) por esse valor.
Um método para multiplicação da matriz por um vetor do tipo vet2, recebido como parâmetro, cujo retorno deve ser um novo objeto vet2 contendo o resultado do produto.
Um método para multiplicação da matriz por outra matriz mat2, recebida como parâmetro, cujo retorno deve ser uma nova instância de mat2 contendo o resultado do produto matricial.
Um método que realize a transposição da matriz, trocando as posições das linhas pelas colunas.
Um método que retorne uma matriz bidimensional do tipo float, de dimensões 2x2, contendo exatamente os valores armazenados nos atributos da classe.
As classes mat3 e mat4 deverão possuir exatamente a mesma estrutura e os mesmos métodos descritos para a classe mat2, adaptando apenas a quantidade de atributos e as dimensões da matriz para 3x3 e 4x4, respectivamente. Na classe mat3, os métodos que utilizarem vetores deverão trabalhar com objetos do tipo vet3. Na classe mat4, os métodos que utilizarem vetores deverão trabalhar com objetos do tipo vet4. Todas as operações devem seguir corretamente as regras da álgebra matricial conforme a dimensão da matriz.