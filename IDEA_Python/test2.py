#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
print(f1)
f1(1, 2, c=3)
print(f1)
f1(1, 2, 3, 'a', 'b')
print(f1)
f1(1, 2, 3, 'a', 'b', x=99)
print(f1)
f2(1, 2, d=99, ext=None)
print(f2)
