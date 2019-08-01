import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
	README = readme.read()
# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
setup(
	name='django-city',
	version='0.1.0',
	packages=find_packages(),
	include_package_data=True,
	license='BSD License', 
	description='A simple Django app to show city weather state.',
	long_description=README,
	url='https://www.example.com/',
	author='john maluki',
	author_email='john.maluki12@gmail.com',
	classifiers=[
		'Environment :: Web Environment',
		'Framework :: Django',
		'Framework :: Django :: 2.2', 
		'Intended Audience :: Developers',
		'License :: OSI Approved :: BSD License', 
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Topic :: Internet :: WWW/HTTP',
		'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
	],

	install_requires=[
        'Django>=2.2',
        'python>=3.6.0',
        # Additional requirements, or parse the requirements file and add it here
    ],
)