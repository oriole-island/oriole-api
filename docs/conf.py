#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))
import oriole_test

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'oriole-test'
copyright = u"2018, ZhouXiaoxiang"
author = u"ZhouXiaoxiang"
version = oriole_test.__version__
release = oriole_test.__version__
language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'alabaster'
html_static_path = ['_static']
htmlhelp_basename = 'oriole_testdoc'
latex_elements = {
}
latex_documents = [
    (master_doc, 'oriole_test.tex',
     u'oriole-test Documentation',
     u'ZhouXiaoxiang', 'manual'),
]
man_pages = [
    (master_doc, 'oriole_test',
     u'oriole-test Documentation',
     [author], 1)
]
texinfo_documents = [
    (master_doc, 'oriole_test',
     u'oriole-test Documentation',
     author,
     'oriole_test',
     'One line description of project.',
     'Miscellaneous'),
]
