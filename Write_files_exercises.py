#Purpose of this code will be to try different ways to learn how to write into a file.
def write_a_file(filename, data):
    output_file=open(filename,"w")
    for value in data:
        output_file.write(value)
        print(value,file=output_file)
    output_file.close()

def write_a_file_a(filename,data):
    output_file= open(filename,"w")
    for value in data:
        output_file.write(value+"\n")
        print(value, file=output_file)
    output_file.close()

def write_a_file_b(filename,data):
    output_file=open(filename,"w")
    for value in data:
        print(value, file=output_file)
        output_file.write(value+ "\t")
        #aprint(value, file=output_file)
    output_file.close()


data=["Dios","salud","familia","amor","abundancia"]
write_a_file("New_file.txt",data)
write_a_file_a("New_file_a.txt",data)
write_a_file_b("New_file_b.txt",data)