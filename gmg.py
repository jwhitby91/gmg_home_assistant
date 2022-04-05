import socket
import binascii
import ipaddress
# from webbrowser import get

class grill(object):
    UDP_PORT = 8080
    CODE_SERIAL = b'UL!'
    CODE_STATUS = b'UR001!'
    
    def __init__(self, ip):
        
        if not ipaddress.ip_address(ip):
            raise ValueError(f"IP address not valid {ip}")

        self._ip = ip 

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

        self.serial_number = self.send(grill.CODE_SERIAL).decode('utf-8')

        return self.serial_number

    def send(self, message):

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        try:
            sock.sendto(message, (self._ip, grill.UDP_PORT))
            data, _ = sock.recvfrom(1024)
        
        except socket.timeout:
            print('timeout')
           
        return data
