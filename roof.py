def roof(z,dy):
    numerator=[]
    denominator=[]
    for i in range(len(z)):
        numerator.append(z[i]/(dy[i])**2)
        denominator.append(1/(dy[i])**2)
    return (sum(numerator)/sum(denominator))