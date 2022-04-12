#!/usr/bin/env python3

import argparse

import yaml


PARSER = argparse.ArgumentParser(
    description="Create configs for conky-gyre."
)
PARSER.add_argument(
    "--conky",
    action=argparse.BooleanOptionalAction,
    default=True,
    help="Generate conky file.",
)
PARSER.add_argument(
    "--lua",
    action=argparse.BooleanOptionalAction,
    default=True,
    help="Generate lua file.",
)


def main(args):
    with open("settings_gyre.yaml", "rt", encoding="utf-8") as infile:
        settings = yaml.load(infile, yaml.CLoader)

    if args.conky:
        with open(
            "conky_gyre_conky.template", "rt", encoding="utf-8"
        ) as infile:
            conky_src = infile.read()
        with open("conky_gyre.conkyrc", "wt", encoding="utf-8") as outfile:
            outfile.write(conky_src.format(**settings))

    if args.lua:
        with open("conky_gyre_lua.template", "rt", encoding="utf-8") as infile:
            lua_src = infile.read()
        with open("conky_gyre.lua", "wt", encoding="utf-8") as outfile:
            outfile.write(lua_src.format(**settings))


if __name__ == "__main__":
    ARGS = PARSER.parse_args()
    main(ARGS)
