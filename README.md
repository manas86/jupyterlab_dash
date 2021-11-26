# jupyterlab_dash

**This Docker container runs as root user!**

> This is reference from https://www.youtube.com/watch?v=QkOKkrKqI-k 

### Your notebooks

Volumes can be mounted into `/notebooks` folder. If the folder contains a requirements.txt file, it will be installed automatically when the container starts up.

### Run
```bash
docker run --rm -it -p 8888:8888 -p 8050:8050 <imagename>
```

or if you want to define your own password
```bash
docker run --rm -it -p 8888:8888 -p 8050:8050 -e PASSWORD="<your_secret>" <imagename>
```
or 
```bash
docker run --rm -it -p 8888:8888  -p 8050:8050 -v `pwd`:/notebooks -e PASSWORD="<your_secret>" <imagename>
```

The container will install requirements from files present at the root of the repository at `docker run` (in this order):

* `packages.txt`: install apt-get packages
* `requirements.txt`: install pip packages
* `extensions.txt`: install Jupyterlab extensions

After installtion access the jupyterlab using url displayed on stdoutput.
Then to test `dash` application, copy/paste the `dash.py` script in the editor. this will show the dash is running on http://0.0.0.0.8050 

### Build from source

```bash
docker build -t <imagename> .
```
