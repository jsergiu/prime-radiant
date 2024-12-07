import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from .enums import Gender
import plotly.graph_objs as go
from collections import Counter

from .attributes.attr_age import assign_age
from .attributes.attr_education import assign_education
from .attributes.attr_employment import assign_employment
from .attributes.attr_ethnicity import assign_ethnicity
from .attributes.attr_gender import assign_gender
from .attributes.attr_health import assign_health
from .attributes.attr_income import assign_income
from .attributes.attr_marital import assign_marital_status
from .attributes.attr_residence import assign_residence
from .attributes.attr_religion import assign_religion
from .attributes.attr_political_affiliation import assign_political_affiliation
from .attributes.attr_technology_use import assign_technology_use

from .person import Person


def generate_population(population_size=100, gender_ratio=0.5):
    population = [Person() for _ in range(population_size)]

    # Assign attributes
    for person in population:
        assign_age(person)
        assign_gender(person, gender_ratio)
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

    return population


# report = Report(population)
# report.show_report()

app = dash.Dash("PrimeRadiant")

# App layout
app.layout = html.Div(
    [
        html.Div(
            [
                html.Label("Adjust Male-Female Ratio:"),
                dcc.Slider(
                    id="gender-ratio-slider",
                    min=0,
                    max=1,
                    step=0.05,
                    value=0.5,  # Default 50-50 ratio
                    marks={0: "0% Male", 0.5: "50-50", 1: "100% Male"},
                ),
            ],
            style={"width": "400px", "margin": "left"},
        ),
        dcc.Graph(id="live-gender-graph"),
        dcc.Graph(id="live-political-graph"),
        dcc.Interval(id="interval-component", interval=1000, n_intervals=0),
    ]
)

# Extract gender distribution graph
def generate_gender_graph(population):
    # Define age intervals
    age_intervals = [(0, 14), (15, 24), (25, 39), (40, 59), (60, 99)]
    interval_labels = [f"{low}-{high}" for low, high in age_intervals]

    # Count people in each age interval for each gender
    male_counts = [
        sum(
            1
            for person in population
            if low <= person.age <= high and person.gender == Gender.MALE
        )
        for low, high in age_intervals
    ]
    female_counts = [
        sum(
            1
            for person in population
            if low <= person.age <= high and person.gender == Gender.FEMALE
        )
        for low, high in age_intervals
    ]

    # Create histogram figure
    fig = go.Figure()

    # Add Male counts
    fig.add_trace(
        go.Bar(x=interval_labels, y=male_counts, name="Male", marker_color="#4682B4")
    )

    # Add Female counts
    fig.add_trace(
        go.Bar(
            x=interval_labels, y=female_counts, name="Female", marker_color="#FF6347"
        )
    )

    # Update layout
    fig.update_layout(
        title="Age and Gender Distribution",
        xaxis_title="Age Intervals",
        yaxis_title="Count of People",
        barmode="group",  # Change to 'group' for side-by-side bars
        legend=dict(title="Gender"),
        template="plotly_white",
        width=600,
    )

    return fig
    

# Extract political affiliation graph
def generate_political_graph(population):
    # Count the occurrences of each political affiliation
    affiliation_counts = Counter(
        [str(person.political_affiliation) for person in population]  # Convert to string
    )

    # Extract labels and values
    labels = list(affiliation_counts.keys())
    values = list(affiliation_counts.values())

    # Create a bar chart
    fig = go.Figure(
        data=[
            go.Bar(
                x=labels,
                y=values,
                marker=dict(color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]),
            )
        ]
    )

    # Customize layout
    fig.update_layout(
        title="Political Affiliation Distribution",
        xaxis_title="Political Affiliation",
        yaxis_title="Number of People",
        template="plotly_white",
        width=600,
    )

    return fig

@app.callback(
    [Output("live-gender-graph", "figure"), Output("live-political-graph", "figure")],
    [Input("gender-ratio-slider", "value")],
)
def update_graphs(male_ratio):
    # Generate population based on male-female ratio
    population = generate_population(100, male_ratio)

    # Generate separate graphs
    gender_graph = generate_gender_graph(population)
    political_graph = generate_political_graph(population)

    return gender_graph, political_graph


if __name__ == "__main__":
    app.run_server(debug=True)
