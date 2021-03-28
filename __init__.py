#Custom Bold Color Shortcut
#Based on Quick Colour Changing (https://ankiweb.net/shared/info/2491935955)
#Added Bold function on top of changing the colour

from aqt import mw
from aqt import gui_hooks
from functools import partial

config = mw.addonManager.getConfig(__name__)
bold_config = config['bold']

def updateColour(editor, colour):
    if bold_config == "on":
        editor.toggleBold()
    editor.fcolour = colour
    editor.onColourChanged()
    editor._wrapWithColour(editor.fcolour)



def onSetupShortcuts(cuts, editor):
    for color_code, keyboard_shortcut in config['keys']:
        def append_function(hex_code):
            return updateColour(editor, hex_code)
        append_this = partial(append_function,color_code)
        cuts.append((keyboard_shortcut,append_this))

gui_hooks.editor_did_init_shortcuts.append(onSetupShortcuts)
