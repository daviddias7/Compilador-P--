from compiler.syntactic_analyzer.grammar_file_parser import grammar_file_parser

class PascalSyntactic:
    def __init__(self):
        self.grammar_rules = grammar_file_parser("./compiler/gramatica.txt")
        self.complete_first_search()
        self.complete_followers_search()

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


    #def complete_followers_search(self):
    #    for rule_name, rule_obj in self.grammar_rules.items():
    #        for option in rule.rules_options_list:
            

    #def followers_search(self, rule_name):
    #        for elem_index in range(0, len(option)):
    #            if option[elem_index].rule_type == "non-terminal":
    #                if elem_index + 1 == len(option):
                        #sera o seguidor de rule_name
                    


            





