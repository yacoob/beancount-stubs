from collections.abc import Generator
from typing import Any, Callable, Iterable, Iterator, Pattern
from typing_extensions import TypeAlias

Account: TypeAlias = str
sep: str
ACC_COMP_TYPE_RE: Pattern
ACC_COMP_NAME_RE: Pattern
ACCOUNT_RE: Pattern
TYPE: str

def is_valid(string: Account) -> bool: ...
def join(*components: tuple[str]) -> Account: ...
def split(account_name: Account) -> list[str]: ...
def parent(account_name: Account) -> Account: ...
def leaf(account_name: Account) -> Account: ...
def sans_root(account_name: Account) -> Account: ...
def root(num_components: int, account_name: Account) -> str: ...
def has_component(account_name: Account, component: str) -> bool: ...
def commonprefix(accounts: Iterable[Account]) -> Account: ...
def walk(
    root_directory: Account,
) -> Iterator[tuple[str, Account, list[str], list[str]]]: ...
def parent_matcher(account_name: Account) -> Callable[[str], Any]: ...
def parents(account_name: Account) -> Iterator[Account]: ...

class AccountTransformer:
    rsep: Any
    def __init__(self: AccountTransformer, rsep: str | None = ...) -> None: ...
    def render(self: AccountTransformer, account_name: Account) -> str: ...
    def parse(self: AccountTransformer, transformed_name: str) -> Account: ...
