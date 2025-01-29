from flask import Flask, render_template
from repository.database import db
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'development_test'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)
socketio = SocketIO(app)

@app.route('/chat', methods=['GET'])
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    print(f'Message received: {message}')
    socketio.emit('message', message, namespace='/')

if __name__ == '__main__':
    socketio.run(app, debug=True)