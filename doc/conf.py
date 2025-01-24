# -*- coding: utf-8 -*-
#
# py_trees documentation build configuration file, created by
# sphinx-quickstart on Thu Jul 30 16:43:58 2015.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

##############################################################################
# Imports
##############################################################################

import os
import sphinx_rtd_theme
import sys
import unittest.mock

##############################################################################
# Paths
##############################################################################

project_dir = os.path.abspath(
    os.path.join(
        os.path.abspath(__file__), os.pardir, os.pardir
    )
)

sys.path.insert(0, project_dir)

##############################################################################
# Project Information
##############################################################################

# General information about the project.
project = u'py_trees_ros_tutorials'
copyright = u'2020, Daniel Stonier'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = "2.1"
# The full version, including alpha/beta/rc tags.
release = "2.1.0"

##############################################################################
# Regular Sphinx Configuration
##############################################################################

# -- General Configuration ------------------------------------------------

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['.build', 'weblinks.rst']

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'py_trees': ('https://py-trees.readthedocs.io/en/release-2.2.x', None),
    'py_trees_ros': ('https://py-trees-ros.readthedocs.io/en/release-2.1.x', None),
    'rclpy': ('http://docs.ros2.org/foxy/api/rclpy/', None),
}

# -- Options for HTML output ----------------------------------------------

html_theme = 'sphinx_rtd_theme'

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True
html_show_sphinx = False

# Output file base name for HTML help builder.
htmlhelp_basename = 'py_trees_ros_tutorials_doc'

# -- Options for LaTeX output ---------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'py_trees_ros_tutorials.tex', u'py\\_trees\\_ros\\_tutorials Documentation',
   u'Daniel Stonier', 'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'py_trees_ros_tutorials', u'py_trees_ros_tutorials Documentation',
     [u'Daniel Stonier'], 1)
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'py_trees_ros_tutorials', u'py_trees_ros_tutorials Documentation',
   u'Daniel Stonier', 'py_trees', 'One line description of project.',
   'Miscellaneous'),
]

##############################################################################
# Extensions & Extension Configuration
##############################################################################

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.graphviz',
    'sphinx.ext.ifconfig',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinxarg.ext',
    # this plays nicely with mock
    'sphinx_autodoc_typehints',
    # an alternative
    # 'sphinx_autodoc_annotation',
]

# True to use the :ivar: role for instance variables.
# False to use the .. attribute:: directive instead.
napoleon_use_ivar = True

# Might need this to have napolean and sphinx_autodoc_typehints to play nicely
#   https://github.com/agronholm/sphinx-autodoc-typehints/issues/15#issuecomment-403540299
# napolean_use_param = True

# If you don't add this, todos don't appear
todo_include_todos = True

##############################################################################
# Autodoc Mocks
##############################################################################


# Caveats: Currently autodoc is failing on classes which
# inherit from a mocked class. I don't know if this is a bug
# in sphinx, or something I'm not implementing correctly.

# Workaround: I only inherit from py_trees, so make sure that
# is in the environment and not mocked.


MOCK_MODULES = [
    'action_msgs', 'action_msgs.msg',
    'geometry_msgs', 'geometry_msgs.msg',
    'launch', 'launch_ros', 'launch_ros.actions',
    # https://github.com/splintered-reality/py_trees_ros_tutorials/issues/18#issuecomment-487982404
    # 'PyQt5', 'PyQt5.QtCore', 'PyQt5.QtWidgets',
    'py_trees_ros', 'py_trees_ros.exceptions', 'py_trees_ros.mock',
    'py_trees_ros.mock.actions',
    'py_trees_ros_interfaces', 'py_trees_ros_interfaces.action',
    'py_trees_ros_interfaces.msg', 'py_trees_ros_interfaces.srv',
    'rcl_interfaces', 'rcl_interfaces.msg', 'rcl_interfaces.srv',
    'rclpy', 'rclpy.action', 'rclpy.callback_groups', 'rclpy.executors',
    'rclpy.expand_topic_name', 'rclpy.node', 'rclpy.parameter',
    'rclpy.qos', 'rclpy.time',
    'ros2topic', 'ros2topic.api',
    'sensor_msgs', 'sensor_msgs.msg',
    'std_msgs', 'std_msgs.msg',
    'unique_identifier_msgs', 'unique_identifier_msgs.msg'
]

# Has some caveats, see
#    https://github.com/splintered-reality/py_trees_ros_tutorials/issues/18#issuecomment-487975890
autodoc_mock_imports = MOCK_MODULES

##############################################################################
# Default Sphinx
##############################################################################

# Add any paths that contain templates here, relative to this directory.
templates_path = ['.templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['.static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
}

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False