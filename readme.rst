
APT, a Command-line Wrapper
============================

A shorter, simpler, and slightly-saner interface to the Debian APT command-line
tools.
apt is a single command that will automatically elevate itself with sudo if
need-be.
It consolidates all commands from apt-get and apt-cache, and a few from
aptitude, dpkg, dpkg-query, and apt-key, etc.
It has a much narrower focus than similar tools such as "wajig".

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

    apt                   # for a list of available commands
    apt search foo
    apt policy foo
    apt install foo bar
    Password:

    apt rm foo            # alias
    apt instdeb foo.deb

etc. 
``apt`` can also handle shortened commands.  Add letters to the command until it
is uniquely identified::

    apt cl

results in::

    sudo apt-get clean

``-d`` can help by outputting debugging information such as the full
command-line.

::

    apt searchfiles /bin/less -d


License
~~~~~~~~~

Licensed under the `GPL, version 3+ <http://www.gnu.org/licenses/gpl.html>`_.
