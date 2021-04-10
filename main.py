from covid import Covid

c = Covid()

def active():
    active = c.get_total_active_cases()
    print(active)

def recovered():
    recovered = c.get_total_recovered()
    print(recovered)

def deaths():
    deaths = c.get_total_deaths()
    print(deaths)

print("Covid Tracker\na = active\nr = recovered\nd = deaths\n")

case = input("What do you want to see: ")

if case == "a":
    active()

if case == "r":
    recovered()

if case == "d":
    deaths()

