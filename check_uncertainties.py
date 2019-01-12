def check_uncertainties(values_dict): #check if uncertainties are valid
    for i in values_dict['dx']:
        if float(i)<0:
            return "Input file error: Not all uncertainties are positive."
    for i in values_dict['dy']:
        if float(i)<0:
            return "Input file error: Not all uncertainties are positive."
    return 0