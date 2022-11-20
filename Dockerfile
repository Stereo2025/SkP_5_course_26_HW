#FROM python:3.10-slim
#
#ENV HOME=/home/app
#WORKDIR $HOME
#
#COPY requirements.txt .
#RUN python3 -m pip install -r requirements.txt
#
#COPY . .
#
#ENTRYPOINT ["sh", "entrypoint.sh"]
