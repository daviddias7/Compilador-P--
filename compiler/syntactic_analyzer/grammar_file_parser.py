import os
import re
from compiler.syntactic_analyzer.rule_element import RuleElement
from compiler.syntactic_analyzer.rule import Rule


def rule_element_parser(rule):
    rules_elements_list = []
    elements_list = rule.split(" ")
    
    for raw_element in elements_list:
        
        rule_type = "terminal"
        if re.match(r"<[^>]+>", raw_element):
            rule_type = "non_terminal"

        rules_elements_list.append(RuleElement(rule_type, raw_element))

    return rules_elements_list

def grammar_file_parser(file_name: str):

    if(not os.path.isfile(file_name)):
        print("O arquivo " + file_name + " nao existe")
        exit()

    grammar_rules = {}

    with open(file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            split_line = line.split(" ::= ")
            raw_rules_options = split_line[1].split(" | ")
            rules_parsed = []

            for rule in raw_rules_options:
                rules_parsed.append(rule_element_parser(rule))

            grammar_rules.update({split_line[0]: Rule(rules_parsed)})
    
    return grammar_rules
    
