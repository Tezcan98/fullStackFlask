import base64

blob = "blob:http://localhost:5000/c4a29220-3327-4381-b45a-3335dfae5465"

base64.b64encode(blob).decode('utf-8')
