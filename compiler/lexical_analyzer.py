import re

class PascalLexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []
        self.keywords = [
            'if', 'then', 'else', 'while', 'do', 'procedure', 'for'
        ]
        self.operators = [
            '+', '-', '*', '/', '=', '<', '>', '<=', '>=', '<>', ':=', '.', '(', ')'
        ]
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
            elif source_code[0].isalpha():
                identifier = re.match(r'[a-zA-Z]\w*', source_code).group()
                if identifier == 'program':
                    self.tokens.append(('SIMB_PROGRAM', identifier))
                elif identifier == 'var':
                    self.tokens.append(('SIMB_VAR', identifier))
                elif identifier == 'begin':
                    self.tokens.append(('SIMB_BEGIN', identifier))
                elif identifier == 'end':
                    self.end_found = True
                    self.tokens.append(('SIMB_END', identifier))
                elif identifier == 'integer' or identifier == 'real':
                    self.tokens.append(('SIMB_TIPO', identifier))
                elif identifier in self.keywords:
                    self.tokens.append(('PALAVRA-CHAVE', identifier))
                else:
                    self.tokens.append(('IDENTIFICADOR', identifier))
                source_code = source_code[len(identifier):]
            elif source_code[0] == '{':
                comment = re.match(r'.*\}', source_code)
                if comment == None:
                    break;
                comment = re.match(r'.*\}', source_code).group()
                source_code = source_code[len(comment):]
            elif source_code[0] in self.operators:
                operator = source_code[0]
                self.tokens.append(('OPERADOR', operator))
                source_code = source_code[1:]
            elif source_code[0] == ',':
                vir = source_code[0]
                self.tokens.append(('SIMB_VIR', vir))
                source_code = source_code[1:]
            elif source_code[0] == ':':
                dp = source_code[0]
                self.tokens.append(('SIMB_DP', dp))
                source_code = source_code[1:]
            elif source_code[0] == ';':
                pv = source_code[0]
                self.tokens.append(('SIMB_PV', pv))
                source_code = source_code[1:]
            else:
                error = source_code[0]
                self.tokens.append(("ERRO('CARACTERE NAO PERMITIDO')",  error))
                source_code = source_code[1:]
        if self.end_found == False:
            self.tokens.append(("ERRO('FIM DE ARQUIVO INESPERADO')",'1'))


