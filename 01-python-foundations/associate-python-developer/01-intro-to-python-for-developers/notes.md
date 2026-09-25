# Course Notes: Introduction to Python for Developers

---

## 1. Python Variables & Primitive Data Types
* **Integers (`int`)**: Whole numbers, e.g., `count = 42`
* **Floats (`float`)**: Decimal numbers, e.g., `price = 19.99`
* **Strings (`str`)**: Text sequences, e.g., `name = "Ada Lovelace"`
* **Booleans (`bool`)**: `True` or `False`

### Type Casting & Inspection
```python
x = "100"
y = int(x)       # 100
is_active = bool(1) # True
print(type(y))   # <class 'int'>
```

---

## 2. Strings & Formatting
### Modern String Interpolation (f-strings)
```python
user = "Alex"
score = 95
print(f"User {user} achieved a score of {score}.")
```

### Common String Methods
* `.strip()`: Remove leading/trailing whitespace
* `.lower()`, `.upper()`, `.title()`: Case modification
* `.replace(old, new)`: Replace occurrences
* `.split(delim)`: Split string into a list

---

## 3. Lists & Sequences
* **Zero-based indexing**: `items[0]`
* **Negative indexing**: `items[-1]` (last element)
* **Slicing**: `items[start:stop:step]`
* **List Methods**:
  * `.append(item)`: Add item to end
  * `.extend(iterable)`: Concatenate elements
  * `.pop(index)`: Remove and return element

---

## 4. Control Flow & Functions
```python
def calculate_tax(amount: float, rate: float = 0.2) -> float:
    """Calculates tax on a given amount."""
    if amount < 0:
        raise ValueError("Amount cannot be negative.")
    return round(amount * rate, 2)
```

---

## 5. Key Pitfalls & Best Practices
* Use descriptive variable names (PEP 8 snake_case).
* Strings and integers are immutable in Python; operations return new instances.
* Avoid using Python keywords (`list`, `str`, `dict`, `sum`) as variable names.
