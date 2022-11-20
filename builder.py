from typing import Optional, Iterable, List, Union, Generator, Dict, Callable

from functions import filter_query, map_query, unique_query, sorted_query, limit_query, regex_query

FILE_NAME = 'data/apache_logs.txt'
CMD_TO_FUNCTIONS: Dict[str, Callable] = {
    'filter': filter_query, 'map': map_query, 'unique': unique_query,
    'sort': sorted_query, 'limit': limit_query, 'regex': regex_query
}


def iter_file(file_name: str) -> Generator[str, None, None]:
    """Генератор для чтения логов"""

    with open(file_name) as file:
        for row in file:
            yield row


def query_builder(cmd: str, value: Union[str, int], data: Optional[Iterable[str]]) -> List[str]:

    if data is None:
        prepared_data: Union[Generator, Iterable[str]] = iter_file(FILE_NAME)
    else:
        prepared_data = data
    result: Iterable[str] = CMD_TO_FUNCTIONS[cmd](param=value, data=prepared_data)
    return list(result)
