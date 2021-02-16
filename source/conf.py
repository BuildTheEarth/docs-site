# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import recommonmark
from recommonmark.transform import AutoStructify


'''PROJECT INFORMATION'''
project = 'Build The Earth: Guide'
author = 'BTE Contributors'
copyright = '2021, BTE Contributors'

release = '2.0.0'
## The full version, including alpha/beta/rc tags


'''GENERAL CONFIGURATION'''

#source_parsers = {
#    '.md': 'recommonmark.parser.CommonMarkParser',
#}
#source_suffix = ['.rst', '.md']
# Source config

templates_path = ['_templates']
## Add any paths that contain templates here, relative to this directory.

exclude_patterns = []
## List of patterns, relative to source directory, that match files and directories to ignore when looking for source files.
## This pattern also affects html_static_path and html_extra_path.


'''INTERNATIONALIZATION OPTIONS'''
language = 'en'

#locale_dirs = ['locale/']   # path is example but recommended.
#gettext_compact = False     # optional.
## Deprecated due to custom language handling.


'''HTML OUTPUT OPTIONS'''
html_theme = 'sphinx_rtd_theme'
## The theme to use for HTML and HTML Help pages. See the documentation for a list of builtin themes.


html_static_path = ['_static']
## Add any paths that contain custom static files (such as style sheets) here, relative to this directory.
## They are copied after the builtin static files, so a file named "default.css" will overwrite the built-in "default.css".

html_css_files = [
    'css/textstyles.css'
]

html_favicon = '_static/img/BTELogo.gif'
html_title = "Build The Earth Guide"
html_short_title = "BTEGuide"
html_last_updated_fmt = ""


'''rST BUILD OPTIONS'''

rst_prolog = """
.. include:: .textstyles.rst
"""
## rST Header include.


keep_warnings = True
suppress_warnings = [
    'ref.ref'
]


extensions = [
    'recommonmark',
    'sphinx.ext.todo',
    'sphinx.ext.extlinks',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.duration',
    'sphinx_markdown_tables'
]
## Add any Sphinx extension module names here, as strings. They can be extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.

todo_include_todos = True
extlinks = {
    'bte': ('https://buildtheearth.net/%s', 'Website ')
}
autosectionlabel_prefix_document = True
## Extension Options.

github_doc_root = 'https://github.com/rtfd/recommonmark/tree/master/doc/'
def setup(app):
    app.add_config_value('recommonmark_config', {
            'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)