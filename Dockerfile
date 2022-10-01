FROM wettyoss/wetty

RUN apk add python3 bash openssh

ENV WEB_TTY_CMD "python3 /workspace/main.py"

RUN mkdir -p /workspace
COPY . /workspace
RUN bash /workspace/setup.sh

RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
RUN python3 -m pip install -r /workspace/requirements.txt

ENTRYPOINT ["./wetty.sh"]
