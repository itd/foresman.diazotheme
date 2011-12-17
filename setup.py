# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = open(os.path.join("foresman", "diazotheme", "version.txt")).read().strip()

setup(name='foresman.diazotheme',
      version=version,
      description="A responsive design for Plone/Diazo powered sites",
      long_description=open(os.path.join("README.rst")).read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='web zope plone theme responsive mobile',
      author='Kurt Bendl',
      author_email='kurt.tool.net',
      url='http://tool.net/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['foresman',],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'plone.app.theming',
      ],
      entry_points={
          'z3c.autoinclude.plugin': 'target = plone',
      },
      )