from setuptools import setup

# deploy steps:
# $ virtualenv -p python3 --no-site-packages ./
# $ pip install -r requirements.txt
# $ python setup.py install

# test steps:
# $ coverage run setup.py test
# $ coverage report

setup(name='cerberus',
    packages=['cerberus'],
    license='MIT',
    setup_requires=['pytest_runner'],
    tests_require=['pytest'],
)    
