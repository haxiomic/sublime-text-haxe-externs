# Generated by Haxe 3.4.2
# coding: utf-8

from sublime_plugin import EventListener as sublime_plugin_EventListener
import sublime as sublime_Sublime


class TestPlugin(sublime_plugin_EventListener):
    __slots__ = ()

    @staticmethod
    def main():
        print(str(("Hello Test Plugin! " + HxOverrides.stringOrNull(sublime_Sublime.version()))))


class HxOverrides:
    __slots__ = ()

    @staticmethod
    def stringOrNull(s):
        if (s is None):
            return "null"
        else:
            return s



TestPlugin.main()