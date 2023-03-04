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
    ListView,
    margin,
    border,
    Icon

)

from users import PatientList
from patient_details_view import PatientDetailsView

# class Patient:
#     def __init__(self,patient_id,name,age,address,location,Ctas,rank=0,latest_record=None):
#         self.patient_id = patient_id
#         self.name = name
#         self.age = age
#         self.address = address
#         self.location = location
#         self.Ctas=Ctas
#         self.rank = rank

class PatientsListView(UserControl):
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app
        self.patitents_list = app.patients_list.get_patients()
        self.lv = ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self.layout = self.lv
        self.build()
    
    def build(self):  
        self.load()  
        return self.layout
    
    def load(self):
        self.lv.controls.clear()
        for patient in self.patitents_list:
            self.lv.controls.append(
                Container(
                    Row([
                Row([Icon(name=icons.PERSON, size=30, color=colors.WHITE), Text(value=patient.name, style="headlineMedium")]),
                Row([Icon(name=icons.TIMER, size=30, color=colors.WHITE), Text(value=patient.age, style="headlineMedium")]),
                Row([Icon(name=icons.SIGNPOST, size=30, color=colors.WHITE), Text(value=patient.address, style="headlineMedium")]),
                Row([Icon(name=icons.LOCATION_ON, size=30, color=colors.WHITE), Text(value=patient.location, style="headlineMedium")]),
                Row([Icon(name=icons.FAVORITE, size=30, color=colors.WHITE), Text(value=patient.Ctas, style="headlineMedium")]),
                Row([Icon(name=icons.SPORTS_SCORE, size=30, color=colors.WHITE), Text(value=patient.rank, style="headlineMedium")]),
                    ]),
                    padding=padding.all(10),
                    margin=margin.all(10),
                    bgcolor=self.get_color_based_on_rank(patient.rank),
                    border_radius=5,
                    expand=False,
                    on_click=self.patient_selected,
                )
                
            )

    def refresh(self):
        self.patitents_list = self.app.patients_list.get_patients()
        self.load()
        self.update()

    def patient_selected(self, control):
        PatientDetailsView(self.app, patient=control.patient)



    def get_color_based_on_rank(self, rank):
        if rank == 1:
            return colors.RED_400
        elif rank == 2:
            return colors.YELLOW_400
        elif rank == 3:
            return colors.GREEN_400
        else:
            return colors.BROWN_400




            
