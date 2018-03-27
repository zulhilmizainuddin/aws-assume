import os
import sys

from awsassume import __version__
from setuptools import setup


sys.path.append(f'{os.getcwd()}/awsassume')
sys.path.append(f'{os.getcwd()}/tests')

setup(name='awsassume',
      version=__version__,
      description='Execute AWS CLI after assuming role',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6',
          'Topic :: Utilities'
      ],
      url='https://github.com/zulhilmizainuddin/aws-assume',
      author='Zulhilmi Mohamed Zainuddin',
      author_email='zulhilmi.zainuddin@outlook.com',
      license='MIT',
      packages=['awsassume'],
      install_requires=[
          'boto3',
          'botocore',
          'python-dateutil'
      ],
      tests_require=[
          'pytest'
      ],
      setup_requires=[
          'pytest-runner'
      ],
      test_suite='tests',
      zip_safe=False)
