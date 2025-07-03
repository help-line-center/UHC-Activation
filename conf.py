# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# Example:
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'UHC Card Activation Guide'
copyright = '2025, UnitedHealthcare'
author = 'UnitedHealthcare Support Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Main title shown in the browser and on pages
html_title = "How to Easily Activate Your UHC Card Online – Step-by-Step Help"

# Short title for navigation bar
html_short_title = "UHC Card Activation Guide"

# Theme (Uncomment and install if needed)
# html_theme = 'sphinx_rtd_theme'

# Hide "View page source" link
html_show_sourcelink = False

# Enable raw HTML blocks (important for custom buttons)
html_allow_unsafe = True
raw_enabled = True

# Theme customization
html_theme_options = {
    'show_powered_by': False,
}

Path to favicon (optional)
html_favicon = 'favicon.ico'

# Static and template directories
# Uncomment and place files accordingly
# html_static_path = ['_static']
templates_path = ['_templates']
