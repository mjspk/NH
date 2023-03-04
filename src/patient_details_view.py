from flet import (
    AlertDialog,
    AppBar,
    Column,
    Container,
    DataTable,
    ElevatedButton,
    Icon,
    Page,
    PopupMenuButton,
    PopupMenuItem,
    RoundedRectangleBorder,
    Row,
    TemplateRoute,
    Text,
    TextField,
    UserControl,
    View,
    colors,
    icons,
    margin,
    padding,
    theme,
    IconButton,
    ButtonStyle
)




import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import flet as ft 
from flet.matplotlib_chart import MatplotlibChart
matplotlib.use("svg")


class PatientDetailsView(UserControl):
    
    # class ChartView(UserControl):
    #     def __init__(app):
            
    #         fig, ax = plt.subplots()

    #         fruits = ["apple", "blueberry", "cherry", "orange"]
    #         counts = [40, 100, 30, 55]
    #         bar_labels = ["red", "blue", "_red", "orange"]
    #         bar_colors = ["tab:red", "tab:blue", "tab:red", "tab:orange"]

    #         ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

    #         ax.set_ylabel("fruit supply")
    #         ax.set_title("Fruit supply by kind and color")
    #         ax.legend(title="Fruit color")

    #         MatplotlibChart(fig, expand=True)
    
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app
        self.build()

    def build(self):
        
        self.layout=Column(
            horizontal_alignment = "center",
            controls=[
            
            Text(value="Department Name", style="headlineLarge", text_align="center"), #Header one
            Text(value="Patient Tracker", style="headlineMedium", text_align="center"), #Header Two
            ft.Divider(height=9, thickness=3), #Divider line

            Row(
                controls =[
                Column(
                    controls = [
                    ft.DataTable(
                        columns=[
                            ft.DataColumn(ft.Text(value = "PATIENT NAME", weight="bold"), ),
                            ft.DataColumn(ft.Text(value = "CTAS SCORE (1-5)", weight="bold"), numeric=True),
                            ft.DataColumn(ft.Text(value = "NEWS", weight="bold"), numeric=True),
                            ft.DataColumn(ft.Text(value = "Priority", weight="bold"), numeric=True),
                            ],
                        rows=[
                            ft.DataRow(
                                color = "red",
                                cells=[
                                    ft.DataCell(ft.Text("John Doe")),
                                    ft.DataCell(ft.Text("3")),
                                    ft.DataCell(ft.Text("11")),
                                    ft.DataCell(ft.Text("1")),
                                ],
                            ),
                            ],
                        ),
                        Row(
                            controls = [
                                Text(value= "Arrival: ", weight="bold"),
                                Text(value= "TIME1"),
                                Text(value= "Location: ", weight="bold"),
                                Text(value= "Loc")
                            ]
                        ),
            
                    Row(
                        controls = [
                            Text(value = "CEDIS Complaint: ", weight="bold"),
                            Text(value = "broken leg")
                        ]
                    ),
                    ],
                ),
                ft.DataTable(
                    vertical_lines=ft.border.BorderSide(2, "black"),
                    horizontal_lines=ft.border.BorderSide(2, "black"),
                    border=ft.border.all(2, "black"),
                    data_row_height = 20,
                    column_spacing = 2,
                    
                    columns=[
                        ft.DataColumn(ft.Text("")),
                        ft.DataColumn(ft.Text("TIME1"), numeric=True),
                        ft.DataColumn(ft.Text("TIME2"), numeric=True),
                        ft.DataColumn(ft.Text("TIME3"), numeric=True),
                        ft.DataColumn(ft.Text("TIME4"), numeric=True),
                        ft.DataColumn(ft.Text("TIME5"), numeric=True),
                        ],
                    rows=[
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text("RR")),
                                ft.DataCell(ft.Text("10")),
                                ft.DataCell(ft.Text("11")),
                                ft.DataCell(ft.Text("12")),
                                ft.DataCell(ft.Text("13")),
                                ft.DataCell(ft.Text("14")),
                            ],
                        ),
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text("O2")),
                                ft.DataCell(ft.Text("10")),
                                ft.DataCell(ft.Text("11")),
                                ft.DataCell(ft.Text("12")),
                                ft.DataCell(ft.Text("13")),
                                ft.DataCell(ft.Text("14")),
                            ],
                        ),
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text("Temp")),
                                ft.DataCell(ft.Text("10")),
                                ft.DataCell(ft.Text("11")),
                                ft.DataCell(ft.Text("12")),
                                ft.DataCell(ft.Text("13")),
                                ft.DataCell(ft.Text("14")),
                            ],
                        ),
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text("SBP")),
                                ft.DataCell(ft.Text("10")),
                                ft.DataCell(ft.Text("11")),
                                ft.DataCell(ft.Text("12")),
                                ft.DataCell(ft.Text("13")),
                                ft.DataCell(ft.Text("14")),
                            ],
                        ),
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text("HR")),
                                ft.DataCell(ft.Text("10")),
                                ft.DataCell(ft.Text("11")),
                                ft.DataCell(ft.Text("12")),
                                ft.DataCell(ft.Text("13")),
                                ft.DataCell(ft.Text("14")),
                            ],
                        ),
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text("Supplemental O2")),
                                ft.DataCell(ft.Text("10")),
                                ft.DataCell(ft.Text("11")),
                                ft.DataCell(ft.Text("12")),
                                ft.DataCell(ft.Text("13")),
                                ft.DataCell(ft.Text("14")),
                            ],
                        ),
                        ],
                    ),
                ],
            ),
            
        
            # chart = ChartView(self),
        
            
            
            
            # Container(
            #     ChartView(self)
            # )
            
            
            
            ] #maincolumnend
        )

        # chart = ChartView(self)

        return self.layout
    

    
    

            