

def unique_file(input_filename, output_filename):
    input_file = open(input_filename, 'r')
    file_contents = input_file.read()
    input_file.close()
    duplicates = []
    word_list = file_contents.split()
    file = open(output_filename, 'w')
    for word in word_list:
        
        if word not in duplicates:
            duplicates.append(word)
            file.write(str(word) + "\n")
            file.close()


    unique_file('sample.txt','unique_output.txt')
    for line in sorted(open('unique_output.txt')):
        print(line, end='')
