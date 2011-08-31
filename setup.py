#! /usr/bin/env python

# Copyright (c) 2007-2011 PediaPress GmbH
# See README.txt for additional licensing information.

import sys

if not (2, 4) < sys.version_info[:2] < (3, 0):
    sys.exit("""
***** ERROR ***********************************************************
* mwlib does not work with your python version. You need to use python
* 2.5, 2.6 or 2.7
***********************************************************************
""")

try:
    from setuptools import setup, Extension
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, Extension


def main():
    install_requires = ["mwlib>=0.12.16"]

    setup(name="mwlib.xhtml",
          version="0.1.0",
          entry_points={'mwlib.writers': ['xhtml = mwlib.xhtmlwriter:xhtmlwriter']},
          install_requires=install_requires,
          packages=["mwlib", "mwlib.xmlcat"],
          namespace_packages=['mwlib'],
          include_package_data=True,
          zip_safe=False,
          url="http://code.pediapress.com/",
          description="xhtml writer for mwlib",
          license="BSD License",
          maintainer="pediapress.com",
          maintainer_email="info@pediapress.com")

if __name__ == '__main__':
    main()
