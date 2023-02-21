radio.set_group(1)

def on_forever():
    pass


def on_received_number(receivedNumber):
    basic.show_number(receivedNumber)
    if receivedNumber==0:
        basic.show_number(0)
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 255)
    elif receivedNumber==1:
        maqueen.motor_stop(maqueen.Motors.M1)
        maqueen.motor_stop(maqueen.Motors.M1)


radio.on_received_number(on_received_number)
basic.forever(on_forever)