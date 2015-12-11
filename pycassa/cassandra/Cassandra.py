from __future__ import absolute_import
from .client import cassandra_thrift

locals_variables = locals()
for fname in ['add_args', 'add_result', 'atomic_batch_mutate_args', 'atomic_batch_mutate_result', 'batch_mutate_args', 'batch_mutate_result', 
              'cas_args', 'cas_result', 'describe_cluster_name_args', 'describe_cluster_name_result', 'describe_keyspace_args', 'describe_keyspace_result', 
              'describe_keyspaces_args', 'describe_keyspaces_result', 'describe_local_ring_args', 'describe_local_ring_result', 'describe_partitioner_args', 
              'describe_partitioner_result', 'describe_ring_args', 'describe_ring_result', 'describe_schema_versions_args', 'describe_schema_versions_result', 
              'describe_snitch_args', 'describe_snitch_result', 'describe_splits_args', 'describe_splits_ex_args', 'describe_splits_ex_result', 'describe_splits_result', 
              'describe_token_map_args', 'describe_token_map_result', 'describe_version_args', 'describe_version_result', 'execute_cql3_query_args', 
              'execute_cql3_query_result', 'execute_cql_query_args', 'execute_cql_query_result', 'execute_prepared_cql3_query_args', 'execute_prepared_cql3_query_result', 
              'execute_prepared_cql_query_args', 'execute_prepared_cql_query_result', 'get_args', 'get_count_args', 'get_count_result', 'get_indexed_slices_args', 
              'get_indexed_slices_result', 'get_paged_slice_args', 'get_paged_slice_result', 'get_range_slices_args', 'get_range_slices_result', 'get_result', 
              'get_slice_args', 'get_slice_result', 'insert_args', 'insert_result', 'login_args', 'login_result', 'multiget_count_args', 'multiget_count_result', 
              'multiget_slice_args', 'multiget_slice_result', 'prepare_cql3_query_args', 'prepare_cql3_query_result', 'prepare_cql_query_args', 'prepare_cql_query_result', 
              'remove_args', 'remove_counter_args', 'remove_counter_result', 'remove_result', 'set_cql_version_args', 'set_cql_version_result', 'set_keyspace_args', 
              'set_keyspace_result', 'system_add_column_family_args', 'system_add_column_family_result', 'system_add_keyspace_args', 'system_add_keyspace_result', 
              'system_drop_column_family_args', 'system_drop_column_family_result', 'system_drop_keyspace_args', 'system_drop_keyspace_result', 'system_update_column_family_args', 
              'system_update_column_family_result', 'system_update_keyspace_args', 'system_update_keyspace_result', 'thrift_services', 'trace_next_query_args', 
              'trace_next_query_result', 'truncate_args', 'truncate_result']:
    locals_variables[fname] = getattr(cassandra_thrift.Cassandra,fname)

#from thrift.Thrift import TType, TMessageType, TException, TApplicationException
from thriftpy.thrift import TType, TMessageType, TException, TApplicationException
from .ttypes import *
#from thrift.Thrift import TProcessor
#from thrift.transport import TTransport
#from thrift.protocol import TBinaryProtocol, TProtocol


class Iface(object):
  def login(self, auth_request):
    """
    Parameters:
     - auth_request
    """
    pass

  def set_keyspace(self, keyspace):
    """
    Parameters:
     - keyspace
    """
    pass

  def get(self, key, column_path, consistency_level):
    """
    Get the Column or SuperColumn at the given column_path. If no value is present, NotFoundException is thrown. (This is
    the only method that can throw an exception under non-failure conditions.)

    Parameters:
     - key
     - column_path
     - consistency_level
    """
    pass

  def get_slice(self, key, column_parent, predicate, consistency_level):
    """
    Get the group of columns contained by column_parent (either a ColumnFamily name or a ColumnFamily/SuperColumn name
    pair) specified by the given SlicePredicate. If no matching values are found, an empty list is returned.

    Parameters:
     - key
     - column_parent
     - predicate
     - consistency_level
    """
    pass

  def get_count(self, key, column_parent, predicate, consistency_level):
    """
    returns the number of columns matching <code>predicate</code> for a particular <code>key</code>,
    <code>ColumnFamily</code> and optionally <code>SuperColumn</code>.

    Parameters:
     - key
     - column_parent
     - predicate
     - consistency_level
    """
    pass

  def multiget_slice(self, keys, column_parent, predicate, consistency_level):
    """
    Performs a get_slice for column_parent and predicate for the given keys in parallel.

    Parameters:
     - keys
     - column_parent
     - predicate
     - consistency_level
    """
    pass

  def multiget_count(self, keys, column_parent, predicate, consistency_level):
    """
    Perform a get_count in parallel on the given list<binary> keys. The return value maps keys to the count found.

    Parameters:
     - keys
     - column_parent
     - predicate
     - consistency_level
    """
    pass

  def get_range_slices(self, column_parent, predicate, range, consistency_level):
    """
    returns a subset of columns for a contiguous range of keys.

    Parameters:
     - column_parent
     - predicate
     - range
     - consistency_level
    """
    pass

  def get_paged_slice(self, column_family, range, start_column, consistency_level):
    """
    returns a range of columns, wrapping to the next rows if necessary to collect max_results.

    Parameters:
     - column_family
     - range
     - start_column
     - consistency_level
    """
    pass

  def get_indexed_slices(self, column_parent, index_clause, column_predicate, consistency_level):
    """
    Returns the subset of columns specified in SlicePredicate for the rows matching the IndexClause
    @deprecated use get_range_slices instead with range.row_filter specified

    Parameters:
     - column_parent
     - index_clause
     - column_predicate
     - consistency_level
    """
    pass

  def insert(self, key, column_parent, column, consistency_level):
    """
    Insert a Column at the given column_parent.column_family and optional column_parent.super_column.

    Parameters:
     - key
     - column_parent
     - column
     - consistency_level
    """
    pass

  def add(self, key, column_parent, column, consistency_level):
    """
    Increment or decrement a counter.

    Parameters:
     - key
     - column_parent
     - column
     - consistency_level
    """
    pass

  def remove(self, key, column_path, timestamp, consistency_level):
    """
    Remove data from the row specified by key at the granularity specified by column_path, and the given timestamp. Note
    that all the values in column_path besides column_path.column_family are truly optional: you can remove the entire
    row by just specifying the ColumnFamily, or you can remove a SuperColumn or a single Column by specifying those levels too.

    Parameters:
     - key
     - column_path
     - timestamp
     - consistency_level
    """
    pass

  def remove_counter(self, key, path, consistency_level):
    """
    Remove a counter at the specified location.
    Note that counters have limited support for deletes: if you remove a counter, you must wait to issue any following update
    until the delete has reached all the nodes and all of them have been fully compacted.

    Parameters:
     - key
     - path
     - consistency_level
    """
    pass

  def batch_mutate(self, mutation_map, consistency_level):
    """
      Mutate many columns or super columns for many row keys. See also: Mutation.

      mutation_map maps key to column family to a list of Mutation objects to take place at that scope.
    *

    Parameters:
     - mutation_map
     - consistency_level
    """
    pass

  def atomic_batch_mutate(self, mutation_map, consistency_level):
    """
      Atomically mutate many columns or super columns for many row keys. See also: Mutation.

      mutation_map maps key to column family to a list of Mutation objects to take place at that scope.
    *

    Parameters:
     - mutation_map
     - consistency_level
    """
    pass

  def truncate(self, cfname):
    """
    Truncate will mark and entire column family as deleted.
    From the user's perspective a successful call to truncate will result complete data deletion from cfname.
    Internally, however, disk space will not be immediatily released, as with all deletes in cassandra, this one
    only marks the data as deleted.
    The operation succeeds only if all hosts in the cluster at available and will throw an UnavailableException if
    some hosts are down.

    Parameters:
     - cfname
    """
    pass

  def describe_schema_versions(self, ):
    """
    for each schema version present in the cluster, returns a list of nodes at that version.
    hosts that do not respond will be under the key DatabaseDescriptor.INITIAL_VERSION.
    the cluster is all on the same version if the size of the map is 1.
    """
    pass

  def describe_keyspaces(self, ):
    """
    list the defined keyspaces in this cluster
    """
    pass

  def describe_cluster_name(self, ):
    """
    get the cluster name
    """
    pass

  def describe_version(self, ):
    """
    get the thrift api version
    """
    pass

  def describe_ring(self, keyspace):
    """
    get the token ring: a map of ranges to host addresses,
    represented as a set of TokenRange instead of a map from range
    to list of endpoints, because you can't use Thrift structs as
    map keys:
    https://issues.apache.org/jira/browse/THRIFT-162

    for the same reason, we can't return a set here, even though
    order is neither important nor predictable.

    Parameters:
     - keyspace
    """
    pass

  def describe_token_map(self, ):
    """
    get the mapping between token->node ip
    without taking replication into consideration
    https://issues.apache.org/jira/browse/CASSANDRA-4092
    """
    pass

  def describe_partitioner(self, ):
    """
    returns the partitioner used by this cluster
    """
    pass

  def describe_snitch(self, ):
    """
    returns the snitch used by this cluster
    """
    pass

  def describe_keyspace(self, keyspace):
    """
    describe specified keyspace

    Parameters:
     - keyspace
    """
    pass

  def describe_splits(self, cfName, start_token, end_token, keys_per_split):
    """
    experimental API for hadoop/parallel query support.
    may change violently and without warning.

    returns list of token strings such that first subrange is (list[0], list[1]],
    next is (list[1], list[2]], etc.

    Parameters:
     - cfName
     - start_token
     - end_token
     - keys_per_split
    """
    pass

  def trace_next_query(self, ):
    """
    Enables tracing for the next query in this connection and returns the UUID for that trace session
    The next query will be traced idependently of trace probability and the returned UUID can be used to query the trace keyspace
    """
    pass

  def describe_splits_ex(self, cfName, start_token, end_token, keys_per_split):
    """
    Parameters:
     - cfName
     - start_token
     - end_token
     - keys_per_split
    """
    pass

  def system_add_column_family(self, cf_def):
    """
    adds a column family. returns the new schema id.

    Parameters:
     - cf_def
    """
    pass

  def system_drop_column_family(self, column_family):
    """
    drops a column family. returns the new schema id.

    Parameters:
     - column_family
    """
    pass

  def system_add_keyspace(self, ks_def):
    """
    adds a keyspace and any column families that are part of it. returns the new schema id.

    Parameters:
     - ks_def
    """
    pass

  def system_drop_keyspace(self, keyspace):
    """
    drops a keyspace and any column families that are part of it. returns the new schema id.

    Parameters:
     - keyspace
    """
    pass

  def system_update_keyspace(self, ks_def):
    """
    updates properties of a keyspace. returns the new schema id.

    Parameters:
     - ks_def
    """
    pass

  def system_update_column_family(self, cf_def):
    """
    updates properties of a column family. returns the new schema id.

    Parameters:
     - cf_def
    """
    pass

  def execute_cql_query(self, query, compression):
    """
    Executes a CQL (Cassandra Query Language) statement and returns a
    CqlResult containing the results.

    Parameters:
     - query
     - compression
    """
    pass

  def execute_cql3_query(self, query, compression, consistency):
    """
    Parameters:
     - query
     - compression
     - consistency
    """
    pass

  def prepare_cql_query(self, query, compression):
    """
    Prepare a CQL (Cassandra Query Language) statement by compiling and returning
    - the type of CQL statement
    - an id token of the compiled CQL stored on the server side.
    - a count of the discovered bound markers in the statement

    Parameters:
     - query
     - compression
    """
    pass

  def prepare_cql3_query(self, query, compression):
    """
    Parameters:
     - query
     - compression
    """
    pass

  def execute_prepared_cql_query(self, itemId, values):
    """
    Executes a prepared CQL (Cassandra Query Language) statement by passing an id token and  a list of variables
    to bind and returns a CqlResult containing the results.

    Parameters:
     - itemId
     - values
    """
    pass

  def execute_prepared_cql3_query(self, itemId, values, consistency):
    """
    Parameters:
     - itemId
     - values
     - consistency
    """
    pass

  def set_cql_version(self, version):
    """
    @deprecated This is now a no-op. Please use the CQL3 specific methods instead.

    Parameters:
     - version
    """
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def login(self, auth_request):
    """
    Parameters:
     - auth_request
    """
    self.send_login(auth_request)
    self.recv_login()

  def send_login(self, auth_request):
    self._oprot.writeMessageBegin('login', TMessageType.CALL, self._seqid)
    args = login_args()
    args.auth_request = auth_request
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_login(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = login_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.authnx is not None:
      raise result.authnx
    if result.authzx is not None:
      raise result.authzx
    return

  def set_keyspace(self, keyspace):
    """
    Parameters:
     - keyspace
    """
    self.send_set_keyspace(keyspace)
    self.recv_set_keyspace()

  def send_set_keyspace(self, keyspace):
    self._oprot.writeMessageBegin('set_keyspace', TMessageType.CALL, self._seqid)
    args = set_keyspace_args()
    args.keyspace = keyspace
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_set_keyspace(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = set_keyspace_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.ire is not None:
      raise result.ire
    return

  def get(self, key, column_path, consistency_level):
    """
    Get the Column or SuperColumn at the given column_path. If no value is present, NotFoundException is thrown. (This is
    the only method that can throw an exception under non-failure conditions.)

    Parameters:
     - key
     - column_path
     - consistency_level
    """
    self.send_get(key, column_path, consistency_level)
    return self.recv_get()

  def send_get(self, key, column_path, consistency_level):
    self._oprot.writeMessageBegin('get', TMessageType.CALL, self._seqid)
    args = get_args()
    args.key = key
    args.column_path = column_path
    args.consistency_level = consistency_level
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_get(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = get_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ire is not None:
      raise result.ire
    if result.nfe is not None:
      raise result.nfe
    if result.ue is not None:
      raise result.ue
    if result.te is not None:
      raise result.te
    raise TApplicationException(TApplicationException.MISSING_RESULT, "get failed: unknown result");

  def get_slice(self, key, column_parent, predicate, consistency_level):
    """
    Get the group of columns contained by column_parent (either a ColumnFamily name or a ColumnFamily/SuperColumn name
    pair) specified by the given SlicePredicate. If no matching values are found, an empty list is returned.

    Parameters:
     - key
     - column_parent
     - predicate
     - consistency_level
    """
    self.send_get_slice(key, column_parent, predicate, consistency_level)
    return self.recv_get_slice()

  def send_get_slice(self, key, column_parent, predicate, consistency_level):
    self._oprot.writeMessageBegin('get_slice', TMessageType.CALL, self._seqid)
    args = get_slice_args()
    args.key = key
    args.column_parent = column_parent
    args.predicate = predicate
    args.consistency_level = consistency_level
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_get_slice(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = get_slice_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ire is not None:
      raise result.ire
    if result.ue is not None:
      raise result.ue
    if result.te is not None:
      raise result.te
    raise TApplicationException(TApplicationException.MISSING_RESULT, "get_slice failed: unknown result");

  def get_count(self, key, column_parent, predicate, consistency_level):
    """
    returns the number of columns matching <code>predicate</code> for a particular <code>key</code>,
    <code>ColumnFamily</code> and optionally <code>SuperColumn</code>.

    Parameters:
     - key
     - column_parent
     - predicate
     - consistency_level
    """
    self.send_get_count(key, column_parent, predicate, consistency_level)
    return self.recv_get_count()

  def send_get_count(self, key, column_parent, predicate, consistency_level):
    self._oprot.writeMessageBegin('get_count', TMessageType.CALL, self._seqid)
    args = get_count_args()
    args.key = key
    args.column_parent = column_parent
    args.predicate = predicate
    args.consistency_level = consistency_level
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_get_count(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = get_count_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ire is not None:
      raise result.ire
    if result.ue is not None:
      raise result.ue
    if result.te is not None:
      raise result.te
    raise TApplicationException(TApplicationException.MISSING_RESULT, "get_count failed: unknown result");

  def multiget_slice(self, keys, column_parent, predicate, consistency_level):
    """
    Performs a get_slice for column_parent and predicate for the given keys in parallel.

    Parameters:
     - keys
     - column_parent
     - predicate
     - consistency_level
    """
    self.send_multiget_slice(keys, column_parent, predicate, consistency_level)
    return self.recv_multiget_slice()

  def send_multiget_slice(self, keys, column_parent, predicate, consistency_level):
    self._oprot.writeMessageBegin('multiget_slice', TMessageType.CALL, self._seqid)
    args = multiget_slice_args()
    args.keys = keys
    args.column_parent = column_parent
    args.predicate = predicate
    args.consistency_level = consistency_level
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_multiget_slice(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = multiget_slice_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ire is not None:
      raise result.ire
    if result.ue is not None:
      raise result.ue
    if result.te is not None:
      raise result.te
    raise TApplicationException(TApplicationException.MISSING_RESULT, "multiget_slice failed: unknown result");

  def multiget_count(self, keys, column_parent, predicate, consistency_level):
    """
    Perform a get_count in parallel on the given list<binary> keys. The return value maps keys to the count found.

    Parameters:
     - keys
     - column_parent
     - predicate
     - consistency_level
    """
    self.send_multiget_count(keys, column_parent, predicate, consistency_level)
    return self.recv_multiget_count()

  def send_multiget_count(self, keys, column_parent, predicate, consistency_level):
    self._oprot.writeMessageBegin('multiget_count', TMessageType.CALL, self._seqid)
    args = multiget_count_args()
    args.keys = keys
    args.column_parent = column_parent
    args.predicate = predicate
    args.consistency_level = consistency_level
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_multiget_count(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = multiget_count_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ire is not None:
      raise result.ire
    if result.ue is not None:
      raise result.ue
    if result.te is not None:
      raise result.te
    raise TApplicationException(TApplicationException.MISSING_RESULT, "multiget_count failed: unknown result");

  def get_range_slices(self, column_parent, predicate, range, consistency_level):
    """
    returns a subset of columns for a contiguous range of keys.

    Parameters:
     - column_parent
     - predicate
     - range
     - consistency_level
    """
    self.send_get_range_slices(column_parent, predicate, range, consistency_level)
    return self.recv_get_range_slices()

  def send_get_range_slices(self, column_parent, predicate, range, consistency_level):
    self._oprot.writeMessageBegin('get_range_slices', TMessageType.CALL, self._seqid)
    args = get_range_slices_args()
    args.column_parent = column_parent
    args.predicate = predicate
    args.range = range
    args.consistency_level = consistency_level
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_get_range_slices(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = get_range_slices_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ire is not None:
      raise result.ire
    if result.ue is not None:
      raise result.ue
    if result.te is not None:
      raise result.te
    raise TApplicationException(TApplicationException.MISSING_RESULT, "get_range_slices failed: unknown result");

  def get_paged_slice(self, column_family, range, start_column, consistency_level):
    """
    returns a range of columns, wrapping to the next rows if necessary to collect max_results.

    Parameters:
     - column_family
     - range
     - start_column
     - consistency_level
    """
    self.send_get_paged_slice(column_family, range, start_column, consistency_level)
    return self.recv_get_paged_slice()

  def send_get_paged_slice(self, column_family, range, start_column, consistency_level):
    self._oprot.writeMessageBegin('get_paged_slice', TMessageType.CALL, self._seqid)
    args = get_paged_slice_args()
    args.column_family = column_family
    args.range = range
    args.start_column = start_column
    args.consistency_level = consistency_level
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_get_paged_slice(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = get_paged_slice_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ire is not None:
      raise result.ire
    if result.ue is not None:
      raise result.ue
    if result.te is not None:
      raise result.te
    raise TApplicationException(TApplicationException.MISSING_RESULT, "get_paged_slice failed: unknown result");

  def get_indexed_slices(self, column_parent, index_clause, column_predicate, consistency_level):
    """
    Returns the subset of columns specified in SlicePredicate for the rows matching the IndexClause
    @deprecated use get_range_slices instead with range.row_filter specified

    Parameters:
     - column_parent
     - index_clause
     - column_predicate
     - consistency_level
    """
    self.send_get_indexed_slices(column_parent, index_clause, column_predicate, consistency_level)
    return self.recv_get_indexed_slices()

  def send_get_indexed_slices(self, column_parent, index_clause, column_predicate, consistency_level):
    self._oprot.writeMessageBegin('get_indexed_slices', TMessageType.CALL, self._seqid)
    args = get_indexed_slices_args()
    args.column_parent = column_parent
    args.index_clause = index_clause
    args.column_predicate = column_predicate
    args.consistency_level = consistency_level
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_get_indexed_slices(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = get_indexed_slices_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ire is not None:
      raise result.ire
    if result.ue is not None:
      raise result.ue
    if result.te is not None:
      raise result.te
    raise TApplicationException(TApplicationException.MISSING_RESULT, "get_indexed_slices failed: unknown result");

  def insert(self, key, column_parent, column, consistency_level):
    """
    Insert a Column at the given column_parent.column_family and optional column_parent.super_column.

    Parameters:
     - key
     - column_parent
     - column
     - consistency_level
    """
    self.send_insert(key, column_parent, column, consistency_level)
    self.recv_insert()

  def send_insert(self, key, column_parent, column, consistency_level):
    self._oprot.writeMessageBegin('insert', TMessageType.CALL, self._seqid)
    args = insert_args()
    args.key = key
    args.column_parent = column_parent
    args.column = column
    args.consistency_level = consistency_level
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_insert(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = insert_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.ire is not None:
      raise result.ire
    if result.ue is not None:
      raise result.ue
    if result.te is not None:
      raise result.te
    return

  def add(self, key, column_parent, column, consistency_level):
    """
    Increment or decrement a counter.

    Parameters:
     - key
     - column_parent
     - column
     - consistency_level
    """
    self.send_add(key, column_parent, column, consistency_level)
    self.recv_add()

  def send_add(self, key, column_parent, column, consistency_level):
    self._oprot.writeMessageBegin('add', TMessageType.CALL, self._seqid)
    args = add_args()
    args.key = key
    args.column_parent = column_parent
    args.column = column
    args.consistency_level = consistency_level
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_add(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = add_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.ire is not None:
      raise result.ire
    if result.ue is not None:
      raise result.ue
    if result.te is not None:
      raise result.te
    return

  def remove(self, key, column_path, timestamp, consistency_level):
    """
    Remove data from the row specified by key at the granularity specified by column_path, and the given timestamp. Note
    that all the values in column_path besides column_path.column_family are truly optional: you can remove the entire
    row by just specifying the ColumnFamily, or you can remove a SuperColumn or a single Column by specifying those levels too.

    Parameters:
     - key
     - column_path
     - timestamp
     - consistency_level
    """
    self.send_remove(key, column_path, timestamp, consistency_level)
    self.recv_remove()

  def send_remove(self, key, column_path, timestamp, consistency_level):
    self._oprot.writeMessageBegin('remove', TMessageType.CALL, self._seqid)
    args = remove_args()
    args.key = key
    args.column_path = column_path
    args.timestamp = timestamp
    args.consistency_level = consistency_level
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_remove(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = remove_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.ire is not None:
      raise result.ire
    if result.ue is not None:
      raise result.ue
    if result.te is not None:
      raise result.te
    return

  def remove_counter(self, key, path, consistency_level):
    """
    Remove a counter at the specified location.
    Note that counters have limited support for deletes: if you remove a counter, you must wait to issue any following update
    until the delete has reached all the nodes and all of them have been fully compacted.

    Parameters:
     - key
     - path
     - consistency_level
    """
    self.send_remove_counter(key, path, consistency_level)
    self.recv_remove_counter()

  def send_remove_counter(self, key, path, consistency_level):
    self._oprot.writeMessageBegin('remove_counter', TMessageType.CALL, self._seqid)
    args = remove_counter_args()
    args.key = key
    args.path = path
    args.consistency_level = consistency_level
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_remove_counter(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = remove_counter_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.ire is not None:
      raise result.ire
    if result.ue is not None:
      raise result.ue
    if result.te is not None:
      raise result.te
    return

  def batch_mutate(self, mutation_map, consistency_level):
    """
      Mutate many columns or super columns for many row keys. See also: Mutation.

      mutation_map maps key to column family to a list of Mutation objects to take place at that scope.
    *

    Parameters:
     - mutation_map
     - consistency_level
    """
    self.send_batch_mutate(mutation_map, consistency_level)
    self.recv_batch_mutate()

  def send_batch_mutate(self, mutation_map, consistency_level):
    self._oprot.writeMessageBegin('batch_mutate', TMessageType.CALL, self._seqid)
    args = batch_mutate_args()
    args.mutation_map = mutation_map
    args.consistency_level = consistency_level
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_batch_mutate(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = batch_mutate_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.ire is not None:
      raise result.ire
    if result.ue is not None:
      raise result.ue
    if result.te is not None:
      raise result.te
    return

  def atomic_batch_mutate(self, mutation_map, consistency_level):
    """
      Atomically mutate many columns or super columns for many row keys. See also: Mutation.

      mutation_map maps key to column family to a list of Mutation objects to take place at that scope.
    *

    Parameters:
     - mutation_map
     - consistency_level
    """
    self.send_atomic_batch_mutate(mutation_map, consistency_level)
    self.recv_atomic_batch_mutate()

  def send_atomic_batch_mutate(self, mutation_map, consistency_level):
    self._oprot.writeMessageBegin('atomic_batch_mutate', TMessageType.CALL, self._seqid)
    args = atomic_batch_mutate_args()
    args.mutation_map = mutation_map
    args.consistency_level = consistency_level
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_atomic_batch_mutate(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = atomic_batch_mutate_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.ire is not None:
      raise result.ire
    if result.ue is not None:
      raise result.ue
    if result.te is not None:
      raise result.te
    return

  def truncate(self, cfname):
    """
    Truncate will mark and entire column family as deleted.
    From the user's perspective a successful call to truncate will result complete data deletion from cfname.
    Internally, however, disk space will not be immediatily released, as with all deletes in cassandra, this one
    only marks the data as deleted.
    The operation succeeds only if all hosts in the cluster at available and will throw an UnavailableException if
    some hosts are down.

    Parameters:
     - cfname
    """
    self.send_truncate(cfname)
    self.recv_truncate()

  def send_truncate(self, cfname):
    self._oprot.writeMessageBegin('truncate', TMessageType.CALL, self._seqid)
    args = truncate_args()
    args.cfname = cfname
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_truncate(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = truncate_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.ire is not None:
      raise result.ire
    if result.ue is not None:
      raise result.ue
    if result.te is not None:
      raise result.te
    return

  def describe_schema_versions(self, ):
    """
    for each schema version present in the cluster, returns a list of nodes at that version.
    hosts that do not respond will be under the key DatabaseDescriptor.INITIAL_VERSION.
    the cluster is all on the same version if the size of the map is 1.
    """
    self.send_describe_schema_versions()
    return self.recv_describe_schema_versions()

  def send_describe_schema_versions(self, ):
    self._oprot.writeMessageBegin('describe_schema_versions', TMessageType.CALL, self._seqid)
    args = describe_schema_versions_args()
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_describe_schema_versions(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = describe_schema_versions_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ire is not None:
      raise result.ire
    raise TApplicationException(TApplicationException.MISSING_RESULT, "describe_schema_versions failed: unknown result");

  def describe_keyspaces(self, ):
    """
    list the defined keyspaces in this cluster
    """
    self.send_describe_keyspaces()
    return self.recv_describe_keyspaces()

  def send_describe_keyspaces(self, ):
    self._oprot.writeMessageBegin('describe_keyspaces', TMessageType.CALL, self._seqid)
    args = describe_keyspaces_args()
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_describe_keyspaces(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = describe_keyspaces_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ire is not None:
      raise result.ire
    raise TApplicationException(TApplicationException.MISSING_RESULT, "describe_keyspaces failed: unknown result");

  def describe_cluster_name(self, ):
    """
    get the cluster name
    """
    self.send_describe_cluster_name()
    return self.recv_describe_cluster_name()

  def send_describe_cluster_name(self, ):
    self._oprot.writeMessageBegin('describe_cluster_name', TMessageType.CALL, self._seqid)
    args = describe_cluster_name_args()
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_describe_cluster_name(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = describe_cluster_name_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "describe_cluster_name failed: unknown result");

  def describe_version(self, ):
    """
    get the thrift api version
    """
    self.send_describe_version()
    return self.recv_describe_version()

  def send_describe_version(self, ):
    self._oprot.writeMessageBegin('describe_version', TMessageType.CALL, self._seqid)
    args = describe_version_args()
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_describe_version(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = describe_version_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "describe_version failed: unknown result");

  def describe_ring(self, keyspace):
    """
    get the token ring: a map of ranges to host addresses,
    represented as a set of TokenRange instead of a map from range
    to list of endpoints, because you can't use Thrift structs as
    map keys:
    https://issues.apache.org/jira/browse/THRIFT-162

    for the same reason, we can't return a set here, even though
    order is neither important nor predictable.

    Parameters:
     - keyspace
    """
    self.send_describe_ring(keyspace)
    return self.recv_describe_ring()

  def send_describe_ring(self, keyspace):
    self._oprot.writeMessageBegin('describe_ring', TMessageType.CALL, self._seqid)
    args = describe_ring_args()
    args.keyspace = keyspace
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_describe_ring(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = describe_ring_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ire is not None:
      raise result.ire
    raise TApplicationException(TApplicationException.MISSING_RESULT, "describe_ring failed: unknown result");

  def describe_token_map(self, ):
    """
    get the mapping between token->node ip
    without taking replication into consideration
    https://issues.apache.org/jira/browse/CASSANDRA-4092
    """
    self.send_describe_token_map()
    return self.recv_describe_token_map()

  def send_describe_token_map(self, ):
    self._oprot.writeMessageBegin('describe_token_map', TMessageType.CALL, self._seqid)
    args = describe_token_map_args()
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_describe_token_map(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = describe_token_map_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ire is not None:
      raise result.ire
    raise TApplicationException(TApplicationException.MISSING_RESULT, "describe_token_map failed: unknown result");

  def describe_partitioner(self, ):
    """
    returns the partitioner used by this cluster
    """
    self.send_describe_partitioner()
    return self.recv_describe_partitioner()

  def send_describe_partitioner(self, ):
    self._oprot.writeMessageBegin('describe_partitioner', TMessageType.CALL, self._seqid)
    args = describe_partitioner_args()
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_describe_partitioner(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = describe_partitioner_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "describe_partitioner failed: unknown result");

  def describe_snitch(self, ):
    """
    returns the snitch used by this cluster
    """
    self.send_describe_snitch()
    return self.recv_describe_snitch()

  def send_describe_snitch(self, ):
    self._oprot.writeMessageBegin('describe_snitch', TMessageType.CALL, self._seqid)
    args = describe_snitch_args()
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_describe_snitch(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = describe_snitch_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "describe_snitch failed: unknown result");

  def describe_keyspace(self, keyspace):
    """
    describe specified keyspace

    Parameters:
     - keyspace
    """
    self.send_describe_keyspace(keyspace)
    return self.recv_describe_keyspace()

  def send_describe_keyspace(self, keyspace):
    self._oprot.writeMessageBegin('describe_keyspace', TMessageType.CALL, self._seqid)
    args = describe_keyspace_args()
    args.keyspace = keyspace
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_describe_keyspace(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = describe_keyspace_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.nfe is not None:
      raise result.nfe
    if result.ire is not None:
      raise result.ire
    raise TApplicationException(TApplicationException.MISSING_RESULT, "describe_keyspace failed: unknown result");

  def describe_splits(self, cfName, start_token, end_token, keys_per_split):
    """
    experimental API for hadoop/parallel query support.
    may change violently and without warning.

    returns list of token strings such that first subrange is (list[0], list[1]],
    next is (list[1], list[2]], etc.

    Parameters:
     - cfName
     - start_token
     - end_token
     - keys_per_split
    """
    self.send_describe_splits(cfName, start_token, end_token, keys_per_split)
    return self.recv_describe_splits()

  def send_describe_splits(self, cfName, start_token, end_token, keys_per_split):
    self._oprot.writeMessageBegin('describe_splits', TMessageType.CALL, self._seqid)
    args = describe_splits_args()
    args.cfName = cfName
    args.start_token = start_token
    args.end_token = end_token
    args.keys_per_split = keys_per_split
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_describe_splits(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = describe_splits_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ire is not None:
      raise result.ire
    raise TApplicationException(TApplicationException.MISSING_RESULT, "describe_splits failed: unknown result");

  def trace_next_query(self, ):
    """
    Enables tracing for the next query in this connection and returns the UUID for that trace session
    The next query will be traced idependently of trace probability and the returned UUID can be used to query the trace keyspace
    """
    self.send_trace_next_query()
    return self.recv_trace_next_query()

  def send_trace_next_query(self, ):
    self._oprot.writeMessageBegin('trace_next_query', TMessageType.CALL, self._seqid)
    args = trace_next_query_args()
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_trace_next_query(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = trace_next_query_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "trace_next_query failed: unknown result");

  def describe_splits_ex(self, cfName, start_token, end_token, keys_per_split):
    """
    Parameters:
     - cfName
     - start_token
     - end_token
     - keys_per_split
    """
    self.send_describe_splits_ex(cfName, start_token, end_token, keys_per_split)
    return self.recv_describe_splits_ex()

  def send_describe_splits_ex(self, cfName, start_token, end_token, keys_per_split):
    self._oprot.writeMessageBegin('describe_splits_ex', TMessageType.CALL, self._seqid)
    args = describe_splits_ex_args()
    args.cfName = cfName
    args.start_token = start_token
    args.end_token = end_token
    args.keys_per_split = keys_per_split
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_describe_splits_ex(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = describe_splits_ex_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ire is not None:
      raise result.ire
    raise TApplicationException(TApplicationException.MISSING_RESULT, "describe_splits_ex failed: unknown result");

  def system_add_column_family(self, cf_def):
    """
    adds a column family. returns the new schema id.

    Parameters:
     - cf_def
    """
    self.send_system_add_column_family(cf_def)
    return self.recv_system_add_column_family()

  def send_system_add_column_family(self, cf_def):
    self._oprot.writeMessageBegin('system_add_column_family', TMessageType.CALL, self._seqid)
    args = system_add_column_family_args()
    args.cf_def = cf_def
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_system_add_column_family(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = system_add_column_family_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ire is not None:
      raise result.ire
    if result.sde is not None:
      raise result.sde
    raise TApplicationException(TApplicationException.MISSING_RESULT, "system_add_column_family failed: unknown result");

  def system_drop_column_family(self, column_family):
    """
    drops a column family. returns the new schema id.

    Parameters:
     - column_family
    """
    self.send_system_drop_column_family(column_family)
    return self.recv_system_drop_column_family()

  def send_system_drop_column_family(self, column_family):
    self._oprot.writeMessageBegin('system_drop_column_family', TMessageType.CALL, self._seqid)
    args = system_drop_column_family_args()
    args.column_family = column_family
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_system_drop_column_family(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = system_drop_column_family_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ire is not None:
      raise result.ire
    if result.sde is not None:
      raise result.sde
    raise TApplicationException(TApplicationException.MISSING_RESULT, "system_drop_column_family failed: unknown result");

  def system_add_keyspace(self, ks_def):
    """
    adds a keyspace and any column families that are part of it. returns the new schema id.

    Parameters:
     - ks_def
    """
    self.send_system_add_keyspace(ks_def)
    return self.recv_system_add_keyspace()

  def send_system_add_keyspace(self, ks_def):
    self._oprot.writeMessageBegin('system_add_keyspace', TMessageType.CALL, self._seqid)
    args = system_add_keyspace_args()
    args.ks_def = ks_def
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_system_add_keyspace(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = system_add_keyspace_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ire is not None:
      raise result.ire
    if result.sde is not None:
      raise result.sde
    raise TApplicationException(TApplicationException.MISSING_RESULT, "system_add_keyspace failed: unknown result");

  def system_drop_keyspace(self, keyspace):
    """
    drops a keyspace and any column families that are part of it. returns the new schema id.

    Parameters:
     - keyspace
    """
    self.send_system_drop_keyspace(keyspace)
    return self.recv_system_drop_keyspace()

  def send_system_drop_keyspace(self, keyspace):
    self._oprot.writeMessageBegin('system_drop_keyspace', TMessageType.CALL, self._seqid)
    args = system_drop_keyspace_args()
    args.keyspace = keyspace
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_system_drop_keyspace(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = system_drop_keyspace_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ire is not None:
      raise result.ire
    if result.sde is not None:
      raise result.sde
    raise TApplicationException(TApplicationException.MISSING_RESULT, "system_drop_keyspace failed: unknown result");

  def system_update_keyspace(self, ks_def):
    """
    updates properties of a keyspace. returns the new schema id.

    Parameters:
     - ks_def
    """
    self.send_system_update_keyspace(ks_def)
    return self.recv_system_update_keyspace()

  def send_system_update_keyspace(self, ks_def):
    self._oprot.writeMessageBegin('system_update_keyspace', TMessageType.CALL, self._seqid)
    args = system_update_keyspace_args()
    args.ks_def = ks_def
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_system_update_keyspace(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = system_update_keyspace_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ire is not None:
      raise result.ire
    if result.sde is not None:
      raise result.sde
    raise TApplicationException(TApplicationException.MISSING_RESULT, "system_update_keyspace failed: unknown result");

  def system_update_column_family(self, cf_def):
    """
    updates properties of a column family. returns the new schema id.

    Parameters:
     - cf_def
    """
    self.send_system_update_column_family(cf_def)
    return self.recv_system_update_column_family()

  def send_system_update_column_family(self, cf_def):
    self._oprot.writeMessageBegin('system_update_column_family', TMessageType.CALL, self._seqid)
    args = system_update_column_family_args()
    args.cf_def = cf_def
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_system_update_column_family(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = system_update_column_family_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ire is not None:
      raise result.ire
    if result.sde is not None:
      raise result.sde
    raise TApplicationException(TApplicationException.MISSING_RESULT, "system_update_column_family failed: unknown result");

  def execute_cql_query(self, query, compression):
    """
    Executes a CQL (Cassandra Query Language) statement and returns a
    CqlResult containing the results.

    Parameters:
     - query
     - compression
    """
    self.send_execute_cql_query(query, compression)
    return self.recv_execute_cql_query()

  def send_execute_cql_query(self, query, compression):
    self._oprot.writeMessageBegin('execute_cql_query', TMessageType.CALL, self._seqid)
    args = execute_cql_query_args()
    args.query = query
    args.compression = compression
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_execute_cql_query(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = execute_cql_query_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ire is not None:
      raise result.ire
    if result.ue is not None:
      raise result.ue
    if result.te is not None:
      raise result.te
    if result.sde is not None:
      raise result.sde
    raise TApplicationException(TApplicationException.MISSING_RESULT, "execute_cql_query failed: unknown result");

  def execute_cql3_query(self, query, compression, consistency):
    """
    Parameters:
     - query
     - compression
     - consistency
    """
    self.send_execute_cql3_query(query, compression, consistency)
    return self.recv_execute_cql3_query()

  def send_execute_cql3_query(self, query, compression, consistency):
    self._oprot.writeMessageBegin('execute_cql3_query', TMessageType.CALL, self._seqid)
    args = execute_cql3_query_args()
    args.query = query
    args.compression = compression
    args.consistency = consistency
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_execute_cql3_query(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = execute_cql3_query_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ire is not None:
      raise result.ire
    if result.ue is not None:
      raise result.ue
    if result.te is not None:
      raise result.te
    if result.sde is not None:
      raise result.sde
    raise TApplicationException(TApplicationException.MISSING_RESULT, "execute_cql3_query failed: unknown result");

  def prepare_cql_query(self, query, compression):
    """
    Prepare a CQL (Cassandra Query Language) statement by compiling and returning
    - the type of CQL statement
    - an id token of the compiled CQL stored on the server side.
    - a count of the discovered bound markers in the statement

    Parameters:
     - query
     - compression
    """
    self.send_prepare_cql_query(query, compression)
    return self.recv_prepare_cql_query()

  def send_prepare_cql_query(self, query, compression):
    self._oprot.writeMessageBegin('prepare_cql_query', TMessageType.CALL, self._seqid)
    args = prepare_cql_query_args()
    args.query = query
    args.compression = compression
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_prepare_cql_query(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = prepare_cql_query_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ire is not None:
      raise result.ire
    raise TApplicationException(TApplicationException.MISSING_RESULT, "prepare_cql_query failed: unknown result");

  def prepare_cql3_query(self, query, compression):
    """
    Parameters:
     - query
     - compression
    """
    self.send_prepare_cql3_query(query, compression)
    return self.recv_prepare_cql3_query()

  def send_prepare_cql3_query(self, query, compression):
    self._oprot.writeMessageBegin('prepare_cql3_query', TMessageType.CALL, self._seqid)
    args = prepare_cql3_query_args()
    args.query = query
    args.compression = compression
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_prepare_cql3_query(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = prepare_cql3_query_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ire is not None:
      raise result.ire
    raise TApplicationException(TApplicationException.MISSING_RESULT, "prepare_cql3_query failed: unknown result");

  def execute_prepared_cql_query(self, itemId, values):
    """
    Executes a prepared CQL (Cassandra Query Language) statement by passing an id token and  a list of variables
    to bind and returns a CqlResult containing the results.

    Parameters:
     - itemId
     - values
    """
    self.send_execute_prepared_cql_query(itemId, values)
    return self.recv_execute_prepared_cql_query()

  def send_execute_prepared_cql_query(self, itemId, values):
    self._oprot.writeMessageBegin('execute_prepared_cql_query', TMessageType.CALL, self._seqid)
    args = execute_prepared_cql_query_args()
    args.itemId = itemId
    args.values = values
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_execute_prepared_cql_query(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = execute_prepared_cql_query_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ire is not None:
      raise result.ire
    if result.ue is not None:
      raise result.ue
    if result.te is not None:
      raise result.te
    if result.sde is not None:
      raise result.sde
    raise TApplicationException(TApplicationException.MISSING_RESULT, "execute_prepared_cql_query failed: unknown result");

  def execute_prepared_cql3_query(self, itemId, values, consistency):
    """
    Parameters:
     - itemId
     - values
     - consistency
    """
    self.send_execute_prepared_cql3_query(itemId, values, consistency)
    return self.recv_execute_prepared_cql3_query()

  def send_execute_prepared_cql3_query(self, itemId, values, consistency):
    self._oprot.writeMessageBegin('execute_prepared_cql3_query', TMessageType.CALL, self._seqid)
    args = execute_prepared_cql3_query_args()
    args.itemId = itemId
    args.values = values
    args.consistency = consistency
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_execute_prepared_cql3_query(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = execute_prepared_cql3_query_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ire is not None:
      raise result.ire
    if result.ue is not None:
      raise result.ue
    if result.te is not None:
      raise result.te
    if result.sde is not None:
      raise result.sde
    raise TApplicationException(TApplicationException.MISSING_RESULT, "execute_prepared_cql3_query failed: unknown result");

  def set_cql_version(self, version):
    """
    @deprecated This is now a no-op. Please use the CQL3 specific methods instead.

    Parameters:
     - version
    """
    self.send_set_cql_version(version)
    self.recv_set_cql_version()

  def send_set_cql_version(self, version):
    self._oprot.writeMessageBegin('set_cql_version', TMessageType.CALL, self._seqid)
    args = set_cql_version_args()
    args.version = version
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_set_cql_version(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = set_cql_version_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.ire is not None:
      raise result.ire
    return