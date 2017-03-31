"name: Spandan Majumder"
"Reg.No.- 15352033"

#(2)
#input part
data = "we dont need we need dont we"
words_split = data.split(" ")

#distinguish unique elements
uniq=set(words_split)
print(uniq)

#function to find position
def find_pos(find_data, words_split):
	new_list = []
	for i in range(len(words_split)):
		if words_split[i] == find_data:
			new_list.append(i)
	return new_list

#calling function and display
for i in uniq:
        if i in words_split:
                print(i," ",find_pos(i,words_split))
