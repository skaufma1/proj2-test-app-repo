import docker
client = docker.from_env()
image, logs = client.images.build(path="/home/skaufma/PycharmProjects/proj2_prod_deploy/my_app", tag="proj2-test-flask-app:1.0.3")
for line in logs:
    print(line)