# xpringbox

This is inteded to demonstrate [trust lines](https://developers.ripple.com/trust-lines-and-issuing.html).

## Installation

### Virtual Environment

For the purposes of this demonstration, we'll be using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/). 

```bash
mkvirtualenv --python=python3 xpringbox
workon xpringbox
which python3 # $HOME/.virtualenvs/xpringbox/bin/python3
```

### Dependencies

Our only requirement beyond python's standard library is [cmd2](https://github.com/python-cmd2/cmd2) for the command-line interpreter.

```bash
pip install -r requirements.txt
```

## Usage

alias pdex_start="cd $PDEX; mux stat ."
alias pdex_stop="tmux kill-session -t pdex"

        - workon xpringbox; ./start-trustline.py --host_ip "127.0.0.1" --host_port 10808 --remote_ip "127.0.0.1" --remote_port 10880
        - sleep 5; workon xpringbox; ./start-trustline.py --host_ip "127.0.0.1" --host_port 10880 --remote_ip "127.0.0.1" --remote_port 10808
