site = "https://apple.com"
site = site[8:-4]

password = site[:3] + str(len(site)) + str(site.count("e")) + "!"
print(password)