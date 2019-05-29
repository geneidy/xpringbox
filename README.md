# xpringbox

Demonstration of trustlines. 

This is inteded to demonstrate [trust lines](https://developers.ripple.com/trust-lines-and-issuing.html).

## Prep

### Virtual Environment

For the purposes of this demonstration, we'll be using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/). 

```bash
mkvirtualenv --python=python3 xpringbox
```

### Dependencies

Our only requirement beyond python's standard library is [cmd2](https://github.com/python-cmd2/cmd2) for the command-line interpreter.

```bash
pip install -r requirements.txt
```
or simply
```bash
pip install cmd2
```

## Usage

Ensure you're using the correct python interpreter.

```bash
workon xpringbox
which python3 # $HOME/.virtualenvs/xpringbox/bin/python3
```

### Terminal 1
```bash
./start-trustline.py --host_addr "127.0.0.1" --host_port 10889 --host_name "alice" --remote_addr "127.0.0.1" --remote_port 10888
```

### Terminal 2
```bash
./start-trustline.py --host_addr "127.0.0.1" --host_port 10888 --host_name "bob" remote_addr "127.0.0.1" --remote_port 10889
```

## Demo