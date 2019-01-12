def create_a_dict(input_file): #check if row or column and return a dictionary
    data=input_file.readlines()
    values_dict={}
    #create lists for the first column and the first row
    column_title=((data[0].lower()).strip('\n')).split()
    row_title=[]
    for i in range(4):
        row_title.append((data[i][0:2].lower()).strip())
    #turns data into 2 dimensional list
    for line in range(len(data)):
        data[line]=(data[line].strip('\n')).split()
    #creates a dictionary which corresponds a variable to the list of his values (in float type)
    if column_title.count('dx')==1 and column_title.count('dy')==1:    
        for j in range(4):
            values_list=[]
            for num_line in range(1,len(data)-3):
                if len(data[num_line])!=4:
                    return 'Input file error: Data lists are not the same length.'
                values_list.append(float(data[num_line][j].strip("\n")))
            values_dict[column_title[j]]=values_list
    else:
        for j in range(4):
            values_dict[row_title[j]]=data[j][1:]
            for k in range(len(values_dict[row_title[j]])):
                values_dict[row_title[j]][k]=float(values_dict[row_title[j]][k])
        for j in row_title:
            if len(values_dict['x'])!=len(values_dict[j]):
                return 'Input file error: Data lists are not the same length.'
    values_dict['y_title'] = data[-1][-2] + (" ") + data[-1][-1]
    values_dict['x_title'] = data[-2][-2] + (" ") + data[-2][-1]
    return(values_dict,data)
input_file=open('abcd.txt')
print(create_a_dict(input_file))