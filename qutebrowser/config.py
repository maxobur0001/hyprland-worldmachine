config.load_autoconfig()

c.auto_save.session = True
c.tabs.position = "top"


###### Completion colors ######

COLORS = {
    "purple": "#9564FD",
    "black": "#000000",
    "white": "#FEFEFE",
    "darkpurple": "#6442A5",
    "red": "#D5206A"
}

# Category
c.colors.completion.category.bg = "#9564FD"
c.colors.completion.category.fg = "#000000"
c.colors.completion.category.border.bottom = "#9564FD"
c.colors.completion.category.border.top = "#9564FD"

# Rows
c.colors.completion.even.bg = "#000000"
c.colors.completion.odd.bg = "#000000"
c.colors.completion.fg = "#9564FD"

# Selected
c.colors.completion.item.selected.bg = "#9564FD"
c.colors.completion.item.selected.fg = "#000000"
c.colors.completion.item.selected.border.bottom = "#9564FD"
c.colors.completion.item.selected.border.top = "#9564FD"

# Matched
c.colors.completion.item.selected.match.fg = "#FEFEFE"
c.colors.completion.match.fg = "#FEFEFE"

# Scrollbar
c.colors.completion.scrollbar.bg = "#000000"
c.colors.completion.scrollbar.fg = "#9564FD"


####### Context menu #######
c.colors.contextmenu.disabled.bg = "#000000"
c.colors.contextmenu.disabled.fg = "#6442A5"
c.colors.contextmenu.menu.bg = "#000000"
c.colors.contextmenu.menu.fg = "#9564FD"
c.colors.contextmenu.selected.bg = "#9564FD"
c.colors.contextmenu.selected.fg = "#000000"


####### Downloads #######
c.colors.downloads.bar.bg = "#000000"

c.colors.downloads.error.bg = "#6442A5"
c.colors.downloads.error.fg = "#000000"

c.colors.downloads.start.bg = "#9564FD"
c.colors.downloads.start.fg = "#000000"

c.colors.downloads.stop.bg = "#9564FD"
c.colors.downloads.stop.fg = "#000000"

c.colors.downloads.system.bg = "none"
c.colors.downloads.system.fg = "none"


###### Hints ######
c.colors.hints.bg = "#000000"
c.colors.hints.fg = "#9564FD"
c.colors.hints.match.fg = "#FEFEFE"

c.colors.keyhint.bg = "#000000"
c.colors.keyhint.fg = "#9564FD"
c.colors.keyhint.suffix.fg = "#FEFEFE"


###### Messages ######
c.colors.messages.error.bg = "#D5206A"
c.colors.messages.error.fg = "#000000"
c.colors.messages.error.border = "#D5206A"

c.colors.messages.warning.bg = "#FFDE81"
c.colors.messages.warning.fg = "#000000"
c.colors.messages.warning.border = "#FFDE81"

c.colors.messages.info.bg = "#000000"
c.colors.messages.info.fg = "#9564FD"
c.colors.messages.info.border = "#000000"



###### Prompts ######
c.colors.prompts.bg = "#000000"
c.colors.prompts.fg = "#9564FD"
c.colors.prompts.border = "#9564FD"
c.colors.prompts.selected.bg = "#9564FD"
c.colors.prompts.selected.fg = "#000000"
c.prompt.radius = 0


###### Caret ######
c.colors.statusbar.caret.bg = "#000000"
c.colors.statusbar.caret.fg = "#9564FD"
c.colors.statusbar.caret.selection.bg = "#9564FD"
c.colors.statusbar.caret.selection.fg = "#000000"


###### Command ######
c.colors.statusbar.command.bg = "#000000"
c.colors.statusbar.command.fg = "#9564FD"
c.colors.statusbar.command.private.bg = "#9564FD"
c.colors.statusbar.command.private.fg = "#000000"


###### Insert ######
c.colors.statusbar.insert.bg = "#000000"
c.colors.statusbar.insert.fg = "#9564FD"


###### Command ######
c.colors.statusbar.normal.bg = "#000000"
c.colors.statusbar.normal.fg = "#9564FD"
c.statusbar.show = "in-mode"


###### Passthrough ######
c.colors.statusbar.passthrough.bg = "#000000"
c.colors.statusbar.passthrough.fg = "#9564FD"


###### Private ######
c.colors.statusbar.private.bg = "#9564FD"
c.colors.statusbar.private.fg = "#000000"


###### URL ######
c.colors.statusbar.progress.bg = "#9564FD"
c.colors.statusbar.url.error.fg = "#D5206A"
c.colors.statusbar.url.fg = "#9564FD"
c.colors.statusbar.url.success.http.fg = "#63ED5E"
c.colors.statusbar.url.success.https.fg = "#63ED5E"
c.colors.statusbar.url.hover.fg = "#7A71EB"
c.colors.statusbar.url.warn.fg = "#FFDE81"


###### Tabs ######

# Tabs
c.colors.tabs.bar.bg = "#000000"
c.colors.tabs.even.bg = "#000000"
c.colors.tabs.even.fg = "#9564FD"
c.colors.tabs.odd.bg = "#000000"
c.colors.tabs.odd.fg = "#9564FD"
c.colors.tabs.selected.even.bg = "#9564FD"
c.colors.tabs.selected.even.fg = "#000000"
c.colors.tabs.selected.odd.bg = "#9564FD"
c.colors.tabs.selected.odd.fg = "#000000"
c.tabs.title.format = "{current_title}" 
c.tabs.show = "multiple"

# Indicator
c.colors.tabs.indicator.error = "#D5206A"
c.colors.tabs.indicator.start = "#63ED5E"
c.colors.tabs.indicator.stop = "#63ED5E"
c.colors.tabs.indicator.system = "none"
c.tabs.indicator.width = 0

# Pinned
c.colors.tabs.pinned.even.bg = "#6442A5"
c.colors.tabs.pinned.even.fg = "#000000"
c.colors.tabs.pinned.odd.bg = "#6442A5"
c.colors.tabs.pinned.odd.fg = "#000000"
c.colors.tabs.pinned.selected.even.bg = "#9564FD"
c.colors.tabs.pinned.selected.even.fg = "#000000"
c.colors.tabs.pinned.selected.odd.bg = "#9564FD"
c.colors.tabs.pinned.selected.odd.fg = "#000000"


###### Tooltip ######
c.colors.tooltip.bg = "#000000"
c.colors.tooltip.fg = "#9564FD"

###### Webpage ######
c.colors.webpage.bg = "#000000"
c.colors.webpage.darkmode.enabled = True


###### Fonts ######
c.fonts.prompts = "20px Terminess Nerd Font Mono"
c.fonts.default_family = "Terminess Nerd Font Mono"
c.fonts.default_size = "20px"


###### Bind ######
config.bind('pi', 'spawn xdotool key space ;; spawn ~/.config/qutebrowser/picinpic.sh {url}')
