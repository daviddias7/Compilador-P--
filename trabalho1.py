import re

class PascalLexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []
        self.keywords = [
            'program', 'var', 'integer', 'real', 'begin', 'end', 'if', 'then', 'else', 'while', 'do'
        ]
        self.operators = [
            '+', '-', '*', '/', '=', '<', '>', '<=', '>=', '<>', ':=', ',', '.', '(', ')'
        ]
        self.simb_dp = ':'
        self.simb_pv = ';'
        
    def tokenize(self):
        source_code = self.source_code
        while source_code:
            if source_code[0].isspace():
                source_code = source_code[1:]
            elif source_code[0].isdigit():
                number = re.match(r'\d+', source_code).group()
                self.tokens.append(('NUMBER', number))
                source_code = source_code[len(number):]
            elif source_code[0].isalpha():
                identifier = re.match(r'[a-zA-Z]\w*', source_code).group()
                if identifier in self.keywords:
                    self.tokens.append(('KEYWORD', identifier))
                else:
                    self.tokens.append(('IDENTIFIER', identifier))
                source_code = source_code[len(identifier):]
            elif source_code[0] in self.operators:
                operator = source_code[0]
                self.tokens.append(('OPERATOR', operator))
                source_code = source_code[1:]
            elif source_code[0] == self.simb_dp:
                dp = source_code[0]
                self.tokens.append(('SIMB_DP', dp))
                source_code = source_code[1:]
            elif source_code[0] == self.simb_pv:
                pv = source_code[0]
                self.tokens.append(('SIMB_PV', pv))
                source_code = source_code[1:]
            else:
                # Ignore any unsupported characters
                error = source_code[0]
                self.tokens.append(("ERRO('CARACTERE NAO PERMITIDO')",  error))
                source_code = source_code[1:]
        
        return self.tokens

# Example usage
f_in = open('meu_programa.txt', 'r')
source_code = f_in.read()
f_in.close()
#source_code = '''
#program HelloWorld;
#var
#    x: integer;
#
#begin
#    x := 10 + 20;
#    if x > 15 then
#        writeln('Hello, World!')
#    else
#        writeln('Goodbye, World!');
#end.
#'''

lexer = PascalLexer(source_code)
tokens = lexer.tokenize()
f_out = open('saida.txt', 'w')

for token in tokens:
    value, word = token
    f_out.write(word + ', ' + value + '\n')

