from flet import (
    AlertDialog,
    AppBar,
    Column,
    Container,
    ElevatedButton,
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

)


class PatientsList(UserControl):
    def __init__(self, app,patitents_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app
        self.patitents_list = patitents_list
        self.build()
    
    def build(self):
        rows = []
        for patient in self.patitents_list:
            rows.append(Row(
                [
                    Text(value=patient.name),
                    Text(value=patient.age),
                    Text(value=patient.address),
                ],
                padding=padding(10, 0),
                horizontal_alignment="center",
                vertical_alignment="center",
            ))
        headers = Row(
            [
                Text(value="Name", style="headlineSmall"),
                Text(value="Age", style="headlineSmall"),
                Text(value="Address", style="headlineSmall"),
            ],
            padding=padding(10, 0),
            horizontal_alignment="center",
            vertical_alignment="center",
        )
        rows.insert(0, headers)
        self.layout = Column(rows)
