#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import socket, select

def broadcast_data(sock, message):
  for socket in list(connections.keys()):
    if socket != server_socket and socket != sock:
      try:
        socket.send(message)
      except:
        pass
def cast(d_name, d_socket, message):
      try:
        d_socket.send(message)
      except:
        if d_name in connections.values(): 
          d_socket.close()
          del connections[d_socket]
        data = 'client: %s is offline\n' %(d_name)
        cast_error(sock, data)
def cast_error(socket, message):
      try:
        socket.send(message)
 except:
        print 'error'
if __name__ == '__main__':
  PORT = 5918
  ADDRESS = ('0.0.0.0',PORT)
  BUFFER = 1024
  connections = {}
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  server_socket.bind(ADDRESS)
  server_socket.listen(5)
  connections = {server_socket: ADDRESS}
  print 'chatroom serving on port: %d' %(PORT)
  while True:
    read_sockets, write_sockets, error_sockets = select.select(connections.keys(), [], [])
    for sock in read_sockets:
      if sock == server_socket:
        sockfd, address = server_socket.accept()
        connections.update({sockfd: None})
        print 'client: [%s:%s] connected' %(address)
        sockfd.send('Welcome to this chatroot! Please input your name:\n')
      else:
        try:
          data = sock.recv(BUFFER)
          if data != None and len(data) > 0:
            if connections.values()[connections.keys().index(sock)] == None:
              if data not in connections.values():
                connections.update({sock: data})
                message = '%s entry chatroom\n' %(data)
                broadcast_data(sock, message)
              else:
                message = 'This name is used!\n'
                cast(None, sock, message)
            elif data[0:3] == 'TO:':
              d_name = data[3:].split()[0]
              if d_name not in connections.values():
                cast(d_name, None, data)
              else:
                r_name = connections.values()[connections.keys().index(sock)]
                d_socket = connections.keys()[connections.values().index(d_name)]
                data = 'FROM: ' + r_name + '\n    ' + data[len(d_name)+4:] + '\n'
                cast(d_name, d_socket, data)
########################################################
            elif data[0:5] == 'kill:' and connections.values()[connections.keys().index(sock)] == 'root':
              d_name = data[5:].split()[0]
              d_socket = connections.keys()[connections.values().index(d_name)]
              d_socket.close()
              del connections[d_socket]
########################################################
            else:
              r_name = connections.values()[connections.keys().index(sock)]
              data = r_name + ':\n    ' + data + '\n'
              broadcast_data(sock, data)
        except:
          pass
  server_socket.close()

