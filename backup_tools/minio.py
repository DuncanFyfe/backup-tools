import argparse
import json
import sys

from jinja2 import Environment, PackageLoader, Template, select_autoescape


def load_config(configfile):
    with open(configfile) as r:
        return json.load(r)


def cl_args(argv=None):
    if not argv:
        argv = sys.argv
    argparser = argparse.ArgumentParser(
        description="Turn a configuration and templates into output."
    )
    parser.add_argument(
        "--config", action="store", type=str, help="The configuration file."
    )
    parser.add_argument(
        "--template", action="store", type=str, help="The template file."
    )
    parser.add_argument(
        "--lib",
        action="store",
        nargs="*",
        default="tempaltes",
        type=str,
        help="Additional sources of additional template components (eg. for includes).",
    )

    args = parser.parse_args(argv)


def main():
    args = cl_args()
    first_template = args.template
    config = load_config(args.config)
    template = Template("Hello {{ name }}!")
    template.render(name="John Doe")
    template = env.get_template()
    pass


if __main__ == "__name__":
    main()
