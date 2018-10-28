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
    'arxiv': 'https://arxiv.org/search/?query={}&searchtype=all&source=header',
    # youtube
    'yt': 'https://youtube.com/search?q={}',
    # library genesis (standard)
    'libgen': 'http://libgen.io/search.php?req={}',
    'lg': 'http://libgen.io/search.php?req={}',
    # library genesis (articles)
    'lgp': 'http://libgen.io/scimag/index.php?s={}'
}
