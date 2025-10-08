# P@ssw0rd Str3ngth!
*October 3, 2025*

Given a password string, return `"weak"`, `"medium"`, or `"strong"` based on the strength of the password.

A password is evaluated according to the following rules:

- It is at least 8 characters long.
- It contains both uppercase and lowercase letters.
- It contains at least one number.
- It contains at least one special character from this set: `!`, `@`, `#`, `$`, `%`, `^`, `&`, or `*`.

Return `"weak"` if the password meets fewer than two of the rules. Return `"medium"` if the password meets 2 or 3 of the rules. Return `"strong"` if the password meets all 4 rules.

## Tests

1. `check_strength("123456")` should return `"weak"`.
2. `check_strength("pass!!!")` should return `"weak"`.
3. `check_strength("Qwerty")` should return `"weak"`.
4. `check_strength("PASSWORD")` should return `"weak"`.
5. `check_strength("PASSWORD!")` should return `"medium"`.
6. `check_strength("PassWord%^!")` should return `"medium"`.
7. `check_strength("qwerty12345")` should return `"medium"`.
8. `check_strength("PASSWORD!")` should return `"medium"`.
9. `check_strength("PASSWORD!")` should return `"medium"`.
10. `check_strength("S3cur3P@ssw0rd")` should return `"strong"`.
11. `check_strength("C0d3&Fun!")` should return `"strong"`.

## Solution

```python
def check_strength(password: str):
    has_8_chars = len(password) >= 8
    has_uppercase_letters = False
    has_lowercase_letters = False
    has_number = False
    has_special_chars = False
    for char in password:
        if char.islower() and not has_lowercase_letters: has_lowercase_letters = True
        if char.isupper() and not has_uppercase_letters: has_uppercase_letters = True
        if char.isnumeric() and not has_number: has_number = True
        if char in ["!", "@", "#", "$", "%", "^", "&", "*"] and not has_special_chars: has_special_chars = True

    num_of_rules = int(has_8_chars) + int(has_uppercase_letters and has_lowercase_letters) + int(hasNumber) + int(has_special_chars)
    print("=> num_of_rules:", num_of_rules)
    if num_of_rules >= 4: return "strong"
    if num_of_rules >= 2: return "medium"
    return "weak"
```
