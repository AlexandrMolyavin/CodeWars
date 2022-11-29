def calc_poly(pol_list, x): #If polynomial degree == 3
    poly_str_list = []
    pol_list.reverse()
    for i in range(len(pol_list)):
        if pol_list[i] != 0:
            if i == 0:
                if pol_list[0] > 0:
                    poly_str_list.append(str(pol_list[i]))
                else:
                    poly_str_list.append("- " + str(abs(pol_list[0])))
            elif i == 1:
                if pol_list[1] > 1:
                    poly_str_list.append(str(pol_list[i])+"*x")
                elif pol_list[1] == 1:
                    poly_str_list.append("x")
                elif pol_list[1] == -1:
                    poly_str_list.append("- x")
                else:
                    poly_str_list.append("- " + str(abs(pol_list[1])) + "*x")
            else:
                if pol_list[i] > 1:
                    poly_str_list.append(str(pol_list[i])+"*x^"+str(i))
                elif pol_list[i] == 1:
                    poly_str_list.append("x^" + str(i))
                elif pol_list[i] == -1:
                    poly_str_list.append("- x^" + str(i))
                else:
                    poly_str_list.append("- " + str(abs(pol_list[i])) + "*x^"+str(i))
    poly_str_list.reverse()
    poly_str = " + ".join(poly_str_list)
    for i in range(1, len(poly_str)):
        if poly_str[i] == "-":
            poly_str = poly_str[:i-2] + poly_str[i:] + "  "
    if poly_str[0] == "-":
        poly_str = poly_str[0] + poly_str[2:]
    print(poly_str)
    poly_str_cal = poly_str.replace("^", "**")
    m = eval(poly_str_cal)
    return "For " + poly_str.rstrip() + " with x = {} the value is {}".format(x, m)