FROM jupyterhub/jupyterhub

RUN pip install jupyterhub-kubespawner
RUN pip install jupyterhub-dummyauthenticator
RUN pip install escapism
# Causes problems with connecting to python intepreter
RUN pip uninstall -y tornado
RUN pip install tornado==5.1.1
RUN pip install oauthenticator
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git
#RUN mkdir jupyter-templates/
ADD jupyter-templates/ jupyter-templates/
RUN pip install git+https://github.com/jupyterhub/wrapspawner
ADD jupyterhub_config.py jupyterhub_config.py
ADD spark-connect.py /home/jovyan/work/spark-connect.py
CMD jupyterhub --no-ssl --log-level=DEBUG
