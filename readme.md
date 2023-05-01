Open in Default Application
===========================
This package adds a command to the side bar menu, the tab context menu and the
command palette to open a file or directory in the system default application.

## System Notes
On *Linux*, `xdg-open` is used which most up-to-date desktop distributions
should provide. If you wish to use a different opening utility, this preference
can be overridden by creating `OpenDefault (Linux).sublime-settings` in your
`User` directory:

    {
        "open_command": "<your opening command>"
    }

On *Windows*, `os.startfile` is used which calls the proper Win32 shell
functions; on *Mac OS X*, the `open` utility is used.
