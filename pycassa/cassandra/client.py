from __future__ import absolute_import

import os
import thriftpy

cassandra_thrift = thriftpy.load(os.path.join(os.path.dirname(os.path.realpath(__file__)), "cassandra-v20.thrift"), module_name="cassandra_thrift")
