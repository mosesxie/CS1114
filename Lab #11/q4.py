def html_table_generator(filename):

    f = open(filename, 'r', encoding="UTF-8")

    html = "<html> \n<table> \n"

    for line in f:

        row = line.split(",")

        html = html + "\t <tr> \n"

        for word in row:

            html = html + "\t\t<th>" + word + "</th>\n"

        html = html + "\t</tr> \n"

            
    html = html + "</table> \n</html>"
        
    return html
        

    f.close()

def main():

    w = html_table_generator("lab11_q4_samplefile1-mac.csv")
    print (w)

main()
