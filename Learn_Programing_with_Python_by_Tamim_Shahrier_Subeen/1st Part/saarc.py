saarc = ["Bangladesh", "Afghanistan", "Bhutan", "Nepal", "India", "Pakistan", "Sri Lanka"]

for country in saarc:
	print(country, "is a member of SAARC")

country = input("Enter the name of the country: ")

if country in saarc:
	print(country, "is a member of SAARC")
else:
	print(country, "is not a member of SAARC")

print("Program terminated")