# Written by Juan Pablo Gutierrez

import machine
import socket

uploadedFile = ""

# Method that returns the web page
def webPage():
    html = """
    
    <!DOCTYPE html>
<html>

<head>
  <title>Dalia</title>

  <style>
    p {
      font-family: Arial;
      margin-top: 0;
      margin-bottom: 0;
    }

    .title {
      color: black;
      font-size: 25px;
      font-weight: bold;
      text-align: center;
    }

    .subtitle {
      font-size: 15px;
      font-weight: bold;
      text-align: center;
      color: rgb(96, 96, 96);
      margin-top: 15px;
      margin-bottom: 15px;
    }

    .submit-button {
      background-color: rgb(4, 157, 228);
      color: white;
      border: none;
      padding: 10px;
      padding-left: 20px;
      padding-right: 20px;
      border-radius: 18px;
      cursor: pointer;
      font-weight: bold;
      font-size: 15px;
      transition: opacity 0.15s, box-shadow 0.15s;
    }

    .submit-button:hover {
      opacity: 0.7;
      box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.15);
    }

    .upload-button:active {
      opacity: 0.4;
    }

    .submit-button:active {
      opacity: 0.4;
    }

    input {
      display: none;
    }

    label {
      font-family: Arial;
      display: inline-block;
      vertical-align: center;
      text-align: center;
      padding-left: 150px;
      padding-right: 150px;
      padding-top: 100px;
      padding-bottom: 100px;
      border-radius: 6px;
      border: 1px dashed #999;
    }

    label:hover {
      color: #de0611;
      border: 1px dashed #de0611;
    }

    .file-paragraph {
      display: flex;
      justify-content: center;
      align-items: center;
      margin-top: 20px;
    }

    .file-uploader-div {
      display: flex;
      justify-content: center;
      align-items: center;
    }

    .button-div {
      display: flex;
      justify-content: center;
      align-items: center;
      margin-top: 20px;
    }
  </style>
</head>

<body>
  <p class="title"> Dalia Gcode uploader</p>
  <p class="subtitle">Select a file to upload</p>
  <div class="file-uploader-div">
    <input type="file" id="file-input" accept=".gcode" />
    <label for="file-input">Upload Gcode</label>
  </div>

  <p id="file-name" class="file-paragraph"></p>

  <div class="button-div">
    <button class="submit-button" id="submit-button">Submit</button>
  </div>

  <script>
    const fileInput = document.getElementById('file-input');
    const fileName = document.getElementById('file-name');
    const uploadButton = document.getElementById('submit-button');

    fileInput.addEventListener('change', function () {
      const file = fileInput.files[0];
      if (file) {
        fileName.textContent = "File uploaded: " + file.name;
      } else {
        fileName.textContent = 'Failed to upload file';
      }
    });

    uploadButton.addEventListener('click', function () {
      const file = fileInput.files[0];

      const reader = new FileReader();
      reader.onload = function () {
        const contents = reader.result;
        console.log('File contents:', contents);
      };
      reader.readAsText(file);
    });
  </script>

</body>

</html>
    """
    return html


def runMain():
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
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
    
