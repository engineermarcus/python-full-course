Here's a complete, structured list of Python topics as of 2026 (current stable: Python 3.14, released October 7, 2025; Python 3.15 is expected in October 2026):

---

**FOUNDATIONS**
1. Syntax, indentation, comments
2. Variables and assignment
3. Data types — `int`, `float`, `str`, `bool`, `NoneType`
4. Type casting / conversion
5. Operators — arithmetic, comparison, logical, bitwise, membership, identity
6. String methods and formatting (`f-strings`, `format()`, `%`)
7. Input/output — `print()`, `input()`

---

**CONTROL FLOW**
8. `if / elif / else`
9. `match / case` (structural pattern matching — Python 3.10+)
10. `for` loops
11. `while` loops
12. `break`, `continue`, `pass`
13. `else` on loops

---

**DATA STRUCTURES**
14. Lists — indexing, slicing, methods
15. Tuples — immutability, unpacking
16. Sets — `set`, `frozenset`
17. Dictionaries — methods, comprehensions
18. Ranges
19. Nested structures
20. List/dict/set comprehensions
21. Generator expressions

---

**FUNCTIONS**
22. Defining and calling functions
23. Arguments — positional, keyword, default, `*args`, `**kwargs`
24. Return values
25. Scope — `global`, `nonlocal`, LEGB rule
26. Lambda functions
27. Recursion
28. Decorators
29. Closures
30. `functools` — `partial`, `reduce`, `lru_cache`, `wraps`

---

**OBJECT-ORIENTED PROGRAMMING**
31. Classes and instances
32. `__init__`, `self`
33. Instance vs class vs static methods
34. Inheritance and `super()`
35. Multiple inheritance and MRO
36. Dunder/magic methods (`__str__`, `__repr__`, `__len__`, etc.)
37. Properties (`@property`, `setter`, `deleter`)
38. Abstract classes (`abc` module)
39. Dataclasses (`@dataclass`)
40. `__slots__`

---

**ITERATORS & GENERATORS**
41. Iterators protocol (`__iter__`, `__next__`)
42. `iter()`, `next()`
43. Generator functions (`yield`)
44. `yield from`
45. `itertools` module

---

**ERROR HANDLING**
46. `try / except / else / finally`
47. Built-in exception hierarchy
48. Raising exceptions
49. Custom exceptions
50. Exception groups and `except*` (Python 3.11+)

---

**MODULES & PACKAGES**
51. `import`, `from ... import`, `as`
52. `__name__ == "__main__"`
53. Creating and structuring packages
54. `__init__.py`
55. `sys.path` and module search
56. Virtual environments — `venv`, `pip`
57. `pyproject.toml`, `setup.cfg`, packaging

---

**FILE I/O**
58. Reading/writing files — `open()`, `with` statement
59. Text vs binary mode
60. `pathlib.Path` (preferred over `os.path`)
61. Working with CSV — `csv` module
62. JSON — `json` module
63. YAML, TOML, XML parsing

---

**STANDARD LIBRARY ESSENTIALS**
64. `os`, `sys`
65. `datetime`, `time`, `calendar`
66. `re` — regular expressions
67. `collections` — `Counter`, `defaultdict`, `deque`, `OrderedDict`, `namedtuple`
68. `math`, `statistics`, `random`
69. `argparse` — CLI argument parsing
70. `logging`
71. `subprocess`
72. `shutil`, `glob`
73. `hashlib`, `hmac`
74. `copy` — shallow vs deep copy
75. `enum`
76. `typing` — type hints, `Optional`, `Union`, `Literal`, `TypeVar`

---

**TYPE SYSTEM & ANNOTATIONS**
77. Type hints (PEP 484, 526)
78. `from __future__ import annotations`
79. Deferred annotations (Python 3.14) — lazily evaluated, improving startup time
80. `TypeAlias`, `ParamSpec`, `TypeVarTuple`
81. Static type checkers — `mypy`, `pyright`

---

**CONCURRENCY**
82. Threading — `threading` module
83. Multiprocessing — `multiprocessing` module
84. `concurrent.futures` — `ThreadPoolExecutor`, `ProcessPoolExecutor`
85. `asyncio` — event loop, `async/await`, coroutines, tasks
86. Free-threaded build mode (GIL disabled) — experimental in 3.13, improved in 3.14
87. JIT compiler — complements the specializing adaptive interpreter, replaces bytecode sequences with pre-generated machine code

---

**TESTING**
88. `unittest`
89. `pytest` — fixtures, parametrize, markers
90. Mocking — `unittest.mock`
91. `doctest`
92. Code coverage — `coverage.py`

---

**DEBUGGING & PROFILING**
93. `pdb` / `breakpoint()`
94. Improved interactive interpreter (3.13+) with multi-line editing, color support, and colorized exception tracebacks
95. `cProfile`, `timeit`, `tracemalloc`
96. Logging best practices

---

**WEB & NETWORKING**
97. `http.client`, `urllib`
98. `requests` library
99. `httpx` (async HTTP)
100. Flask — routing, blueprints, context
101. FastAPI — path params, Pydantic, async endpoints
102. Django — ORM, views, templates, migrations
103. WebSockets — `websockets`, `aiohttp`
104. REST API design
105. Web scraping — `BeautifulSoup`, `Playwright`

---

**DATA SCIENCE & ML**
106. `numpy` — arrays, broadcasting, linear algebra
107. `pandas` — DataFrames, groupby, merge, IO
108. `matplotlib`, `seaborn`, `plotly` — visualization
109. `scikit-learn` — preprocessing, models, pipelines
110. `tensorflow` / `pytorch` — deep learning
111. `huggingface transformers` — LLMs, inference
112. Jupyter notebooks

---

**DATABASES**
113. `sqlite3`
114. `SQLAlchemy` — ORM and core
115. `psycopg2` / `asyncpg` for PostgreSQL
116. `pymongo` for MongoDB
117. Redis with `redis-py`
118. Migrations — `alembic`

---

**SECURITY**
119. `secrets` module
120. `cryptography` library
121. Secure password hashing — `bcrypt`, `argon2`
122. SSL/TLS — `ssl` module
123. Input validation and sanitization
124. JWT handling

---

**PACKAGING & TOOLING**
125. `uv` — fast package/project manager (modern replacement for pip+venv as of 2025)
126. `ruff` — linter and formatter (fast, Rust-based)
127. `black` — code formatter
128. `pre-commit` hooks
129. `tox`, `nox` for test automation
130. `Makefile` / `just` for task running

---

**ADVANCED / MODERN PYTHON**
131. Context managers — `with`, `contextlib`, `__enter__/__exit__`
132. Metaclasses
133. Descriptors
134. `__init_subclass__`, `__class_getitem__`
135. Protocol classes (structural subtyping)
136. `TypedDict`
137. `ParamSpec`, `Concatenate`
138. Python is evolving toward production-grade performance, safer concurrency, and observability — 3.13 through 3.15 mark a major transition
139. Multi-interpreter support (`interpreters` module, 3.13+)
140. `tomllib` (built-in TOML parsing, 3.11+)

---
