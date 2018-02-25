from setuptools import setup

setup(name='awsassumerole',
      version='0.1.0',
      description='Execute AWS command after assuming role',
      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities'
      ],
      url='https://github.com/zulhilmizainuddin/aws-assumerole',
      author='Zulhilmi Mohamed Zainuddin',
      author_email='zulhilmi.zainuddin@outlook.com',
      license='MIT',
      packages=['awsassumerole'],
      install_requires=[
        'boto3'
      ],
      zip_safe=False)
