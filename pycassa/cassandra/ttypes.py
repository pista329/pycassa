from __future__ import absolute_import
from .client import cassandra_thrift

class AuthenticationException(cassandra_thrift.AuthenticationException):
    pass
class AuthenticationRequest(cassandra_thrift.AuthenticationRequest):
    pass
class AuthorizationException(cassandra_thrift.AuthorizationException):
    pass
class ConsistencyLevel(cassandra_thrift.ConsistencyLevel):
    pass
class InvalidRequestException(cassandra_thrift.InvalidRequestException):
    pass
class NotFoundException(cassandra_thrift.NotFoundException):
    pass
class UnavailableException(cassandra_thrift.UnavailableException):
    pass
class TimedOutException(cassandra_thrift.TimedOutException):
    pass

class Column(cassandra_thrift.Column):
    pass
class ColumnOrSuperColumn(cassandra_thrift.ColumnOrSuperColumn):
    pass
class ColumnParent(cassandra_thrift.ColumnParent):
    pass
class ColumnPath(cassandra_thrift.ColumnPath):
    pass
class ConsistencyLevel(cassandra_thrift.ConsistencyLevel):
    pass
class NotFoundException(cassandra_thrift.NotFoundException):
    pass
class SlicePredicate(cassandra_thrift.SlicePredicate):
    pass
class SliceRange(cassandra_thrift.SliceRange):
    pass
class SuperColumn(cassandra_thrift.SuperColumn):
    pass
class KeyRange(cassandra_thrift.KeyRange):
    pass
class KsDef(cassandra_thrift.KsDef):
    pass
class CfDef(cassandra_thrift.CfDef):
    pass
class ColumnDef(cassandra_thrift.ColumnDef):
    pass
class SchemaDisagreementException(cassandra_thrift.SchemaDisagreementException):
    pass
class IndexExpression(cassandra_thrift.IndexExpression):
    pass
class IndexClause(cassandra_thrift.IndexClause):
    pass
class IndexOperator(cassandra_thrift.IndexOperator):
    pass
class IndexType(cassandra_thrift.IndexType):
    pass
class CounterColumn(cassandra_thrift.CounterColumn):
    pass
class Mutation(cassandra_thrift.Mutation):
    pass
class Deletion(cassandra_thrift.Deletion):
    pass