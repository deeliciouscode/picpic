from flask import Flask, jsonify, request, url_for
from flask_cors import CORS
from celery import Celery
import random
import time
from mosaicpy import *

img_folders = [
            './img/picsProcessed', 
            './img/picsProcessed/small', 
            './img/pics', 
            './img/pics/small',
            './img/metaImg', 
            './img/metaImg/small'
            ]

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)
# app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/nametags', methods=['POST'])
def nametags():
    post_data = request.get_json()
    task = download_images.delay(post_data)
    d_sub(post_data)
    return jsonify({'location': url_for('taskstatus', task_id=task.id)}), 202

@app.route('/status/<task_id>')
def taskstatus(task_id):
    task = download_images.AsyncResult(task_id)
    if task.state == 'PENDING':
        # job did not start yet
        response = {
            'state': task.state,
            'current': 0,
            'total': 1,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'current': task.info.get('current', 0),
            'total': task.info.get('total', 1),
            'status': task.info.get('status', '')
        }
        if 'result' in task.info:
            response['result'] = task.info['result']
    else:
        # something went wrong in the background job
        response = {
            'state': task.state,
            'current': 1,
            'total': 1,
            'status': str(task.info),  # this is the exception raised
        }
    return jsonify(response)

@celery.task(bind=True)
def download_images(self, post_data):
    """Background task that runs a long function with progress reports."""

    
    verb = ['Starting up', 'Booting', 'Repairing', 'Loading', 'Checking']
    adjective = ['master', 'radiant', 'silent', 'harmonic', 'fast']
    noun = ['solar array', 'particle reshaper', 'cosmic ray', 'orbiter', 'bit']
    message = ''
    total = random.randint(10, 50)
    for i in range(total):
        if not message or random.random() < 0.25:
            message = '{0} {1} {2}...'.format(random.choice(verb),
                                              random.choice(adjective),
                                              random.choice(noun))
        self.update_state(state='PROGRESS',
                          meta={'current': i, 'total': total,
                                'status': message})
        time.sleep(1)
    return {'current': 100, 'total': 100, 'status': 'Task completed!',
            'result': 42}


def d_sub(post_data):
    print("i am here")
    print(post_data) # TODO: add the algorithm 

if __name__ == '__main__':
    app.run()
