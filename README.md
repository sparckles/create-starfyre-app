# create-starfyre-app

This is a very basic implementation Right now.

The steps to run:
1. `git clone https://github.com/sansyrox/create-starfyre-app` - git clone the repo and `cd` in the folder
2. `npm run start` - this will build the custom src file as a package and then start an http server
3. Go to `http://localhost:8000/public` to see the file

*All the source code is hosted on the main repo.*

## Disclaimer

The code is a demonstration of the initial syntax, component state, global state, reactive rendering and component stacking. However, please do keep in mind that is still version 1 and full of bugs. 

I would appreciate any kind of bug report on any form of feedback/support.


## Sample Usage:

src/__init__.py
```python
import starfyre

from .component import Component


def main():
    component = Component()
    starfyre.render(component, starfyre.js.document.getElementById("root"))
```

src/component.py
```python

from starfyre import create_component, create_signal

[get_component_state, set_state] = create_signal(0)


def updateCounter(component, *args):
    set_state(get_component_state(component) + 1)


def Component():
    return create_component("""<div onClick={updateCount}>
        This is the component state
        <button>Click Here to increment</button> {get_component_state}
        </div>""",
        {"updateCount": updateCounter},
        state={"get_component_state": get_component_state},
    )

```
