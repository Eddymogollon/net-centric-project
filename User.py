import Util

class User:
    def __init__(self, client_socket, username='', nickname=Util.generate_random_nickname(), password='', usertype='user'):
        self._client_socket = client_socket
        self._username = username
        self._nickname = nickname
        self._password = password
        self._usertype = usertype
        self._status = "Online"
        self._PRVMSG = "This user is currently away"
        self._chat_messages_in_channel = {}
        ### add time connected

    @property
    def socket(self):
        return self._client_socket

    @property
    def username(self):
        return self._username

    @property
    def nickname(self):
        return self._nickname

    @property
    def usertype(self):
        return self._usertype

    @property
    def password(self):
        return self._password

    @property
    def status(self):
        return self._status

    @property
    def PRVMSG(self):
        return self._PRVMSG

    @property
    def chat_messages_in_channels(self):
        return self._chat_messages_in_channel

    @username.setter
    def username(self, new_username):
        self._username = new_username

    @nickname.setter
    def nickname(self, new_nickname):
        self._nickname = new_nickname

    @usertype.setter
    def usertype(self, new_usertype):
        self._usertype = new_usertype

    @password.setter
    def password(self, new_password):
        self._password = new_password

    @status.setter
    def status(self, new_status):
        self._status = new_status

    @PRVMSG.setter
    def PRVMSG(self, new_PRVMSG):
        self._PRVMSG = new_PRVMSG

    @chat_messages_in_channels.setter
    def chat_messages_in_channels(self, chat_messsages):
        self._chat_messages_in_channel = chat_messsages