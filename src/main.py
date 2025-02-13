from mailer import Mailer
from excel_reader import ExcelReader

def main():
    mail = Mailer()
    excel = ExcelReader("./data/contacts.xlsx")

    while (True):
        command = int(input(">"))

        if (command == 1):
            row = int(input("Type Row Number: "))
            rowList = excel.getRow(row)
            print(f"Name: {rowList[0]}\nEmail: {rowList[1]}\nSubject: {rowList[2]}\nBody: {rowList[3]}")

        elif (command == 2):
            row = int(input("Type Row Number to Send Mail: "))
            mail.sendMail(excel.getRow(row))

        else:
            break

if __name__ == '__main__':
    main()