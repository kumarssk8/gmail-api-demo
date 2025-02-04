import unittest

from unittest.mock import patch
from rules.filter import StringFilter
from rules.actions import MarkAsReadActions
from rules.rule import AllRule, AnyRule
from gmail_service import GmailService
from db.gmail_msg import GmailMsg

class TestRule(unittest.TestCase):

    @patch.object(GmailMsg, 'select_msg_ids', return_value=["1","2","3"])
    @patch.object(GmailService, 'batch_modify', return_value=None)
    def test_all_rule(self, mock_batch_modify, mock_select_msg_ids):
        filters = [StringFilter("from_address","contains","abc"), StringFilter("from_address","contains","def")]
        action = [MarkAsReadActions()]
        all_rule = AllRule("rule1", filters, action)
        self.assertEqual(all_rule.get_condition(), 'from_address like "%abc%" and from_address like "%def%"', "all rule condition failed")
        all_rule.execute()
        mock_batch_modify.assert_called_once()
        mock_select_msg_ids.assert_called_once()

    
    @patch.object(GmailMsg, 'select_msg_ids', return_value=["1","2","3"])
    @patch.object(GmailService, 'batch_modify', return_value=None)
    def test_any_rule(self, mock_batch_modify, mock_select_msg_ids):
        filters = [StringFilter("from_address","contains","abc"), StringFilter("from_address","contains","def")]
        action = [MarkAsReadActions()]
        any_rule = AnyRule("rule1", filters, action)
        self.assertEqual(any_rule.get_condition(), 'from_address like "%abc%" or from_address like "%def%"', "any rule condition failed")
        any_rule.execute()
        mock_batch_modify.assert_called_once()
        mock_select_msg_ids.assert_called_once()
