import socket
import sys



class IRC:
    irc = socket.socket()

    def __init__(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, chan, msg):
        self.irc.send("PRIVMSG " + chan + " " + msg + "\r\n")

    def get_text(self):
        text = self.irc.recv(2040)  # receive the text

        if text.find('PING') != -1:
            clean = text.translate(None, ':')
            print('PONG ' + clean.split()[1] + '\r\n')
            self.irc.send('PONG ' + clean.split()[1] + '\r\n')

        return text

    def connect(self, server):
        # defines the socket
        print "connecting to:" + server
        self.irc.connect((server, 6667))  # connects to the server

    def user(self, botnick):
        self.irc.send("USER " + botnick + " " + botnick + " " + botnick + " :Sam's!\r\n")

    def nick(self, botnick):
        self.irc.send("NICK " + botnick + "\r\n")

    def join(self, channel):
        self.irc.send("JOIN " + channel + "\r\n")  # join the chan




