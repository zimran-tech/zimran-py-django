## Installation

```bash
pip install zimran-django
```

## Usage

```python
# settings.py

MIDDLEWARE = [
    'zimran.django.middleware.HttpHostRenameMiddleware',
    ...
]
```

**Adding logging**

```python
# settings.py

MIDDLEWARE = [
    'zimran.django.middleware.LoguruMiddleware'
]

```
