Yes
│
├── Keep every item?
│ │
│ ├── Yes
│ │ │
│ │ ├── Same value?
│ │ │ [x for x in iterable]
│ │ │
│ │ └── Change value?
│ │ [f(x) for x in iterable]
│ │
│ └── No (filter items)
│ [x for x in iterable if condition]
│
└── Keep every item but change based on condition?
[a if condition else b for x in iterable]
