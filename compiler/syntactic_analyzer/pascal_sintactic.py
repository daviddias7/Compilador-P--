from compiler.syntactic_analyzer.grammar_file_parser import grammar_file_parser

class PascalSyntactic:
    def __init__(self):
        self.grammar_rules = grammar_file_parser("./compiler/gramatica.txt")
        self.complete_first_search()
        self.complete_followers_search()
        self.panic_list = [';', ')']

    def complete_first_search(self):
        for rule in self.grammar_rules.keys():
            self.first_search(rule)

    def first_search(self, rule_name):
        
        rule = self.grammar_rules[rule_name]

        if rule.first:
            return list(rule.first.keys())

        for option_index in range(0, len(rule.rules_options_list)):
            rule_option = rule.rules_options_list[option_index]

            first_element = rule_option[0]

            if(first_element.rule_type == "terminal"):
                rule.first.update({first_element.value: option_index})
            else:
                first_list = self.first_search(first_element.value)
                final_first_list = first_list.copy()
                for rule_option_position in range(1, len(rule_option)):
                    if "λ" in first_list:
                        if rule_option[rule_option_position].rule_type == "terminal":
                            first_list = [rule_option[rule_option_position].value]
                        else:
                            first_list = self.first_search(rule_option[rule_option_position].value)
                        final_first_list += first_list
                    else:
                        if "λ" in final_first_list:
                            final_first_list.remove("λ")
                        break

                for elem in final_first_list:
                    if not elem in rule.first:
                        rule.first[elem] = option_index

        return list(rule.first.keys())

    def print_first(self):
        for rule_name, rule_obj in self.grammar_rules.items():
            print(rule_name + " " + str(rule_obj.first))


    # A funcao abaixo eh o ponto de entrada para a obtencao dos seguidores
    # de cada nao terminal. Os nomes dos nao terminais sao passados um por
    # um para a funcao followers_search, a qual fara as buscas necessarias
    # para determinar os seguidores do elemento nao terminal solicitado pela
    # complete_followers_search.
    def complete_followers_search(self):
        visited = dict.fromkeys(self.grammar_rules.keys(), 0)
        
        for rule in self.grammar_rules.keys():
            self.followers_search(rule, visited)

    # A funcao abaixo retorna uma lista contendo os indices das posicoes onde
    # uma regra especifica foi encontrada. A derivation_option armazena uma 
    # opcao de derivacao para uma regra especifica. Por exemplo, a regra
    # 'condicao> ::= <expressao> <relacao> <expressao>' possui apenas uma opcao
    # de derivacao, entao a unica possibilidade de derivation_option eh 
    # derivation_option = [<expressao>, <relacao>, <expressao>]. Nesse caso,
    # se desired_rule = "<expressao>", entao a list indexes a ser retornada
    # seria igual a [0, 2]. Se desired_rule = "<relacao>", entao indexes seria
    # igual a [1]. Vale comentar que derivation_option nao eh uma lista de strings
    # mas sim de objetos do tipo RuleElement. 
    def get_rule_indexes(self, derivation_option, desired_rule):
        indexes = []
        for i in range(0, len(derivation_option)):
            if derivation_option[i].value == desired_rule:
                    indexes.append(i)
        return indexes

    # A funcao followers_search eh utilizada para fazer a busca dos seguidores
    # de uma regra especifica, a qual eh passada pela funcao complete_followers_search.
    # Como a determinacao dos seguidores de uma regra muitas vezes necessita dos 
    # seguidores de outra regra, a funcao followers_search realiza chamadas recursivas.
    # Para que ciclos infinitos nao ocorram, o dicionario visited eh utilizado para 
    # marcar as regras que estao naquela ramificacao recursiva.
    def followers_search(self, desired_rule, visited):
        
        # Primeiro, o objeto da regra desejada eh obtido. Este objeto eh do tipo Rule.
        desired_rule_obj = self.grammar_rules[desired_rule]

        # Se os seguidores da regra desejada ja foram obtidos, ou a regra ja foi visitada
        # durante a recursao, entao o set contendo os seguidores eh retornado.
        if desired_rule_obj.follower or visited[desired_rule] == 1:
            return desired_rule_obj.follower

        # A regra desejada eh marcada como visitada
        visited[desired_rule] = 1
        
        
        for rule_name, rule_obj in self.grammar_rules.items():
            for derivation_option in rule_obj.rules_options_list:

                indexes = self.get_rule_indexes(derivation_option, desired_rule)

                for rule_index in indexes:
                    for rule_option_position in range(rule_index, len(derivation_option)):
                        
                        if derivation_option[rule_option_position].rule_type == "terminal":
                            desired_rule_obj.follower.update({derivation_option[rule_option_position].value}) 
                            break
                        elif derivation_option[rule_option_position].value != desired_rule:
                            rule_option_obj = self.grammar_rules[derivation_option[rule_option_position].value]
                            first_set = set(rule_option_obj.first)

                            if "λ" in first_set:
                                first_set.remove("λ")
                                desired_rule_obj.follower.update(first_set)
                            else:
                                desired_rule_obj.follower.update(first_set)
                                break
                        elif visited[rule_name] == 0 and rule_option_position == len(derivation_option) - 1:
                            desired_rule_obj.follower.update(self.followers_search(rule_name, visited)) 


        visited[desired_rule] = 0

        return desired_rule_obj.follower

    def print_followers(self):
        for rule_name, rule_obj in self.grammar_rules.items():
            print(rule_name + " " + str(rule_obj.follower))

    def parse(self, lexer):
        current_rule = '<programa>'
        token = lexer.get_next_token();
        self.parse_rec(lexer, current_rule, token)
        print()

    def parse_rec(self, lexer, current_rule, token):
        value, word = token
        print("current word: " + word + " current rule: " + current_rule)
        rule_options_index = 0

		# Nesse laço veremos se o token atual esta na lista de primeiros da regra
        firstFound = False
        if word in self.grammar_rules[current_rule].first:
                rule_options_index = self.grammar_rules[current_rule].first[word]
                firstFound = True
		
        if firstFound: # Se foi encontrado na lista de first (analise preditiva)
            nextRule = self.grammar_rules[current_rule].rules_options_list[rule_options_index] # Proxima regra a ser analisada
            # Acho que temos que iterar sobre nextRule [<fator>, <cmd>, <variavel>]
            for ruleElem in nextRule:
                if ruleElem.rule_type == 'non_terminal': # Se for nao terminal, continua recursao
                    self.parse_rec(lexer, ruleElem.value, token) # Encontra as regras do nao terminal em questao
                elif word == ruleElem.value:
                    print("word: " + word + " ruleElem: " + ruleElem.value)
                    value, word = lexer.get_next_token()
                    token = (value, word)

                else:
                    print('Erro sintatico na linha xxx (TODO): Esperado ', ruleElem.value, 'porém recebido ', word)

                #    if ruleElem.value != value: # Se for terminal, mas o valor do token nao for igual ao valor do terminal esperado pela regra gera erro (nao tenho certeza se faz sentido, talvez seja desnecessario pois ja chequei que o word esta certo)
					    # TODO: Erro
                #        print('Erro sintatico na linha xxx (TODO): Esperado ', nextRule.value, 'porém recebido ', value)
            return

	# Caso haja um elemento vazio nos primeiros da regra atual, checar se algum seguidor tem o token atual.
	# Se sim, faz a recursao com o proximo nao terminal
	# TODO: Talvez trocar esse λ por 'lambda' 
        if 'λ' in self.grammar_rules[current_rule].first:
            if word in self.grammar_rules[current_rule].follower:
                return
           # for followElem in self.grammar_rules[current_rule].follower:
           #     if followElem == word:
           #         self.parse_rec(lexer, self.grammar_rules[followElem])
           #         return

        print(word + " " + str(self.grammar_rules[current_rule].first))
	# Se nao encontrou depois de analisar, erro e modo panico
        print('Erro sintatico na linha xxx (TODO): , self.grammar_rules[current_rule].panic,  esperado')

	# Modo panico
        #value, word = lexer.get_next_token()
        #while word not in self.grammar_rules.panic_list:
        #    value, word = lexer.get_next_token()

        return                    


            





