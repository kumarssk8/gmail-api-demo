
from abc import ABC, abstractmethod
from db.gmail_msg import GmailMsg

class Rule(ABC):
    def __init__(self, name, filters, actions):
        self._name = name
        self._filters = filters
        self._actions = actions
    
    def name(self):
        return self._name
    
    def execute(self):
        condition = self.get_condition()
        msg_ids = GmailMsg().select_msg_ids(condition)
        self.perform_actions(msg_ids)

    @abstractmethod
    def get_condition(self):
        pass

    def perform_actions(self, msg_ids):
        for action in self._actions:
            action.execute(msg_ids)
        

class AllRule(Rule):

    def get_condition(self):
        conditions = [r.derive_condition() for r in self._filters]
        return " and ".join(conditions)


class AnyRule(Rule):

    def get_condition(self):
        conditions = [r.derive_condition() for r in self._filters]
        return " or ".join(conditions)

    
