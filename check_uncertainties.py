def check_uncertainties(values_dict): #check if valid
    for i in values_dict['dx']:
        if i<0:
            return "Input file error: Not all uncertainties are positive."
    for i in values_dict['dy']:
        if i<0:
            return "Input file error: Not all uncertainties are positive."
    return 0