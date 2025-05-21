FROM debian
RUN apt update && \
  apt install -y openssh-client
RUN [ ! -f ~/.ssh/id_rsa ] && ssh-keygen -f ~/.ssh/id_rsa -N ""
RUN eval $(ssh-agent)
CMD ["ssh", "-R", "lg1447-tgbotwebapp-test:80:nginx:80", "serveo.net", "-o", "StrictHostKeyChecking=no", "/bin/bash"]
