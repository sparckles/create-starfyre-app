import starfyre

from .counter import Counter
from .display import Display
from .component_state_example import ComponentStateExample


def main():
    counter = Counter()
    display = Display()
    component_state_example = ComponentStateExample()
    counter.children.append(display)
    counter.children.append(component_state_example)
    starfyre.render(counter, starfyre.js.document.getElementById("root"))
