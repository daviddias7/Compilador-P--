# Compilador-P--
Compilador para a linguagem educacional P--

## Estrutura do projeto
```
.
├── compiler
│   ├── lexical_analyzer
│   └── pascal_lexer.py
│   └── simbols.py
│   └── token.py
│
│   ├── syntactic_analyser
|   └── grammar_file_parser.py
│   └── pascal_syntactic.py
│   └── rule.py
│   └── rule_element.py
│
├── exemplo_programa.txt
├── saida.txt
├── main.py
└── README.md
```

## Execução
Para executar o programa em um ambiente Linux, basta utilizar o seguinte comando na raiz do projeto. Substituindo ```<nome do programa>``` pelo arquivo que se deseja realizar a análise léxica.
```
python3 main.py <nome do programa>
```
Isso fará com que um arquivo chamado ```saida.txt``` seja criado no diretório raiz, contendo os pares cadeia-token da análise léxica.

## Exemplo
O projeto contém um programa de exemplo que pode ser utilizado, chamado ```exemplo_programa.txt```. Para isso, basta executar o seguinte comando.
```
python3 main.py exemplo_programa.txt
```
Este comando resultará na criação do arquivo ```saida.txt``` com o seguinte conteúdo.

```
Erro lexico na linha 4: Identificador mal formado 
Erro sintatico na linha 8: Esperado , porém recebido ;
Erro sintatico na linha 13: Esperado ; porém recebido end
```
