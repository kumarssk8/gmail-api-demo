import json

from rules.rule import AllRule, AnyRule
from rules.filter import StringFilter, DateFilter
from rules.actions import MoveMessageActions, MarkAsReadActions

class RuleParser:

    def create_rules(self, json_data):
        return [
            self.create_rule( k, v["predicate"],
                             [self.create_filters(f) for f in v.get("filter")],
                             [self.create_actions(a) for a in v.get("actions")])
            for k,v in json_data.items()
        ]

    
    string_fields = ["from_address", "subject"]
    date_fields = ["date_received"]

    def create_filters(self, json_data):
        field = json_data.get("field")
        if( field in self.string_fields):
            return StringFilter(field, json_data["condition"], json_data["value"])
        elif(field in self.date_fields):
            return DateFilter(field, json_data["condition"], json_data["value"], json_data["unit"])
        else:
            raise RuntimeError("Unhandled field " + field)
    
    def create_actions(self, json_data):
        action_name = json_data["name"]
        if(action_name == "move_message"):
            return MoveMessageActions(json_data["label"])
        elif(action_name == "mark_as_read"):
            return MarkAsReadActions()
        else:
            raise RuntimeError("Unhandled action " + action_name)
        
    def create_rule(self, name, predicate, filters, actions):
        if(predicate == "ALL"):
            return AllRule(name, filters, actions)
        elif(predicate == "ANY"):
            return AnyRule(name, filters, actions)
        else:
            raise RuntimeError("Unhandled predicate type " + predicate)

        