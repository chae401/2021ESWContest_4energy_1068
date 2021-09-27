'''
Input pulse preferred (vs. time preferred) Stopped rotation OK.
Loops on pulses input, not on time. Output only when flowing
Note, YF-s201 give 6 pulses /1 revolution
Nested While version using RPi clock.
Input on pin 13, pin 6 gnd, 5Vcc pin to RPi pin 2
Input must go thru voltage divider circuit
Input -> 4.7k ohm res -> RPi pin 13 + 10k ohm -> Gnd RPi
Warning : From actuals, RPi can only poll 30 times/sec(15 transitions)
'''
import RPi.GPIO as GPIO
import time, sys
from multiprocessing import Process, Queue

def upper_flow_sensor(upper_que):
    GPIO.setmode(GPIO.BCM)
    inpt = 14
    GPIO.setup(inpt,GPIO.IN)

    rate_cnt = 0 # Recolution counts(r/min)
    tot_cnt = 0 # Total count

    time_zero = 0.0 #system start up time
    time_start = 0.0 #Keep measurement begin time
    time_end = 0.0 #Keep measurement end time

    gpio_last = 0 # Was last state 0 or 1 or other?
    pulses = 0 #0-5 pulses from YF-s201
    constant = 1.79 #water meter calibration factor
    Flow_data = 0
    # print('Water flow - approximate')
    # print('Control C to exit')

    time_zero = time.time() 


    rate_cnt = 0 # Loop forever
    pulses = 0 # Reset rate counter
    time_start = time.time() # Keep start time
    while pulses <= 5:
        gpio_cur = GPIO.input(inpt)
        if gpio_cur != 0 and gpio_cur != gpio_last: # Input changed
            pulses += 1
        gpio_last = gpio_cur
        try:
            # print(GPIO.input(inpt), end='') # Status bit. LOWERS accuracy
            None
        except KeyboardInterrupt: # Look for exit commend
            print('\nCTRL C - Exiting nicely')
            GPIO.cleanup() # Clean up GPIO
            print('Done') # print 'Done'
            sys.exit() # Exit nicely

    rate_cnt += 1 # Revolutions / time
    tot_cnt += 1 # Total revs since start
    time_end = time.time() # End of measurement time
    Flow_data =  round((rate_cnt * constant)/(time_end-time_start),2)
    print(Flow_data)
    upper_que.put(Flow_data)
    GPIO.cleanup()
    # print('\nLiters / min', Flow_data , 'approximate')
    # print('Total Liters ', round(tot_cnt * constant,1))
    # print('time (min & clock)', round((time.time()-time_zero)/60,2), '\t', time.asctime(time.localtime(time.time())),'\n')

def under_flow_sensor(under_que):
    GPIO.setmode(GPIO.BCM)
    inpt = 15
    GPIO.setup(inpt,GPIO.IN)

    rate_cnt = 0 # Recolution counts(r/min)
    tot_cnt = 0 # Total count

    time_zero = 0.0 #system start up time
    time_start = 0.0 #Keep measurement begin time
    time_end = 0.0 #Keep measurement end time

    gpio_last = 0 # Was last state 0 or 1 or other?
    pulses = 0 #0-5 pulses from YF-s201
    constant = 1.79 #water meter calibration factor
    Flow_data = 0
    # print('Water flow - approximate')
    # print('Control C to exit')

    time_zero = time.time() 


    rate_cnt = 0 # Loop forever
    pulses = 0 # Reset rate counter
    time_start = time.time() # Keep start time
    while pulses <= 5:
        gpio_cur = GPIO.input(inpt)
        if gpio_cur != 0 and gpio_cur != gpio_last: # Input changed
            pulses += 1
        gpio_last = gpio_cur
        try:
            # print(GPIO.input(inpt), end='') # Status bit. LOWERS accuracy
            None
        except KeyboardInterrupt: # Look for exit commend
            print('\nCTRL C - Exiting nicely')
            GPIO.cleanup() # Clean up GPIO
            print('Done') # print 'Done'
            sys.exit() # Exit nicely

    rate_cnt += 1 # Revolutions / time
    tot_cnt += 1 # Total revs since start
    time_end = time.time() # End of measurement time
    Flow_data =  round((rate_cnt * constant)/(time_end-time_start),2)
    print('under')
    print(Flow_data)
    under_que.put(Flow_data)
    GPIO.cleanup()
    # print('\nLiters / min', Flow_data , 'approximate')
    # print('Total Liters ', round(tot_cnt * constant,1))
    # print('time (min & clock)', round((time.time()-time_zero)/60,2), '\t', time.asctime(time.localtime(time.time())),'\n')
    #
def flow_main():

    upper_flow_que = Queue()
    under_flow_que = Queue()

    upper_proc =  Process(target=upper_flow_sensor,args=((upper_flow_que),))
    under_proc =  Process(target=under_flow_sensor,args=((under_flow_que),))

    upper_proc.start()
    under_proc.start()
    upper_proc.join()
    under_proc.join()

    upper_flow_data = upper_flow_que.get()
    under_flow_data = under_flow_que.get()

    upper_flow_que.close()
    under_flow_que.close()



    print('upper'+ str(upper_flow_data))
    print('under'+ str(under_flow_data))

    return upper_flow_data, under_flow_data


