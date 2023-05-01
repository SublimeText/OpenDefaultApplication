from __future__ import print_function

import os
import shutil
import subprocess

import sublime
import sublime_plugin


def open_with_command(cmd, paths):
    if isinstance(cmd, str):
        args = [cmd]
    elif isinstance(cmd, list):
        args = cmd[:]
    else:
        args = list(cmd)
    if not os.path.isabs(args[0]):
        args[0] = shutil.which(args[0])

    for path in paths:
        subprocess.Popen(args + [path])


class OpenDefaultCommand(sublime_plugin.WindowCommand):
    def __init__(self, window):
        self.settings = sublime.load_settings("OpenDefault.sublime-settings")
        sublime_plugin.WindowCommand.__init__(self, window)

    @property
    def use_os_startfile(self):
        return self.settings.get("use_os_startfile", False)

    @property
    def open_command(self):
        return self.settings.get("open_command", None)

    @property
    def have_open_method(self):
        return bool(self.use_os_startfile or self.open_command)

    def open_default(self, paths):
        if self.use_os_startfile:
            for path in paths:
                os.startfile(path)
        elif self.open_command:
            open_with_command(self.open_command, paths)
        else:
            print("no open method found")

    def run(self, files=[], dirs=[]):
        paths = []
        paths.extend(files)
        paths.extend(dirs)
        self.open_default(paths)

    def is_enabled(self, files=[], dirs=[]):
        return len(files) > 0 or len(dirs) > 0

    def is_visible(self, **kwargs):
        return self.have_open_method


class OpenDefaultForCurrentViewCommand(OpenDefaultCommand):
    @property
    def files_list(self):
        filename = self.window.active_view().file_name()
        return [filename] if filename is not None else []

    def run(self):
        OpenDefaultCommand.run(self, files=self.files_list)

    def is_enabled(self):
        return OpenDefaultCommand.is_enabled(self, files=self.files_list)

    def is_visible(self):
        return OpenDefaultCommand.is_visible(self, files=self.files_list)
