class Rule:
    def __init__(self, rules_options_list):
        self.rules_options_list = rules_options_list
        self.first = {}
        self.follower = set()
