#методы list
model_list = []

model_list.append(self, __object: _T) -> None
model_list.count(self, __value: _T) -> int
model_list.extend(self, __iterable: Iterable[_T]) -> None
model_list.index(self,
          __value: _T,
          __start: SupportsIndex = ...,
          __stop: SupportsIndex = ...) -> int
model_list.pop(self, __index: SupportsIndex = ...) -> _T


# методы dict
model_dict = {}

model_dict.items(self) -> _dict_items[_KT, _VT]
model_dict.keys(self) -> _dict_keys[_KT, _VT]
model_dict.values(self) -> _dict_values[_VT, _KT]
model_dict.update(self,
           __m: Mapping[_KT, _VT],
           **kwargs: _VT) -> None
model_dict.clear(self) -> None


# методы set
model_set = {1, 1}

model_set.add(self, element: _T) -> None
model_set.update(self, *s: Iterable[_T]) -> None
model_set.clear(self) -> None
model_set.difference(self, *s: Iterable) -> Set[_T]
model_set.issubset(self, s: Iterable) -> bool


# методы str
model_str = ''

model_str.index(self,
          __sub: str,
          __start: SupportsIndex | None = ...,
          __end: SupportsIndex | None = ...) -> int
model_str.replace(self,
            __old: str,
            __new: str,
            __count: SupportsIndex = ...) -> str
model_str.encode(self,
           encoding: str = ...,
           errors: str = ...) -> bytes
model_str.format(format(self,
           *args: object,
           **kwargs: object) -> str)
model_str.join(join(self, __iterable: Iterable[str]) -> str)