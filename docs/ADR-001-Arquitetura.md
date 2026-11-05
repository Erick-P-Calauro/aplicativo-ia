# ADR-001 : Arquitetura

## Contexto

Esta decisão foi tomada na concepção do projeto, delineando a organização do sistema.

## Decisão 01 - Arquitetura Geral

O sistema será organizado em uma arquitetura Cliente-Servidor sem separação física dos componentes e com comunicação por HTTP. O Cliente será o componente responsável por disponibilizar a interface visual e de interação para o usuário e o Servidor será o componente responsável por processar as ações do usuário, especialmente no que tange a parte de utilização dos modelos de inteligência artificial.

## Decisão 02 - Arquitetura do Servidor

O Servidor adotará um estilo arquitetural inspirado no MVC para gerenciar as interações dos clientes de forma simples. O processamento que envolve modelos de inteligência artifical será executado localmente no Servidor.

## Consequências

Espera-se que essa decisões estabeleçam uma organização do projeto que seja simples e que facilite a evolução do sistema ao longo do desenvolvimento.