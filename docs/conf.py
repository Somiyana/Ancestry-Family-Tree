# -- Project information -----------------------------------------------------
project = 'Family Tree'
copyright = 'Family Tree'
author = 'Your Name'

# The full version, including alpha/beta/rc tags
release = '1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',  # For automatic documentation generation
    'sphinx.ext.napoleon',  # For Google-style docstrings
]

# The master toctree document.
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'  # Theme to use (you can change this to 'sphinx_rtd_theme' for Read the Docs theme)
html_static_path = ['_static']

# -- Add custom robots.txt -----------------------------------------
# Specify additional files to include, like robots.txt
html_extra_path = ['robots.txt']
