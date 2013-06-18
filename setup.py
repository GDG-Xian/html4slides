#!/usr/bin/env python
from setuptools import setup

setup(name='html4slides',
      version='0.1',
      description="It's a tool to convert markdown file into slides file",
      url='https://github.com/GDG-Xian/html4slides',
      author='David Xie',
      author_email='david.scriptfan@gmail.com',
      packages=['html4slides'],
      platforms='any',
      zip_safe=False,
      install_requires=['markdown', 'BeautifulSoup'],
      entry_points = {
            'console_scripts': ['givemeslides = html4slides.cmdline:main'],
        },
    )
