# Nexus-Stats-py
[![PyPI](https://img.shields.io/pypi/v/nexus-stats.py.svg)](https://pypi.python.org/pypi/nexus-stats.py/)

An easy to use Warframe API

### How to download

To download, simply run the following code
```
pip install nexus_stats
```

Simple example
```python
import nexus_stats

client = nexus_stats.Client()

print(client.get_user_profile('OrangutanGaming').clan.name)
```