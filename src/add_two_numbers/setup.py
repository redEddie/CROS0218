Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from setuptools import find_packages, setup
... 
... package_name = 'add_two_numbers'
... 
... setup(
...     name=package_name,
...     version='0.0.0',
...     packages=[package_name],
...     install_requires=['setuptools'],
...     zip_safe=True,
...     maintainer='Your Name',
...     maintainer_email='your_email@example.com',
...     description='A simple package for adding two numbers',
...     license='Apache License 2.0',
...     tests_require=['pytest'],
...     entry_points={
...         'console_scripts': [
...             'add_two_numbers_service = add_two_numbers.add_two_numbers_service:main',
...             'add_two_numbers_client = add_two_numbers.add_two_numbers_client:main',
...         ],
...     },
... )
