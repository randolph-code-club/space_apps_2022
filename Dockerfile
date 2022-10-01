FROM wettyoss/wetty

RUN apk add python3 bash openssh

ENV WEB_TTY_CMD "python3 /workspace/main.py"

RUN mkdir -p /workspace
COPY . /workspace
RUN bash /workspace/setup.sh

ENTRYPOINT ["./wetty.sh"]
