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

class AddPatientView(AlertDialog):
    def __init__(self, app):
        self.app = app
        super().__init__(title=Text("Add new Patient", size=16, text_align="center"),
            content=Column(
                [
                    TextField(
                        hint_text="Patient Name",
                        autofocus=False,
                        width=200,
                        height=40,
                        text_size=12,
                        border_color=colors.BLACK26,
                    ),
                    TextField(
                        hint_text="Patient Age",
                        autofocus=False,
                        width=200,
                        height=40,
                        text_size=12,
                        border_color=colors.BLACK26,
                    ),
                    TextField(
                        hint_text="Patient Address",
                        autofocus=False,
                        width=200,
                        height=40,
                        text_size=12,
                        border_color=colors.BLACK26,
                    ),
                    TextField(
                        hint_text="Patient Location",
                        autofocus=False,
                        width=200,
                        height=40,
                        text_size=12,
                        border_color=colors.BLACK26,
                    ),
                     TextField(
                        hint_text="Patient complaint",
                        autofocus=False,
                        width=200,
                        height=40,
                        text_size=12,
                        border_color=colors.BLACK26,
                    ),
                    TextField(
                        hint_text="Ctas Score",
                        autofocus=False,
                        width=200,
                        height=40,
                        text_size=12,
                        border_color=colors.BLACK26,
                    )
                ],
             height=300,
             horizontal_alignment="center",
            ),
            content_padding=padding.all(10),
            actions=[
                ElevatedButton(
                    "Add",
                    on_click=self.app.add_patient,
                    style=ButtonStyle(
                        bgcolor=colors.BLUE_400,
                        shape={"": RoundedRectangleBorder(radius=3)},
                    ),
                    width=100,
                ),
                ElevatedButton(
                    "Cancel",
                    on_click=self.app.cancel_add_patient,
                    style=ButtonStyle(
                        bgcolor=colors.RED_400,
                        shape={"": RoundedRectangleBorder(radius=3)},
                    ),
                    width=100,
                    
                ),
            ],
           actions_alignment= "center",)
    
    