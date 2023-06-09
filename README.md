# Compilador-P--
Compilador para a linguagem educacional P--

## Estrutura do projeto
```
.
├── compiler
│   ├── lexical_analyzer.py
│   └── simbols.py
├── exemplo_programa.txt
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
program, SIMB_PROGRAM
leimprime, IDENTIFICADOR
;, SIMB_PV
var, SIMB_VAR
a, IDENTIFICADOR
@, ERRO('CARACTERE NAO PERMITIDO')
:, SIMB_DP
real, SIMB_TIPO
;, SIMB_PV
var, SIMB_VAR
1b1b, ERRO('IDENTIFICADOR MAL FORMADO')
:, SIMB_DP
integer, SIMB_TIPO
;, SIMB_PV
procedure, SIMB_PROCEDURE
nomep, IDENTIFICADOR
(, SIMB_PA_ESQ
x, IDENTIFICADOR
:, SIMB_DP
real, SIMB_TIPO
), SIMB_PA_DIR
;, SIMB_PV
var, SIMB_VAR
a, IDENTIFICADOR
,, SIMB_VIR
c, IDENTIFICADOR
:, SIMB_DP
integer, SIMB_TIPO
;, SIMB_PV
begin, SIMB_BEGIN
read, SIMB_READ
(, SIMB_PA_ESQ
c, IDENTIFICADOR
,, SIMB_VIR
a, IDENTIFICADOR
), SIMB_PA_DIR
;, SIMB_PV
if, SIMB_IF
a, IDENTIFICADOR
<, SIMB_MENOR
x, IDENTIFICADOR
+, SIMB_MAIS
c, IDENTIFICADOR
then, SIMB_THEN
begin, SIMB_BEGIN
a, IDENTIFICADOR
:=, SIMB_ATRIB
23.5, REAL
;, SIMB_PV
write, SIMB_WRITE
(, SIMB_PA_ESQ
a, IDENTIFICADOR
), SIMB_PA_DIR
;, SIMB_PV
end, SIMB_END
else, SIMB_ELSE
c, IDENTIFICADOR
:=, SIMB_ATRIB
a, IDENTIFICADOR
+, SIMB_MAIS
x, IDENTIFICADOR
;, SIMB_PV
end, SIMB_END
;, SIMB_PV
begin, SIMB_BEGIN
read, SIMB_READ
(, SIMB_PA_ESQ
b, IDENTIFICADOR
), SIMB_PA_DIR
;, SIMB_PV
nomep, IDENTIFICADOR
(, SIMB_PA_ESQ
b, IDENTIFICADOR
), SIMB_PA_DIR
;, SIMB_PV
end, SIMB_END
., SIMB_P
```
