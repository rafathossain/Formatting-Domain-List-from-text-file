domain_file_name = "Domains_list.txt"
url_file_name = "URLs_list.txt"


domain_file = open(domain_file_name, "r")
url_file = open(url_file_name, "r")
domain_dictionary = []
url_dictionary = []

for line in domain_file:
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

for line in url_file:
	# print(line.strip())
	line = line.strip()
	if line != "":
		full_url = line
		# full_url = full_url.split("/")[0]
		final_url = full_url.strip()
		if final_url[0:4] != "www.":
			final_url = "www." + final_url
		url_dictionary.append(final_url)

domain_file.close()
output_file = open("Domains_And_URL_List.txt", "w")
output_file.write("#Domains\n")

for domains in domain_dictionary:
	output_file.write("domain:" + domains + "\n")

output_file.write("\n#URLs\n")

for url in url_dictionary:
	output_file.write(url + "\n")

output_file.close()
