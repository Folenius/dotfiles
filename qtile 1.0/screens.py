from libqtile import bar, widget
from libqtile.config import Screen 
import colors as palette

colors = ["#965fd4", "#8bd450", "#1d1a2f", "#734f9a", "#e6770b"]

bar = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(

                    foreground = colors[2],
                    background = colors[2]

                    ),

                widget.GroupBox(

                    border = colors[1],
                    borderwidth = 3,
                    margin_x = None,
                    margin_y = None,
                    foreground = palette.catpuccin["dark"]["macchiato"]["teal"],
                    background = palette.catpuccin["dark"]["macchiato"]["base"], 
                    highlight_method = "block",
                    block_highlight_text_color = palette.catpuccin["dark"]["macchiato"]["base"],
                    this_current_screen_border =  palette.catpuccin["dark"]["macchiato"]["lavender"],
                    active = palette.catpuccin["dark"]["macchiato"]["text"],
                    inactive = palette.catpuccin["dark"]["macchiato"]["teal"],
                    disable_drag = True,
                    center_aligned = True

                    ),

                widget.WindowName(
                    
                    font = "Ubuntu Bold",
                    background = palette.catpuccin["dark"]["macchiato"]["base"],
                    foreground = palette.catpuccin["dark"]["macchiato"]["text"]

                    ),
                
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                
                widget.TextBox(

                    text = "",
                    foreground = palette.catpuccin["dark"]["macchiato"]["text"],
                    background = palette.catpuccin["dark"]["macchiato"]["base"],
                    padding = 0,
                    fontsize = 80

                    ),

                widget.CPU(

                    font = "Ubuntu Bold",
                    foreground = palette.catpuccin["dark"]["macchiato"]["base"],
                    background = palette.catpuccin["dark"]["macchiato"]["text"],
                    padding = 0,
                    margin = 0

                    ),

                widget.TextBox(

                    text = "",
                    foreground = palette.catpuccin["dark"]["macchiato"]["lavender"],
                    background = palette.catpuccin["dark"]["macchiato"]["text"],
                    padding = 0,
                    fontsize = 80

                    ),

                widget.Memory(

                    font = "Ubuntu Bold",
                    foreground = palette.catpuccin["dark"]["macchiato"]["base"],
                    background = palette.catpuccin["dark"]["macchiato"]["lavender"],
                    padding = 0,
                    margin = 0

                    ),

                widget.TextBox(

                    text = "",
                    foreground = palette.catpuccin["dark"]["macchiato"]["blue"],
                    background = palette.catpuccin["dark"]["macchiato"]["lavender"],
                    padding = 0,
                    fontsize = 80

                    ),

                widget.Net(
                    
                    format='{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}',
                    foreground = palette.catpuccin["dark"]["macchiato"]["base"],
                    background = palette.catpuccin["dark"]["macchiato"]["blue"],
                    font = "Ubuntu Bold",
                    padding = 0,
                    margin = 0,
                    max_chars = 12

                    ),

                widget.TextBox(

                    text = "",
                    foreground = palette.catpuccin["dark"]["macchiato"]["sapphire"],
                    background = palette.catpuccin["dark"]["macchiato"]["blue"],
                    padding = 0,
                    fontsize = 80

                    ),

                widget.CheckUpdates(

                    distro = "Arch",
                    update_interval = 60,
                    font = "Ubuntu Bold",
                    colour_have_updates = palette.catpuccin["dark"]["macchiato"]["base"],
                    colour_no_updates = palette.catpuccin["dark"]["macchiato"]["base"],
                    foreground = palette.catpuccin["dark"]["macchiato"]["base"],
                    background = palette.catpuccin["dark"]["macchiato"]["sapphire"],
                    padding = 0,
                    margin = 0,
                    execute = "kitty -e sudo pacman -Sy"

                    ),

                widget.TextBox(

                    text = "",
                    foreground = palette.catpuccin["dark"]["macchiato"]["sky"],
                    background = palette.catpuccin["dark"]["macchiato"]["sapphire"],
                    padding = 0,
                    fontsize = 80
                    
                    ),

                widget.CurrentLayout(

                    font = "Ubuntu Bold",
                    foreground = palette.catpuccin["dark"]["macchiato"]["base"],
                    background = palette.catpuccin["dark"]["macchiato"]["sky"],
                    padding = 0,
                    margin = 0

                    ),

                widget.TextBox(

                    text = "",
                    foreground = palette.catpuccin["dark"]["macchiato"]["teal"],
                    background = palette.catpuccin["dark"]["macchiato"]["sky"],
                    padding = 0,
                    fontsize = 80
                    
                    ),

                widget.Systray(

                    foreground = palette.catpuccin["dark"]["macchiato"]["base"],
                    background = palette.catpuccin["dark"]["macchiato"]["teal"]

                    ),

                widget.TextBox(

                    text = "",
                    foreground = palette.catpuccin["dark"]["macchiato"]["green"],
                    background = palette.catpuccin["dark"]["macchiato"]["teal"],
                    padding = 0,
                    fontsize = 80

                    ),

                widget.Clock(

                    format="%d/%m/%y %H:%M",
                    font = "Ubuntu Bold",
                    foreground = palette.catpuccin["dark"]["macchiato"]["base"],
                    background = palette.catpuccin["dark"]["macchiato"]["green"],
                    margin = 0,
                    padding = 0

                    ),
                
                widget.Sep(
                    
                    background = palette.catpuccin["dark"]["macchiato"]["green"]

                    )

            ],
            24,
            border_width=[0, 0, 0, 0],  # Draw top and bottom borders
            border_color=["ff00ff", "000000", "ff00ff", "000000"],  # Borders are magenta
            opacity=1
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        x11_drag_polling_rate = 144,
    ),
]
