#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cuter_global import *

JSON_TYPE_ANY = 0
JSON_TYPE_INT = 1
JSON_TYPE_FLOAT = 2
JSON_TYPE_ATOM = 3
JSON_TYPE_LIST = 4
JSON_TYPE_TUPLE = 5
JSON_TYPE_PID = 6
JSON_TYPE_REF = 7
JSON_TYPE_BITSTRING = 8
JSON_TYPE_FUN = 9

JSON_ERLTYPE_NTUPLE = -2
JSON_ERLTYPE_CONS = -1
JSON_ERLTYPE_ANY = 0
JSON_ERLTYPE_ATOM = 1
JSON_ERLTYPE_ATOMLIT = 2
JSON_ERLTYPE_FLOAT = 3
JSON_ERLTYPE_INTEGER = 4
JSON_ERLTYPE_INTEGERLIT = 5
JSON_ERLTYPE_LIST = 6
JSON_ERLTYPE_NIL = 7
JSON_ERLTYPE_TUPLE = 8
JSON_ERLTYPE_TUPLEDET = 9
JSON_ERLTYPE_UNION = 10
JSON_ERLTYPE_RANGE = 11
JSON_ERLTYPE_NONEMPTY_LIST = 12
JSON_ERLTYPE_BITSTRING = 13
JSON_ERLTYPE_GENERIC_FUN = 14
JSON_ERLTYPE_FUN = 15

CMD_LOAD_TRACE_FILE = 1
CMD_SOLVE = 2
CMD_GET_MODEL = 3
CMD_ADD_AXIOMS = 4
CMD_FIX_VARIABLE = 5
CMD_RESET_SOLVER = 6
CMD_STOP = 42

RSP_MODEL_DELIMITER_START = "model_start"
RSP_MODEL_DELIMITER_END = "model_end"

CONSTRAINT_TRUE = 1
CONSTRAINT_FALSE = 2
NOT_CONSTRAINT = 3

OP_PARAMS = 1
OP_SPEC = 2
OP_LAMBDA = 68
OP_GUARD_TRUE = 3
OP_GUARD_FALSE = 4
OP_MATCH_EQUAL_TRUE = 5
OP_MATCH_EQUAL_FALSE = 6
OP_TUPLE_SZ = 7
OP_TUPLE_NOT_SZ = 8
OP_TUPLE_NOT_TPL = 9
OP_LIST_NON_EMPTY = 10
OP_LIST_EMPTY = 11
OP_LIST_NOT_LST = 12
OP_SPAWN = 13
OP_SPAWNED = 14
OP_MSG_SEND = 15
OP_MSG_RECEIVE = 16
OP_MSG_CONSUME = 17
OP_UNFOLD_TUPLE = 18
OP_UNFOLD_LIST = 19
OP_HD = 25
OP_TL = 26
OP_IS_INTEGER = 27
OP_IS_ATOM = 28
OP_IS_FLOAT = 29
OP_IS_LIST = 30
OP_IS_TUPLE = 31
OP_IS_BOOLEAN = 32
OP_IS_NUMBER = 33
OP_PLUS = 34
OP_MINUS = 35
OP_TIMES = 36
OP_RDIV = 37
OP_IDIV_NAT = 38
OP_REM_NAT = 39
OP_UNARY = 40
OP_EQUAL = 41
OP_UNEQUAL = 42
OP_FLOAT = 47
OP_BOGUS = 48
OP_ATOM_NIL = 49
OP_ATOM_HEAD = 50
OP_ATOM_TAIL = 51
OP_LIST_TO_TUPLE = 52
OP_TUPLE_TO_LIST = 53
OP_LT_INT = 54
OP_LT_FLOAT = 55
OP_CONS = 56
OP_TCONS = 57
OP_POW = 58
OP_MAKE_BITSTR = 59
OP_EMPTY_BITSTR = 60
OP_NONEMPTY_BITSTR = 61
OP_CONCAT_SEGS = 62
OP_BITMATCH_CONST_TRUE = 63
OP_BITMATCH_CONST_FALSE = 64
OP_BITMATCH_VAR_TRUE = 65
OP_BITMATCH_VAR_FALSE = 66
OP_IS_BITSTRING = 67
OP_IS_FUN = 69
OP_IS_FUN_WITH_ARITY = 70
OP_NOT_LAMBDA_WITH_ARITY = 71
OP_FRESH_LAMBDA_WITH_ARITY = 72
OP_EVALUATED_CLOSURE = 73
OP_TRUNC = 74

SOLVER_STATUS_SAT = "sat"
SOLVER_STATUS_UNSAT = "unsat"
SOLVER_STATUS_UNKNOWN = "unknown"
SOLVER_STATUS_TIMEOUT = "timeout"

def is_constraint_kind(tp):
  return tp == CONSTRAINT_TRUE or tp == CONSTRAINT_FALSE

def is_interpretable(tp):
  xs = set([OP_SPAWN, OP_SPAWNED, OP_MSG_SEND, OP_MSG_RECEIVE, OP_MSG_CONSUME])
  return tp not in xs

def is_reversible(tp, opcode):
  return is_constraint_kind(tp)
