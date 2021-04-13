import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio)

#connections events
@sio.event
def connect(sid , environ):
    print(" # LOGS # " + sid , " connected")
    sio.emit('welkome_message' ,sid + " is conected !!!" )

#disconnect events
@sio.event
def disconnect(sid):
    print(" # LOGS # " + sid , " disconnect")
    sio.emit('disconnect_message' , sid + "is disconnected !!!")

#get message from client and recive from all clients
@sio.on('message')
def get_message_from_client(sid , data=[]):
    print("### LOGS ### " + sid + " - " + data[0] + " - " + data[1])
    #print(data)
    sio.emit('recive_message' , data[0] + " -> " + data[1])

@sio.on('login')
def get_login_info(sid , data):
    print("### LOGS ### " + sid + " - " + data + " # login")
    sio.emit('recive_login' , data)

@sio.on('logout')
def get_logout_info(sid , data):
    print("### LOGS ### " + sid + " - " + data + " # logout")
    sio.emit('recive_logout', data)

#start gunicorn server <gunicorn :8000 --threads 50 server:app >

#stop ps|grep gunicorn | sudo kill -9 19450