from typing import Optional, Any, List, Union

def get_name(name: Optional[str] = None) -> str:
    if name:
        return name
    return "Anonymous"

print(get_name())

def get_value(value: Union[int, str]) -> str:
    if isinstance(value, int):
        return f"Number: {value}"
    return f"String: {value}"

print(get_value(1))

def get_any_value(value: Any):
    return value

print(get_any_value(False))

def sum_list(num: List[int]) -> int:
    return sum(num)

numbers: List[int] = [1,2,3]
result: int = sum_list(numbers)
print(result)