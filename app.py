from flask import Flask, request
import redis
import json

app = Flask(__name__)
redis_client = redis.Redis(host='localhost', port=6379)


@app.route('/')
def home():
    return 'welcome to web service'

@app.route('/task', methods=['POST'])
def receive_task():
    task_data = request.json
    print(task_data)
    # Publish task to Redis channel
    redis_client.publish('tasks', json.dumps(task_data))
    if task_data:
        return 'Task received and sent to worker', 200 
    else:
        return 'Error in the Process', 400 
    

if __name__ == '__main__':
    app.run(debug=True)