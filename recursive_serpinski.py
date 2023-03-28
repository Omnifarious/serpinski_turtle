#!/usr/bin/python3


from turtle import *
from math import sqrt


def serpinski(size: int) -> None:
    """serpinks(size) -> Results in using Python's turtle module to draw a
                      Serpinski's Gasket.

    size should be interpreted using binary.  The number of trailing 0 bits
    represent the number of levels of recursion for the resulting Serpinski's
    Gasket, and the value as a whole is the length of an edge on the biggest
    triangle."""
    def serpinski_sub(size):
        if size & 1:
            fd(size)
            yield None
            rt(120)
            fd(size)
            lt(120)
            yield None
            lt(120)
            fd(size)
            rt(120)
        else:
            size = size // 2
            g = serpinski_sub(size)
            next(g)
            h = serpinski_sub(size)
            next(h)
            yield None
            next(h)
            try:
                next(h)
            except StopIteration:
                pass
            else:
                assert False
            next(g)
            h = serpinski_sub(size)
            next(h)
            next(h)
            yield None
            try:
                next(h)
            except StopIteration:
                pass
            else:
                assert False
            try:
                next(g)
            except StopIteration:
                pass
            else:
                assert False

    def serpinski_top(size):
        if size & 1:
            fd(size)
            rt(120)
            fd(size)
            rt(120)
            fd(size)
            rt(120)
        else:
            size = size // 2
            for _ in serpinski_sub(size):
                serpinski_top(size)

    pu()
    a = 139.10660535086907
    h = size * sqrt(7) / 4
    lt(a)
    fd(h)
    rt(a)
    pd()
    serpinski_top(size)
    pu()
    rt(180 - a)
    fd(h)
    lt(180 - a)
    pd()
