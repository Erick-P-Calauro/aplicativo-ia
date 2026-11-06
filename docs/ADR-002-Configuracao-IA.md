# ADR-002 : Configuração de Inteligência Artificial

## Contexto

Essa decisão foi tomada no processo de concepção do projeto, para definir qual será a configuração utilizada no fluxo de reconhecimento facial

## Decisão

O sistema de reconhecimento facial será executado na configuração YuNet, responsável pela detecção facial, e Facenet via torchvision, para reconhecimento facial. Essa decisão foi tomada pois essa configuração teve o melhor desempenho nos experimentos realizados anteriormente.

## Consequências

Espera-se que essa decisões estabeleçam uma configuração eficaz para reconhecimento facial dos usuários cadastrados no sistema.