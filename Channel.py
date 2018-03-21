class Channel:
    def __init__(self, name, topic="no topic set"):
        self.users = [] # A list of the users in this channel.
        self.channel_name = name
        self.topic = topic

    def update_channels(self, user, all_channels):
        print('update_channels')
        print(' '.join(all_channels))
        user.socket.sendall('[update channel]|{0}'.format(' '.join(all_channels)).encode('utf8'))

    def remove_channels(self, user, channel):
        print('remove_channel')

        user.socket.sendall('[remove channel]|{0}'.format(channel).encode('utf8'))


    def welcome_user(self, username):
        all_users = self.get_all_users_in_channel()

        for user in self.users:
            if user.username is username:
                chatMessage = '\n\n> {0} have joined the channel {1}!\n|{2}'.format("You", self.channel_name, all_users).encode('utf8')
                user.socket.sendall(chatMessage)
            else:
                chatMessage = '\n\n> {0} has joined the channel {1}!\n|{2}'.format(username, self.channel_name, all_users).encode('utf8')
                user.socket.sendall(chatMessage)

    def broadcast_message(self, chatMessage, username=''):
        for user in self.users:
            if user.username is username:
                user.socket.sendall("You: {0}".format(chatMessage).encode('utf8'))
            else:
                user.socket.sendall("{0} {1}".format(username, chatMessage).encode('utf8'))

    def get_all_users_in_channel(self):
        return ' '.join([user.username for user in self.users])

    def remove_user_from_channel(self, user):
        print(user)
        self.users.remove(user)
        leave_message = "\n> {0} has left the channel {1}\n".format(user.username, self.channel_name)
        self.broadcast_message(leave_message)
