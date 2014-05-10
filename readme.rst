
APT, a Command-line Wrapper
============================

A shorter, simpler, and slightly saner interface to the
`Debian APT <http://en.wikipedia.org/wiki/Advanced_Packaging_Tool>`_
command-line tools.

``apt`` may be thought of as a traffic cop
that directs commands to the appropriate tool,
automatically elevating itself with sudo if need-be.
It consolidates all commands from ``apt-get`` and ``apt-cache``,
and the most common from
``aptitude, dpkg, dpkg-query, add-apt-repository``, and ``apt-key``.
It has a much narrower focus than "kitchen-sink" tools such as ``wajig``.

| Hopefully this micro-project will make your life a tiny bit easier.
|

Installation
--------------

::

    sudo pip install apt-wrapper

or for a possibly more up-to-date version::

    sudo pip install https://bitbucket.org/mixmastamyk/apt/get/default.tar.gz

|

Usage
--------------

Examples::

    apt                             # list available commands
    apt addrepo universe partner    # invokes sudo automatically.
    Password:

    apt addrepo ppa:who/foo
    apt update
    apt search foo
    apt policy foo
    apt install foo bar
    apt purge foo
    apt instdeb foo.deb
    apt instdeb http://foo...       # new

    apt who-owns `which tr`         # dpkg-query --searchfiles
    coreutils: /usr/bin/tr

|

Shortened commands
~~~~~~~~~~~~~~~~~~~~

``apt`` can also handle shortened commands.
Add letters until it can be uniquely identified::

    apt cl

results in::

    sudo apt-get clean

|

Aliases
~~~~~~~~~

There are a few aliases for common commands as well::

    apt in foo                  # install
    apt rm bar                  # remove
    apt se baz                  # apt-cache search
    apt ls boo                  # list installed packages, optionally
                                # with pkg name or name fragment\*
    apt dir                     # dir (e.g. NT or ls -l) installed

Problem?
``-d`` can help by outputting debugging information such as the full
command-line::

    $ apt who-owns /bin/less -d
    Running: dpkg-query -S /bin/less
    less: /bin/less

|

License
~~~~~~~~~

Licensed under the `GPL, version 3+ <http://www.gnu.org/licenses/gpl.html>`_.

|

Release Notes
~~~~~~~~~~~~~~~

- 1.09 - enh: addrepo can now enable standard repos, print commands.
- 1.08 - enh: instdeb can now download and install from urls.
- 1.07 - Fix auto elevate for instdeb.
- 1.06 - Add ls and dir aliases and doc syntax.
- 1.05 - Doc improvements.
- 1.04 - Allow additional options to be passed thru w/o error.
- 1.03 - Update readme with release notes and document new aliases.
- 1.02 - Add ``who-owns`` alias for ``searchfiles``.
- 1.01 - Add ``in`` alias for ``install``.
