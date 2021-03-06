from selection.index import Index


class PartialIndex(Index):
    """
    only partial indexes
    predicates
    """

    def __init__(self, columns, predicates, estimated_size=None):
        super(Index, self).__init__(columns, estimated_size)
        self.predicates = None
        self.is_partial = True

    def __repr__(self):
        # columns_string = ",".join(map(str, self.columns))
        columns_string = ",".join(
            [
                str(col) + "_" + pre[0] + "_" + pre[1]
                for col, pre in zip(self.columns, self.predicates)
            ]
        )
        return f"I({columns_string})"
