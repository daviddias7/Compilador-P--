from enum import Enum


class RuleElement:
    class RuleType(Enum):
        terminal = "terminal"
        non_terminal = "non_terminal"
    
    def __init__(self, RuleType, value):
        self._set_RuleType(RuleType)    
        self.value = value

    def _set_RuleType(self, RuleType):
        if RuleType in set(item.value for item in self.RuleType):
            self.rule_type = RuleType
        else:
            raise ValueError("Rule type value not valid")
