# SPEC-001 : Gerenciamento de Usuários

Essa especificação trata da necessidade de cadastro, listagem e exclusão dos usuários no sistema.

## Requisitos Funcionais

RF-01 : O sistema deve possibilitar o cadastro de novos usuários no sistema mediante o fornecimento de nome e foto.

RF-02 : O sistema deve possibilitar a listagem dos usuários do sistema.

RF-03 : O sistema deve possibilitar a exclusão dos usuários do sistema.

## Requisitos Não Funcionais

RNF-01 : A exclusão de usuários do sistema deve compreender qualquer dado associado aos dados fornecidos pelo usuário, incluindo seu registro no banco de dados, fotos e embeddings faciais.

RNF-02 : Os requisitos funcionais 02 e 03 devem ser acessíveis mediante autenticação.

## Modelagem de usuário

O usuário padrão do sistema deverá ter as seguintes informações que devem ser armazenadas no sistema : id, nome, foto e data e hora de cadastro.