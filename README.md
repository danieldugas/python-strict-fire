# Python Strict Fire [![PyPI](https://img.shields.io/pypi/pyversions/fire.svg?style=plastic)](https://github.com/google/python-fire)

Strict Fire is a temporary patch to the Fire python library. Whereas Fire currently ignores unknown arguments, Strict Fire always complains by default.

Install with

```
pip install strictfire
```

To use, replace the Fire() method with StrictFire()

```
from strictfire import StrictFire

def myfunc(arg1, arg2=0):
  print((arg1, arg2))

StrictFire(myfunc)
```

Things work like before

```
$ python test.py --arg1 1 --arg2 2
(1, 2)
```

Except if you pass an unexpected argument

```
$ python test.py --arg1 1 --arg3 2
ERROR: Unknown arguments: ['--arg3', '2']
Usage: test.py ARG1 <flags>
  optional flags:        --arg2

For detailed information on this command, run:
  test.py --help
```

# Notes

Refer to [this Issue](https://github.com/google/python-fire/issues/168) for more information.

This was done because the current non-strict behavior is risky in production,
and though other solutions exist (e.g. decorators), they would add code overhead to several projects.

There is no intention of disrespecting the original project / authors,
and their position on the matter of non-strict default behavior, and not breaking existing workflows is very reasonable.
I wouldn't be surprised if their efforts to address this on the main project deprecates this fork in a few months.
Until then, this is simply a temporary fix for myself and others.
If the original authors have any issues with this unofficial fork / pypi entry, 
please contact me and I will take them down.

I use Fire every day and think it's great. Thank you to its authors!
