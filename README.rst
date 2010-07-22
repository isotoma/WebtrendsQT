WebtrendsQT is an interactive command line tool for querying a Webtrends analytics reporting web service via a Windows ODBC connection, allowing you to run ``psql`` and ``mysql`` like commands and raw SQL against databases respresenting reports.

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

    PS C:\blah> wtqt -h subdomain.mywthosting.com -d Webtrends -p foo -t bar
    Webtrends Query Tool v0.1
    wtqt#

This example was run in Windows PowerShell, a much nicer ``cmd.exe`` replacement by Microsoft.
In this example we're relying on a System DSN already being setup in Windows called "Webtrends", with the username/password etc. PyODBC likes to complain if you don't provide it with a System DSN for the Webtrends driver, even if you override all the settings, right down to host and port.

To get started you can use ``help`` and ``?`` to find out about available commands, most of which are based on ``psql`` (e.g. ``\d``, ``l``), but also have some custom ones like ``clear`` to clear the data cache (caches schema, lists, ``\d`` output etc., but not queries, these are always re-run) and ``\p`` which lists Webtrends profiles.
