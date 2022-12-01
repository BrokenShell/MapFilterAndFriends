""" Real World Objective:

4. Tally the totals for each team. No pivot tables or pandas allowed!

There are several valid solutions for this challenge. For this lesson, let's use
map and filter's best friend - the compound generator expression! """

teams = [
    {"TeamId": 1, "Name": "Awakening"},
    {"TeamId": 2, "Name": "Symphony of Blades"},
    {"TeamId": 3, "Name": "Team Cupcake"},
]
subtotals = [
    {"TeamId": 2, "Subtotal": 1.00},
    {"TeamId": 3, "Subtotal": 2.50},
    {"TeamId": 1, "Subtotal": 0.25},
    {"TeamId": 3, "Subtotal": 8.00},
    {"TeamId": 1, "Subtotal": 5.00},
]

# Comprehension Approach
team_totals = [{
    "TeamId": team["TeamId"],
    "Name": team["Name"],
    "Total": sum(
        subtotal["Subtotal"] for subtotal in subtotals
        if subtotal["TeamId"] == team["TeamId"]
    ),
} for team in teams]
print(team_totals)


# Alternate Approach without comprehensions
result = []
for team in teams:
    result.append({
        "TeamId": team["TeamId"],
        "Name": team["Name"],
        "Total": sum(
            map(lambda d: d["Subtotal"],
                filter(lambda t: t["TeamId"] == team["TeamId"], subtotals))
        )
    })
print(result)
