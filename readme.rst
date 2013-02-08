
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

    apt                         # list available commands
    apt addrepo ppa:who/foo     # invokes sudo...
    Password:

    apt update
    apt search foo
    apt policy foo
    apt install foo bar

    apt remove foo
    apt instdeb foo.deb


Shortened commands
~~~~~~~~~~~~~~~~~~~~

``apt`` can also handle shortened commands.
Add letters until it can be uniquely identified::

    apt cl

results in::

    sudo apt-get clean

Aliases
~~~~~~~~~

There are a few aliases for common commands as well::

    apt in foo                  # install
    apt rm bar                  # remove
    apt se baz                  # search

|

Problem?
``-d`` can help by outputting debugging information such as the full
command-line::

    $ apt searchfiles /bin/less -d
    Running: dpkg-query -S /bin/less
    less: /bin/less

|

License
~~~~~~~~~

Licensed under the `GPL, version 3+ <http://www.gnu.org/licenses/gpl.html>`_.
