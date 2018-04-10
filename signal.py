import signal

def signal_handler(sig, num):
    print('Quit')

signal.signal(signal.SIGINT, signal_handler)

