# SERVICE TESTING WITH PYTHON AND BEHAVE

## Configuring a Python virtual environment

Let’s start by installing the **python3-venv** package that provides the venv module.

```$ sudo apt install python3-venv```


To create a virtual environment using Python use the following command:

```$ python3 -m venv venv```


Now it’s time to activate the environments created.

```$ source venv/bin/activate```


Installing Packages regarding dependencies.

```$ pip3 install -r requirements.txt```


Once you are done with your work to deactivate the environment, simply type deactivate and you will return to your normal shell.

```$ deactivate```

## Environments
There are  ```develop, local, production``` environments in which has to export the env variables, such as: 

__Note: ```develop``` is the default environment.__

- Develop:
```export TARGET_ENV="DEVELOP"```


## Running

- Using behave
> behave

- For CI/CD
> python3 main.py
