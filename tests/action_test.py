import unittest

from unittest.mock import patch
from gmail_service import GmailService
from rules.actions import MoveMessageActions, MarkAsReadActions

class TestActions(unittest.TestCase):

    @patch.object(GmailService, 'batch_modify', return_value=None)
    def test_mark_as_read_action(self, mock_batch_modify):
        msg_ids = ["1","2","3"]
        MarkAsReadActions().execute(msg_ids)
        mock_batch_modify.assert_called_once()
    
    @patch.object(GmailService, 'batch_modify', return_value=None)
    def test_move_a_message_action(self, mock_batch_modify):
        msg_ids = ["1","2","3"]
        MoveMessageActions("inbox").execute(msg_ids)
        mock_batch_modify.assert_called_once()
    
