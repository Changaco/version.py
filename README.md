`version.py` saves you from having to hard-code the version number of your
project by getting it from git tags (directly or indirectly).

To use the script, simply import it in your `setup.py` file
and use the results of `get_version()` as your package version:

    from version import *

    setup(
        ...
        version=get_version(),
        ...
    )

You need to distribute the `version.py` file in your sdist packages
by adding the following line in the `MANIFEST.in` file:

    include version.py

For the script to work within git archives you need to add the following line
to the `.gitattributes` file:

    version.py  export-subst

---

Licence: [CC0 Public Domain Dedication](http://creativecommons.org/publicdomain/zero/1.0/)
