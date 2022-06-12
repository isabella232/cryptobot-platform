from flask import Flask
import json
import docker
app = Flask(__name__)
docker_client = docker.from_env()


@app.route('/create_instance/', methods=['POST'])
def create_instance():
    created = docker_client.containers.run(
        "ubuntu", detach=True)
    response = {"message": f"container {created.id} is now running"}
    return json.dumps(response)


@app.route('/get_status/<string:id>/', methods=['GET'])
def get_status(id):
    status = docker_client.containers.get(id).status
    response = {f"{id}": f"{status}"}
    return json.dumps(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
