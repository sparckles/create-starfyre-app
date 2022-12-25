import starfyre
from .header import Body

def main():
    div = f"<div>{Body()}</div>"
    starfyre.render_root(div)
