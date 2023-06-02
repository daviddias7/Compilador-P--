import sys
import os

from compiler.lexical_analyzer import PascalLexer 

if __name__ == '__main__':  

    file_name = sys.argv[1]

    if(not os.path.isfile(file_name)):
        print("O arquivo " + file_name + " nao existe")
        exit()

    f_in = open(file_name, 'r')
    source_code = f_in.read()
    f_in.close()
    
    lexer = PascalLexer(source_code)
    tokens = lexer.tokenize()
    f_out = open('saida.txt', 'w')
    
    for token in tokens:
        value, word = token
        f_out.write(word + ', ' + value + '\n')

    f_out.close()

