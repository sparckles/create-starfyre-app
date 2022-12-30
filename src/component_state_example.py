from starfyre import create_component, create_signal

[get_component_state, set_state] = create_signal(0)


def updateCounter(component, *args):
    set_state(get_component_state(component) + 1)


def ComponentStateExample():
    return create_component(
        """<div onClick={updateCount}>This is the component state <button>Click Here to increment</button> {get_component_state}</div>""",
        {"updateCount": updateCounter},
        state={"get_component_state": get_component_state},
    )
