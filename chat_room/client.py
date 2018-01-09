#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import socket, select, string, sys 

def prompt(data=None):
  if data != None:
    sys.stdout.write(data)
  sys.stdout.write('>>> ')
  sys.stdout.flush()
if __name__ == '__main__':
#  HOST = '111.67.192.214'
  HOST = '127.0.0.1'
#  HOST = '59.110.223.71'
  PORT = 5918
  BUFFER = 1024
  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client_socket.settimeout(2)
  try:
    client_socket.connect((HOST, PORT))
  except:
    print 'unable to connect chatroom server'
    sys.exit()
  print 'connected to chatroom server, have a nice chatting.'
prompt()
  while True:
    socket_list = [sys.stdin, client_socket]
    read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])
    for sock in read_sockets:
      if sock == client_socket:
        data = sock.recv(BUFFER)
        if data and len(data):
          prompt(data)
        else:
          print 'disconnection from chatroom server'
          sys.exit()
      else:
        message = sys.stdin.readline().strip('\n')
        client_socket.send(message)
        prompt()
  client_socket.close()
