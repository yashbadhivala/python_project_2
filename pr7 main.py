
from pr7_pack_c import pr7_clockmod as tmod, pr7_numbers as mmod, pr7_shuffler as rmod, pr7_ident as uidmod, pr7_filer as fmod, pr7_scout as xmod
import math

def menu():
    print("\n========================")
    print("Welcome to Multi-Utility Toolkit (variant 3)")
    print("========================")
    print("1. Datetime and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers (UUID)")
    print("5. File Operations (Custom Module)")
    print("6. Explore Module Attributes (dir())")
    print("7. Exit")
    print("========================")

def dt_menu():
    print("Datetime and Time Operations:")
    print("1. Display current date/time")
    print("2. Difference between two ISO dates")
    print("3. Format a date string")
    print("4. Stopwatch")
    print("5. Countdown")
    print("6. Back")

def math_menu():
    print("Mathematical Operations:")
    print("1. Factorial")
    print("2. Compound Interest")
    print("3. Trig values")
    print("4. Areas")
    print("5. Back")

def rand_menu():
    print("Random Data Generation:")
    print("1. Random number")
    print("2. Random list sample")
    print("3. Password")
    print("4. OTP")
    print("5. Back")

def file_menu():
    print("File Operations:")
    print("1. Create file (x)")
    print("2. Write file (w)")
    print("3. Read file (r)")
    print("4. Append file (a)")
    print("5. Back")

def explore_menu():
    print("Explore Module Attributes:")
    print("1. math module")
    print("2. random module")
    print("3. toolkit package module list")
    print("4. Back")

def run():
    while True:
        menu()
        c = input("Enter your choice: ").strip()
        if c == "1":
            dt_menu()
            ch = input("Enter: ").strip()
            if ch == "1":
                print(tmod.nowtime())
            elif ch == "2":
                d1 = input("first date (YYYY-MM-DD): "); d2 = input("second date (YYYY-MM-DD): ")
                print(tmod.delta(d1+" 00:00:00", d2+" 00:00:00"))
            elif ch == "3":
                d = input("date time ISO (YYYY-MM-DD HH:MM:SS): ")
                fmt = input("format string (default %d-%m-%Y): ") or "%d-%m-%Y"
                print(tmod.stamp_format(d, fmt))
            elif ch == "4":
                print("elapsed:", tmod.sw_run(1), "sec")
            elif ch == "5":
                print(tmod.cd_go(3))
        elif c == "2":
            math_menu(); ch = input("Enter: ").strip()
            if ch == "1":
                n = int(input("n: ")); print(mmod.facto(n))
            elif ch == "2":
                p=float(input("P: ")); r=float(input("R%: ")); t=float(input("T: ")); print(mmod.ci_value(p,r,t))
            elif ch == "3":
                a=float(input("angle in degree: ")); print(mmod.trig_calc(a))
            elif ch == "4":
                sh=input("shape (circle/rect/tri): ")
                if sh=="circle":
                    print(mmod.areas("circle", float(input("r: ")))) 
                elif sh=="rect":
                    print(mmod.areas("rect", float(input("w: ")), float(input("h: ")))) 
                else:
                    print(mmod.areas("tri", float(input("b: ")), float(input("h: ")))) 
        elif c == "3":
            rand_menu(); ch=input("Enter: ").strip()
            if ch == "1":
                print(rmod.pick_number())
            elif ch == "2":
                print(rmod.random_list())
            elif ch == "3":
                ln=int(input("length: ")); print(rmod.password_make(ln))
            elif ch == "4":
                print(rmod.rand_otp())
        elif c == "4":
            print(uidmod.get_uuid())
        elif c == "5":
            file_menu(); ch=input("Enter: ").strip()
            if ch == "1":
                nm=input("file name: "); 
                try:
                    print(fmod.file_create(nm))
                except FileExistsError:
                    print("already exists")
            elif ch == "2":
                nm=input("file name: "); txt=input("data: "); print(fmod.save_file(nm, txt))
            elif ch == "3":
                nm=input("file name: "); 
                try:
                    print(fmod.open_read(nm))
                except FileNotFoundError:
                    print("missing file")
            elif ch == "4":
                nm=input("file name: "); txt=input("append: "); print(fmod.plus_write(nm, txt))
        elif c == "6":
            explore_menu(); ch=input("Enter: ").strip()
            if ch == "1":
                import math as M; print(xmod.dir_info(M))
            elif ch == "2":
                import random as R; print(xmod.dir_info(R))
            elif ch == "3":
                import pr7_pack_c as P; print([m for m in dir(P) if m.startswith("pr7_")])
        elif c == "7":
            print("Goodbye!"); break
        else:
            print("Invalid.")

if __name__ == "__main__":
    run()
