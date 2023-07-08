import re
from compiler.lexical_analyzer.simbols import *  

class PascalLexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []
        self.end_found = False;

        self.tokenize()

        self.token_index = 0

    
    def get_next_token(self):

        if(self.token_index == len(self.tokens)):
            self.token_index = 0
            return None

        token = self.tokens[self.token_index]

        self.token_index += 1
        return token

    def get_all_tokens(self):
        return self.tokens

    def tokenize(self):
        source_code = self.source_code
        while source_code:
            if source_code[0].isspace():
                source_code = source_code[1:]
            elif source_code[0].isdigit():
                if source_code[1].isalpha():
                    erro = re.match(r'[a-zA-Z0-9]+', source_code).group()
                    self.tokens.append(("ERRO('IDENTIFICADOR MAL FORMADO')", erro))
                    source_code = source_code[len(erro):]
                else:
                    integer = re.match(r'\d+', source_code)
                    real = re.match(r'\d+\.\d+', source_code)
                    if real == None:
                        # Rodando o match de novo porque integer.group() nao esta transformando em string
                        integer = re.match(r'\d+', source_code).group()
                        #integer.group()
                        self.tokens.append(('INTEIRO', integer))
                        source_code = source_code[len(integer):]
                    else:
                        real = re.match(r'\d+\.\d+', source_code).group()
                        #real.group()
                        self.tokens.append(('REAL', real))
                        source_code = source_code[len(real):]
            elif source_code[0] == '{':
                comment = re.match(r'.*\}', source_code)
                if comment == None:
                    break;
                comment = re.match(r'.*\}', source_code).group()
                source_code = source_code[len(comment):]
            elif source_code[0].isalpha() or source_code[0] == '_':
                identifier = re.match(r'[a-zA-Z_]\w*', source_code).group()
                if identifier in simbols_table:
                    self.tokens.append((simbols_table[identifier], identifier))
                    if identifier == 'end':
                        self.end_found = True
                else:
                    self.tokens.append(('IDENTIFICADOR', identifier))
                source_code = source_code[len(identifier):]
            elif source_code[:2] in operators_table:
                self.tokens.append((operators_table[source_code[:2]], source_code[:2]))
                source_code = source_code[2:]
            elif source_code[0] in operators_table:
                self.tokens.append((operators_table[source_code[0]], source_code[0]))
                source_code = source_code[1:]
            else:
                error = source_code[0]
                self.tokens.append(("ERRO('CARACTERE NAO PERMITIDO')",  error))
                source_code = source_code[1:]
        if self.end_found == False:
            self.tokens.append(("ERRO('FIM DE ARQUIVO INESPERADO')",'1'))


