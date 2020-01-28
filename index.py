from time import sleep, time
from datafiler.main import main_program
from datafiler.get_settings import get_settings
from datafiler.flash_light import flash

# Henter informasjon om programmet
settings = get_settings()
timer_fremover = settings["timer_fremover"]
delay = settings["delay"]

def wo_controller(timer_fremover, delay):
    start_time = time()
    a_run = 1
    while True:
        s_time = time()
        print("|")
        print("|")
        print("|")
        main_program(int(timer_fremover))
        print("---")
        print("---")
        print("---")
        ex_time = float(time()) - float(s_time)
        print(f"Execution time: {ex_time}")
        next_run = float(start_time) + (float(a_run) * float(int(delay)))
        sleep_time = float(next_run) - float(time())
        sleep_time = str(sleep_time)
        sleep_time = sleep_time.split(".")
        sleep_time = int(sleep_time[0])
        a_run += 1
        print("<ctrl> + <c> for exit")
        flash()
        sleep(sleep_time)

wo_controller(timer_fremover, delay)
print("Prosess stoppet")







