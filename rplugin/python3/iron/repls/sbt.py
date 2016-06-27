# encoding:utf-8
"""Scala repl definitions for iron.nvim. """

sbt = {
    'command': 'sbt',
    'language': 'sbt',
    'detect': lambda *args, **kwargs: True,
    'multiline': (':paste', '<C-D>'),
}