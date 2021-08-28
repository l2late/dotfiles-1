from libqtile.config import EzClick as Click, EzDrag as Drag
from libqtile.config import EzKey as Key
from libqtile.command import lazy
from libqtile.config import Group, Match, Screen
from libqtile import layout, bar, widget, qtile
import os
import subprocess
from libqtile import hook

@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

#---COLORS---#
bg = '#282828'
bg_2= '#1d2021'
red = '#cc241d'
green = '#98971a'
yellow = 'd79921'
blue = '#458588'
purple = '#b16286'
aqua = '#689d6a'
orange = '#d65d0e'
white = '#fbf1c7'
gray = '#a89984'
dark_gray = '#665c54'


modifier_keys = {
   'M': 'mod4',
   'A': 'mod1',
   'S': 'shift',
   'C': 'control',
   'T': 'Tab',
}

keys = [

#----------SETTINGS FROM QTILE-----------#

        Key('M-C-r',lazy.restart()),
        Key('M-C-q',lazy.shutdown()),

#-----------------APPS-------------------#

        Key('M-q',lazy.window.kill()),
        Key('M-a',lazy.spawn("alacritty")),
        Key('M-f',lazy.spawn("firefox")),
        Key('M-r',lazy.spawn("alacritty -e ranger")),

#-----------------MENU-------------------#

        Key('M-e',lazy.spawn("rofi -show drun")),

#--------------SCREENSHOT----------------#

        Key('M-s',lazy.spawn("flameshot gui")),

#-------SWITCH FOCUS BETWEEN WDOWS IN A LAYER-------#

        Key('M-h',lazy.layout.left()),
        Key('M-l',lazy.layout.right()),
        Key('M-j',lazy.layout.down()),
        Key('M-k',lazy.layout.up()),

#---------CHANGE WINDOWS POSITION IN A CURRENT STACK-------#  

        Key('M-C-h', lazy.layout.swap_left()),
        Key('M-C-l', lazy.layout.swap_right()),
        Key('M-C-j', lazy.layout.shuffle_down()),
        Key('M-C-k', lazy.layout.shuffle_up()),

#----------CHANGE SIZE OF WINDOW FOCUSED------------#

        Key('M-S-h',lazy.layout.grow_left()),
        Key('M-S-l',lazy.layout.grow_right()),
        Key('M-S-j',lazy.layout.grow_down()),
        Key('M-S-k',lazy.layout.grow_up()),
        Key('M-S-n',lazy.layout.normalize()),

#------------------CHANGE LAYOUT--------------------#

        Key('M-p',lazy.next_layout()),
]


groups = [Group(i) for i in [
    "  ", "  ", "  ", "  ", " ", " ", " ", " ", " ",
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        Key('M-' + actual_key, lazy.group[group.name].toscreen()),
        Key('M-S-' + actual_key, lazy.window.togroup(group.name)),
])


layout_constants = {
    'border_focus': yellow,
    'border_on_single': yellow,
    'border_normal': bg,
    'border_focus_stack': yellow,
    'margin': 30,
    'margin_on_single': 30
}


layouts = [
    layout.Columns(**layout_constants),
    layout.Max(**layout_constants),
#    layout.Stack(**layout_constants),
    layout.MonadTall(**layout_constants),
]

floating_layout = layout.Floating(
    **layout_constants,
    border_width = 2
)

mouse= [
    Drag("M-1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag("M-3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
    Click("M-2", lazy.window.bring_to_front())
]


powerline_left = lambda : widget.TextBox(
    foreground= bg_2,
    background= bg,
    font="Space Mono Nerd Font",
    fontsize=18,
    text="",
    padding= -1
)

powerline_right = lambda : widget.TextBox(
    foreground= bg_2,
    background= bg,
    font="Space Mono Nerd Font",
    fontsize=18,
    text="",
    padding= -1
)
separate = lambda : widget.Sep(
    linewidth=0,
    padding=10,
    size_percent=50,
)

widget_constants = {
    'font': 'Space Mono Nerd Font',
    'fontsize': 18,
    'background': bg_2
}

screens = [
    Screen(
        top=bar.Bar([

            widget.GroupBox(
                padding = 0,
                fontsize = 25,
                active = white,
                this_current_screen_border = yellow
            ),

            separate(),

            powerline_left(),
            widget.Notify(
                **widget_constants,
                audiofile = '~/.config/qtile/notification.mp3'
            ),
            powerline_right(),

            widget.Spacer(),

            separate(),

            powerline_left(),
            widget.Net(
                **widget_constants,
                foreground = yellow,
                format = '直 {down} ↓↑ {up}'
            ),
            powerline_right(),

            separate(),

            powerline_left(),
            widget.CPU(
                **widget_constants,
                foreground = green,
                format = ' {freq_current}GHz  {load_percent}%',
                mouse_callbacks = {'Button1':lambda: qtile.cmd_spawn("alacritty -e gotop")},
            ),
            powerline_right(),

            separate(),

            powerline_left(),
            widget.Memory(
                **widget_constants,
                format="{MemPercent: .0f}%",
                foreground = blue,
                mouse_callbacks = {"Button1":lambda:qtile.cmd_spawn("alacritty -e gotop")},
            ),
            powerline_right(),

            separate(),

            powerline_left(),
            widget.TextBox(
                **widget_constants,
                text = '墳 ',
                foreground = purple,
                mouse_callbacks = {
                    'Button1': lambda: qtile.cmd_spawn("amixer sset Master toggle"),
                    'Button4': lambda: qtile.cmd_spawn("amixer -D pulse sset Master 2+"),
                    'Button5': lambda: qtile.cmd_spawn("amixer -D pulse sset Master 2%-"),
                },
            ),
            widget.PulseVolume(
                **widget_constants,
                foreground = purple,
            ),
            powerline_right(),

            separate(),

            powerline_left(),
            widget.Clock(
                **widget_constants,
                foreground=white,
                mouse_callbacks={"Button1":lambda : qtile.cmd_spawn("alacritty --hold -e khal calendar ")},
            ),
            powerline_right(),

            separate(),
            ],26, background = "#282828"),
)]

cursor_warp = False
follow_mouse_focus = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_fullscreen = True
auto_minimize = True
wmname = "LG3B"

