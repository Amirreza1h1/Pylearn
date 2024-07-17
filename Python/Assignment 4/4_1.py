import qrcode

name = input("your name: ")
phone_number = input("your phone number: ")
file_name ="name_" + name +"_phone number_"+ phone_number

qr_code = qrcode.make(file_name)
qr_code.save(file_name+".png")