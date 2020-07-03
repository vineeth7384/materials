import argparse
import re
# construct the argument parser and parse the arguments

LANDMARKS = set(list(range(64, 84)))
PART = re.compile("part name='[0-9]+'")
# load the contents of the original XML file and open the output file
# for writing
print("[INFO] parsing data split XML file...")
rows = open("new_data.xml").read().strip().split("\n")
output = open("new_data1.xml", "w")
# loop over the rows of the data split file
for row in rows:
	# check to see if the current line has the (x, y)-coordinates for
	# the facial landmarks we are interested in
	parts = re.findall(PART, row)
	# if there is no information related to the (x, y)-coordinates of
	# the facial landmarks, we can write the current line out to disk
	# with no further modifications
	if len(parts) == 0:
		output.write("{}\n".format(row))
	# otherwise, there is annotation information that we must process
	else:
		# parse out the name of the attribute from the row
		attr = "name='"
		i = row.find(attr)
		j = row.find("'", i + len(attr) + 1)
		name = int(row[i + len(attr):j])
		# if the facial landmark name exists within the range of our
		# indexes, write it to our output file
		if name in LANDMARKS:
			output.write("{}\n".format(row))
# close the output file
output.close()
