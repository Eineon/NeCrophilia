# Configuration file for the Sphinx documentation builder.

# -- Project information

project = '死灵年代记：幻日咏叹调'
copyright = '2024, ネオン様'
author = 'Eineon'

release = '错位的开幕曲'
version = 'v1.0'

# These are options specifically for the Wagtail Theme.
html_theme_options = dict(
    project_name = "幻日咏叹调 ~错位的开幕曲~",
    logo = "logo.svg",
    logo_alt = "回到首页",
    logo_height = 64,
    logo_width = 64,
    github_url = "https://github.com/Eineon/NeCrophilia/tree/main/docs/source/",
)

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_markdown_tables',
    'sphinx_wagtail_theme',
    'recommonmark',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
# -- Options for HTML output
html_theme = 'sphinx_wagtail_theme'
# 这组 Sphinx 文档的名称。
html_title = "死灵年代记：幻日咏叹调 ~错位的开幕曲~"
# 导航栏的较短标题。
html_short_title = "幻日咏叹调"

html_static_path = ["_necro"]
html_css_files = ["necro-style.css"]

html_last_updated_fmt = "%Y/%m/%d"

# -- Options for HTMLHelp output
htmlhelp_basename = '死灵年代记：幻日咏叹调 ~错位的开幕曲~'

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