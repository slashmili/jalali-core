jalali-core
===========

A lightweight Gregorian to Jalali (Persian/Shamsi) and vice versa date converter.

Overview
--------

`jalali_core` provides the core conversion logic between Gregorian and Jalali calendars. It is intentionally minimal and has no external dependencies. Starting from version 5, `jdatetime` uses this package as its underlying converter.

If you need full date/time objects (like `datetime`), use `jdatetime`. If you only need calendar conversion with minimal overhead, use `jalali_core`.

Features
--------

- Convert **Gregorian → Jalali** and **Jalali → Gregorian**
- Accurate and lightweight algorithm, no third‑party dependencies
- Suitable for resource‑limited environments
- Access to Jalali month lengths via a static list `j_days_in_month`
- Licensed under **LGPL** – safe for commercial use (with reciprocity)

Installation
------------

Install directly from PyPI:


```bash
pip install jalali-core
```

Usage
------------

First, import the main classes and constant:

---python
from jalali_core import GregorianToJalali, JalaliToGregorian, j_days_in_month
```

1. Gregorian to Jalali

```python
# Convert 2024-05-11 to Jalali
jalali = GregorianToJalali(2024, 5, 11)
print(jalali.getJalaliList())   # Output: (1403, 2, 22)
```

2. Jalali to Gregorian

```python
# Convert 1403-02-22 to Gregorian
gregorian = JalaliToGregorian(1403, 2, 22)
print(gregorian.getGregorianList())   # Output: (2024, 5, 11)
```

3. Access month lengths

j_days_in_month is a list of 12 integers (days per month from Farvardin to Esfand):

```python
# Days in Farvardin (month 1)
days_farvardin = j_days_in_month[0]   # 31

# Days in Esfand (month 12)
days_esfand = j_days_in_month[11]     # 29
```

Note: The list is zero‑based. Month number m (1‑12) corresponds to index m-1.

Project Structure

---

```bash
jalali-core/
├── jalali_core/
│   └── __init__.py      # Core conversion logic
├── .github/             # GitHub Actions config (if any)
├── .gitignore
├── LICENSE              # LGPL license text
├── README.rst           # This file
└── setup.py             # Installation script
```