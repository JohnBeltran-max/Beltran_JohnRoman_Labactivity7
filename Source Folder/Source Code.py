import requests
import matplotlib.pyplot as plt
from datetime import datetime


test_cases = [
    {"name": "Manila", "lat": 14.5995, "lon": 120.9842},
    {"name": "Cebu City", "lat": 10.3157, "lon": 123.8854},
    {"name": "Davao City", "lat": 7.1907, "lon": 125.4553}
]

for i, test in enumerate(test_cases, start=1):

    url = f"https://api.open-meteo.com/v1/forecast?latitude={test['lat']}&longitude={test['lon']}&daily=temperature_2m_max&timezone=Asia%2FSingapore"
    response = requests.get(url)
    data = response.json()

    dates = data['daily']['time']
    max_temps = data['daily']['temperature_2m_max']
    formatted_dates = [datetime.strptime(d, "%Y-%m-%d").strftime("%b %d") for d in dates]

    
    plt.figure(figsize=(9, 4))
    plt.plot(formatted_dates, max_temps, marker='o', linestyle='-', color='#2ca02c', linewidth=2)
    plt.title(f'Test Case {i}: 7-Day Max Temperatures in {test["name"]}', fontsize=13, pad=12)
    plt.xlabel('Date', fontsize=11)
    plt.ylabel('Max Temperature (°C)', fontsize=11)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    plt.tight_layout()

    
    filename = f"test_case_{i}_{test['name'].lower().replace(' ', '_')}.png"
    plt.savefig(filename)
    
    
    peak_temp = max(max_temps)
    avg_temp = sum(max_temps) / len(max_temps)
    peak_date = formatted_dates[max_temps.index(peak_temp)]
    
    print(f"--- Test Case {i}: {test['name']} ---")
    print(f"Average Peak Temp: {avg_temp:.2f}°C")
    print(f"Maximum Temp Recorded: {peak_temp}°C on {peak_date}")
    print(f"Interpretation: {test['name']} shows a peak of {peak_temp}°C, indicating consistent thermal conditions requiring standard heat mitigation.\n")

    # Display plot
    plt.show()