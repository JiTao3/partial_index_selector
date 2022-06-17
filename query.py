from selection.workload import Query

class Predicate:
    """
    if op is =, min_b = predicate and max_b = None
    should be converted that the predicate is  min_b < A.a < max_b
    """
    def __init__(self, table, attr, min_b, max_b) -> None:
        self.table = table
        self.attr = attr
        self.min_b = min_b
        self.max_b = max_b



class PQuery(Query):
    def __init__(self, query_id, query_text, columns=None):
        super(Query, self).__init__(query_id, query_text, columns)
        self.predicates = None
        self.logical_op = None
        
        # todo get query predicates
    
    def normalize_predicates(self):
        pass