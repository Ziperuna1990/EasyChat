import socketio

sio = socketio.AsyncServer(async_mode='asgi')
app = socketio.ASGIApp(sio)


#connections events
@sio.event
async def connect(sid , environ):
    print(" # LOGS # " + sid , " connected")
    await sio.emit('welkome_message' ,sid + " is conected !!!" )

#disconnect events
@sio.event
async def disconnect(sid):
    print(" # LOGS # " + sid , " disconnect")
    await sio.emit('disconnect_message' , sid + "is disconnected !!!")

#get message from client and recive from all clients
@sio.on('message')
async def get_message_from_client(sid , data=[]):
    print("### LOGS ### " + sid + " - " + data[0] + " - " + data[1])
    print(data)
    await sio.emit('recive_message' , data[0] + " -> " + data[1])

@sio.on('login')
async def get_login_info(sid , data):
    print("### LOGS ### " + sid + " - " + data + " # login")
    await sio.emit('recive_login' , data)

@sio.on('logout')
async def get_logout_info(sid , data):
    print("### LOGS ### " + sid + " - " + data + " # logout")
    await sio.emit('recive_logout', data)