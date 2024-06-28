import qrcode


wifi_type = input("Wifi type:")
wifi_ssid = input("Wifi ssid:")
wifi_password = input("Wifi password:")
wifi = f'WIFI:T:{wifi_type};S:{wifi_ssid};P:{wifi_password};'
qr = qrcode.make(wifi)
type(qr)
qr.save(f"{wifi_ssid}.png")
