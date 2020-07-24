from contextlib import contextmanager
import logging

from tractor.plugins.input.base import DbInputPlugin
from tractor.plugins import registery

try:
    from hdbcli import dbapi

    ENABLED = True
except ImportError:
    ENABLED = False


logger = logging.getLogger("plugins.input.oracle")


class Oracle(DbInputPlugin):
    @classmethod
    def enabled(cls):
        return ENABLED

    def help(self):
        print("""
            host:[required]     = Hostname or ip address
            port:[1521]         = Port number
            username            = Connection username
            password            = Connection password or environment variable $PASSWORD
            table:[*]           = Table name schema.table_name or table_name
            columns             = [{name: column_name, type: column_type}, ...]
            query:[*]           = Query file or query string
            batch_size          = Batch insert size
            metadata:[True]     = Send metadata to ouput plugin
            count:[True]        = Send count to ouput plugin

            * either query or table must be given
        """)


    @contextmanager
    def open_connection(self):
        connection = dbapi.connect(
            address=self.config['host'],
            port=self.config.get('port', 30015),
            user=self.config['username'],
            password=self.config['password']
        )
        try:
            yield connection
        finally:
            connection.close()


    def run(self):
        error = None
        try:
            with self.open_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(self.query)
                self.publish_metadata(conn, cursor)
                while True:
                    rows = cursor.fetchmany(self.config.get("fetch_size", 1000))
                    if not rows:
                        break
                    self.send_data(rows)

            self.success()
        except Exception as err:  # pylint: disable=broad-except
            logger.error("Read error", exc_info=err)
            self.error()
            error = err

        self.done()
        if error is not None:
            raise error


registery.register(Oracle)

