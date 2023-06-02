import sys
from compiler.lexical_analyzer import PascalLexer 

if __name__ == '__main__':  

    f_in = open(sys.argv[1], 'r')
    source_code = f_in.read()
    f_in.close()
    
    lexer = PascalLexer(source_code)
    tokens = lexer.tokenize()
    f_out = open('saida.txt', 'w')
    
    for token in tokens:
        value, word = token
        f_out.write(word + ', ' + value + '\n')

    f_out.close()

