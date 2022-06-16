from query import PQuery
from typing import *


class TableInfo:
    def __init__(self, table_name, domain, table_size, attribute_size) -> None:
        self.table_name = table_name
        self.domain = domain
        self.table_size = table_size

        self.attribute_size = attribute_size
        # attribute size = [] attribute number of  each table


class WorkloadEncoder:
    def __init__(self, table_info: TableInfo, querys: List[PQuery], bin_size=50) -> None:
        self.bin_size = bin_size
        self.querys = querys
        self.workload_size = len(self.querys)
        self.table_info = table_info
        self.embedding_vec = [None for _ in range(self.table_info.table_size)]

    def encode(self):

        for query in self.querys:
            for predicates in query.predicates:
                pass

