import os;
import subprocess;
from qutebrowser.api import interceptor;
config.set("colors.webpage.darkmode.enabled", True);

# Load existing settings made via :set
config.load_autoconfig()

config.bind('xm'  , 'spawn mpv {url}')
config.bind('xM'  , 'hint links spawn mpv {hint-url}')

config.bind('xhta', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/apprentice/apprentice-all-sites.css ""')
config.bind('xhtd', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/darculized/darculized-all-sites.css ""')
config.bind('xhtg', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/gruvbox/gruvbox-all-sites.css ""')
config.bind('xhtsd', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/solarized-dark/solarized-dark-all-sites.css ""')
config.bind('xhtsl', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/solarized-light/solarized-light-all-sites.css ""')
config.bind('xhtt', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/tokyo-night/tn.css ""')

config.source('tokyo-night.py')
# config.source('qutewal.py')


config.set('content.javascript.enabled', True, 'chrome-devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome://*/*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'qute://*/*')

# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only xall` and `never` are
# supported as per-domain values. Setting xno-3rdparty` or `no-
# unknown-3rdpartyx per-domain on QtWebKit will have the same effect as
# xall`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set('content.cookies.accept', 'all', 'chrome-devtools://*')

# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only xall` and `never` are
# supported as per-domain values. Setting xno-3rdparty` or `no-
# unknown-3rdpartyx per-domain on QtWebKit will have the same effect as
# xall`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set('content.cookies.accept', 'all', 'devtools://*')

# User agent to send.  The following placeholders are defined:  *
# x{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * x{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * x{qt_version}`: The underlying Qt version. *
# x{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * x{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * x.config/qutebrowser_version}`: The currently
# running.config/qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')

# User agent to send.  The following placeholders are defined:  *
# x{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * x{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * x{qt_version}`: The underlying Qt version. *
# x{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * x{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * x.config/qutebrowser_version}`: The currently
# running.config/qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version} Edg/{upstream_browser_version}', 'https://accounts.google.com/*')

# User agent to send.  The following placeholders are defined:  *
# x{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * x{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * x{qt_version}`: The underlying Qt version. *
# x{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * x{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * x.config/qutebrowser_version}`: The currently
# running.config/qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'chrome-devtools://*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool


# Allow websites to show notifications.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask

config.bind("xly", "hint links spawn alacritty -e lynx {hint-url}")

config.bind("xxt", "config-cycle tabs.show always switching")
config.bind("xxx", "config-cycle statusbar.show always never;; config-cycle tabs.show always switching")
config.bind("xxb", "config-cycle statusbar.show always never")
config.bind("xjn", "set content.javascript.enabled false ;; reload")
config.bind("xjy", "set content.javascript.enabled true ;; reload")

config.bind("xst", "set statusbar.position top")
config.bind("xsb", "set statusbar.position bottom")

config.bind("xtt", "set tabs.position top")
config.bind("xtl", "set tabs.position left")
config.bind("xtr", "set tabs.position right")
config.bind("xtb", "set tabs.position bottom")

c.url.default_page = "file:home/abissal/.config/qutebrowser/startpage.html"
c.url.start_pages = ['file:home/abissal/.config/qutebrowser/startpage.html']

c.url.searchengines = {
    # 'DEFAULT': 'https://search.brave.com/search?q={}&source=web',
    'DEFAULT': 'https://www.google.com/search?q={}',
    'b': 'https://search.brave.com/search?q={}&source=web',
    'aw': 'https://wiki.archlinux.org/index.php?search={}&title=Special%3ASearch&wprov=acrw1', 
    'au': 'https://aur.archlinux.org/packages?O=0&K={}',
    'ap': 'https://archlinux.org/packages/?sort=&q={}&maintainer=&flagged=',
    'd': 'https://duckduckgo.com/?q={}',
    'g': 'https://www.google.com/search?q={}',
    'rs': 'https://docs.rs/releases/search?query={}',
    're': 'https://www.reddit.com/r/{}',
    'ub': 'https://www.urbandictionary.com/define.php?term={}',
    'w': 'https://en.wikipedia.org/wiki/{}',
    'y': 'https://www.youtube.com/results?search_query={}',
    'gh': 'https://github.com/search?q=user%3ARaghav-Dixit+{}',
    'gl': 'https://gitlab.com/search?group_id=&nav_source=navbar&project_id=&repository_ref=&search={}&snippets=false'
}

c.fonts.statusbar = '11pt "JetBrainsMono NF"'
c.fonts.debug_console = '11pt "JetBrainsMono NF"'
c.fonts.completion.entry = '11pt "JetBrainsMono NF"'
c.fonts.default_family = '11pt "JetBrainsMono NF"'

  #############
 ## Adblock ##
#############

c.content.blocking.method = 'auto'
c.content.blocking.adblock.lists = [
        "https://easylist.to/easylist/easylist.txt",
        "https://easylist.to/easylist/easyprivacy.txt",
        "https://easylist.to/easylist/fanboy-social.txt",
        "https://secure.fanboy.co.nz/fanboy-annoyance.txt",
        "https://easylist-downloads.adblockplus.org/abp-filters-anti-cv.txt",
        # "https://pgl.yoyo.org/adservers/serverlist.php?showintro=0;hostformat=hosts",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/legacy.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2020.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2021.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/badware.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/privacy.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/badlists.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/annoyances.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/resource-abuse.txt",
        "https://www.i-dont-care-about-cookies.eu/abp/",
        "https://secure.fanboy.co.nz/fanboy-cookiemonster.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/unbreak.txt"
]

config.bind("xb", "adblock-update")

config.bind('xM', 'hint links spawn mpv {hint-url}')
config.bind("xr", "config-source")
config.bind("xt", "set-cmd-text -s :tab-select")
