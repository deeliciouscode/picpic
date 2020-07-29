from flask import Flask, jsonify, request, url_for, g, abort, current_app, send_from_directory
from werkzeug.exceptions import HTTPException, InternalServerError
from flask_restful import Resource, Api
from datetime import datetime
from functools import wraps
import threading
import time
import uuid
from flask_cors import CORS
from mosaicpy import *
import requests
import shutil

img_folders = [
            './server/img/pics', 
            './server/img/pics/small',
            './server/img/final',
            './server/img/pics/meta'
            ]

tasks = {}

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__, static_url_path='')
app.config.from_object(__name__)
api = Api(app)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.before_first_request
def before_first_request():
    """Start a background thread that cleans up old tasks."""
    def clean_old_tasks():
        """
        This function cleans up old tasks from our in-memory data structure.
        """
        global tasks
        while True:
            # Only keep tasks that are running or that finished less than 5
            # minutes ago.
            five_min_ago = datetime.timestamp(datetime.utcnow()) - 5 * 60
            tasks = {task_id: task for task_id, task in tasks.items()
                     if 'completion_timestamp' not in task or task['completion_timestamp'] > five_min_ago}
            time.sleep(60)

    if not current_app.config['TESTING']:
        thread = threading.Thread(target=clean_old_tasks)
        thread.start()


def async_api(wrapped_function):
    @wraps(wrapped_function)
    def new_function(*args, **kwargs):
        def task_call(flask_app, environ):
            # Create a request context similar to that of the original request
            # so that the task can have access to flask.g, flask.request, etc.
            with flask_app.request_context(environ):
                try:
                    tasks[task_id]['return_value'] = wrapped_function(*args, **kwargs)
                except HTTPException as e:
                    tasks[task_id]['return_value'] = current_app.handle_http_exception(e)
                except Exception as e:
                    # The function raised an exception, so we set a 500 error
                    tasks[task_id]['return_value'] = InternalServerError()
                    if current_app.debug:
                        # We want to find out if something happened so reraise
                        raise
                finally:
                    # We record the time of the response, to help in garbage
                    # collecting old tasks
                    tasks[task_id]['completion_timestamp'] = datetime.timestamp(datetime.utcnow())

                    # close the database session (if any)

        # Assign an id to the asynchronous task
        task_id = uuid.uuid4().hex

        # Record the task, and then launch it
        tasks[task_id] = {'task_thread': threading.Thread(
            target=task_call, args=(current_app._get_current_object(),
                               request.environ))}
        tasks[task_id]['task_thread'].start()

        # Return a 202 response, with a link that the client can use to
        # obtain task status
        print(url_for('gettaskstatus', task_id=task_id))
        return {'Location': url_for('gettaskstatus', task_id=task_id)}, 202
    return new_function

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/nametags', methods=['POST'])
def nametags():
    post_data = request.get_json()
    task_info = download_images(post_data)
    return task_info

@app.route('/getimgids', methods=['GET'])
def getimgids():
    ids = get_files_no_dirs("./server/img/pics")
    return jsonify({"ids": ids})

@app.route('/final/<path:filename>', methods=['GET'])
def getfinal(filename):
    return send_from_directory('./img/final', filename)

@app.route('/largeimgbyid/<path:filename>')
def largeimgbyid(filename):
    return send_from_directory('./img/pics', filename)

@app.route('/composemosaic', methods=['POST'])
def init_composemosaic():
    data = request.get_json()
    task_info = composemosaic(data["id"])
    return task_info

@app.route('/cleardata', methods=['POST'])
def clear_data():
    what = request.get_json()["what"]
    if what == 'all':
        delete_data()
    return jsonify({"worked": True})

def delete_data():
    shutil.rmtree('./server/img')
    createFolders(img_folders)

@async_api
def composemosaic(id):
    compose_and_safe_mosaic(id)

@async_api
def download_images(post_data):
    scrape_and_clean_images(post_data["creds"]["username"], post_data["creds"]["password"], post_data["tags"])
    print("finished downloading and cleaning the images")

class GetTaskStatus(Resource):
    def get(self, task_id):
        """
        Return status about an asynchronous task. If this request returns a 202
        status code, it means that task hasn't finished yet. Else, the response
        from the task is returned.
        """
        task = tasks.get(task_id)
        if task is None:
            abort(404)
        if 'return_value' not in task:
            return {'Location': url_for('gettaskstatus', task_id=task_id)}, 202
        return task['return_value']

api.add_resource(GetTaskStatus, '/status/<task_id>')

if __name__ == '__main__':
    createFolders(img_folders)
    app.run(debug=False, host='0.0.0.0')


# class CatchAll(Resource):
#     @async_api
#     def get(self, path=''):
#         # perform some intensive processing
#         print("starting processing task, path: '%s'" % path)
#         time.sleep(10)
#         print("completed processing task, path: '%s'" % path)
#         return f'The answer is: {path}'


# api.add_resource(CatchAll, '/<path:path>', '/')
