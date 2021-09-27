# client
"""
client.py
"""
import socket
import json
import flow as fl

if __name__ == '__main__':

    try:
        print('start')
        # initialize Socket
        SERVER_ADDR = ('192.168.0.53', 3105)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect(SERVER_ADDR)
            print('connection.')
            while True:
                upper_data, under_data = fl.flow_main()
                upper_str = str(upper_data)
                under_str = str(under_data)
                convert_upper = '"'+ upper_str +'"'
                convert_under = '"'+ under_str +'"'
                data = '{"ctname": "upper", "con": '+convert_upper+'}' + '<EOF>' + '{"ctname": "under", "con": '+convert_under+'}' + '<EOF>'
                print("send : " + str(data) )
 
                client.send(data.encode('utf-8'))

    except Exception as e:
        print(e)