from query import PQuery
from partial_index import PartialIndex
from typing import *


class TableInfo:
    def __init__(
        self, table_name, domain, table_size, attr_list: List[str]
    ) -> None:
        self.table_name = table_name
        self.domain = domain
        self.table_size = table_size

        self.attribute_size = len(attr_list)
        self.attr_idx = {attr: idx for idx, attr in attr_list}
        # attribute size = [] attribute number of  each table


class WorkloadEncoder:
    def __init__(
        self, table_info: List[TableInfo], querys: List[PQuery], bin_size=50
    ) -> None:
        self.bin_size = bin_size
        self.querys = querys
        self.workload_size = len(self.querys)
        self.table_info = table_info
        self.embedding_vec = [
            [[0] * self.bin_size for _ in range(table.attribute_size)]
            for table in self.table_info
        ]
        self.table_idx = {
            table.name: idx for idx, table in enumerate(self.table_info)
        }


    def encode(self):

        for query in self.querys:
            for predicates in query.predicates:
                table_idx = self.table_idx[predicates.table]
                attr_idx = self.table_info[table_idx].attr_idx[predicates.attr]
                pre_vec = [0] * self.bin_size
                if predicates.op == "=":
                    bin_idx = predicates.min_b * self.bin_size
                    pre_vec[bin_idx] += 1
                else:
                    min_bin_idx = predicates.min_b * self.bin_size
                    max_bin_idx = predicates.max_b * self.bin_size
                    for i in range(min_bin_idx, max_bin_idx):
                        pre_vec[i] += 1 / (max_bin_idx - min_bin_idx + 1)
                self.embedding_vec[table_idx][attr_idx] += pre_vec

        # todo : normalize the embedding vector according to the table (attribute)
                

class IndexEncoder:
    def __init__(
        self,
        table_info: List[TableInfo],
        partial_indexes: List[PartialIndex],
        bin_size=50,
    ) -> None:
        self.bin_size = bin_size
        self.table_info = table_info
        self.partial_indexes = partial_indexes
        self.index_size = len(self.partial_indexes)
        self.embedding_vec = [
            [[] for _ in range(table.attribute_size)]
            for table in self.table_info
        ]
        self.table_idx = {
            table.name: idx for idx, table in enumerate(self.table_info)
        }

    def encoder(self):
        for partial_index in self.partial_indexes:
            colums = partial_index.columns
            for idx, predicate in enumerate(partial_index.predicates):
                table_idx = self.table_idx[predicate.table]
                attr_idx = self.table_info[table_idx].attr_idx[predicate.attr]
                pre_vec = [0] * self.bin_size
                if idx == 0:
                    if predicate.op == "=":
                        bin_idx = predicate.min_b * self.bin_size
                        pre_vec[bin_idx] += 1
                    else:
                        min_bin_idx = predicate.min_b * self.bin_size
                        max_bin_idx = predicate.max_b * self.bin_size
                        for i in range(min_bin_idx, max_bin_idx):
                            pre_vec[i] += 1
                else:
                    if predicate.op == "=":
                        bin_idx = predicate.min_b * self.bin_size
                        pre_vec[bin_idx] += 0.25
                    else:
                        min_bin_idx = predicate.min_b * self.bin_size
                        max_bin_idx = predicate.max_b * self.bin_size
                        for i in range(min_bin_idx, max_bin_idx):
                            pre_vec[i] += 0.25
                self.embedding_vec[table_idx][attr_idx] += pre_vec
                

