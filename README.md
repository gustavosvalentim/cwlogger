# CWLogger
API to manage CloudWatch Log Group events using Python.

# Installation
1. Clone this repo

`git clone https://github.com/gustavosvalentim/cwlogger`

2. Install using pip

`pip install ./cwlogger`

# Usage
Get logs in real-time as they are generated
```python
import cwlogger.core as cwlogger

logger = cwlogger.CWLogger('/aws/service/resource_name')
for log in logger.get_logs(watch=True):
    # manage your log
```

Get all logs from a date range
```python
for log in logger.get_logs(start='-2days', end='-1days'):
    # manage your logs
```

If you want to use a profile that is not the default, use.
```python
logger = cwlogger.CWLogger('log_group', profile_name='your-profile-name')
```