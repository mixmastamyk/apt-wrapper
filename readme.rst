
APT, a Command-line Wrapper
============================

A shorter, simpler, and slightly saner interactive interface to the
`Debian/Ubuntu APT <http://en.wikipedia.org/wiki/Advanced_Packaging_Tool>`_
command-line tools.

``apt`` may be thought of as a traffic cop
that directs commands to the appropriate tool,
automatically elevating itself with sudo if need-be.
It consolidates all commands from ``apt-get`` and ``apt-cache``,
and the most common from
``aptitude, dpkg, dpkg-query, add-apt-repository``, and ``apt-key``.
It has a much narrower focus than "kitchen-sink" tools such as ``wajig``.

Hopefully this micro-project will make your life a tiny bit easier.

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

    apt                         # List available commands.
    apt add universe            # Invokes sudo automatically,
    Password:                   # when necessary.

    apt add ppa:who/foo
    apt update
    apt search foo
    apt policy foo
    apt install foo bar
    apt purge foo
    apt instdeb foo.deb
    apt instdeb http://foo...   # new

    apt who-owns `which tr`
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

    apt in foo          # install foo
    apt rm bar          # remove
    apt se baz          # apt-cache search
    apt ls boo          # list installed packages, optionally
                        # with pkg name or glob\* argument syntax.
    apt dir             # dir (e.g. NT or ls -l) installed packages.

|

License
~~~~~~~~~

Licensed under the `GPL, version 3+ <http://www.gnu.org/licenses/gpl.html>`_.

|

Release Notes
~~~~~~~~~~~~~~~

- 1.13 - fix: instdeb exception under Python 3.
- 1.12 - enh: Python 3 support, refactoring.
- 1.11 - enh: rmrepo command to remove ppa's.
- 1.10 - enh: reorder messages, refactoring.
- 1.09 - enh: addrepo can now enable standard repos, print commands by default.
- 1.08 - enh: instdeb can now download and install from urls.
- 1.07 - Fix auto elevate for instdeb.
- 1.06 - Add ls and dir aliases and doc syntax.
- 1.05 - Doc improvements.
- 1.04 - Allow additional options to be passed thru w/o error.
- 1.03 - Update readme with release notes and document new aliases.
- 1.02 - Add ``who-owns`` alias for ``searchfiles``.
- 1.01 - Add ``in`` alias for ``install``.
