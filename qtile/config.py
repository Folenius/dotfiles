# Qtile configuration and shortcuts file
# Hato Folenius Schmidt Martinetsu
# General Director of the World Liberation Insurgency





#    [---------------Libs imports goes here---------------]



from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown 
from libqtile.lazy import lazy
from libqtile import hook
from libqtile import qtile
from colors import catpuccin
import screens





#    [-------------Variables and stuff go here-------------]


#Default this keys to be easier to setup new key bindings
mod = "mod4"
alt = "mod1"
control = "control"


terminal = "kitty" # Change terminal emulator here.
browser = "librewolf"
private_window_browser = " librewolf --private-window"
sec_browser = "floorp"
sec_prv_win_browser = "floorp --private-window"
file_manager = "thunar"
home_dir = "/home/Folenius/"





#    [-------------Rest of the code goes here--------------]



# Here goes the command that executes when the pc is booted

@hook.subscribe.startup_once
def autostart():
    qtile.cmd_spawn("bash {}.config/qtile/autostart.sh".format(home_dir))



# Here is the list of all key combinations, the formula is the next:
# Key([*Special key*, *Second special key, this one is opcional*], "*Key*", lazy.*action*, desc="*Description, this one is optional*"), <<<<---VERY IMPORTANT, PUT THE FRICKING COMMA!!!---

keys = [
    # [---------------Switch between windows---------------]


    Key([mod], "h", lazy.layout.left(),
        desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(),
        desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(),
        desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(),
        desc="Move focus up"),
    Key([alt], "Tab", lazy.layout.next(),
        desc="Move window focus to other window"),


    # [--------------------Move windows--------------------]


    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(),
        desc="Move window up"),


    # [--------------------Grow windows--------------------]


    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(),
        desc="Grow window up"),
    Key([mod, alt], "k", lazy.layout.normalize(),
        desc="Reset all window sizes"),
    Key([mod, alt], "m", lazy.window.toggle_minimize(),
        desc="Toggle minimize"),
    Key([mod, "control"], "m", lazy.window.toggle_maximize(),
        desc="Toggle maximize"),


    #[---Toggle between split and unsplit sides of stack---]


    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal),
        desc="Launch terminal"),


    # [--Toggle between different layouts as defined below--]


    Key([mod], "Tab", lazy.next_layout(),
        desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(),
        desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "z", lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window"),


    # [--------------Qtile control keybindings--------------]


    Key([mod, "control"], "r", lazy.reload_config(),
        desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(),
        desc="Shutdown Qtile"),


    # [------------------App spawn commands-----------------]


    Key([mod], "r", lazy.spawn("rofi -show drun"),
        desc = "Spawn Rofi's drun menu"),
    Key([mod], "q", lazy.spawn("rofi -show")),
    Key([mod], "b", lazy.spawn(browser)),
    Key([mod, "shift"], "b", lazy.spawn(private_window_browser),
        desc = "Open the browser on aprivate window."),
    Key([mod, "control"], "b", lazy.spawn(sec_browser)),
    Key([mod, "control", "shift"], "b", lazy.spawn(sec_prv_win_browser)),
    Key([mod], "f", lazy.spawn(file_manager)),
    Key([mod], "d", lazy.spawn("discord")),
    Key([mod], "c", lazy.spawn("code")),


    # [-------------------Extra Shortcuts-------------------]'

    
    Key([mod, alt], "s", lazy.spawn("scrot"),
        desc="Take a screenshot."),

    # Use this section to define multiple keyboard layouts
    Key([mod, control],  'Return', lazy.spawn('setxkbmap us')),
    Key([mod, control, alt],  'Return', lazy.spawn('setxkbmap -layout latam,es')),  


    # [---------------------ScratchPads---------------------]


    Key([mod], "space", lazy.group["scratchpad"].dropdown_toggle("term")),
    Key([control], "1", lazy.group["scratchpad"].dropdown_toggle("mixer_pulse")), 
    Key([control], "2", lazy.group["scratchpad"].dropdown_toggle("file")),
    Key([control], "0", lazy.group["scratchpad"].dropdown_toggle("nvidia-config")),
    Key([control], "space", lazy.group["scratchpad"].dropdown_toggle("config"))
]



# All related to groups, scratchpads, etc goes here


# Here the iconns of the groups.
groups = [Group(i) for i in ["󰈹", "", "󰝚", "", "", "", "", "", ""]]

#Uncomment this line if you would like your groups to be like this instead of an icon
#groups = [Group(i) for i in ["www", "dev", "cmd", "vid", "mus", "file", "gfx", "chat", "doc"]]

group_hotkeys = "123456789" # Hotkeys to switch between groups.

for g, k in zip(groups, group_hotkeys):
    keys.extend(
        [
            Key(
                [mod],
                k,
                lazy.group[g.name].toscreen(),
                desc=f"Switch to group {g.name}",
            ),
            Key(
                [mod, "shift"],
                k,
                lazy.window.togroup(g.name, switch_group=True),
                desc=f"Switch to & move focused window to group {g.name}",
            ),
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )


# Here there is the Scratchpads definition, you may add as much as you want to.

groups.append(
        ScratchPad("scratchpad", [
            DropDown("term", terminal, opacity=1, x=0.25, y=0.15, height=0.6, width=0.5, on_focus_lost_hide=False),
            DropDown("mixer_pulse", "kitty -e pulsemixer", opacity=1, x=0.11, y=0.2, height=0.5, width=0.8, on_focus_lost_hide=False),
            DropDown("nvidia-config", "nvidia-settings", opacity=1, x=0.25, y=0.2, height=0.5, width=0.5, on_focus_lost_hide=False),
            DropDown("file", "kitty -e ranger", opacity=1, x=0.2, y=0.2, height=0.5, width=0.6, on_focus_lost_hide=False),
            DropDown("config", "kitty -e nvim /home/Folenius/.config/qtile/config.py", opacity=1, x=0.25, y=0.15, height=0.6, width=0.5, on_focus_lost_hide=False),
    ]),
)



# Here are all related to the layouts of Qtile
# The available ones not active are commented, uncomment, and set their properties manually from the official qtile documentation



layouts = [
    layout.Columns(
        border_focus = catpuccin["dark"]["macchiato"]["teal"],
        border_normal = catpuccin["dark"]["macchiato"]["base"],
        border_width = 2,
        margin = 15,
        ),
    layout.Max(),
    # layout.Stack(num_stacks=2),
    #layout.Bsp(
        #border_width =2,
        #margin = 5,
        #border_focus = "#965fd4",
        #border_normal = "#1d1a2f",
        #),
    # layout.Matrix(),
    layout.MonadTall(
        border_width = 2,
        margin = 5,
        border_focus = "#965fd4",
        border_normal = "#1d1a2f",
        ),
    layout.MonadWide(
        border_width = 2,
        margin = 5,
        border_focus = "#965fd4",
        border_normal = "#1d1a2f",
       ),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()



# Finally, here is all the configuration of the bar
# Modify carefully, and at your own risk


# The bar and widgets configuration is in ./screens.py, if you want to, you could add your own bar, just edit the following line
screens = screens.bar



 # From here you are entering wild space, idk what is beyond here, but whatever, go on if you want to



# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
