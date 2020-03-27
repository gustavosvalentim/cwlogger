# CWLogger
API to manage CloudWatch Log Group events using Python.

# Installation
1. Clone this repo

`git clone https://github.com/gustavosvalentim/cwlogger`

2. Install using pip

`pip install ./cwlogger`

# Usage
```python
import cwlogger.core as cwlogger

logger = cwlogger.CWLogger('/aws/service/resource_name')
logger.tail()
```