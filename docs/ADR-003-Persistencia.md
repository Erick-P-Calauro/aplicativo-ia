# ADR-003 : Persistência de Dados

## Contexto

Essa decisão foi tomada no processo de concepção do projeto, delineando como os dados dos usuários serão armazenados no sistema.

## Decisão

O sistema armazenará os dados do usuário e seu embedding em um banco de dados postgresql. Dois campos merecem atenção especial : Foto e Vetor de embedding. A foto será salva em disco local e em banco de dados será armazenado apenas seu caminho relativo. O vetor de embedding será armazenado diretamente no banco de dados como um vetor serializado.

## Consequências

Espera-se que a configuração escolhida par armazenamento dos dados facilite a implementação e evolução do sistema.