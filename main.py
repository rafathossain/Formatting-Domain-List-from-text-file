file_name = "Domains_list.txt"

file = open(file_name, "r")
domain_dictionary = []
key = 0


for line in file:
	# print(line.strip())
	line = line.strip()
	if line != "":
		full_domain = line
		if "domian:" in line:
			full_domain = line.split("domian:")[1]
		elif "domain:" in line:
			full_domain = line.split("domain:")[1]
		final_domain = full_domain.split("/")[0]
		final_domain = final_domain.strip()
		if final_domain not in domain_dictionary:
			domain_dictionary.append(final_domain)
			# print(final_domain)

file.close()
output_file = open("Domains_list_final.txt", "a")

for domains in domain_dictionary:
	output_file.write("domain:" + domains + "\n")

output_file.close()
