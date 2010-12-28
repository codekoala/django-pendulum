#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import pendulum

setup(
    name='django-pendulum',
    version=pendulum.version(),
    description="A simple timeclock/timecard application for use in Django-powered Web sites.",
    long_description=open('README.rst', 'r').read(),
    keywords='django, time tracking, pendulum',
    author='Josh VanderLinden',
    author_email='codekoala@gmail.com',
    url='http://bitbucket.org/codekoala/django-pendulum/',
    license='MIT',
    package_dir={'pendulum': 'pendulum'},
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Office/Business :: Financial :: Accounting',
        'Topic :: Office/Business :: Scheduling',
    ],
    zip_safe=False,
)
