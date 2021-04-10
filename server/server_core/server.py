import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid , environ):
    print(" # LOGS # " + sid , " connected")
    sio.emit('welkome_message' ,sid + " is conected !!!" )

@sio.event
def disconnect(sid):
    print(" # LOGS # " + sid , " disconnect")
    sio.emit('disconnect_message' , sid + "is disconnected !!!")

@sio.on('message')
def get_message_from_client(sid , data):
    print("Client SID > " + sid + " # " + data)
    sio.emit('recive_message' , "Name > " + data)

#start gunicorn server <gunicorn :8000 --threads 50 server:app >

#stop ps|grep gunicorn | sudo kill -9 19450