#!/bin/bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"

/etc/init.d/redis-server force-reload
python3 /track/bot/run.py --sync &
python3 /track/bot/worker.py -q single

wait -n

exit $?