FROM debian
RUN apt update && \
  apt install -y openssh-client
RUN [ ! -f ~/.ssh/id_rsa ] && ssh-keygen -f ~/.ssh/id_rsa -N ""
RUN eval $(ssh-agent)
# RUN ssh-add ~/.ssh/id_rsa
# RUN ssh -R lg1447-test-server-webhooks:80:localhost:8080 serveo.net -o StrictHostKeyChecking=no
CMD ["ssh", "-R", "lg1447-tgbotwebapp-test-webhook:80:webhook:5000", "-R", "lg1447-tgbotwebapp-test-webapp:80:frontend:3000", "-R", "lg1447-tgbotwebapp-test-backend:80:backend:4000", "serveo.net", "-o", "StrictHostKeyChecking=no", "/bin/bash"]
