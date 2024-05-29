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

# deactivete the enviroment
$ source deactivate

```

### Connection / Authenthication



### User stories 

**User Story 1**
As a Cyber Security Engineer, I want to be able to authenthicate via Tenable API using `user_name` and `password`, so that I can progamatically consume tennable and automate scans.

Acceptence Criterea: 

- Uses Tenable API
- Authenthicates via `user_name` and  `password`
- Seesion Tokens and other returned information is store in memory
- Fails with wrong password or user

**User Story 1**
As a Cyber Security Engineer, I want to be able to setup basic scans via Tenable API with `name`,  `description`, Target , so that I can progamatically create basics scans 


Acceptence Criterea: 

- Uses Tenable API
- Uses stored logged in session
- All requiered fields are used, 
  


for pid in $(ps -ef | grep nessus | awk '{print $2}'); do kill -9 $pid; done

