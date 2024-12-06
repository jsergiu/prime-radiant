import matplotlib.pyplot as plt
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import random

from .attr_age import assign_age
from .attr_education import assign_education
from .attr_employment import assign_employment
from .attr_ethnicity import assign_ethnicity
from .attr_gender import assign_gender
from .attr_health import assign_health
from .attr_income import assign_income
from .attr_marital import assign_marital_status
from .attr_residence import assign_residence
from .attr_religion import assign_religion
from .attr_political_affiliation import assign_political_affiliation
from .attr_technology_use import assign_technology_use

from .person import Person
from .report import Report

# Create a population
population_size = 100
population = [Person() for _ in range(population_size)]

# Assign attributes
for person in population:
    assign_age(person)
    assign_gender(person)
    assign_ethnicity(person)
    assign_residence(person)
    assign_religion(person)
    assign_marital_status(person)
    assign_income(person)
    assign_education(person)
    assign_employment(person)
    assign_health(person)
    assign_political_affiliation(person)
    assign_technology_use(person)


report = Report(population)
report.show_report()

app = dash.Dash("PrimeRadiant")

app.layout = html.Div([
    dcc.Graph(id='live-graph'),
    dcc.Interval(
        id='interval-component',
        interval=1000,
        n_intervals=0
    )
])

@app.callback(
    Output('live-graph', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_graph(n):
    # Define age intervals
    age_intervals = [(0, 14), (15, 24), (25, 39), (40, 59), (60, 99)]
    interval_labels = [f"{low}-{high}" for low, high in age_intervals]

    # Count people in each age interval for each gender
    male_counts = [sum(1 for person in population if low <= person.age <= high and person.gender == "Male") 
                   for low, high in age_intervals]
    female_counts = [sum(1 for person in population if low <= person.age <= high and person.gender == "Female") 
                     for low, high in age_intervals]

    # Create histogram figure
    fig = go.Figure()
    
    # Add Male counts
    fig.add_trace(go.Bar(
        x=interval_labels,
        y=male_counts,
        name='Male',
        marker_color='blue'
    ))
    
    # Add Female counts
    fig.add_trace(go.Bar(
        x=interval_labels,
        y=female_counts,
        name='Female',
        marker_color='pink'
    ))
    
    # Update layout for better visualization
    fig.update_layout(
        title='Age and Gender Distribution in Population',
        xaxis_title='Age Intervals',
        yaxis_title='Count of People',
        barmode='stack',
        legend=dict(title='Gender'),
        template='plotly_white'
    )
    
    return fig



if __name__ == '__main__':
    app.run_server(debug=True)



