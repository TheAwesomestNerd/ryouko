#! /usr/bin/env python

# This file is released under the terms of the following MIT license:

## START OF LICENSE ##
"""
Copyright (c) 2012 Daniel Sim
Portions of the code are copyright (c) 2011 roberto.alsina

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
## END OF LICENSE ##

import os, sys

try:
    filename = __file__
except:
    __file__ = sys.executable
else:
    del filename
app_lib = os.path.join(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(app_lib)

if sys.version_info[0] >= 3:
    def unicode(data):
        return str(data)
    def unichr(data):
        return chr(data)
    from html.entities import name2codepoint
    from html.parser import HTMLParser
else:
    import HTMLParser
    from htmlentitydefs import name2codepoint

import re

try: from urllib.parse import unquote, quote
except ImportError:
    try: from urllib import unquote, quote
    except:
        pass

from xml.sax.saxutils import escape, quoteattr

try: from urllib.request import urlopen
except ImportError:
    try: from urllib2 import urlopen
    except:
        pass

_entity_re = re.compile(r'&(?:(#)(\d+)|([^;]+));')

def getMimeType(filename):
    return get_mimetype(filename)

def get_mimetype(filename):
    try: f = urlopen("file://" + metaunquote(filename).replace("file://",""))
    except:
        print("Error! Something went wrong!")
        return None
    else:
        return f.headers['content-type']

def ryouko_file(fname):
    return os.path.join(app_lib, fname)

def read_file(fname):
    f = open(fname)
    t = f.read()
    f.close()
    return t

def shred_directory(directory):
    if os.path.isdir(directory):
        d = os.listdir(directory)
        for f in d:
            fname = os.path.join(directory, f)
            if sys.platform.startswith("linux") and not os.path.isdir(fname):
                os.system("shred -v \"" + fname + "\"")
            try: os.remove(fname)
            except:
                pass

def _repl_func(match):
    if match.group(1): # Numeric character reference
        return unichr(int(match.group(2)))
    else:
        return unichr(name2codepoint[match.group(3)])

def handle_html_entities(data):
    return unescape(_entity_re.sub(_repl_func, data))
    
def metaunquote(data):
    return handle_html_entities(unquote(data))

def unescape(text):
   """Removes HTML or XML character references 
      and entities from a text string.
      keep &amp;, &gt;, &lt; in the source code.
   from Fredrik Lundh
   http://effbot.org/zone/re-sub.htm#unescape-html
   """
   def fixup(m):
      text = m.group(0)
      if text[:2] == "&#":
         # character reference
         try:
            if text[:3] == "&#x":
               return unichr(int(text[3:-1], 16))
            else:
               return unichr(int(text[2:-1]))
         except ValueError:
            print("Value error!")
            pass
      else:
         # named entity
         try:
            if text[1:-1] == "amp":
               text = "&amp;amp;"
            elif text[1:-1] == "gt":
               text = "&amp;gt;"
            elif text[1:-1] == "lt":
               text = "&amp;lt;"
            else:
               print(text[1:-1])
               text = unichr(name2codepoint[text[1:-1]])
         except KeyError:
            print("Key error!")
            pass
      return text # leave as is
   return re.sub("&#?\w+;", fixup, text)

def match_url(url, match):
    for urlc in match:
        if not urlc in url:
            return False
    return True
