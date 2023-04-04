# Written by Juan Pablo Gutierrez

import machine
import socket

def webPage():
    html = """
    <!DOCTYPE html><html><head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width">
      <title>Dalia Web page</title>
      <link href="style.css" rel="stylesheet" type="text/css" />
    </head><body>
      <!-- Input Form -->
      <p>Created by Juan Pablo Gutierrez</p>
      <form>
        <label for="iText">Choose file to upload</label><br>
        <input type = 'file'id= 'gcodeFile' name="gcodeFile"accept=".gcode">
        <input type="submit">
        <input type="reset">
      </form>
    </body>

    </html>
    """
    return html


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  file = request.find('gcodeFile')
  response = webPage()
  # This reads the input and sends it to the printer
  uart = machine.UART(1, baudrate=115200, tx=17, rx=16)
  command = file  # Send a G28 command to home the printe
  #uart.write(file)
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()

