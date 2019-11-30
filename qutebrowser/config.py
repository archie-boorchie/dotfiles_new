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

# Bind keys to commands
config.bind('ch', 'history-clear')
config.bind('gh', 'home')
config.bind(';', 'set-cmd-text :')

# Bind keys to spawn commands
config.bind(',m', 'spawn mpv {url}')
config.bind(',f', 'spawn -u rss')

# Auto-save session
config.set('auto_save.session', True)

# Set spell to British English
config.set('spellcheck.languages', ["en-GB"])

# More search engine options
c.url.searchengines = {
    # duckduckgo (default)
    'DEFAULT': 'https://duckduckgo.com/?q={}',
    # duckduckgo
    'dd': 'https://duckduckgo.com/?q={}',
    # google search
    'gg': 'https://www.google.com/search?hl=en&q={}',
    # google translate (english to greek)
    'tr': 'https://translate.google.com/#en/el/{}',
    # arch wiki
    'aw': 'https://wiki.archlinux.org/index.php?title=Special%3ASearch&search={}',
    # inspire
    'in': 'http://inspirehep.net/search?ln=en&p={}&of=hb&action_search=Search&sf=earliestdate&so=d',
    # arxiv (paper id)
    'ar': 'https://arxiv.org/abs/{}',
    # arxiv (search)
    'ars': 'https://arxiv.org/search/?query={}&searchtype=all&source=header',
    # youtube
    'yt': 'https://youtube.com/search?q={}',
    # library genesis (standard)
    'lg': 'http://libgen.unblockall.org/search.php?req={}',
    # library genesis (scientific articles)
    'lgp': 'http://libgen.unblockall.org/scimag/?q={}',
    # library genesis (fiction)
    'lgf': 'http://libgen.unblockall.org/fiction/?q={}',
    # audiobook bay
    'ab': 'http://audiobookbay.nl/?s={}',
    # get comics
    'gc': 'https://getcomics.info/?s={}',
    # local files
    'lf': 'file://{}'
}
