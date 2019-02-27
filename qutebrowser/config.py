# Autogenerated config.py
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Uncomment this to still load settings configured via autoconfig.yml
config.load_autoconfig()

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'file://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome://*/*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'qute://*/*')

# More search engine options
c.url.searchengines = {
    # duckduckgo (default)
    'DEFAULT': 'https://duckduckgo.com/?q={}',
    # arch wiki
    'aw': 'https://wiki.archlinux.org/index.php?title=Special%3ASearch&search={}',
    # arxiv (paper id)
    'ar': 'https://arxiv.org/abs/{}',
    # arxiv (search)
    'ars': 'https://arxiv.org/search/?query={}&searchtype=all&source=header',
    # youtube
    'yt': 'https://youtube.com/search?q={}',
    # library genesis (standard)
    'lg': 'http://libgen.io/search.php?req={}',
    # library genesis (scientific articles)
    'lgp': 'http://libgen.io/scimag/index.php?s={}',
    # library genesis (fiction)
    'lgf': 'http://libgen.io/foreignfiction/index.php?s={}',
    # google search
    'gg': 'https://www.google.com/search?hl=en&q={}',
    # google translate (english to greek)
    'tr': 'https://translate.google.com/#en/el/{}',
    # local files
    'lf': 'file://{}'
}
