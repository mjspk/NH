
from flet import (
    AlertDialog,
    AppBar,
    Column,
    Container,
    ElevatedButton,
    Icon,
    Page,
    PopupMenuButton,
    PopupMenuItem,
    UserControl,
    View,
    colors,
    Row,
    Text,
    TextField,
    TextButton,
    ButtonStyle,
    icons,
    padding,
    theme,
    IconButton,
    RoundedRectangleBorder
)


class SettingsView(UserControl):
     
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app
        self.build()
    
    def build(self):
        self.layout = Container(
            Text(value="Settings", style="headlineMedium"),
            expand=True,
            padding=padding.only(top=15, left=15, right=15),
        )

        return self.layout