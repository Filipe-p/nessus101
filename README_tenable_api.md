# Tenable Nessus Essential API testing 

This `README` is to keep our notes as we're going to explore the Tennable Nessus API. 


### Pre requisits 

- Tenable instance running 
- Tenable has been activated
- Tenable dependencies has installed (you can scann)
- Python 3

Note: See original `README.md` to setup a container with a pod

### Getting Started 

**API docs**
We're using the internal documentation as reference https://0.0.0.0:8834/api#/overview.

**Virtual environment and dependencies**

Create a virtual environment, activate it and consume the requierments 

```python
# Create env
$ python3 -m venv ./venv/

# Activate the environemnt
$ source venv/bin/activate

# Consume dependencies
$ pip install -r .requirements.txt

```

### Connection / Authenthication