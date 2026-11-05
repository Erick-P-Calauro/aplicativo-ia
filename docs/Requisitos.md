## Especificação de Requisitos de Software

### 1. Introdução

Este documento registra os requisitos detalhados do aplicativo de reconhecimento facial, na forma de requisitos textuais do produto.

### 2. Classes de usuários

Root : Usuário com acesso a todas as funcionalidades do sistema. Na prática só existirá um usuário root que consistirá em quem estiver hospedando a aplicação.

Usuário Padrão : Usuário comum da aplicação que tem acesso às operaçoes básicas do sistema.

### 3. Requisitos de Software

Nesta seção são descritos os requisitos textuais do produto. Na Seção 3.1 são descritos os requisitos funcionais. 

#### 3.1. Requisitos funcionais

RF-01 : O sistema deve possibilitar o cadastro de novos usuários no sistema mediante o fornecimento de nome e foto.

RF-02 : O sistema deve possibilitar a listagem dos usuários do sistema.

RF-03 : O sistema deve possibilitar a exclusão dos usuários do sistema.

RF-04 : O sistema deve ser capaz de gerar embeddings faciais com base nas imagens das faces dos usuários cadastrados.

RF-05 : O sistema deve ser capaz de detectar e reconhecer faces com base em uma imagem fornecida pelo usuário. 

RF-06 : O sistema deve ser capaz de diferenciar pessoas cadastradas no sistema de pessoas não cadastradas. Pessoas não cadastradas devem ser identificadas como tal durante o reconhecimento facial.

RF-07 : O sistema de reconhecimento facial deve suportar imagens com múltiplas faces, identificando cada uma delas de acordo com os usuários cadastrados.

RF-08 : O sistema de reconhecimento facial deve suportar imagens com nenhuma face, retornando "Nenhuma pessoa encontrada na imagem" nesses casos.

#### 3.2 Requisitos Não Funcionais

RNF-01 : A exclusão de usuários do sistema deve compreender qualquer dado associado aos dados fornecidos pelo usuário, incluindo seu registro no banco de dados, fotos e embeddings faciais.