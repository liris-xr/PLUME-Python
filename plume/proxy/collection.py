from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, Callable, Optional, Dict, Type, Sequence, List, Iterable, Any

C = TypeVar('C', bound='Collection')
T = TypeVar('T')
K = TypeVar('K')

class Collection(ABC, Generic[T], Iterable[T]):

    _items: List[T]

    def __init__(self, items: Optional[Sequence[T]] = None):
        self._items = []

        if items is not None:
            for item in items:
                if item not in self._items:
                    self._items.append(item)

        self.__post_init__()

    def __post_init__(self):
        pass

    def _add(self, item: T) -> bool:
        if item not in self._items:
            self._items.append(item)
            return True
        return False
    
    def _remove(self, item: T) -> bool:
        if item is None:
            return False
        if item in self._items:
            self._items.remove(item)
            return True
        return False

    def __len__(self) -> int:
        return len(self._items)

    def __getitem__(self, index: int) -> T:
        return self._items[index]

    def __iter__(self):
        return iter(self._items)

    def __contains__(self, item: T) -> bool:
        return item in self._items

    def __str__(self) -> str:
        return str(self._items)

    def __repr__(self) -> str:
        return repr(self._items)
    
    def where(self: C, predicate: Callable[[T], bool]) -> C:
        return type(self)([item for item in self._items if predicate(item)])

    def first_or_default(self, predicate: Optional[Callable[[T], bool]] = None, default: Optional[T] = None) -> Optional[T]:
        for item in self._items:
            if predicate is None or predicate(item):
                return item
        return default

    def last_or_default(self, predicate: Optional[Callable[[T], bool]] = None, default: Optional[T] = None) -> Optional[T]:
        for item in reversed(self._items):
            if predicate is None or predicate(item):
                return item
        return default

    def first(self, predicate: Optional[Callable[[T], bool]] = None) -> Optional[T]:
        for item in self._items:
            if predicate is None or predicate(item):
                return item
        raise ValueError("Sequence contains no matching element")
    
    def last(self, predicate: Optional[Callable[[T], bool]]) -> Optional[T]:
        for item in reversed(self._items):
            if predicate is None or predicate(item):
                return item
        raise ValueError("Sequence contains no matching element")

    def sort_by(self: C, key: Callable[[T], int], reverse: bool = False) -> C:
        return type(self)(sorted(self._items, key=key, reverse=reverse))

    def group_by(self: C, key: Callable[[T], K]) -> Dict[Type[K], C]:
        groups: Dict[K, C] = {}
        for item in self._items:
            key = key(item)
            if key in groups:
                groups[key]._add(item)
            else:
                groups[key] = type(self)([item])
        return groups
    
    def except_with(self: C, predicate: Callable[[T], bool]) -> C:
        return type(self)({item for item in self._items if not predicate(item)})

    def __or__(self, value):
        if isinstance(value, (list, set, tuple, Collection)):
            return type(self)(set(self._items) | set(value))
        else:
            return type(self)(set(self._items) | {value})
    
    def __and__(self, value):
        if isinstance(value, (list, set, tuple, Collection)):
            return type(self)(set(self._items) & set(value))
        else:
            return type(self)(set(self._items) & {value})
    
    def __sub__(self, value):
        if isinstance(value, (list, set, tuple, Collection)):
            return type(self)(set(self._items) - set(value))
        else:
            return type(self)(set(self._items) - {value})

    def __xor__(self, value):
        if isinstance(value, (list, set, tuple, Collection)):
            return type(self)(set(self._items) ^ set(value))
        else:
            return type(self)(set(self._items) ^ {value})
    
    def __eq__(self, value):
        if isinstance(value, Collection):
            return self._items == value._items
        else:
            return False
    
    def __str__(self):
        return f"[{', '.join(str(item) for item in self._items)}]"

    def __repr__(self):
        return f"{type(self).__name__}(items={self._items})"