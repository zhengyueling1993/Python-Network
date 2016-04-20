import getpass
import sys
import telnetlib

def run_telnet_session():
    host = raw_input("Enter remote localhost:")
    user = raw_input("Enter your remote")
    password = getpass.getpass()

    session = telnetlib.Telnet(host)
    session.read_until("login:")
    session.write(user + "\n")
    if password:
        session.read_until("Password:")
        session.write(password + "\n")

    session.write("ls\n")
    session("exit\n")

    print  session.read_all()

if __name__ == '__main__':
  run_telnet_session()