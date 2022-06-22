from typing import Dict
import operator
from functools import reduce


operator_dict = {">": operator.gt, "<": operator.lt}


def MutliFilters(data: Dict):
    def __operatorFunc(op, column, value):
        return op(column, value)

    filters = list(
        map(
            lambda col_name: __operatorFunc(
                operator_dict.get(col_name.get("comparisonType")),
                col(col_name.get("name")),
                col_name.get("value"),
            ),
            data["filter"],
        )
    )
    if data.get("matchAll"):
        return reduce(operator.and_, filters)
    else:
        return reduce(operator.or_, filters)
