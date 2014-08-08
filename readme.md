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

## About
Copyright (c) 2014 Felix Krull \<f_krull@gmx.de\>  
All rights reserved.

    Redistribution and use in source and binary forms, with or without modification,
    are permitted provided that the following conditions are met:

    1) Redistributions of source code must retain the above copyright notice, this
       list of conditions and the following disclaimer.  
    2) Redistributions in binary form must reproduce the above copyright notice,
       this list of conditions and the following disclaimer in the documentation
       and/or other materials provided with the distribution.  
    3) The names of its contributors may not be used to endorse or promote products
       derived from this software without specific prior written permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
    ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
    WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES'(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
