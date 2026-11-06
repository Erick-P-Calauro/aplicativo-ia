# SPEC-002 : Reconhecimento Facial

Essa especificação trata do pipeline de detecção e reconhecimento facial que deve ser suportado pelo sistema.

## Requisitos Funcionais 

RF-04 : O sistema deve ser capaz de gerar embeddings faciais com base nas imagens das faces dos usuários cadastrados.

RF-05 : O sistema deve ser capaz de detectar e reconhecer faces com base em uma imagem fornecida pelo usuário. 

RF-06 : O sistema deve ser capaz de diferenciar pessoas cadastradas no sistema de pessoas não cadastradas. Pessoas não cadastradas devem ser identificadas como tal durante o reconhecimento facial.

RF-07 : O sistema de reconhecimento facial deve suportar imagens com múltiplas faces, identificando cada uma delas de acordo com os usuários cadastrados.

RF-08 : O sistema de reconhecimento facial deve suportar imagens com nenhuma face, retornando "Nenhuma pessoa encontrada na imagem" nesses casos.

## Requisitos Não Funcionais

RNF-03 : O sistema deve adotar como threshold de similaridade o valor de 0.688 para separação de pessoas conhecidas e desconhecidas.

## Modelagem dos Embeddings

Os Embeddings deverão ter as seguintes informações que devem ser armazenadas no sistema : id, usuário associado, o vetor e a data de criação.