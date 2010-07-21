``WebtrendsQT`` is an interactive command line tool for querying Webtrends analytics reporting web service via a Windows ODBC connection, allowing you to run ``psql`` and ``mysql`` like commands and raw SQL against databases respresenting reports.

Requirements
============

- pyDBCLI >= 0.1
- PyODBC >= 2.0
- Webtrends Windows ODBC driver

Installation
============

Install ``WebtrendsQT`` using easy_install::

    easy_install WebtrendsQT

Or from the setup script::

    python setup.py install

Usage
=====

If you run ``wtqt`` without any arguments, the standard usage message will tell you the list of optionala and mandatory arguments to prompt up a wtqt prompt.

To get you going here's an example::


