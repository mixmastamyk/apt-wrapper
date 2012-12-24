
APT, a Command-line Wrapper
============================

A shorter, simpler, and slightly-saner interface to the Debian APT command-line
tools.
apt is a single command that will automatically elevate itself with sudo if
need-be.  It consolidates all commands from apt-get and apt-cache, and a few
from aptitude and apt-key, etc.

Hopefully this micro-project will make your life a tiny bit easier.


Installation
--------------

::

    sudo pip install apt-wrapper

or for a possibly more up-to-date version::

    sudo pip install https://bitbucket.org/mixmastamyk/apt/get/default.tar.gz


Usage
--------------

::

    apt search foo
    apt policy foo
    apt install foo bar
    Password:

    apt remove foo

etc.
It can also handle shortened commands, as long as they are unique::

    apt cl

results in::

    sudo apt-get clean


License
~~~~~~~~~

Licensed under the GPL, version 3+.
