import warnings
from logging import getLogger
from nekbot.protocols import Message
from nekbot.protocols.xmpp.group_chat import GroupChatXMPP
from nekbot.protocols.xmpp.user import UserXMPP

__author__ = 'nekmo'

logger = getLogger('nekbot.protocols.xmpp.message')


class XMPPMessage(Message):
    def __init__(self, protocol, msg):
        user = UserXMPP(protocol, msg['mucnick'], msg['from'])
        self.msg = msg
        super(XMPPMessage, self).__init__(protocol, msg['body'], user)

    def create_group_chat(self):
        GroupChatXMPP(self.protocol, self.msg.receiver)

    @property
    def is_public(self):
        return False

    @property
    def is_own(self):
        return False

    @property
    def is_groupchat(self):
        return False
