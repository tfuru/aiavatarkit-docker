FROM python

ENV LANG C.UTF-8

RUN apt-get update
RUN apt install -y pulseaudio alsa-utils portaudio19-dev

RUN pip install --upgrade pip

COPY ./app/requirements.txt /tmp

WORKDIR /aiavatar
RUN pip install -r /tmp/requirements.txt

# CMD ["python", "run.py"]