
# Step 2: Define Hypotheses
def hypothesis_young_urban(people):
    """Young urban professionals are more likely to attend."""
    return [p for p in people if 20 <= p.age <= 40 and p.residential_medium == "urban"]

def hypothesis_high_income(people):
    """High-income individuals are more likely to attend."""
    return [p for p in people if p.income >= 800]

def hypothesis_married_and_middle_age(people):
    """Married middle-aged individuals are more likely to attend."""
    return [p for p in people if p.marital_status == "married" and 30 <= p.age <= 50]

# Step 3: Apply Hypotheses and Test
def test_hypotheses(people):
    hypotheses = {
        "Young Urban": hypothesis_young_urban,
        "High Income": hypothesis_high_income,
        "Married and Middle Age": hypothesis_married_and_middle_age,
    }
    
    results = {}
    for name, func in hypotheses.items():
        filtered_people = func(people)
        results[name] = len(filtered_people)
    
    return results

# Step 4: Visualize Results
def visualize_hypotheses(results):
    labels = list(results.keys())
    values = list(results.values())

    plt.bar(labels, values, color='skyblue', edgecolor='black')
    plt.title("Hypothesis Testing: Likely Event Attendees")
    plt.ylabel("Number of People")
    plt.xlabel("Hypotheses")
    for i, value in enumerate(values):
        plt.text(i, value, str(value), ha='center', va='bottom')
    plt.show()

# Main Code: Generate Population and Test Hypotheses
results = test_hypotheses(population)
visualize_hypotheses(results)

# Optional: Print Matching Subsets
for hypothesis, func in [("Young Urban", hypothesis_young_urban), 
                         ("High Income", hypothesis_high_income), 
                         ("Married and Middle Age", hypothesis_married_and_middle_age)]:
    print(f"\n{hypothesis}:")
    for person in func(population)[:10]:  # Show first 5 matches
        print(f"  Age: {person.age}, Gender: {person.gender}, Income: {person.income}, Marital Status: {person.marital_status}, Residence: {person.residential_medium}")

