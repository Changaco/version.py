# Source: https://github.com/Changaco/version.py

from os.path import dirname, isdir, join
import re
from subprocess import CalledProcessError, check_output

__all__ = ('get_version')

tag_re = re.compile(r'\btag: ([0-9][^,]*)\b')
version_re = re.compile('^Version: (.+)$', re.M)


def get_version():
    # Return the version if it has been injected into the file by git-archive
    version = tag_re.search('$Format:%D$')
    if version:
        return version.group(1)

    d = dirname(__file__)

    if isdir(join(d, '.git')):
        # Get the version using "git describe".
        cmd = 'git describe --tags --match [0-9]* --dirty'.split()
        try:
            version = check_output(cmd).decode().strip()
        except CalledProcessError:
            print('Unable to get version number from git tags')
            exit(1)

        # PEP 440 compatibility
        if '-' in version:
            if version.endswith('-dirty'):
                print('The working tree is dirty')
                exit(1)
            version = '.post'.join(version.split('-')[:2])

    else:
        # Extract the version from the PKG-INFO file.
        with open(join(d, 'PKG-INFO')) as f:
            version = version_re.search(f.read()).group(1)

    return version


if __name__ == '__main__':
    print(get_version())
