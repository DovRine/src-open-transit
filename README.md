# src-open-transit
Code repository for the InnovateVegas Open Transit project


## Developer Setup

NOTE: Since we haven't fully decided which language(s) we are using yet, there are prototypes in a few different languages.

A better way to do this might be to make different branches/tags or even repos for the different implementations but I'm expecting to decide on the stack pretty quickly once development starts in earnest.

Ultimately, I plan to setup Docker containers for each env and expect to develop locally inside them using vscode's remote extension.


---

### Beginner Resources
#### Tools
- Git
    - Download: https://git-scm.com/downloads
    - Tutorial: https://www.freecodecamp.org/news/an-introduction-to-git-for-absolute-beginners-86fa1d32ff71/
- Docker
    - Download: https://docs.docker.com/get-docker/ (Note that Docker Desktop is different than Docker. Ask one of the seniors for help if you have questions or aren't sure how to proceed.)
    - Tutorial: https://www.docker.com/101-tutorial/
- VsCode
    - Download: https://code.visualstudio.com/download
    - Tutorial: https://code.visualstudio.com/docs/introvideos/basics

#### Technologies and Concepts
- Protocol Buffers (protobuf)
  - github repository: https://github.com/protocolbuffers/protobuf

---

### Prerequisites for all environments
    - git v2+
    - Docker v18+



fork this repo: https://github.com/DovRine/src-open-transit

clone the forked repo

---

### Java
No working examples yet


---

### Python
There is an initial, working, implementation of receiving real-time data.
#### Prerequisites
    - Python 3.9+

##### Local Setup
Note: These instructions are assuming a Mac or Linux environment.

TODO: write instructions for windows users 

NOTE: the commands that activate and deactivate the virtualenv are dependent on how you named it, so if you name your virtualenv differently, you must adapt these commands to match

NOTE: if you name the virtualenv differently, make sure that you update the .gitignore file so that you don't accidentally commit your virtualenv

Initial setup
```bash
$ cd <project root>/src/python
$ python -m venv .venv
$ source .venv/bin/activate
(.venv) $ pip install -r requirements.txt
```

Start Developing
```bash
$ cd <project root>/src/python
$ source .venv/bin/activate
(.venv) $
```

Done for the day
```bash
(.venv) $ deactivate
$
```

Run the current code:
```bash
(.venv) <project root>/src/python $ python main.py 
```