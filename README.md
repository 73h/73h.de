# 73h.de

This is my homepage.

## local start

Set these entries in your local /etc/hosts file for domain-handling.

```
127.0.0.1 blog.73h-dev.de
127.0.0.1 www.73h-dev.de
127.0.0.1 73h-dev.de
```

Create a virtual env (venv)

```
pip install virtualenv
virtualenv --python C:\Path\To\Python\python.exe venv
.\venv\Scripts\activate
```

Start the flask application with the following command.

```
cd app
python -m flask run -p 80
```

Go to http://73h-dev.de in your browser.
