from fabric.api import *
from fabric.contrib.console import confirm

def pack():
    # build the package
    local('python setup.py sdist --formats=gztar', capture=False)

def dev():
    # uninstall
    local('pip uninstall convertextract')

    # build the package
    pack()

    # reinstall
    fn = "convertextract-" + "1.6.2" + ".tar.gz"
    local('pip install dist/' + fn)

    # local('python run.py')