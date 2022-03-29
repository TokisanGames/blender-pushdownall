# MIT License

# Copyright (c) 2021 Cory Petkovsek

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

bl_info = {
    "name": "Push Down All",
    "author": "Cory Petkovsek",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "Dope Sheet > Action Editor > Sidebar > Push Down All",
    "description": "Automatically 'Pushes Down' all matching animations to NLA tracks.",
    "warning": "",
    "doc_url": "https://github.com/tinmanjuggernaut/blender-pushdownall",
    "tracker_url": "https://github.com/tinmanjuggernaut/blender-pushdownall/issues",
    "category": "Animation",
}

import bpy

def register():
    from .PushDownAll import register as reg
    reg()

def unregister():
    from .PushDownAll import unregister as unreg
    unreg()
