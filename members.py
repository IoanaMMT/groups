musical_groups = [
    ["Ad Rock", "MCA", "Mike D."],
    ["John Lennon", "Paul McCartney", "Ringo Starr", "George Harrison"],
    ["Salt", "Peppa", "Spinderella"],
    ["Rivers Cuomo", "Patrick Wilson", "Brian Bell", "Scott Shriner"],
    ["Chuck D.", "Flavor Flav", "Professor Griff", "Khari Winn", "DJ Lord"],
    ["Axl Rose", "Slash", "Duff McKagan", "Steven Adler"],
    ["Run", "DMC", "Jam Master Jay"],
]

# first approach using a variable
PRINT = False
for groups in musical_groups:
	if PRINT:
		print(', '.join(groups))
		PRINT = False
	else:
		PRINT = True




# second approach using a enumarate list and % operator
for line, groups in enumerate(musical_groups):
	if line % 2:
		print(', '.join(groups))


# third option using range and length
for line in range(len(musical_groups)):
	if line % 2:
		print(', '.join(musical_groups[line]))