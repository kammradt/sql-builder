import re
from typing import Union


class Select:
    __select: str  # TODO accept list[str]
    __from: str = ''
    __where: str = ''
    __group_by: Union[str, int] = ''  # TODO accept list[str] or list[int]
    __order_by: Union[str, int] = ''  # TODO accept list[str] or list[int]
    __limit: int = 0

    def __init__(self, select_expression: str = None) -> None:
        """For easier usage, if no fields are given, '*' is used."""

        # Explicit verify for None since there are other non-None invalid values
        if select_expression is not None:
            self.__if_falsy_then_raise(select_expression, 'SELECT')
            self.__select = select_expression
        else:
            self.__select = '*'

    def from_(self, from_expression: str):
        self.__if_falsy_then_raise(from_expression, 'FROM')
        self.__from = from_expression
        return self

    def where_(self, where_expression: str):
        self.__if_falsy_then_raise(where_expression, 'WHERE')
        self.__where = where_expression
        return self

    def and_(self, conditional_expression: str):
        self.__if_falsy_then_raise(conditional_expression, 'AND')
        self.__where += f' AND {conditional_expression}'
        return self

    def or_(self, conditional_expression: str):
        self.__if_falsy_then_raise(conditional_expression, 'OR')
        self.__where += f' OR {conditional_expression}'
        return self

    def group_by_(self, group_by_expression: Union[str, int]):
        self.__if_falsy_then_raise(group_by_expression, 'GROUP BY')
        self.__group_by = group_by_expression
        return self

    def order_by_(self, order_by_expression: Union[str, int]):
        self.__if_falsy_then_raise(order_by_expression, 'ORDER BY')
        self.__order_by = order_by_expression
        return self

    def limit_(self, limit_expression: int):
        self.__if_falsy_then_raise(limit_expression, 'LIMIT')
        self.__limit = limit_expression
        return self

    def __if_falsy_then_raise(self, expression: Union[str, int], name: str) -> None:
        # TODO: Should check for valid strings, and raise for stuff like `'`, `/`, etc..
        if not expression:
            raise ValueError(f'{expression} is not valid for {name}')

    def __repr__(self) -> str:
        return self.__to_sql()

    def __to_sql(self) -> str:
        result = f'''
            SELECT {self.__select}
            {f'FROM {self.__from}' if self.__from else ''}
            {f'WHERE {self.__where}' if self.__where else ''}
            {f'GROUP BY {self.__group_by}' if self.__group_by else ''}
            {f'ORDER BY {self.__order_by}' if self.__order_by else ''}
            {f'LIMIT {self.__limit}' if self.__limit else ''}
        '''
        without_breaks = result.replace('\n', '').strip()
        without_spaces = re.sub(' +', ' ', without_breaks)
        return f'{without_spaces};'

    def sql(self) -> str:
        return self.__to_sql()
