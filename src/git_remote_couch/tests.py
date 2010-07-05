import unittest
import doctest
from lovely.testlayers.server import ServerLayer

import os

class CouchDBLayer(ServerLayer):

    """A layer that starts and stops CouchDB,
    executable needs to be in the path"""

    __bases__ = ()

    COMMAND = 'couchdb -a ./local.ini'

    def __init__(self, name, port=5984, connections=10):
        self.port = port
        start_cmd = self.COMMAND

        super(CouchDBLayer, self).__init__(
            name, servers=['localhost:%s' % port],
            start_cmd=start_cmd)

def test_suite():
    os.environ['PATH'] += ":" + os.path.join(
        os.path.dirname(__file__), '../../parts/couchdb/bin/')
    return unittest.TestSuite(
        doctest.DocFileSuite('fetch.rst',
            optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS),
    )

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
