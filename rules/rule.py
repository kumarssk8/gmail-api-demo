
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
        msg_ids = self.filter_results()
        self.perform_actions(msg_ids)

    @abstractmethod
    def filter_results(self):
        pass

    def perform_actions(self, msg_ids):
        for action in self._actions:
            action.execute(msg_ids)
        

class AllRule(Rule):

    def filter_results(self):
        conditions = [r.derive_condition() for r in self._filters]
        return GmailMsg().select_msg_ids(" and ".join(conditions))


class AnyRule(Rule):

    def filter_results(self):
        conditions = [r.derive_condition() for r in self._filters]
        return GmailMsg().select_msg_ids(" or ".join(conditions))

    
