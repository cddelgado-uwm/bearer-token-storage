from setuptools import setup, find_packages

setup(
    name='bearer-token-storage',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'keyring',
        'getpass',
        'requests'
    ],
    author='David Delgado',
    author_email='delgadcd@uwm.edu',
    description='Securely store bearer tokens in the keychain for your PC',
    license='MIT',
    url='https://github.com/cddelgado-uwm/bearer-token-storage'
)
