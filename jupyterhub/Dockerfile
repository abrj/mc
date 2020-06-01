FROM python


RUN apt-get update
RUN apt-get install -y nodejs npm
RUN git clone https://github.com/jupyterhub/kubespawner
WORKDIR kubespawner
RUN npm install -g configurable-http-proxy
#RUN pip install jupyterhub jupyterhub-dummyauthenticator
#RUN pip install jupyterhub-kubespawner
RUN pip install -e .
RUN pip install notebook
RUN pip install dockerspawner
RUN pip install netifaces
RUN pip install 
ENV USERNAME=admin
ENV PASSWORD=Password2020
#ENV KUBE-MASTER-IP=192.168.64.2

RUN useradd -m -p $(openssl passwd -1 ${PASSWORD}) -s /bin/bash -G sudo ${USERNAME}
#USER admin
RUN export HUB_CONNECT_IP=192.168.64.2
ADD jupyterhub_config2.py jupyterhub_config.py
CMD jupyterhub --no-ssl
#FROM jupyterhub/jupyterhub
#RUN pip install notebook
#RUN pip install jupyterhub-kubespawner
#RUN pip install jupyterhub jupyterhub-dummyauthenticator


#ADD jupyterhub_config2.py jupyterhub_config.py
#RUN export HUB_CONNECT_IP=${KUBE-MASTER-IP}
#CMD jupyterhub --config jupyterhub_config.py --no-ssl



# https://github.com/jupyterhub/kubespawner/issues/18
#FROM jupyterhub/jupyterhub-onbuild:0.7.1
# Install kubespawner and its dependencies
#RUN /opt/conda/bin/pip install \
#    oauthenticator==0.5.* \
#    git+https://github.com/derrickmar/kubespawner \
#    git+https://github.com/yuvipanda/jupyterhub-nginx-chp.git
#RUN pip install jupyterhub jupyterhub-dummyauthenticator
#ADD jupyterhub_config.py /srv/jupyterhub_config.py
#ADD userlist /srv/userlist
#WORKDIR /srv/jupyterhub
#EXPOSE 8081
#CMD jupyterhub --config /srv/jupyterhub_config.py --no-ssl