import sys

symbols = {
    "SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4,
    "SCREEN": 16384, "KBD": 24576
}

for i in range(16):
    symbols["R" + str(i)] = i

dest = {
    "": "000", "M": "001", "D": "010", "MD": "011",
    "A": "100", "AM": "101", "AD": "110", "AMD": "111"
}

jump = {
    "": "000", "JGT": "001", "JEQ": "010", "JGE": "011",
    "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111"
}

comp = {
    "0": "0101010", "1": "0111111", "-1": "0111010",
    "D": "0001100", "A": "0110000", "M": "1110000",
    "!D": "0001101", "!A": "0110001", "!M": "1110001",
    "-D": "0001111", "-A": "0110011", "-M": "1110011",
    "D+1": "0011111", "A+1": "0110111", "M+1": "1110111",
    "D-1": "0001110", "A-1": "0110010", "M-1": "1110010",
    "D+A": "0000010", "D+M": "1000010",
    "D-A": "0010011", "D-M": "1010011",
    "A-D": "0000111", "M-D": "1000111",
    "D&A": "0000000", "D&M": "1000000",
    "D|A": "0010101", "D|M": "1010101"
}

def assemble(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    instructions = []

    for number, line in enumerate(lines, start=1):
        line = line.split("//")[0].strip()
        if line:
            instructions.append((number, line))

    rom = 0

    for _, line in instructions:
        if line.startswith("(") and line.endswith(")"):
            label = line[1:-1]
            if label in symbols:
                raise ValueError("Duplicate label: " + label)
            symbols[label] = rom
        else:
            rom += 1

    result = []
    variable = 16

    for line_number, line in instructions:
        try:
            if line.startswith("("):
                continue

            if line.startswith("@"):
                value = line[1:]

                if value.isdigit():
                    address = int(value)
                else:
                    if value not in symbols:
                        symbols[value] = variable
                        variable += 1
                    address = symbols[value]

                if address < 0 or address > 32767:
                    raise ValueError()

                result.append(format(address, "016b"))

            else:
                dest_part = ""
                jump_part = ""

                if "=" in line:
                    dest_part, line = line.split("=")

                if ";" in line:
                    line, jump_part = line.split(";")

                if line not in comp or dest_part not in dest or jump_part not in jump:
                    raise ValueError()

                result.append("111" + comp[line] + dest[dest_part] + jump[jump_part])

        except:
            print("Invalid instruction at line", line_number)
            return
 
    output = filename.replace(".asm", ".hack")

    with open(output, "w") as file:
        file.write("\n".join(result))

    print("Assembly completed:", output)


if __name__ == "__main__":
    assemble(sys.argv[1])