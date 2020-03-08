FROM python:3

RUN apt update -y && apt install -y docker.io vim
RUN pip install ansible==2.9.6 molecule==2.22 docker==4.2.0

WORKDIR /project
CMD ["/bin/bash"]
