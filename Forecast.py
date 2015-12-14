"""Forecast"""
def process(year, data, yearpre):
    """Print values is processed from year, data and y predict
    Ex. year = 2555, 2556, 2557, 2558
    data = 1794030, 2412968, 2306622, 2178955
    ypre = 2559 """

    num = year.count(',')
    year = year.split(', ')
    data = data.split(',')
    mul_xy, log_x, val_year , val_data = [], [], [], []

    for i in range(num+1):
        mul_xy.append(int(year[i])*int(data[i]))
        log_x.append(int(year[i])**2)
        val_year.append(int(year[i]))
        val_data.append(int(data[i]))

    xbar = sum(val_year)/(num+1)
    ybar = sum(val_data)/(num+1)

    val_a = sum(mul_xy)/sum(log_x)
    val_b = ybar - (val_a*xbar)

    print(int(val_b+(val_a*yearpre)))
process(input(), input(), int(input()))
