# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Demo Versions'
copyright = '2021, Graziella'
author = 'Graziella'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Extension configuration -------------------------------------------------

# add sourcecode to path
import sys, os
import logging
logging.basicConfig(level=logging.INFO)
sys.path.insert(0, os.path.abspath('../src'))

############################
# SETUP THE RTD LOWER-LEFT #
############################
try:
   html_context
except NameError:
   html_context = dict()
html_context['display_lower_left'] = True

templates_path = ['_templates']

if 'REPO_NAME' in os.environ:
   REPO_NAME = os.environ['REPO_NAME']
else:
   REPO_NAME = ''
 
# SET CURRENT_LANGUAGE
if 'current_language' in os.environ:
   # get the current_language env var set by buildDocs.sh
   current_language = os.environ['current_language']
else:
   # the user is probably doing `make html`
   # set this build's current language to english
   current_language = 'en'
 
# tell the theme which language to we're currently building
html_context['current_language'] = current_language

# SET CURRENT_VERSION
from git import Repo
from pprint import pprint
repo = Repo( search_parent_directories=True )
logging.info('----------');
logging.info(repo);
if 'current_version' in os.environ:
   # get the current_version env var set by buildDocs.sh
   current_version = os.environ['current_version']
   logging.info('--if---');
   logging.info(current_version);
else:
   # the user is probably doing `make html`
   # set this build's current version by looking at the branch
   #current_version = repo.active_branch.name   ISSUE HERE
   current_version = repo.head.object.hexsha
   logging.info('--else---');
   logging.info(current_version);
 
# tell the theme which version we're currently on ('current_version' affects
# the lower-left rtd menu and 'version' affects the logo-area version)
html_context['current_version'] = current_version
html_context['version'] = current_version
 
# POPULATE LINKS TO OTHER LANGUAGES
html_context['languages'] = [ ('en', '/' +REPO_NAME+ '/en/' +current_version+ '/') ]
logging.info('--REPO NAmE:---');
logging.info(REPO_NAME);
 
languages = [lang.name for lang in os.scandir('locales') if lang.is_dir()]
for lang in languages:
   html_context['languages'].append( (lang, '/' +REPO_NAME+ '/' +lang+ '/' +current_version+ '/') )
 
# POPULATE LINKS TO OTHER VERSIONS
html_context['versions'] = list()
 
versions = [branch.name for branch in repo.branches]
for version in versions:
   html_context['versions'].append( (version, '/' +REPO_NAME+ '/'  +current_language+ '/' +version+ '/') )
 
# POPULATE LINKS TO OTHER FORMATS/DOWNLOADS
 
# settings for creating PDF with rinoh
#rinoh_documents = [(
# master_doc,
# 'target',
# project+ ' Documentation',
# '© ' +copyright,
#)]
#today_fmt = "%B %d, %Y"
 
# settings for EPUB
#epub_basename = 'target'
 
html_context['downloads'] = list()
html_context['downloads'].append( ('pdf', '/' +REPO_NAME+ '/' +current_language+ '/' +current_version+ '/' +project+ '-docs_' +current_language+ '_' +current_version+ '.pdf') )
 
html_context['downloads'].append( ('epub', '/' +REPO_NAME+ '/' +current_language+ '/' +current_version+ '/' +project+ '-docs_' +current_language+ '_' +current_version+ '.epub') )
 
