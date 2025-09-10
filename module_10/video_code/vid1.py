def main():
    outfile = open("myfile.txt", "w")

    outfile.write('Dan Kahn')
    outfile.write("john")
    outfile.write('mary')

    outfile.close()

main()