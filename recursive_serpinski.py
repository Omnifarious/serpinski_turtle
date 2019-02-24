#!/usr/bin/python3


from turtle import *


def serpinski(size):
    def serpinski_top(size):
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
            g = serpinski_top(size)
            next(g)
            h = serpinski_top(size)
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
            h = serpinski_top(size)
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

    if size & 1:
        fd(size)
        rt(120)
        fd(size)
        rt(120)
        fd(size)
        rt(120)
    else:
        size = size // 2
        for _ in serpinski_top(size):
            serpinski(size)
