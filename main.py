import sys
import os

from compiler.lexical_analyzer.pascal_lexer import PascalLexer 
from compiler.syntactic_analyzer.pascal_sintactic import PascalSyntactic

if __name__ == '__main__':  

    file_name = sys.argv[1]

    if(not os.path.isfile(file_name)):
        print("O arquivo " + file_name + " nao existe")
        exit()

    f_in = open(file_name, 'r')
    source_code = f_in.read()
    f_in.close()
    
    lexer = PascalLexer(source_code)
    syntactic = PascalSyntactic()
    syntactic.parse(lexer)
    
    #token = lexer.get_next_token()
    #f_out = open('saida.txt', 'w')
    #while(token != None):
    #    value, word = token
    #    f_out.write(word + ', ' + value + '\n')
    #    token = lexer.get_next_token()

    #f_out.close()


