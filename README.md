# BASIQuinho Compiler  BASIQuinho

Bem-vindo ao repositório do Compilador BASIQuinho! Este projeto é um compilador pedagógico desenvolvido em Python 3 para um subconjunto da linguagem BASIC, carinhosamente chamado de "BASIQuinho". O objetivo principal é servir como ferramenta de aprendizado para estudantes de Engenharia da Computação nas disciplinas de compiladores, demonstrando todas as fases clássicas da compilação, desde a análise léxica até a geração de código de baixo nível (LLVM IR).

**Link do Repositório:** [https://github.com/edwilsonferreira/BASIQuinho](https://github.com/edwilsonferreira/BASIQuinho)

---

## Funcionalidades da Linguagem BASIQuinho

O BASIQuinho atualmente suporta os seguintes comandos e construções:

* **`PRINT <expr_list>`**: Escreve o valor de uma ou mais expressões (separadas por vírgula) na saída padrão.
    * Ex: `PRINT "Olá Mundo!"`
    * Ex: `PRINT "Valor: ", MINHA_VAR, 10 * 2`
* **`INPUT <variável>`**: Lê um valor numérico da entrada padrão e o armazena na variável especificada.
    * Ex: `INPUT IDADE`
* **`LET <variável> = <expressão>`**: Atribui o resultado de uma expressão a uma variável.
    * Ex: `LET X = 10`
    * Ex: `LET RESULTADO = (A + B) * (C / 2)`
    * Ex: `LET NOME = "Basiquinho"`
* **Expressões Aritméticas**: Suporte a `+`, `-`, `*`, `/` com precedência usual e uso de parênteses `()`.
* **Tipos de Dados**: Suporte implícito a números (inteiros ou ponto flutuante simples) e strings literais. As variáveis assumem o tipo do valor atribuído (tipagem dinâmica na semântica, embora o LLVM gerado possa ter simplificações).
* **Comentários**: Linhas iniciadas com `REM` são ignoradas.
    * Ex: `REM Isto é um comentário`
    * Ex: `LET A = 10 REM Comentário no fim da linha`
* **Terminador de Comando**: Comandos podem ser terminados por uma nova linha ou por um ponto e vírgula (`;`).
* **Linhas em Branco**: Linhas em branco no código fonte são ignoradas.

---

## Arquitetura do Compilador

O compilador BASIQuinho segue as fases tradicionais de um compilador:

```mermaid
graph LR
    A[Código Fonte BASIQuinho (.bas)] --> B(Análise Léxica);
    B --> C(Análise Sintática);
    C --> D(Análise Semântica);
    D --> E(Geração de Código Intermediário - TAC);
    E --> F(Geração de Código Final - LLVM IR);
    F --> G[Código LLVM IR (.ll)];
    G -- clang --> H[Código Executável];
