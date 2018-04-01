import pprint

message = "I've, seen things you people wouldn't believe. Attack ships on fire off the shoulder of Orion. I watched C-beams glitter in the dark near the Tannhauser Gate. All those, moments... will be lost in time... like tears, in rain. Time to die."

count = {}

for character in message:
	count.setdefault(character, 0)
	count[character] += 1

pprint.pprint(count)