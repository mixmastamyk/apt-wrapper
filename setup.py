#!/usr/bin/env python
from distutils.core import setup

# grab metadata
version = '1.00'
with open('apt') as f:
    for line in f:
        if line.startswith('__version__'):
            try:
                version = line.split("'")[1]
            except IndexError:
                pass
            break
# readme is needed at register time, not install time
try:
    with open('readme.rst') as f:
        long_description = f.read()
except IOError:
    long_description = ''


setup(
    name          = 'apt-wrapper',
    version       = version,
    description   = 'A simpler interface to the Debian/Ubuntu APT command-line tools.',
    author        = 'Mike Miller',
    author_email  = 'mixmastamyk@bitbucket.org',
    url           = 'https://bitbucket.org/mixmastamyk/apt',
    download_url  = 'https://bitbucket.org/mixmastamyk/apt/get/default.tar.gz',
    license       = 'GPLv3',
    scripts       = ['apt'],

    long_description = long_description,
    classifiers     = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],
)
