FROM jupyterhub/jupyterhub

RUN pip install jupyterhub-kubespawner
RUN pip install jupyterhub-dummyauthenticator
RUN pip install escapism
# Causes problems with connecting to python intepreter
RUN pip uninstall -y tornado
RUN pip install tornado==5.1.1
ADD jupyterhub_config.py jupyterhub_config.py
CMD jupyterhub --no-ssl --log-level=DEBUG