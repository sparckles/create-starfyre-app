# create-starfyre-app

## Usage

1. To build the application
```bash
python3 -m starfyre --build --path "."
```

2. To serve the application
```bash
python3 -m starfyre --serve --path "."
```

## Sample Usage


```python
# Path: pages/__init__.fyre
from ..store import store
import "../styles/index.css"

def message():
  return "World"

<pyxide>
  <div>
    Hello, {message()}
  </div>
</pyxide>

```



