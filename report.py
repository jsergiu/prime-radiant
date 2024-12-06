import matplotlib.pyplot as plt

from .enums import Residence

class Report:
    def __init__(self, people):
        self.people = people

    def generate_age_distribution(self):
        ages = [person.age for person in self.people]
        return ages

    def generate_marital_status_distribution(self):
        marital_statuses = [person.marital_status for person in self.people]
        distribution = {}
        for status in marital_statuses:
            if status not in distribution:
                distribution[status] = 0
            distribution[status] += 1
        return distribution

    def show_report(self):
        ages = self.generate_age_distribution()
        marital_status_distribution = self.generate_marital_status_distribution()

        # Convert enum keys to strings
        statuses = [status.name for status in marital_status_distribution.keys()]  # Convert enums to strings
        counts = list(marital_status_distribution.values())

        # Generate rural vs urban, gender, and income distributions
        rural_urban_distribution = {Residence.URBAN: 0, Residence.RURAL: 0}
        gender_distribution = {"male": 0, "female": 0}
        income_distribution = {}

        for person in self.people:
            # Count rural vs urban
            rural_urban_distribution[person.residence] += 1
            # Count gender
            gender_distribution[person.gender] += 1
            # Categorize income into ranges
            income_range = f"${(person.income // 100) * 100}-{((person.income // 100) + 1) * 100}"
            if income_range not in income_distribution:
                income_distribution[income_range] = 0
            income_distribution[income_range] += 1

        # Create a figure with four subplots in a 2x2 grid
        fig, axes = plt.subplots(2, 3, figsize=(18, 10))
        axes = axes.flatten()  # Flatten axes for easier indexing

        # Plot Age Distribution Histogram
        axes[0].hist(ages, bins=10, edgecolor="black")
        axes[0].set_title("Age Distribution")
        axes[0].set_xlabel("Age Ranges")
        axes[0].set_ylabel("Number of People")

        # Plot Marital Status Distribution Bar Chart
        bars = axes[1].bar(statuses, counts, color="skyblue", edgecolor="black")
        axes[1].set_title("Marital Status Distribution")
        axes[1].set_xlabel("Marital Status")
        axes[1].set_ylabel("Number of People")
        self.add_labels_to_bars(axes[1], bars)

        # Plot Rural vs Urban Distribution
        bars = axes[2].bar(
            rural_urban_distribution.keys(),
            rural_urban_distribution.values(),
            color="green",
            edgecolor="black",
        )
        axes[2].set_title("Rural vs Urban Distribution")
        axes[2].set_xlabel("Residence Type")
        axes[2].set_ylabel("Number of People")
        self.add_labels_to_bars(axes[2], bars)

        # Plot Gender Distribution
        bars = axes[3].bar(
            gender_distribution.keys(),
            gender_distribution.values(),
            color="purple",
            edgecolor="black",
        )
        axes[3].set_title("Gender Distribution")
        axes[3].set_xlabel("Gender")
        axes[3].set_ylabel("Number of People")
        self.add_labels_to_bars(axes[3], bars)

        # Plot Income Distribution
        income_labels = list(income_distribution.keys())
        income_values = list(income_distribution.values())
        bars = axes[4].bar(
            income_labels, income_values, color="orange", edgecolor="black"
        )
        axes[4].set_title("Income Distribution")
        axes[4].set_xlabel("Income Ranges")
        axes[4].set_ylabel("Number of People")
        self.add_labels_to_bars(axes[4], bars)

        # Adjust layout and show
        plt.tight_layout()
        plt.show()

    def add_labels_to_bars(self, ax, bars):
        """Add labels on top of each bar in the chart."""
        for bar in bars:
            height = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                height,
                f"{int(height)}",
                ha="center",
                va="bottom",
            )

