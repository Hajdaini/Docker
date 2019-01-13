FROM ansible/ansible:centos7

LABEL maintainer="AJDAINI Hatim <ajdaini.hatim@gmail.com>" \
      description="Docker image to configure your ansible environment"

RUN yum install -y ansible nano openssh-clients sshpass

# override ansible hosts with our config
COPY hosts /etc/ansible/hosts

# genereate ssh key
RUN ssh-keygen -q -t rsa -N '' -f /id_rsa

# add your public key to remote machines
RUN sshpass -p <YOUR_ROOT_REMOTE_MACHINE_PASSWORD> ssh-copy-id -f -o StrictHostKeyChecking=no root@192.168.1.2
RUN sshpass -p <YOUR_ROOT_REMOTE_MACHINE_PASSWORD> ssh-copy-id -f -o StrictHostKeyChecking=no root@192.168.1.3

# tests your command ansible in remote hosts and also ensures that all your ssh connections work
RUN yes 'y' | ansible all -m ping
