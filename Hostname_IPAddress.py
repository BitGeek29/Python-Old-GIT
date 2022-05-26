import socket

def get_hostnsme_IP():
    hostname = input("Please enter website addressk(URL):")
    try:
        print(f'Hostname: {hostname}')
        print(f'IP: {socket.gethostbyname(hostname)}')
    except socket.gaierror as error:
        print(f'Invaid Hostname, error raised is {error}')

get_hostname_IP()
