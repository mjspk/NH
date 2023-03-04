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

from add_patient_view import AddPatientView
from src.patients_list_view import PatientsListView

class PatientsView(UserControl):
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app
        self.build()
    
    def build(self):
        self.layout =Container(
             Column([
                Row(
                    [
                        Container(
                            Text(value="Waiting Patients", style="headlineMedium"),
                            expand=False,
                        ),
                        Container(
                            TextButton(
                                "Add new Patient",
                                icon=icons.ADD,
                                on_click=self.add_patient_dialog,
                                style=ButtonStyle(
                                    bgcolor=colors.BLUE_400,
                                    shape={"": RoundedRectangleBorder(radius=3)},
                                ),
                                
                            ),
                            
                        ),
                    ]
                ),
                Row(
                    [
                        TextField(
                            hint_text="Search all Patients",
                            autofocus=False,
                            content_padding=padding.only(left=10),
                            width=400,
                            height=40,
                            text_size=12,
                            border_color=colors.BLACK26,
                            focused_border_color=colors.BLUE_ACCENT,
                            suffix_icon=icons.SEARCH,
                            
                        )
                    ]
                ),
                Row(PatientsListView()),
            ],
            expand=True,        
        ),
        padding=padding.only(top=15, left=15),
        )

        return self.layout
    
    
      
    def add_patient_dialog(self, e):
        self.page.dialog = AddPatientView(self)
        self.page.dialog.open=True
        self.page.update()


    def add_patient(self, e):
        self.page.dialog.open=False
        self.page.update()
        patient_name = self.page.dialog.content.controls[0].value
        patient_age = self.page.dialog.content.controls[1].value
        patient_address = self.page.dialog.content.controls[2].value


    def cancel_add_patient(self, e):
        self.page.dialog.open=False
        self.page.update()



    
    