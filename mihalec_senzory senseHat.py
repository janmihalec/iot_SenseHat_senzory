from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

sense.set_rotation(180)

#zadefinovanie farieb
red = (255,0,0)
green = (0,255,0)

while True:
    #cita yo vsetkych troch senzorov
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()
    
    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)
    
    #vytvorenie spravy
    message = "Teplota: " + str(t) + " °C,   Tlak: " + str(p) + " hPa,   Vlhkost: " + str(h) + " %"
    
    if t < 18:
        bg = red
        sense.show_message("Volaj skolnika aby zakuril", text_colour=bg)
        
    if t > 18.1 and t < 30:
        bg = green
    else:
        bg = red
    
    if t > 30.1:
        bg = red 
        sense.show_message(" Stiahni temohlavicu mas prilis teplo", text_colour=bg)
    else:
        sense.show_message(message, text_colour=bg)
    
    sense.clear()
    
sleep(50)


