#-*- coding: utf-8 -*-

"""Query util for Webtrends data
"""
__author__ = 'Wes Mason <wes.mason@isotoma.com>'
__docformat__ = 'restructuredtext en'
__version__ = '0.1'


import pyodbc
import getopt
import sys
from urlparse import urlparse
from pyDBCLI.extras.odbc import ODBCUtility
from pyDBCLI.helpers import print_table, error, usage, memoized

class WTUtility(ODBCUtility):
        prompt = 'wtqt# '
        intro = 'Webtrends Query Tool v%s' % (__version__,)

        def do_p(self, line):
                """\p
List WT profiles.
"""
                if not self.current:
                        print_table(self.get_profiles(), self.vertical_display)

        @memoized()
        def get_profiles(self):
                """Helper method to return a list of WT profiles,
                from WTSystem.
                """
                profiles = [['Profile name', 'GUID']]
                r = self.system_cursor.execute('{Call wtGetProfileList()}')
                for row in r.fetchall():
                        profiles.append([row.PROFILE_NAME, row.PROFILE_GUID])
                return profiles

        @memoized()
        def get_schemas(self, profile_id):
                """Helper method to return a list of templates,
                for a given profile GUID, from WTSystem.
                """
                templates = [['Template GUID']]
                r = self.system_cursor.execute('{Call wtGetTemplateList(%s)}' % (profile_id,))
                for row in r.fetchall():
                        templates.append([row.TEMPLATE_GUID])
                return templates

        @memoized()
        def get_tables(self):
                tables = [['Table name']]
                for row in self.cursor.tables():
                        tables.append([row])
                return tables

        @memoized()
        def get_columns(self, name):
                columns = [['Column name', 'Type', 'Size',]]
                r = self.connect.execute('SELECT * FROM %s LIMIT 1' % (table,))
                for row in r.cursor.description:
                        columns.append([row[0], self.db_types[row[1]], row[3],])
                return columns

        def connect(self, schema):
                self.dsn['schema'] = schema
                try:
                        conn = pyodbc.connect(self.query, **self.dsn)
                        self.cursor = conn.cursor()
                except:
                        error(e, False)
                        return False
                else:
                        return True

# Shell script usage instrunctions, pushed to stdout
# by usage()
USAGE_MESSAGE = """
Usage: wtqt.py [-u <user>] [-p <pass>] -d <system DSN> -h <host> [-P <port>] -t <template> -p <profile>

Options:
  -d, --systemdsn: Predefined system DSN
  -p, --profile : Webtrends profile GUID
  -t, --template : Template/schema
  -h, --host : Webtrends web instance
  -P, --port : Optional server port (default: 80)
  -u, --username: Optional username
  -k, --password: Optional password
"""

def main(argv):
        """Main entry function for CLI script, should be
        passed CLI args tuple, normally from sys.argv
        """
        # Get CLI options
        try:
                opts, args = getopt.getopt(
                        argv,
                        "p:t:h:P:d:u:k:",
                        [
                                "profile=",
                                "template=",
                                "host=",
                                "port=",
                                "systemdsn=",
                                "username=",
                                "password=",
                        ]
                )
        except getopt.GetoptError:
                error("Unknown options", True, USAGE_MESSAGE)


        profile = None
        template = None
        host = None
        port = None
        system_dsn = None
        username = None
        password = None
        dsn = {}

        # Parse CLI options
        for opt, arg in opts:
                if opt in ("-p", "--profile"):
                        profile = arg
                elif opt in ("-t", "--template"):
                        template = arg
                elif opt in ("-h", "--host"):
                        host = arg
                elif opt in ("-P", "--port"):
                        port = arg
                elif opt in ("-d", "--systemdsn"):
                        system_dsn = arg
                elif opt in ("-u", "--username"):
                        username = arg
                elif opt in ("-k", "--password"):
                        password = arg

        if not profile:
                error("Must have a profile GUID, -p", True, USAGE_MESSAGE)
        if not template:
                error("Must have a template/schema, -t", True, USAGE_MESSAGE)
        if not host:
                error("Must have a host, -h", True, USAGE_MESSAGE)
        if not system_dsn:
                error("Must have a predefined system DSN, -d", True, USAGE_MESSAGE)

        dsn['DSN'] = system_dsn
        dsn['ProfileGuid'] = profile
        dsn['DATABASE'] = template
        dsn['SERVER'] = host
        if port:
                dsn['PORT'] = port
        else:
                dsn['PORT'] = '80'
        if password:
                dsn['Password'] = password
        if username:
                dsn['User ID'] = dsn['UID'] = user
        dsn['SSL'] = '0'
        dsn['AccountId'] = '1'

        # Setup cursor
        u = WTUtility()
        u.dsn = dsn

        conn = pyobc.connect(dsn)
        u.cursor = conn.cursor()

        del dsn['ProfileGuid']
        dsn['Profile'] = 'WTSystem'
        dsn['DATABASE'] = 'WTSystem'
        conn = pyobc.connect(dsn)
        u.system_cursor = conn.cursor()

        u.cmdloop()

if __name__ == "__main__":
        # Pass all CLI args except the first one, which is normally
        # the scripts filename
        main(sys.argv[1:])
