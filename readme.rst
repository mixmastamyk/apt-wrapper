
APT, a Command-line Wrapper
============================

A shorter, simpler, and slightly-saner interface to the
`Debian APT <http://en.wikipedia.org/wiki/Advanced_Packaging_Tool>`_
command-line tools.

``apt`` may be thought of as a traffic cop
that directs commands to the appropriate tool,
automatically elevating itself with sudo if need-be.
It consolidates all commands from ``apt-get`` and ``apt-cache``,
and the most common from
``aptitude, dpkg, dpkg-query, add-apt-repository``, and ``apt-key``.
It has a much narrower focus than "kitchen-sink" tools such as ``wajig``.

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

    apt                       # for a list of available commands
    apt addrepo ppa:who/foo
    apt search foo
    apt policy foo
    apt install foo bar
    Password:

    apt rm foo                # an alias to remove
    apt instdeb foo.deb

etc.
``apt`` can also handle shortened commands.  Add letters to the command until it
is uniquely identified::

    apt cl

results in::

    sudo apt-get clean

Problem?
``-d`` can help by outputting debugging information such as the full
command-line::

    apt searchfiles /bin/less -d

|

License
~~~~~~~~~

Licensed under the `GPL, version 3+ <http://www.gnu.org/licenses/gpl.html>`_.
