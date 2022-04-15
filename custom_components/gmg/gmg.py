"""Green Mountain Grill API library"""


from audioop import add
from distutils.log import error
from email import message
import socket
import binascii
import ipaddress
from tkinter import W
# from webbrowser import get

def grills(timeout = 1, ip_bind_address = '0.0.0.0'):

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    # this needs to be 0.0.0.0 ... it was binding to wrong adapter
    sock.bind((ip_bind_address, grill.UDP_PORT))

    grills = [] 

    try:
        message = grill.CODE_SERIAL
        sock.sendto(message, ('<broadcast>', grill.UDP_PORT))
        # Each recv should have the full timeout period to complete
        sock.settimeout(timeout)

        while True:
            # Get some packets from the network
            data, (address, _) = sock.recvfrom(1024)
            response = data.decode('utf-8')

            # Confirm it's a GMG serial number
            try:
                if response.startswith('GMG'):
                    grills.append(grill(address, response))
            except ValueError:
                pass

    except socket.timeout:
        # This will always happen, a timeout occurs when we no longer hear from any fires
        # This is the required flow to break out of the `while True:` statement above.
        pass
    finally:
        # Always close the socket
        sock.close()

    return grills


class grill(object):
    UDP_PORT = 8080
    MIN_TEMP = 150
    MAX_TEMP = 550
    CODE_SERIAL = b'UL!'
    CODE_STATUS = b'UR001!'
    
    def __init__(self, ip, serial_number = ''):
        
        if not ipaddress.ip_address(ip):
            raise ValueError(f"IP address not valid {ip}")

        self._ip = ip 
        self._serial_number = serial_number

    def gmg_status_response (self, value_list):
        # accept list of values from status 
        self.state = {}

        # grill general status
        self.state['on'] = value_list[30]
        self.state['temp'] = value_list[2]
        self.state['temp_high'] = value_list[3]
        self.state['grill_set_temp'] = value_list[6]
        self.state['grill_set_temp_high'] = value_list[7]

        # probe 1 stats
        self.state['probe_temp'] = value_list[4]
        self.state['probe_temp_high'] = value_list[5]
        self.state['prob_set_temp'] = value_list[28]
        self.state['prob_set_temp_high'] = value_list[29]
        
        # probe 2 stats
        self.state['probe2_temp'] = value_list[16]
        self.state['probe2_temp_high'] = value_list[17]
        self.state['probe2_set_temp'] = value_list[18]
        self.state['probe2_set_temp_high'] = value_list[19]
        
        # print(self.gmg_status)

        return self.state

    def status(self):
        return self.gmg_status_response(list(self.send(grill.CODE_STATUS)))

    def serial(self):

        self._serial_number = self.send(grill.CODE_SERIAL).decode('utf-8')

        return self._serial_number

    def send(self, message):

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        try:
            sock.sendto(message, (self._ip, grill.UDP_PORT))
            data, _ = sock.recvfrom(1024)
        
        except socket.timeout:
            print('timeout')
           
        return data
