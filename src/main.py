import sys
import os

def send_error(error):
    print(f"ERROR: {error}")

def read_file(FILE_PATH):
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            return file.read()
    else:
        send_error("file does not exist")

def new_variable(FILE, variable, variable_type, variable_name):
    temp_list = []
    
    with open(FILE, "r") as read:
        lines = read.readlines()
        temp_list.extend(lines)
        
    with open(FILE, "w") as write:
        write.writelines(temp_list)
        write.write(variable_name + " = " + variable_type + "(" + variable + ")\n")
        
def new_command(file, variable, command):
    temp_list = []
    
    with open(file, "r") as read:
        lines = read.readlines()
        temp_list.extend(lines)
    
    with open(file, "w") as write:
        write.writelines(temp_list)
        write.write(command + "(" + variable + ")\n")
    
def main(FILE_PATH):
    file_info = read_file(FILE_PATH)

    i = 0
    radek = 1
    col = 1
    
    comment = False
    new_line = False

    if file_info != None:
        while i < len(file_info):
            character = file_info[i]

            if comment:
                if character == ";":
                    comment = False

            elif new_line:
                radek += 1
                col = 1
                new_line = False
                if character == "\n" or character == " " or i == len(file_info):
                    pass

                elif character == "l":
                    if file_info[i+1] == "e" and file_info[i+2] == "t" and (file_info[i+3] == " " or file_info[i+3] == "\n"): # buffer overflow

                        i += 3
                        while file_info[i] == " " or file_info[i] == "\n":
                            i += 1

                        variable = []
                        while(file_info[i] != " " and file_info[i] != "\n"):
                            variable.append(file_info[i])
                            i += 1

                        i -= 1

                        variable_type = []
                        i += 2 # buffer overflow
                        while file_info[i] != "(":
                            if file_info[i] != " " and file_info[i] != "\n":
                                send_error(f"invalid syntax line {radek} character y 1")
                                return -1

                            i += 1 # buffer overflow

                        i += 1

                        while file_info[i] != ")":
                            variable_type.append(file_info[i])
                            i += 1 # buffer overflow

                        i += 1

                        while file_info[i] != "<":
                            if file_info[i] != " " and file_info[i] != "\n":
                                send_error(f"invalid syntax line {radek} character y 2")
                                return -1

                            i += 1

                        if file_info[i+1] != "-":
                            send_error(f"invalid syntax line {radek} character y 3")
                            break

                        i += 2
                        while file_info[i] == " " or file_info[i] == "\n": # buffer overflow
                            i += 1

                        variable_name = []
                        while file_info[i] != " " and file_info[i] != "\n" and file_info[i] != "": # buffer overflow
                            variable_name.append(file_info[i])
                            i += 1

                        variable_type = "".join(variable_type)
                        variable_name = "".join(variable_name)
                        variable = "".join(variable)
                        
                        print(variable_name, variable_type, variable)

                        if variable_type == "int" or variable_type == "str":
                            new_variable("temp.py", variable, variable_type, variable_name)
                        
                        elif variable_type == "input":
                            new_variable("temp.py", variable, variable_type, variable_name)
                            
                        else:
                            send_error(f"invalid syntax line {radek} character y 4")
                            break

                    else:
                        send_error(f"invalid syntax line {radek} character y 5")
                        break

				#run - na print a podobny bez definovani
                elif character == "r":
                    if file_info[i+1] == "u" and file_info[i+2] == "n" and (file_info[i+3] == " " or file_info[i+3] == "\n"):  # buffer overflow
                    
                        i += 3
                        while file_info[i] == " " or file_info[i] == "\n":
                            i += 1
                        
                        #variable - to co chces printnout treba
                        variable =[]
                        while(file_info[i] != " " and file_info[i] != "\n"):
                            variable.append(file_info[i])
                            i += 1
                        
                        i -= 1
                        
                        #command - co s tim chces delat
                        command = []
                        i += 2
                        if file_info[i] != "(":
                            send_error(f"Error at line {radek} character y")
                            break
                        
                        else:
                            i += 1
                            while file_info[i] != ")":
                                command.append(file_info[i])
                                i += 1
                        
                        command = "".join(command)
                        variable = "".join(variable)
                        
                        if command == "print":
                            new_command("temp.py", variable, command)
                            
            #if statementy
#            elif character == XXX:
            	#neco, nevim jak
            	
            	#znaminka
#            	znaminko = []
#            	if file_info[i] == "<"and file_info[i+1] == "-" and file_info[i+2] == "-" and file_info[i+3] == ">":
#            		znaminko.append("==")
#            		
#            	elif file_info[i] == "<"and file_info[i+1] == "<" and file_info[i+2] == "-" and file_info[i+3] == ">":
#            		znaminko.append(">=")
            		
#            	elif file_info[i] == "<"and file_info[i+1] == "-" and file_info[i+2] == ">" and file_info[i+3] == ">":
#            		znaminko.append("<=")
#            		
#            	elif file_info[i] == "!"and file_info[i+1] == "<" and file_info[i+2] == "-" and file_info[i+3] == ">":
#            		znaminko.append("!=")
            	
#            	elif file_info[i] == "<"and file_info[i+1] == "<" and file_info[i+2] == "-" and file_info[i+3] == "-":
#            		znaminko.append(">")
            		
#            	elif file_info[i] == "-"and file_info[i+1] == "-" and file_info[i+2] == ">" and file_info[i+3] == ">":
#            		znaminko.append("<")

            #elif character == "":
            elif character == "#":
                new_line = True

            elif character == ";":
                comment = True

            elif character == "\n" or character == " ":
                pass

            else:
                send_error("invalid syntax line x character y")
                break

            i += 1

        print("Done")

if len(sys.argv) == 2:
    main(sys.argv[1])

else:
    send_error(f"Expected 1 argument got {len(sys.argv) - 1}")