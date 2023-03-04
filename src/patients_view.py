import datetime
import uuid
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
from patients_list_view import PatientsListView
from data_simulator import Simulator
from users import Patient, PatientList

class PatientsView(UserControl):
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app
        self.patients_list = PatientList()
        self.patients_list_view = PatientsListView(self)
        self.data_simulator=Simulator(self)
        self.build()
    
    def build(self):
        self.layout =Container(
             Column([
                Row(
                    [
                     Text(value="Waiting Patients", style="headlineMedium",text_align="center"),
                     TextButton(
                                "Add new Patient",
                                icon=icons.ADD,
                                on_click=self.add_patient_dialog,
                                style=ButtonStyle(
                                    bgcolor=colors.BLUE_400,
                                    shape={"": RoundedRectangleBorder(radius=3)},
                                ),
                            
                            )

                    ],
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
                Row([Container(self.patients_list_view,height=600,width=600)]),
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
        name = self.page.dialog.content.controls[0].value
        age = self.page.dialog.content.controls[1].value
        address = self.page.dialog.content.controls[2].value
        location = self.page.dialog.content.controls[3].value
        complaint = self.page.dialog.content.controls[4].value
        Ctas = self.page.dialog.content.controls[5].value
        current_time = datetime.datetime.now()
        p=Patient(str(uuid.uuid4()),name,age,address,location,current_time,complaint,Ctas)
        self.patients_list.add_patient(p)
        self.patients_list_view.refresh()


    def refresh(self):
        self.patients_list_view.refresh()


    def cancel_add_patient(self, e):
        self.page.dialog.open=False
        self.page.update()


        



    
    