
APT - Command-line Wrapper
============================

A simpler, shorter, and slightly-saner interface to the Debian APT command-line
tools.
apt is a single command that will automatically elevate itself with sudo if
need-be.
Hopefully this micro-project will make your life a tiny bit easier.


Installation
--------------

    sudo pip install apt-wrapper


Usage
--------------

::

    apt search foo
    apt policy foo
    apt install foo bar
    Password:

    apt remove foo
    ...

etc.

