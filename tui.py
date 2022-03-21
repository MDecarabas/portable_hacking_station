import socket
import threading
import sys
  
tello_address = ('192.168.10.1', 8889) # IP and port of Tello

local_address = ('', 9000) # IP and port of local computer

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Create a UDP connection

sock.bind(local_address) # Bind to the local address and port

def send(message):
################### Part of Tello sdk Tutorial
  try:
    sock.sendto(message.encode(), tello_address)
    print("Sending message: " + message)
  except Exception as e:
    print("Error sending: " + str(e))

def receive():
  while True:
    try:
      response, ip_address = sock.recvfrom(128)
      print("Received message: " + response.decode(encoding='utf-8'))
    except Exception as e:
      sock.close()
      print("Error receiving: " + str(e))
      break
##########################################
      
# Continuously monitor for incoming messages
receiveThread = threading.Thread(target=receive)
receiveThread.daemon = True
receiveThread.start()

# Tell the user what to do
print('Type a Tello SDK command and press the enter key to send a command. \r\nEnter "quit" to exit this program.')

# Loop infinitely waiting for commands or until the user types quit or ctrl-c
while True:
  
  try:
    # Read keybord input from the user
    message = input('')
    
    # If user types quit, exit and close the socket
    if 'quit' in message:
      print("Program exited sucessfully")
      sock.close()
      break

    # Send the command to Tello
    send(message)
    
  # Handle ctrl-c to quit and close the socket
  except KeyboardInterrupt as e:
    sock.close()
    break