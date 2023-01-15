import __init__ as pd

print("""
░██████╗████████╗░█████╗░░█████╗░██╗░░██╗██╗░░██╗██╗░░░██╗██████╗░
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝██║░░██║██║░░░██║██╔══██╗
╚█████╗░░░░██║░░░███████║██║░░╚═╝█████═╝░███████║██║░░░██║██████╦╝
░╚═══██╗░░░██║░░░██╔══██║██║░░██╗██╔═██╗░██╔══██║██║░░░██║██╔══██╗
██████╔╝░░░██║░░░██║░░██║╚█████╔╝██║░╚██╗██║░░██║╚██████╔╝██████╦╝
╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═════╝░""")
print("""
    Select site option:
1. English
2. Russian
""")
user_option = input("Menu > ")
if user_option == "English":
    print("English module is loading")
    pd.time.sleep(1)
    print(pd.StackEng.OverEng())
else:
    print("Russian module is loading")
    pd.time.sleep(1)
    print(pd.StackRu.OverRu())
#Create KailUser(☄ S͇͇y͇͇i͇͇r͇͇e͇͇z͇͇z͇͇ ☄#2023)