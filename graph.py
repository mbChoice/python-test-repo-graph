import csv
import matplotlib.pyplot as plt
from pathlib import Path

# Create empty lists for each state and years 1910 - 2020
years = []
massachusetts = []
arizona = []
indiana = []
tennessee = []
washington = []

# Path to csv
file_path = Path(r"C:\Users\matthew.bonaski\projects\personal\Github\python-test-repo-graph\state_stats.csv")

# Open State Population csv and gather population data from years
with file_path.open('r', encoding='utf-8', newline='') as csv_file:
    reader = csv.reader(csv_file)

    # Skip header row
    next(reader)

    # Append each row to appropriate list as and int
    for row in reader:
        years.append(int(row[0]))
        arizona.append(int(row[1]))
        indiana.append(int(row[2]))
        massachusetts.append(int(row[3]))
        tennessee.append(int(row[4]))
        washington.append(int(row[5]))

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(years, arizona, label='Arizona', color='blue')
plt.plot(years, indiana, label='Indiana', color='gold')
plt.plot(years, massachusetts, label='Massachusetts', color='green')
plt.plot(years, tennessee, label='Tennessee', color='orange')
plt.plot(years, washington, label='Washington', color='purple')

# Add a title and x, y labels
plt.title('Population from 1910 to 2020')
plt.xlabel('Year')
plt.ylabel('Population')

# Add a legend
plt.legend()

# Show the graph
plt.show()