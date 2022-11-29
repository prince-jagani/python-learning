# program to get full form of computer related terms


dictionary = {
    "CPU": "Central Processing Unit",
    "RAM": "Random Access Memory",
    "ROM": "Read Only Memory",
    "HDD": "Hard Disk Drive",
    "SSD": "Solid State Drive",
    "GPU": "Graphics Processing Unit",
    "SATA": "Serial Advanced Technology Attachment",
    "HTTP": "Hyper Text Transfer Protocol",
    "URL": "Universal Resource Locator",
    "BIOS": "Basic Input Output System",
    "ASCII": "American Standard Code for Information Interchange",
    "PC": "Personal Computer",
    "PDF": "Portable Document Format",
    "IP": "Internet Protocol",
    "ISP": "Internet Service Provider"
}

print("Enter any Short form:", end=" ")
i_full = input()
i_full = i_full.upper()
print(i_full)
full_form = dictionary.get(i_full)

print("Full form of", i_full, "is", full_form)
