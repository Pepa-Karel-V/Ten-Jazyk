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

def main(FILE_PATH):
    file_info = read_file(FILE_PATH)

    i = 0
    comment = False
    new_line = False
    while i < len(file_info):
        character = file_info[i]

        if comment:
            if character == ";":
                comment = False

        elif new_line:
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
                            send_error("invalid syntax line x character y 1")
                            return -1

                        i += 1 # buffer overflow

                    i += 1

                    while file_info[i] != ")":
                        variable_type.append(file_info[i])
                        i += 1 # buffer overflow

                    i += 1

                    while file_info[i] != "<":
                        if file_info[i] != " " and file_info[i] != "\n":
                            send_error("invalid syntax line x character y 2")
                            return -1

                        i += 1

                    if file_info[i+1] != "-":
                        send_error("invalid syntax line x character y 3")
                        break

                    i += 2
                    while file_info[i] == " " or file_info[i] == "\n": # buffer overflow
                        i += 1

                    variable_name = []
                    while(file_info[i] != " " and file_info[i] != "\n"): # buffer overflow
                        variable_name.append(file_info[i])
                        i += 1

                else:
                    send_error("invalid syntax line x character y 4")
                    break

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

