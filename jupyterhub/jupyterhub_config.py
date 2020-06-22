import os
import socket

# AUTH
from oauthenticator.gitlab import GitLabOAuthenticator
c.JupyterHub.authenticator_class = GitLabOAuthenticator
c.GitLabOAuthenticator.client_id='d6a422cbeb46c61d11a756f07e4f8387cfb03418314fb7ce42aa35f0539587e7'
c.GitLabOAuthenticator.client_secret='4119d1dc08c462da7e0107f4462cd4402eed9f12fdcfe023007f32d1ad888883'

## Who is allowed access the server
c.Authenticator.admin_users = {"andersjio"}
c.Authenticator.whitelist = {
    "andersjio"
}
# maps gitlab users username
#c.Authenticator.username_map = {
#    "eaton-lab": "deren"
#}


# Do not use any authentication at all - any username / password will work.
#c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'

c.JupyterHub.spawner_class = 'kubespawner.KubeSpawner'

c.KubeSpawner.profile_list = [
    {
        'display_name': 'Singleuser - Python',
        'slug': 'singleuser',
        'default': True,
        'kubespawner_override': {
            'image': 'jupyterhub/singleuser:1.0',
            'cpu_limit': 1,
            'mem_limit': '512M',
            'service_account':'jupyter-hub',
            'namespace':'juphub'            
        }
    }, {
        'display_name': 'Spark - Python',
        'slug': 'training-datascience',
        'kubespawner_override': {
            'image': 'jupyter/all-spark-notebook',
            'cpu_limit': 1,
            'mem_limit': '2G',
            'service_account':'jupyter-hub',
            'namespace':'juphub'
        }
    }
]
# First pulls can be really slow, so let's give it a big timeout
c.KubeSpawner.start_timeout = 60 * 5


c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.hub_ip = '0.0.0.0'
c.JupyterHub.template_paths = ["/srv/jupyterhub/jupyter-templates"]
# Don't try to cleanup servers on exit - since in general for k8s, we want
# the hub to be able to restart without losing user containers
c.JupyterHub.cleanup_servers = False


# Our simplest user image! Optimized to just... start, and be small!
#c.KubeSpawner.image = 'jupyterhub/singleuser:1.0'
#c.KubeSpawner.image = 'jupyter/all-spark-notebook'
# Find the IP of the machine that minikube is most likely able to talk to
# Graciously used from https://stackoverflow.com/a/166589
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
host_ip = s.getsockname()[0]
s.close()

c.JupyterHub.hub_connect_ip = host_ip


#c.KubeSpawner.service_account = 'jupyter-hub'
#c.KubeSpawner.singleuser_service_account = 'jupyter-hub'
#c.KubeSpawner.namespace = 'juphub'
#c.KubeSpawner.storage_pvc_ensure = False

#c.JupyterHub.allow_named_servers = True

#c.KubeSpawner.options_form = '''
#<input name="key" val="default_key"></input>
#<br>
#Choose a letter:
#<select name="letter" multiple="true">
#  <option value="A">The letter A</option>
#  <option value="B">The letter B</option>
#</select>
#'''