PLACEHOLDER = "[name]"

#Open the file containing names for read or write accessibility
with open("Day24\\Mail Merge Project Completed\\Input\\Names\\invited_names.txt") as names_file:
    #Turn the content of the txt file into a comma/line spearates list.
    names = names_file.readlines()

with open("Day24\\Mail Merge Project Completed\\Input\\Letters\\starting_letter.txt") as letter_file:
    #Access the entirety of the letter format for later adjustment.
    letter_contents = letter_file.read()
    #Loop through the list of names created by the readlines() used earlier on the names file.
    for name in names:
        #Strip away the extra space that could occur before or after the name in the list.
        stripped_name = name.strip()
        #Save your new combination of the letter with "[name]" placeholder replaced with current line being read in names file.
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        #Use the write method's default action of creating a new file when one does not exist to save and output our newly formatted letter.
        with open(f"Day24\\Mail Merge Project Completed\\Output\\letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

