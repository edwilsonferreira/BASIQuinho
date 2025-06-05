# BASIQuinho Compiler

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
    A[Código Fonte BASIQuinho] --> B(Análise Léxica);
    B --> C(Análise Sintática);
    C --> D(Análise Semântica);
    D --> E(Geração de Código Intermediário - TAC);
    E --> F(Geração de Código Final - LLVM IR);
    F --> G[Código LLVM IR];
    G -- clang --> H[Código Executável];
```

## Estrutura do Projeto e Módulos
O projeto é organizado em módulos Python, cada um responsável por uma fase ou funcionalidade específica:

## 1. BASIQuinho.g4

Função: Arquivo de gramática formal da linguagem BASIQuinho, escrito na sintaxe do ANTLR4.
Responsabilidade: Define as regras léxicas (tokens como palavras-chave, identificadores, números, strings, comentários) e as regras sintáticas (a estrutura dos comandos e expressões válidas). É a especificação formal da linguagem que o ANTLR4 utiliza para gerar os analisadores.

## 2. Integração com ANTLR4

O ANTLR4 (ANother Tool for Language Recognition) é uma ferramenta poderosa usada para gerar o analisador léxico (lexer) e o analisador sintático (parser) a partir do arquivo de gramática BASIQuinho.g4.

**Arquivos Gerados pelo ANTLR4:**
```BASIQuinhoLexer.py```: Contém a classe BASIQuinhoLexer, responsável por quebrar o código fonte em uma sequência de tokens.
```BASIQuinhoParser.py```: Contém a classe BASIQuinhoParser, responsável por verificar se a sequência de tokens forma uma estrutura sintática válida e por construir a Árvore Sintática (Parse Tree).
```BASIQuinhoListener.py```: Contém a classe base BASIQuinhoListener com métodos enterRule e exitRule para cada regra da gramática. Esta classe é estendida para implementar a análise semântica e outras ações baseadas na árvore.

## 3. main.py

**Função:** Ponto de entrada principal do compilador.
**Responsabilidade:** Processa os argumentos da linha de comando (como o nome do arquivo fonte BASIQuinho), instancia a classe Compilador e inicia o processo de compilação.

## 4. compilador.py

**Função:** Orquestrador central do processo de compilação.
**Responsabilidade:**
- Coordena a execução sequencial de todas as fases do compilador (léxica, sintática, semântica, TAC, LLVM).
- Gerencia a comunicação e a passagem de dados entre as diferentes fases (ex: stream de tokens, AST, código TAC).
- Centraliza a interface com o usuário e o tratamento de erros em alto nível.
- Salva os artefatos gerados (ex: .tac, .ll).

## 5. logger_config.py

**Função:** Configuração do sistema de logging do Python.
**Responsabilidade:** Define o formato, o nível (INFO, DEBUG, etc.) e o destino das mensagens de log geradas por todos os módulos do compilador, garantindo um acompanhamento detalhado e padronizado do processo.

## 6. erro.py

**Função:** Módulo centralizado para tratamento e registro de erros.
**Responsabilidade:**
- Define a classe Erro para rastrear os tipos de erros ocorridos (léxicos, sintáticos, semânticos).
- Define CustomErrorListener (que herda de ANTLRErrorListener) para capturar e formatar erros diretamente do lexer e parser do ANTLR, reportando-os através da classe Erro.
- Fornece uma maneira padronizada para todos os módulos reportarem erros, incluindo informações como módulo, linha, coluna e mensagem.

## 7. analise_lexica.py

**Função:** Responsável pela análise léxica.
**Responsabilidade:**
- Utiliza o BASIQuinhoLexer (gerado pelo ANTLR) para ler o arquivo fonte.
- Transforma a sequência de caracteres do código fonte em uma sequência de tokens (palavras-chave, identificadores, literais, operadores).
- Reporta erros léxicos (ex: caracteres inválidos).
- Gera um log dos tokens identificados.
- Fornece o CommonTokenStream para o analisador sintático.

## 8. analise_sintatica.py

**Função:** Responsável pela análise sintática.
**Responsabilidade:**
- Utiliza o BASIQuinhoParser (gerado pelo ANTLR) e o stream de tokens da análise léxica.
- Verifica se a sequência de tokens segue as regras gramaticais do BASIQuinho.
- Constrói a Árvore Sintática (Parse Tree), que representa a estrutura hierárquica do código fonte.
- Reporta erros sintáticos (ex: comandos malformados, estrutura de expressão incorreta).
- Inclui funcionalidade para exportar a AST (Parse Tree) para os formatos DOT (Graphviz) e SVG, auxiliando na visualização e depuração.

## 9. analise_semantica.py

**Função:** Responsável pela análise semântica do código.
**Responsabilidade:**
- Percorre a Árvore Sintática (geralmente usando um Listener ou Visitor do ANTLR, neste caso um BASIQuinhoSemanticoListenerImpl que estende BASIQuinhoListener).
-  Verifica a consistência semântica do código, como:
- Gerenciamento de Escopo e Declaração de Variáveis: Verifica se variáveis são usadas após serem definidas (em BASIQuinho, LET e INPUT definem variáveis).
- Verificação de Tipos: Garante o uso consistente de tipos em expressões e atribuições. BASIQuinho tem um sistema de tipos simples (NUMERO, STRING), e as variáveis assumem o tipo do valor atribuído. As operações aritméticas esperam operandos NUMERO.
- Anotação da AST: Pode adicionar informações de tipo aos nós da árvore sintática para uso em fases posteriores.
- Detecção de Variáveis Não Utilizadas: Emite avisos sobre variáveis declaradas mas nunca lidas.
- Reporta erros semânticos (ex: uso de variável não definida, incompatibilidade de tipos em operações).

## 10. geracao_tac.py

**Função:** Responsável pela geração de Código de Três Endereços (TAC - Three-Address Code).
**Responsabilidade:**
- Recebe a Árvore Sintática (possivelmente anotada pela análise semântica).
- Traduz a estrutura hierárquica da árvore em uma representação linear de instruções simples.
- Cada instrução TAC geralmente envolve no máximo três "endereços" (dois operandos fonte e um destino).
- Decompõe expressões complexas em uma sequência de instruções TAC mais simples.
- Gera variáveis temporárias (ex: t0, t1) para armazenar resultados intermediários de expressões.
- Exemplo de transformação TAC:
```BASIQuinho: LET RESULT = (A + B) * C
TAC:
  t0 := A + B
  t1 := t0 * C
  RESULT := t1```


## 11. geracao_llvm.py

**Função:** Responsável pela geração de código final em LLVM Intermediate Representation (IR).
**Responsabilidade:**
- Recebe o Código de Três Endereços (TAC).
- Traduz as instruções TAC para LLVM IR. LLVM é uma infraestrutura de compilador que oferece otimizações e pode gerar código para diversas arquiteturas de hardware.
- Lida com a alocação de variáveis na stack, representação de literais, mapeamento de operações TAC para instruções LLVM, e chamadas a funções externas (como printf para o comando ```PRINT``` e scanf para ```INPUT`).
`- Gera um arquivo de texto .ll contendo o código LLVM IR.
- Configuração e Instalação
