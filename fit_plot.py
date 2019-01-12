from matplotlib import pyplot

def plot_fit(values_dict,a,b,x_title,y_title):
    f_of_x = [a * x_i + b for x_i in values_dict['x']]
    pyplot.plot(values_dict['x'],f_of_x,'r')
    pyplot.errorbar(values_dict['x'], values_dict['y'], xerr=values_dict['dx']
                                            ,yerr=values_dict['dy'], fmt='b,')
    pyplot.xlabel(x_title)
    pyplot.ylabel(y_title)
    pyplot.show()