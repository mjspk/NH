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
    def __init__(self, app, patients_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app
        self.patients_list = patients_list
        self.build()

    def build(self):
        rows = []
        for patient in self.patients_list:
            rows.append(Row(
                [
                    Text(value=patient.Fname),
                    Text(value=patient.Lname),
                    Text(value=patient.age),
                    Text(value=patient.TOA),
                    Text(value=patient.CTAS),
                    Text(value=patient.complaint),
                    Text(value=patient.address),
                    Text(value=patient.location),
                    Text(value=patient.rank),
                    Text(value=patient.record),
                ],
                padding=padding(10, 0),
                horizontal_alignment="center",
                vertical_alignment="center",
            ))
        headers = Row(
            [
                Text(value="Fname", style="headlineSmall"),
                Text(value="Lname", style="headlineSmall"),
                Text(value="Age", style="headlineSmall"),
                Text(value="Arrival Time", style="headlineSmall"),
                Text(value="CTAS", style="headlineSmall"),
                Text(value="complaint", style="headlineSmall"),
                Text(value="Address", style="headlineSmall"),
                Text(value="location", style="headlineSmall"),
                Text(value="rank", style="headlineSmall"),
                Text(value="record", style="headlineSmall"),
            ],
            padding=padding(10, 0),
            horizontal_alignment="center",
            vertical_alignment="center",
        )
        rows.insert(0, headers)
        self.layout = Column(rows)
