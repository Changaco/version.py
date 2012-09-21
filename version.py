# Original author: Douglas Creager <dcreager@dcreager.net>
# This file is placed into the public domain.

"""
Gets the current version number.
If in a git repository, it is the current git tag.
Otherwise it is the content of the RELEASE-VERSION file.

To use this script, simply import it your setup.py file, and use the
results of get_version() as your package version:

    from version import *

    setup(
        version=get_version(),
        .
        .
        .
    )

This will automatically update the RELEASE-VERSION file. Note that
the RELEASE-VERSION file should *not* be checked into git, you can
add it to your .gitignore file.

You need to distribute the RELEASE-VERSION file in your sdist
packages by adding the following line in the MANIFEST.in file:

    include RELEASE-VERSION
"""

__all__ = ('get_version')


from os.path import dirname, isdir, join
from subprocess import CalledProcessError, check_output


def get_version():
    if isdir(join(dirname(__file__), '.git')):
        # Get the version using "git describe".
        cmd = 'git describe --tags --match [0-9]*'
        try:
            version = check_output(cmd.split()).decode().strip()
        except CalledProcessError:
            return

        # PEP 386 compatibility
        if '-' in version:
            version = '.post'.join(version.split('-')[:2])

        # Update the RELEASE-VERSION file.
        with open('RELEASE-VERSION', 'w') as f:
            f.write('%s\n' % version)

    else:
        # Read the version from the RELEASE-VERSION file.
        with open('RELEASE-VERSION', 'r') as f:
            version = f.read().strip()

    return version


if __name__ == '__main__':
    print(get_version())
