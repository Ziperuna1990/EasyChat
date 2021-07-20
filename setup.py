from setuptools import setup

APP_NAME = "EasyChat"
APP = ['client/main.py']
DATA_FILES = [
    ('images' , ['images/*.png'])
]
OPTIONS = {
    'packages':['python-socketio' , 'psycopg2-binary' , 'websocket-client' , 'python-engineio']
}

setup(
    app=APP,
    name=APP_NAME,
    data_files=DATA_FILES,
    options={'py2app':OPTIONS},
    setup_requires= ['py2app']
)

#finnaly
