import socket
import threading
import time
import udp_server
from datetime import datetime



class UDPServer:
    ''' A simple UDP Server '''
    def __init__(self, host, port):

        self.host = host    # Host address
        self.port = port    # Host port
        self.sock = None    # Socket
        self.socket_lock = threading.Lock()
        self.binder = (self.host,self.port)
    def printwt(self, msg):

        ''' Print message with current date and time '''
        current_date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(current_date_time,msg)
        print(msg)

    def configure_server(self):


        ''' Configure the server '''
        # create UDP socket with IPv4 addressing

        self.printwt('Creating socket...')
        self.printwt('Socket created')
        # bind server to the address
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.printwt('Binding server to ' + str(self.host) + str(self.port))
        self.printwt('Server binded to' + str(self.host) + str(self.port))
        self.sock.bind(self.binder)

    def get_latitude(self, name):
        
        ''' Get latitude for a given uav '''
        uav_list = {'UAV1': '27.653456', 'UAV2': '27.653556'}
        if name in uav_list.keys():
            return name + "latitude is " + uav_list[name]


        else:
            return "No records found for " + name
    def handle_request(self, data, client_address):

        ''' Handle the client '''
        # handle request

        name = data.decode('utf-8')
        self.printwt('[ REQUEST from]' + str(client_address))
        print('\n', name, '\n')
        # send response to the client
        resp = self.get_latitude(name)

        time.sleep(3)
        self.printwt('[ RESPONSE to ]'+ str(client_address))
        self.sock.sendto(resp.encode('utf-8'), client_address)
        print('\n', resp, '\n')
    def wait_for_client(self):

        ''' Wait for a client '''
        try:
            # receive message from a client

            data, client_address = self.sock.recvfrom(4096)
            # handle client's request

            self.handle_request(data, client_address)
        except OSError as err:
            self.printwt(err)
    def shutdown_server(self):


        ''' Shutdown the UDP server '''
        self.printwt('Shutting down server...')
        self.sock.close()


def main():
    ''' Create a UDP Server and handle multiple clients simultaneously '''
    udp_server_multi_client = UDPServer('127.0.0.1', 10000)
    udp_server_multi_client.configure_server()
            
    while(True):

        try:

            udp_server_multi_client.wait_for_client()
            #udp_server_multi_client.handle_request()

        except KeyboardInterrupt:
            UDPServer.shutdown_server()

if __name__ == '__main__':
    main()