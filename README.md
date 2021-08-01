# ml-ya-utils

Yet Another Utilities for Machine Learning

# Installation

```
pip install git+https://github.com/yasuyuky/ml-ya-utils
```

# Usage

```python
from ml.ya.utils import rangelog, SourceBackup, ArgumentBackup, FinalRequest
```

## rangelog

range based logger

```python
def train(args):
    with rangelog("setup dataset"):
        ...
    with rangelog("training") as logger:
        ...
```

Above code output like this.

```
--> Start: setup dataset
<-- End: setup dataset
--> Start: training
<-- End: training
```

### If you want to use the logger you defined

```python
def train(args):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    rangelog.set_logger(logger)
    with rangelog("setup dataset"):
        ...
    with rangelog("training") as logger:
        ...
```

### If you want to set start/end message

```python
def train(args):
    rangelog.set_start_msg("start... {name}")
    rangelog.set_end_msg("  end...")
    with rangelog("setup dataset"):
        ...
    with rangelog("training") as logger:
        ...
```

# License

MIT
