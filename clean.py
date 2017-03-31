"""
Mini project (Day-2): clean raw SMS code file.
Name:  Spandan Majumder  7598108971
Email: spandanmajumderjblss@gmail.com
"""

# Read the input file
f = open("raw_SMS_codes.txt","r")
# Open a file to output the processed output
o = open("output.txt","w")
# Loop through line
	# perform required cleaning
for line in f:
    if line > " ":
	# Write to output file
        o.write(line)
f.close()
o.close()
