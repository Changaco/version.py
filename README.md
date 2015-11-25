`version.py` saves you from having to hard-code the version number of your
project by getting it from git tags (directly or indirectly).

The tags that are considered to be version numbers are those that start with
a digit.

To use the script, simply copy it into your project and call `get_version()`
in your `setup.py` file:

    from version import get_version

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

Compatibility: python 3.x and 2.7

Licence: [CC0 Public Domain Dedication](http://creativecommons.org/publicdomain/zero/1.0/)
