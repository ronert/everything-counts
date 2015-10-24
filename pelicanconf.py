#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ronert Obst'
SITENAME = 'Everything Counts'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

STATIC_PATHS = ['images', 'notebooks', 'code', 'downloads', 'figures', 'pdfs']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ["plugins"]
PLUGINS = ['liquid_tags', 'render_math', "org_pandoc_reader"]

THEME = 'themes/pelican-octopress-theme'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Sharing
TWITTER_USER = 'ronert_obst'
TWITTER_TWEET_BUTTON = True
TWITTER_LATEST_TWEETS = True
TWITTER_FOLLOW_BUTTON = True
TWITTER_TWEET_COUNT = 5
TWITTER_SHOW_REPLIES = 'false'
TWITTER_SHOW_FOLLOWER_COUNT = 'true'

# RSS/Atom feeds
FEED_DOMAIN = SITEURL
FEED_ATOM = 'atom.xml'

# Search
SEARCH_BOX = True

# ORG
# ORG_READER_EMACS_LOCATION = '/Applications/Emacs.app/Contents/MacOS/Emacs'
# ORG_READER_EMACS_SETTINGS = '/Users/ronert/.emacs.d/init.el'
ORG_PANDOC_ARGS = ['--mathjax',
                   '--smart',
                   '--number-sections',
                   '--standalone',
                   '--highlight-style=espresso']
