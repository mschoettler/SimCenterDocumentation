# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'TInF Tool'
copyright = 'SimCenter, University of California at Berkeley'
author = 'Jia-Wei Wan, Peter Mackenzie-Helnwein'

# The full version, including alpha/beta/rc tags
release = '0.2'

# simcenter additions
rst_prolog = """
.. |appName| replace:: Turbulence Inflow Tool
.. |app| replace:: Turbulence Inflow Tool
.. |githubLink| replace:: `Turbulance Inflow Tool Github page`_
.. _Turbulance Inflow Tool Github page: https://github.com/NHERI-SimCenter/TinF
.. |appLink| replace:: `Turbulance Inflow Tool`_
.. _Turbulance Inflow Tool page: https://github.com/NHERI-SimCenter/TurbulanceInflowTool
.. |messageBoard| replace:: `Message Board`_
.. _Message Board: https://simcenter-messageboard.designsafe-ci.org/smf/index.php?board=6.0
.. |toolVersion| replace:: '0.2'
"""

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.bibtex'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

#html_logo = 'figures/TinF-Logo-grey.png' #TODO: replace with EE-UQ logo!


html_theme_options = {
#    'analytics_id': 'UA-158130480-2',
    'logo_only': False,
    'prev_next_buttons_location': None,
#    'style_nav_header_background': '#F2F2F2'
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

numfig = True
#numfig_format = 'Figure %s'

math_number_all = True
math_eqref_format = '({number})'
math_numfig = True
