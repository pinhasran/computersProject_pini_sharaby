from matplotlib import pyplot

def plot_fit(values_dict,a,b,x_title,y_title):
    f_of_x = [a * x_i + b for x_i in values_dict['x']]
    pyplot.plot(values_dict['x'],f_of_x,'r')
    pyplot.errorbar(values_dict['x'], values_dict['y'], xerr=values_dict['dx']
                                            ,yerr=values_dict['dy'], fmt='b,')
    pyplot.xlabel(x_title)
    pyplot.ylabel(y_title)
    pyplot.show()
    pyplot.savefig("linear_fit.svg")

def check_uncertainties(values_dict): #check if uncertainties are valid
    for i in values_dict['dx']:
        if float(i) < 0:
            return "Input file error: Not all uncertainties are positive."
    for i in values_dict['dy']:
        if float(i) < 0:
            return "Input file error: Not all uncertainties are positive."
    return 0

def roof(z,dy): #calculte the "roof" equation
    numerator = []
    denominator = []
    for i in range(len(z)):
        numerator.append(z[i] / (dy[i]) ** 2)
        denominator.append(1 / (dy[i]) ** 2)
    return (sum(numerator)/sum(denominator))

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
            values_dict[row_title[j]] = data[j][1:]
            for k in range(len(values_dict[row_title[j]])):
                values_dict[row_title[j]][k] = float(values_dict[row_title[j]][k])
        for j in row_title:
            if len(values_dict['x'])!=len(values_dict[j]):
                return 'Input file error: Data lists are not the same length.'
    values_dict['y_title'] = data[-1][-2] + (" ") +  data[-1][-1]
    values_dict['x_title'] = data[-2][-2] + (" ") + data[-2][-1]
    return(values_dict)


def fit_linear(filename):
    input_file=open(filename)
    values_dict=create_a_dict(input_file)
    if type(values_dict) == str:
        print(values_dict)
    elif check_uncertainties(values_dict)!= 0:
        print(check_uncertainties(values_dict))
    else:
        x=dy=values_dict['x']
        dx=dy=values_dict['dx']
        y=dy=values_dict['y']
        dy=values_dict['dy']
        xy=[]
        x_squared=[]
        y_squared=[]
        dy_squared=[]
        chi=[]
        for i in range(len(x)):
            xy.append(x[i] * y[i])
            x_squared.append(x[i] ** 2)
            y_squared.append(y[i] ** 2)
            dy_squared.append(dy[i] ** 2)
        a=(roof(xy,dy) - roof(x,dy) * roof(y,dy)) / (roof(x_squared,dy) - roof(x,dy) ** 2)
        da=(roof(dy_squared,dy) / (len(x) * (roof(x_squared,dy) - roof(x,dy) ** 2))) ** 0.5
        b=roof(y,dy)-a*roof(x,dy)
        db=((roof(dy_squared,dy)*roof(x_squared,dy)) / (len(x)*(roof(x_squared,dy)
                                                         - roof(x,dy) ** 2))) ** 0.5
        for i in range(len(x)):
            chi.append(((y[i] - (a * x[i] + b)) / dy[i])**2)
        chi2=sum(chi)
        chi2_reduced= chi2 / (len(chi) - 2)
        print("a = ",a," +- ",da)
        print("b = ",b," +- ",db)
        print("chi2 = ",chi2)
        print("chi2_reduced = ",chi2_reduced)
        plot_fit(values_dict, a, b, values_dict['x_title'], values_dict['y_title'])

fit_linear('r_input.txt')