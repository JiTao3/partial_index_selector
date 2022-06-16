from selection.workload import Query

class Predicate:
    """
    if op is =, min_b = predicate and max_b = None
    """
    def __init__(self, table, op, min_b, max_b) -> None:
        self.table = table
        self.op = op
        self.min_b = min_b
        self.max_b = max_b



class PQuery(Query):
    def __init__(self, query_id, query_text, columns=None):
        super(Query, self).__init__(query_id, query_text, columns)
        self.predicates = None
        # predicates = [(t1, op1, min1, max1), (t2, op2, min2, max2)]
        # todo get query predicates
    
    def normalize_predicates(self):
        pass