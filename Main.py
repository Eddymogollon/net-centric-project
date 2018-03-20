import tkinter as tk
from tkinter import messagebox
import ChatClient as client
import BaseEntry as entry
import BaseDialog as dialog
import threading

class SocketThreadedTask(threading.Thread):
    def __init__(self, socket, **callbacks):
        threading.Thread.__init__(self)
        self.socket = socket
        self.callbacks = callbacks

    def run(self):
        while True:
            try:
                message = self.socket.receive()

                print(message)

                if message == '/quit':
                    self.callbacks['clear_chat_window']()
                    self.callbacks['update_chat_window']('\n> You have been disconnected from the server.\n')
                    self.socket.disconnect()
                    break
                elif message == '/squit':
                    self.callbacks['clear_chat_window']()
                    self.callbacks['update_chat_window']('\n> The server was forcibly shutdown. No further messages are able to be sent\n')
                    self.socket.disconnect()
                    break
                elif 'joined' in message:
                    split_message = message.split('|')
                    self.callbacks['clear_chat_window']()
                    self.callbacks['update_chat_window'](split_message[0])
                    self.callbacks['update_user_list'](split_message[1])

                elif 'left' in message:
                    self.callbacks['update_chat_window'](message)
                    self.callbacks['remove_user_from_list'](message.split(' ')[2])
                elif 'change your name' in message:
                    self.callbacks['update_chat_window'](split_message[0])
                    self.callbacks['update_user_list'](split_message[1])
                elif '[update channel]' in message:
                    print('GUI received update channel')
                    split_message = message.split('|')
                    self.callbacks['update_channel_list'](split_message[1])
                else:
                    self.callbacks['update_chat_window'](message)
            except OSError:
                break

class ChatDialog(dialog.BaseDialog):
    def body(self, master):
        tk.Label(master, text="Enter host:").grid(row=0, sticky="w")
        tk.Label(master, text="Enter port:").grid(row=1, sticky="w")

        # self.hostEntryField = tk.Entry(master)
        # self.portEntryField = tk.Entry(master)

        self.hostEntryField = entry.BaseEntry(master, placeholder="Enter host")
        self.portEntryField = entry.BaseEntry(master, placeholder="Enter port")

        self.hostEntryField.grid(row=0, column=1)
        self.portEntryField.grid(row=1, column=1)
        return self.hostEntryField

    def validate(self):
        host = str(self.hostEntryField.get())

        try:
            port = int(self.portEntryField.get())

            if (port >= 0 and port < 65536):
                self.result = (host, port)
                return True
            else:
                tk.messagebox.showwarning("Error", "The port number has to be between 0 and 65535. Both values are inclusive.")
                return False
        except ValueError:
            tk.messagebox.showwarning("Error", "The port number has to be an integer.")
            return False

class ChatWindow(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.initUI(parent)

    def initUI(self, parent):
        self.backgroundColor = '#36393e'
        self.backgroundListColor = '#2f3136'
        self.textColor = '#b9c1b6'


        self.messageLabel = tk.Label(parent, text="", height='0', justify='left')
        self.messageLabel.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.channelLabel = tk.Label(parent, text="Channels:", height='0', justify='left')
        self.channelLabel.grid(row=0, column=4, sticky="nsew")

        self.usersLabel = tk.Label(parent, text="Users:", height='0', justify='left')
        self.usersLabel.grid(row=0, column=5, sticky="nsew")

        self.messageTextArea = tk.Text(parent, height=34, bg=self.backgroundColor, fg=self.textColor, state=tk.DISABLED, wrap=tk.WORD)
        self.messageTextArea.grid(row=1, column=0, columnspan=2, sticky="nsew")

        self.messageScrollbar = tk.Scrollbar(parent, troughcolor="red", orient=tk.VERTICAL, command=self.messageTextArea.yview)
        self.messageScrollbar.grid(row=1, column=3, sticky="ns")

        self.messageTextArea['yscrollcommand'] = self.messageScrollbar.set

        self.channelsListBox = tk.Listbox(parent, fg="#fff", bg=self.backgroundListColor)
        self.channelsListBox.grid(row=1, column=4, padx=5, sticky="nsew")

        # self.channelsListBox.insert(1, "Status")

        self.usersListBox = tk.Listbox(parent, fg="#fff", bg=self.backgroundListColor)
        self.usersListBox.grid(row=1, column=5, padx=5, sticky="nsew")

        self.entryField = entry.BaseEntry(parent, placeholder="Enter message.", width=80)
        self.entryField.grid(row=2, column=0, padx=5, pady=10, sticky="we")

        self.send_message_button = tk.Button(parent, text="Send", width=10, bg="#CACACA", activebackground="#CACACA")
        self.send_message_button.grid(row=2, column=1, padx=5, sticky="we")

    #  Insert a message to the chat
    def update_chat_window(self, message):
        self.messageTextArea.configure(state='normal')
        self.messageTextArea.insert(tk.END, message)
        self.messageTextArea.configure(state='disabled')
        self.messageTextArea.yview_pickplace("end")  # Sends textarea to bottom


    def update_user_list(self, user_message):
        users = user_message.split(' ')

        for user in users:
            if user not in self.usersListBox.get(0, tk.END):
                self.usersListBox.insert(tk.END, user)

    def update_channel_list(self, channel_message):
        channels = channel_message.split(' ')
        print(channels)
        for channel in channels:
            if channel not in self.channelsListBox.get(0, tk.END):
                self.channelsListBox.insert(tk.END, channel)

    def remove_user_from_list(self, user):
        print(user)
        index = self.usersListBox.get(0, tk.END).index(user)
        self.usersListBox.delete(index)


    def clear_chat_window(self):
        if not self.messageTextArea.compare("end-1c", "==", "1.0"):
            self.messageTextArea.configure(state='normal')
            self.messageTextArea.delete('1.0', tk.END)
            self.messageTextArea.configure(state='disabled')

        if self.usersListBox.size() > 0:
            self.usersListBox.delete(0, tk.END)

    def send_message(self, **callbacks):
        message = self.entryField.get()
        self.set_message("")
        callbacks['send_message_to_server'](message)

    def set_message(self, message):
        self.entryField.delete(0, tk.END)
        self.entryField.insert(0, message)

    def bind_widgets(self, callback):
        self.send_message_button['command'] = lambda sendCallback = callback : self.send_message(send_message_to_server=sendCallback)
        self.entryField.bind("<Return>", lambda event, sendCallback = callback : self.send_message(send_message_to_server=sendCallback))
        self.messageTextArea.bind("<1>", lambda event: self.messageTextArea.focus_set())


class ChatGUI(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)

        # Init window properties
        self.initWindow(root)
        # Add menu to window
        self.initMenu(root)

        self.ChatWindow = ChatWindow(self.parent)

        self.clientSocket = client.Client()

        self.ChatWindow.bind_widgets(self.clientSocket.send)
        self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)

    def initWindow(self, parent):
        self.parent = parent
        self.parent.title("Eddy's IRC Chat")
        self.parent.config(bg="#152225")

        screenSizeX = self.parent.winfo_screenwidth()
        screenSizeY = self.parent.winfo_screenheight()

        frameSizeX = 900
        frameSizeY = 600

        framePosX = (screenSizeX - frameSizeX) / 2
        framePosY = (screenSizeY - frameSizeY) / 2

        self.parent.geometry('%dx%d+%d+%d' % (frameSizeX, frameSizeY, framePosX, framePosY - 25))
        self.parent.resizable(True, True)

    def initMenu(self, parent):
        self.parent = parent

        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(0, weight=1)

        self.mainMenu = tk.Menu(self.parent)
        self.parent.config(menu=self.mainMenu)

        self.subMenu = tk.Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label='File', menu=self.subMenu)
        self.subMenu.add_command(label='Connect', command=self.connect_to_server)
        self.subMenu.add_command(label='Exit', command=self.on_closing)

    def connect_to_server(self):
        if self.clientSocket.isClientConnected:
            tk.messagebox.showwarning("Info", "Already connected to the server.")
            return

        dialogResult = ChatDialog(self.parent).result
        print(dialogResult)

        if dialogResult:
            self.clientSocket.connect(dialogResult[0], dialogResult[1])

            if self.clientSocket.isClientConnected:
                self.ChatWindow.clear_chat_window()
                SocketThreadedTask(self.clientSocket, update_chat_window=self.ChatWindow.update_chat_window,
                                                      update_user_list=self.ChatWindow.update_user_list,
                                                      update_channel_list=self.ChatWindow.update_channel_list,
                                                      clear_chat_window=self.ChatWindow.clear_chat_window,
                                                      remove_user_from_list=self.ChatWindow.remove_user_from_list,).start()
            else:
                tk.messagebox.showwarning("Error", "Unable to connect to the server.")

    def on_closing(self):
        if self.clientSocket.isClientConnected:
            self.clientSocket.send('/quit')

        self.parent.quit()
        self.parent.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    chatGUI = ChatGUI(root)
    root.mainloop()

