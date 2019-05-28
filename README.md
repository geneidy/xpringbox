# xpringbox

This is inteded to demonstrate the use of [trust lines](https://developers.ripple.com/trust-lines-and-issuing.html).

## Installation

For the purposes of this demonstration, we'll be using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/). 

```bash
mkvirtualenv --python=python3 xpringbox
workon xpringbox
which python3 # $HOME/.virtualenvs/xpringbox/bin/python3
```

Install dependencies: our only requirement is [cmd2](https://github.com/python-cmd2/cmd2)

```bash
pip install -r requirements.txt
```

## Usage

alias pdex_start="cd $PDEX; mux stat ."
alias pdex_stop="tmux kill-session -t pdex"

        - workon xpringbox; ./start-trustline.py --host_ip "127.0.0.1" --host_port 10808 --remote_ip "127.0.0.1" --remote_port 10880
        - sleep 5; workon xpringbox; ./start-trustline.py --host_ip "127.0.0.1" --host_port 10880 --remote_ip "127.0.0.1" --remote_port 10808
