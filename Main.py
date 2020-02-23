import config, threading

code_country = input("Do you want generate with country code (y/n) : ")

method_creating = input("What method you want fast/slow : ")

if method_creating == "fast":
    print("if you choose fast mode you generate all operator")
    ans = input("fast / slow: ")
    if ans == "fast":
        operator = 4
    else:
        print("(1) Kiyvstar")
        print("(2) Lifecell")
        print("(3) Vodafone")
        print("(4) All")
        operator = input("Chose the mobile operator: ")
if method_creating == "slow":
    print("(1) Kiyvstar")
    print("(2) Lifecell")
    print("(3) Vodafone")
    print("(4) All")
    operator = input("Chose the mobile operator: ")

if code_country == 'y':
    que = input("Do you want add + (y/n): ")
    code = "380"
if code_country == 'n':
    que = 'n'
    code = ""


def kyivstar_gen():
    file_kyiv = open("number_kyivstar.txt", "w")

    for op in config.Kiyvstar:
        first_half = int(code + str(op)+ "0000000")
        for second_half in range(9999999):
            if que == "y":
                print("+"+str(first_half + second_half))
                file_kyiv.write("+"+str(first_half + second_half)+"\n")
            if que == "n":
                if code_country == 'n':
                    print("0"+str(first_half + second_half))
                    file_kyiv.write("0"+str(first_half + second_half)+"\n")
                else:
                    print(str(first_half + second_half))
                    file_kyiv.write(str(first_half + second_half)+"\n")

    file_kyiv.close()

def lifecell_gen():
    file_life = open("number_lifecell.txt", "w")

    for op in config.Lifecell:
        first_half = int(code + str(op)+ "0000000")
        for second_half in range(9999999):
            if que == "y":
                print("+"+str(first_half + second_half))
                file_life.write("+"+str(first_half + second_half)+"\n")
            else:
                print("0"+str(first_half + second_half))
                file_life.write("0"+str(first_half + second_half)+"\n")
    file_life.close()

def vodafone_gen():
    file_voda = open("number_vodafone.txt", "w")

    for op in config.Vodafone:
        first_half = int(code + str(op)+ "0000000")
        for second_half in range(9999999):
            if que == "y":
                print("+"+str(first_half + second_half))
                file_voda.write("+"+str(first_half + second_half)+"\n")
            else:
                print("0"+str(first_half + second_half))
                file_voda.write("0"+str(first_half + second_half)+"\n")
    file_voda.close()

if method_creating == "slow":
    if operator == "1":
        kyivstar_gen()

    if operator == "2":
        lifecell_gen()

    if operator == "3":
        vodafone_gen()

    if operator == "4":
        kyivstar_gen()
        lifecell_gen()
        vodafone_gen()
if method_creating == "fast":
    threading.Thread(target=kyivstar_gen).start()
    threading.Thread(target=lifecell_gen).start()
    threading.Thread(target=vodafone_gen).start()
