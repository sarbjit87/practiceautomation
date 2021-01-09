Boiler-plate for FLASK

**Features**

- Bootstrap4
- Bootswatch themes with switch to toggle between light and dark theme
- Basic Authentication with user sign-up, login, password reset etc
- LDAP support
- Flask Migrate for migrations

**Want to use Background tasks?**

Use this repo [Link](https://github.com/sarbjit87/flask_boilerplate_background_tasks) if you want to run some background tasks i.e. sending email using Redis Queue and RQ worker.

**Setup**

`git clone https://github.com/sarbjit87/flask_boilerplate.git`

`pip install -r requirements.txt`

`export FLASK_APP=app`

`flask db init`

`flask db migrate`

`flask db upgrade`

`python3 run.py`

**Screenshot**

![Demo](screenshot/screenshot.png)

**DISCLAIMER**

THE CODE IS BEING PROVIDED FOR INFORMATIONAL PURPOSES ONLY.

USE ON YOUR OWN RISK. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDER OR CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES

THIS REPO IS RELEASED WITH NO WARRANTY AT ALL.
