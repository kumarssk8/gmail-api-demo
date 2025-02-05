import os
from abc import ABC, abstractmethod
from gmail_service import GmailService


class Actions(ABC):

    @abstractmethod
    def execute(self, msg_ids):
        pass


class MoveMessageActions(Actions):
    def __init__(self, label):
        self._label = label
    
    def execute(self, msg_ids):
        if len(msg_ids) == 0:
            print(f"No msgs found to apply action")
            return
        
        body = {'ids' : msg_ids, 'addLabelIds' : [self._label] }
        try:
            GmailService.batch_modify(body)
            print(f"Moved message to the label {self._label} " + ",".join(msg_ids))
        except Exception as ex:
            print(f'Bulk mark to move to label {self._label} failed : {ex}')


class MarkAsReadActions(Actions):


    def execute(self, msg_ids):
        if len(msg_ids) == 0:
            print(f"No msgs found to apply action")
            return
    
        body = {'ids' : msg_ids, 'removeLabelIds' : ['UNREAD']}
        try:
            GmailService.batch_modify(body)
            print("Message marked as read for ids " + ",".join(msg_ids))
        except Exception as ex:
            print(f'Bulk mark as read failed {ex}')
        
        
