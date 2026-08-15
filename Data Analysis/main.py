# Opening the file in read mode ('r') and reading all the lines
with open('junk.txt', 'r') as text_file:
    lines = text_file.readlines()
    
# Calculating and reporting the total number of lines
line_count = len(lines)
print("Total lines in the file:", line_count)

# Opening the text_file again in write mode ('w') to save our new changes
with open('junk.txt', 'w') as text_file:
    
    # Looping through each original line and converting it to lowercase
    for line in lines:
        text_file.write(line.lower())
        
    # Adding the new line at the end
    # (Just-in-Case, We put "\n" at the start so it drops down to a fresh line first)
    text_file.write("\n text file nanalyssis")

# The 'with open' block automatically saves and closes the text file for us!
print("Processing complete. The file has been saved!")