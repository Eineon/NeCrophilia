# Configuration file for the Sphinx documentation builder.

# -- Project information

master_doc = 'index'
project = '嵌合创生论'
copyright = '2024, ネオン様'
author = 'Eineon'

release = '1st Ddition'
version = 'v1.0'

# These are options specifically for the Wagtail Theme.
html_theme_options = dict(
    project_name = "嵌合创生论 -The misplaced overture-",
    github_url = "https://github.com/Eineon/NeCrophilia/tree/main/docs/source/"
)

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'recommonmark',
    'sphinx_markdown_tables',
    'sphinx_wagtail_theme',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
html_theme = 'sphinx_wagtail_theme'
html_last_updated_fmt = "%Y/%m/%d"
html_static_path = ["_necro"]
html_css_files = ["necro-style.css"]

# -- Options for HTMLHelp output
htmlhelp_basename = '嵌合创生论'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Options for PDF output
latex_engine = 'xelatex'
latex_use_xindy = False
latex_elements = {
    'preamble': '\\usepackage[UTF8]{ctex}\n',
}

source_parsers = {
    '.md': 'recommonmark.parser.CommonMarkParser',
}

source_suffix = ['.rst', '.md']