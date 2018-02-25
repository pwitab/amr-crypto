from setuptools import setup

setup(
    name='amr-crypto',
    version='0.0.1',
    description='Cryptography for Automatic Meter Reading Systems.',
    url='https://github.com/pwitab/amr-crypto',
    author='Henrik Palmlund Wahlgren, '
           'Palmlund Wahlgren Innovative Technology AB',
    author_email='henrik@pwit.se',
    license='BSD 3-Clause License',
    packages=['amr_crypto', 'amr_crypto.dlms'],
    install_requires=['cryptography', ]

)
