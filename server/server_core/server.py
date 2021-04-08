import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid , environ):
    print(sid , " connected")

@sio.event
def disconnect(sid):
    print(sid , " disconnect")

@sio.on('message')
def get_message_from_client(sid , data):
    print("Client SID > " + sid + " # " + data)
    pass

#start gunicorn server <gunicorn :8000 --threads 50 server:app >

#stop ps|grep gunicorn | sudo kill -9 19450