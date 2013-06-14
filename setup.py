#!/usr/bin/env python

from setuptools import setup

packages = [
    'pelicanext',
    'pelicanext.assets',
    'pelicanext.code_include',
    'pelicanext.disqus_static',
    'pelicanext.extract_toc',
    'pelicanext.github_activity',
    'pelicanext.global_license',
    'pelicanext.goodreads_activity',
    'pelicanext.gravatar',
    'pelicanext.gzip_cache',
    'pelicanext.html_rst_directive',
    'pelicanext.ical',
    'pelicanext.latex',
    'pelicanext.multi_part',
    'pelicanext.neighbors',
    'pelicanext.optimize_images',
    'pelicanext.random_article',
    'pelicanext.related_posts',
    'pelicanext.sitemap',
    'pelicanext.summary',
    'pelicanext.w3c_validate',
]

setup(name='pelicanext',
    version='0.1',
    package_dir={'pelicanext': '.'},
    packages=packages,
)
