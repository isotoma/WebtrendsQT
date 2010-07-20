"""Installer for Webtrends Query Tool"""

try:
        from setuptools import setup, find_packages
except ImportError:
        from ez_setup import use_setuptools
        use_setuptools()
        from setuptools import setup, find_packages
setup(
    name='WebtrendsQT',
    description='Webtrends SQL query tool',
    version='0.1',
    author='Wes Mason',
    author_email='wes.mason@isotoma.com',
    url='http://github.com/isotoma/WebtrendsQT',
    packages=find_packages(exclude=['ez_setup']),
    setup_requires=[
        'pyDBCLI[odbc]>=0.1',
    ]
)
