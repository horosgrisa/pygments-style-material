#!/usr/bin/python

from setuptools import setup

setup(
    name = 'pygments-style-material',
    version = '0.1',
    description = 'Pygments version of material theme.',
    license = 'GPL3',

    author = 'Grigorii Horos',
    author_email = 'horosgrisa@gmail.com',

    url = 'https://github.com/horosgrisa/pygments-style-material',

    packages = ['pygments_style_material'],
    install_requires = ['pygments >= 1.4'],

    entry_points = '''[pygments.styles]
                      material = pygments_style_material:MaterialStyle''',

    classifiers = [
        'Development Status :: 1 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL3 License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
