import socket
import sys
import random
from dataclasses import dataclass







class ChatProgramma:
    
    def __init__(self):
        self.CommandlineArgs()
        
    def CommandlineArgs(self):
        
        Nickname = sys.argv[1]
        Hostname = sys.argv[2]
        port_uitgaand = int(sys.argv[3])
        port_inkomend = int(sys.argv[4])
        return self.UDPSocket(Nickname, Hostname, port_uitgaand, port_inkomend)
    
    def BerichtenDatabase():
        pass
    
    def UDPSocket(self, Nickname, Hostname, port_uitgaand, port_inkomend):
        SocketObject = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        seqnum = 0
        # ontvang en verzend berichten
        SocketObject.bind((Hostname, port_inkomend))
        Verzendbericht = None
        while Verzendbericht != "quit":
            Verzendbericht = input("Geef je bericht:\n")
            try:
                seqnum += 1
                SocketObject.sendto(f"{Nickname}: {Verzendbericht}\n [{seqnum}]".encode('utf-8'), (Hostname, port_uitgaand))
            except Exception:
                SocketObject.sendto(f"{Nickname}: {Verzendbericht}\n [{seqnum}]".encode('utf-8'), (Hostname, port_inkomend))
            try:
                Ontvangen_bericht, adr = SocketObject.recvfrom(1000) # --> dit geeft een tuple terug (b'bericht', (localhost, port))
                print(Ontvangen_bericht.decode())
            except Exception:
                print(f"{Verzendbericht} met seqnum {seqnum}") # ff voor debugging
                continue


    

    
def main():
    Chat = ChatProgramma()



if __name__ == "__main__":
    main()