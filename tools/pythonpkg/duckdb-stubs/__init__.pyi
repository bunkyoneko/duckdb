# to regenerate this from scratch, run scripts/generate_python_stubs.sh .
# be warned - currently there are still tweaks needed after this file is
# generated. These should be annotated with a comment like
# # stubgen override
# to help the sanity of maintainers.
from typing import Any, ClassVar

from typing import overload

# This should probably not be exposed
#_clean_default_connection: Any
comment: token_type
identifier: token_type
keyword: token_type
numeric_const: token_type
operator: token_type
string_const: token_type

class DuckDBPyConnection:
    def __init__(self, *args, **kwargs) -> None: ...
    def append(self, table_name: str, df: object) -> DuckDBPyConnection: ...
    def arrow(self) -> object: ...
    def begin(self) -> DuckDBPyConnection: ...
    def close(self) -> None: ...
    def commit(self) -> DuckDBPyConnection: ...
    def cursor(self) -> DuckDBPyConnection: ...
    @overload
    def df(self) -> object: ...
    @overload
    def df(self, df: object) -> DuckDBPyRelation: ...
    @overload
    def df(aliasoffrom_df) -> Any: ...
    def duplicate(self) -> DuckDBPyConnection: ...
    def execute(self, query: str, parameters: object = ..., multiple_parameter_sets: bool = ...) -> DuckDBPyConnection: ...
    def executemany(self, query: str, parameters: object = ...) -> DuckDBPyConnection: ...
    def fetch_arrow_chunk(self, vectors_per_chunk: int = ..., return_table: bool = ...) -> object: ...
    def fetch_arrow_table(self) -> object: ...
    def fetch_df(self) -> object: ...
    def fetch_df_chunk(self, vectors_per_chunk: int = ...) -> object: ...
    def fetch_record_batch(self) -> object: ...
    def fetchall(self) -> list: ...
    def fetchdf(self) -> object: ...
    def fetchnumpy(self) -> dict: ...
    def fetchone(self) -> object: ...
    def from_arrow_table(self, table: object, rows_per_thread: int = ...) -> DuckDBPyRelation: ...
    def from_csv_auto(self, file_name: str) -> DuckDBPyRelation: ...
    def from_df(self, df: object = ...) -> DuckDBPyRelation: ...
    def from_parquet(self, file_name: str) -> DuckDBPyRelation: ...
    def from_query(self, query: str, alias: str = ...) -> DuckDBPyRelation: ...
    def query(self, query: str, alias: str = ...) -> DuckDBPyRelation: ...
    def register(self, view_name: str, df: object) -> DuckDBPyConnection: ...
    def register_arrow(self, view_name: str, arrow_object: object, rows_per_thread: int = ...) -> DuckDBPyConnection: ...
    def rollback(self) -> DuckDBPyConnection: ...
    def table(self, table_name: str) -> DuckDBPyRelation: ...
    def table_function(self, name: str, parameters: object = ...) -> DuckDBPyRelation: ...
    def unregister(self, view_name: str) -> DuckDBPyConnection: ...
    def values(self, values: object) -> DuckDBPyRelation: ...
    def view(self, view_name: str) -> DuckDBPyRelation: ...
    @property
    def description(self) -> object: ...

class DuckDBPyRelation:
    def __init__(self, *args, **kwargs) -> None: ...
    def aggregate(self, aggr_expr: str, group_expr: str = ...) -> DuckDBPyRelation: ...
    def arrow(self) -> object: ...
    def create(self, table_name: str) -> None: ...
    def create_view(self, view_name: str, replace: bool = ...) -> DuckDBPyRelation: ...
    def df(self) -> object: ...
    def distinct(self) -> DuckDBPyRelation: ...
    def except_(self, other_rel: DuckDBPyRelation) -> DuckDBPyRelation: ...
    def execute(self, *args, **kwargs) -> Any: ...
    def fetchall(self) -> object: ...
    def fetchone(self) -> object: ...
    def filter(self, filter_expr: str) -> DuckDBPyRelation: ...
    def insert(self, values: object) -> None: ...
    def insert_into(self, table_name: str) -> None: ...
    def intersect(self, other_rel: DuckDBPyRelation) -> DuckDBPyRelation: ...
    def join(self, other_rel: DuckDBPyRelation, join_condition: str) -> DuckDBPyRelation: ...
    def limit(self, n: int) -> DuckDBPyRelation: ...
    def map(self, map_function: function) -> DuckDBPyRelation: ...
    def order(self, order_expr: str) -> DuckDBPyRelation: ...
    def project(self, project_expr: str) -> DuckDBPyRelation: ...
    def query(self, *args, **kwargs) -> Any: ...
    def set_alias(self, alias: str) -> DuckDBPyRelation: ...
    def to_arrow_table(self) -> object: ...
    def to_df(self) -> object: ...
    def union(self, arg0: DuckDBPyRelation) -> DuckDBPyRelation: ...
    def write_csv(self, file_name: str) -> None: ...
    @property
    def alias(self) -> str: ...
    @property
    def columns(self) -> list: ...
    @property
    def dtypes(self) -> list: ...
    @property
    def type(self) -> str: ...
    @property
    def types(self) -> list: ...

class DuckDBPyResult:
    def __init__(self, *args, **kwargs) -> None: ...
    def arrow(self, arg0: bool, arg1: int, arg2: bool) -> object: ...
    def close(self) -> None: ...
    def description(self) -> list: ...
    def df(self) -> object: ...
    def fetch_arrow_chunk(self, arg0: int, arg1: bool) -> object: ...
    def fetch_arrow_reader(self) -> object: ...
    def fetch_arrow_table(self, arg0: bool, arg1: int, arg2: bool) -> object: ...
    def fetch_df(self) -> object: ...
    def fetch_df_chunk(self, arg0: int) -> object: ...
    def fetchall(self) -> list: ...
    def fetchdf(self) -> object: ...
    def fetchnumpy(self) -> dict: ...
    def fetchone(self) -> object: ...

class token_type:
    #__doc__: ClassVar[str] = ...  # read-only
    #__members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    comment: ClassVar[token_type] = ...
    identifier: ClassVar[token_type] = ...
    keyword: ClassVar[token_type] = ...
    numeric_const: ClassVar[token_type] = ...
    operator: ClassVar[token_type] = ...
    string_const: ClassVar[token_type] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...


def aggregate(df: object, aggr_expr: str, group_expr: str = ...) -> DuckDBPyRelation: ...
def alias(df: object, alias: str) -> DuckDBPyRelation: ...
def arrow(table: object) -> DuckDBPyRelation: ...
def connect(database: str = ..., read_only: bool = ..., config: dict = ...) -> DuckDBPyConnection: ...
def df(df: object) -> DuckDBPyRelation: ...
def distinct(df: object) -> DuckDBPyRelation: ...
def filter(df: object, filter_expr: str) -> DuckDBPyRelation: ...
def from_arrow_table(table: object) -> DuckDBPyRelation: ...
def from_csv_auto(file_name: str) -> DuckDBPyRelation: ...
def from_df(df: object) -> DuckDBPyRelation: ...
def from_parquet(file_name: str) -> DuckDBPyRelation: ...
def from_query(query: str, alias: str = ...) -> DuckDBPyRelation: ...
def limit(df: object, n: int) -> DuckDBPyRelation: ...
def order(df: object, order_expr: str) -> DuckDBPyRelation: ...
def project(df: object, project_expr: str) -> DuckDBPyRelation: ...
def query(query: str, alias: str = ...) -> DuckDBPyRelation: ...
def query_df(df: object, virtual_table_name: str, sql_query: str) -> DuckDBPyResult: ...
def tokenize(query: str) -> object: ...
def values(values: object) -> DuckDBPyRelation: ...
def write_csv(df: object, file_name: str) -> None: ...
