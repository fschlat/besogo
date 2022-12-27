"""
26.12.22
Frederic Schlattner

This file creates multiple html files for each SGF game from the template.html file.

Remember to add:
1. SGF files to the games_sgf folder, follow nomenclature.
2. Add name of the SGF file in the text file SGF_list.txt.
3. Run this python file to get the html files.
"""

import os 


# Read in the template HTML file
with open("template.html", "r") as f:
    template_html = f.read()

# Open the text file in read mode
with open("SGF_list.txt", "r") as g:
    # Read the contents of the file into a string
    games = g.read()

# Remove all spaces in textfile
games = games.replace(' ', '')


# Split the string into a list of words, using the comma as the delimiter
game = games.split(",")

# Print the list of words
print(game)

# Generate the HTML files
for i, step in enumerate(game):

    # Create the content for the HTML file by replacing the placeholder in the template
    html = template_html.replace("file_name",step)

    filepath = '/generated_html/'+step+'.html'

    # Save the HTML content to a new file in the specified directory
    with open(os.getcwd()+filepath, "w") as f:
        f.write(html)
    











