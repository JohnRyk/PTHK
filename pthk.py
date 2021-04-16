#!/usr/bin/env python3
# coding: utf-8

import sys
import lib.core.inputHandler as inputHandler


if __name__ == '__main__':
    if len(sys.argv) == 0:
        getBanner.banner()
        sys.exit(0)

    inputHandler.handler()


