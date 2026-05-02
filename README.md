#  Support Set (Crisp Set) of a Fuzzy Set in Python

 Introduction

This program is a simple implementation of the **Support Set** concept from **Fuzzy Set Theory** using Python.

In fuzzy logic, every element can belong to a set partially. Instead of only `0` or `1`, fuzzy sets allow values between `0` and `1`.

Example:

```python
A = {
    "a": 0.2,
    "b": 0,
    "c": 0.7,
    "d": 1
}
```

Here:

* `a` belongs to the set by `0.2`
* `b` does not belong because its value is `0`
* `c` belongs by `0.7`
* `d` fully belongs by `1`

The main goal of this program is to print only those elements whose membership value is greater than `0`.

That collection of elements is called the **Support Set**.

---

 Mathematical Idea

The support set of a fuzzy set is:

Support(A) = {x | μ(x) > 0}

Meaning:

* Include every element `x`
* only if its membership value is greater than `0`

---

 Complete Program

```python
# Function to compute Support Set

def support(fuset: dict):

    print("Support set:", end="")

    for element, membership in fuset.items():

        if membership > 0:
            print(element, end=" ")


# Fuzzy Set
A1 = {
    "a": 0.2,
    "b": 0,
    "c": 0.7,
    "d": 1
}


# Function Call
support(A1)
```

---

 Understanding the Program Step-by-Step

## 1. Function Definition

```python
def support(fuset: dict):
```

This line creates a function named `support`.

### Why are we using a function?

Functions help us:

* reuse code
* keep programs organized
* avoid rewriting the same logic
* separate logic from execution

The parameter:

```python
fuset
```

will receive the fuzzy set.

The type hint:

```python
: dict
```

simply tells the developer that the input should be a dictionary.

---

# 2. Printing the Heading

```python
print("Support set:", end="")
```

This prints the heading before displaying the support elements.

### Why use `end=""`?

Normally, `print()` moves to the next line automatically.

But here we want the output to continue on the same line.

So:

```python
end=""
```

prevents the line break.

---

# 3. Looping Through the Dictionary

```python
for element, membership in fuset.items():
```

This loop goes through every item inside the dictionary.

### What does `.items()` do?

It returns:

* key
* value

pairs.

Example:

```python
"a": 0.2
```

becomes:

```python
element = "a"
membership = 0.2
```

So during every loop iteration:

| Variable     | Stores           |
| ------------ | ---------------- |
| `element`    | dictionary key   |
| `membership` | membership value |

---

# 4. Checking the Condition

```python
if membership > 0:
```

This is the main logic of the program.

The support set only contains elements whose membership value is greater than `0`.

So:

| Membership       | Included in Support Set? |
| ---------------- | ------------------------ |
| `0`              | No                       |
| Greater than `0` | Yes                      |

This line acts like a filter.

---

# 5. Printing Valid Elements

```python
print(element, end=" ")
```

If the condition becomes true, the element is printed.

Only the element name is printed because support sets contain elements, not their membership values.

Output becomes:

```python
Support set: a c d
```

---

# 6. Creating the Fuzzy Set

```python
A1 = {
    "a": 0.2,
    "b": 0,
    "c": 0.7,
    "d": 1
}
```

This dictionary represents the fuzzy set.

### Why use a dictionary?

Because dictionaries naturally store:

| Dictionary Part | Fuzzy Concept |
| --------------- | ------------- |
| Key             | Element       |
| Value           | Membership    |

This makes dictionaries perfect for fuzzy set representation.

---

# 7. Function Call

```python
support(A1)
```

This line calls the function.

It sends the fuzzy set `A1` into the function.

Internally Python does:

```python
fuset = A1
```

Then the function starts processing the dictionary.

---

# How the Entire Program Works

## Step 1

The fuzzy set is stored in a dictionary.

## Step 2

The function receives the dictionary.

## Step 3

The loop reads every element and membership value.

## Step 4

The condition checks:

```python
membership > 0
```

## Step 5

If true, the element is printed.

---

# Concepts Used in This Program

# | Concept    | Purpose                   |
 |            |                           |
 | Function   | Organizes logic           |
 | Dictionary | Stores fuzzy set          |
 | Loop       | Traverses elements        |
 | Condition  | Filters elements          |
 | Type Hint  | Improves readability      |
 | Iteration  | Processes data one-by-one |

---

# Principle Behind the Program

The program works on the principle of conditional filtering.

The loop checks every membership value.

The condition:

```python
if membership > 0
```

filters only the valid elements.

This is how the support set is extracted from the fuzzy set.

---

# Time Complexity

The program traverses the dictionary only once.

Overall time complexity:

O(n)

where `n` is the number of elements.

---
Final part

This program is a clean and beginner-friendly implementation of support set computation in fuzzy logic.

It demonstrates:

* how fuzzy sets are represented in Python
* how dictionaries work with key-value mapping
* how loops process data
* how conditions filter valid elements
* how functions improve code structure

The implementation is simple, readable, and follows proper Python programming practices.
