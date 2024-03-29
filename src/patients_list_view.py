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
                Text(value=patient.patient_id, style="headlineMedium", visible=False),
                Row([Icon(name=icons.PERSON, size=30, color=colors.WHITE), Text(value=patient.name, style="headlineMedium")]),
                Row([Icon(name=icons.TIMER, size=30, color=colors.WHITE), Text(value=patient.age, style="headlineMedium")]),
                Row([Icon(name=icons.SIGNPOST, size=30, color=colors.WHITE), Text(value=patient.address, style="headlineMedium")]),
                Row([Icon(name=icons.LOCATION_ON, size=30, color=colors.WHITE), Text(value=patient.location, style="headlineMedium")]),
                Row([Icon(name=icons.FAVORITE, size=30, color=colors.WHITE), Text(value=patient.ctas, style="headlineMedium")]),
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
        pass



    def get_color_based_on_rank(self, rank):
        if rank == 3:
            return colors.RED_400
        elif rank == 2:
            return colors.YELLOW_400
        elif rank == 1:
            return colors.GREEN_400
        else:
            return colors.BROWN_400




            
