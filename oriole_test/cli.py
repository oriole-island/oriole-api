#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import click


@click.command()
def main(args=None):
    click.echo("Eric.Zhou")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
