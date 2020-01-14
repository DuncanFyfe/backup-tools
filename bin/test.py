#!/usr/bin/env python3
import sys

from jinja2 import Environment, PackageLoader, Template, select_autoescape

import backup_tools


def test_text():
    txt = """
    BEGIN
    {% if user.a %}
    >>{{ user.x }}<<
    {% else %}
    >>{{ user.x.y }}<<
    {% endif %}
    END
    """
    return Template(txt)


def main():
    env = Environment(
        loader=PackageLoader("backup_tools", "templates"), autoescape=False
    )

    tpl = env.get_template("test.j2")
    print("DJF A")
    print(tpl)
    print("DJF B")
    out = None
    out = tpl.render(user={"a": "b", "z": "y", "x": {"q": "w", "y": "z"}})
    print(out)


if __name__ == "__main__":
    main()
