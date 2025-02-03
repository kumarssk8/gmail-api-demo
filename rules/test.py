from actions import Actions
from actions import MoveMessage
from actions import MarkAsRead


move_message = MoveMessage("move_message", "inbox")
mark_as_read = MarkAsRead("mark_as_read");

print(move_message.execute())
print(mark_as_read.execute())
