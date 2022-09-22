# syntax=docker/dockerfile:1
FROM matthewc2003/trackbot:v6.1

USER root

COPY . /track

RUN export PYENV_ROOT="$HOME/.pyenv" && export PATH="$PYENV_ROOT/bin:$PATH" && eval "$(pyenv init --path)" && pip3 install -U -r /track/requirements.txt
RUN export PYENV_ROOT="$HOME/.pyenv" && export PATH="$PYENV_ROOT/bin:$PATH" && eval "$(pyenv init --path)" && python3 /track/bot/utils/db.py
RUN chmod +x /track/wrapper.sh

CMD ./track/wrapper.sh