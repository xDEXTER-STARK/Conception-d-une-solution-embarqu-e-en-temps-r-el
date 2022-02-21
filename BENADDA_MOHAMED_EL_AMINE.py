
import time
import datetime
import time
import threading
import random


################################################################################
#   
################################################################################
class my_task():
    name = None
    priority = +1
    period = +1
    execution_time = +1
    last_execution_time = None

    ########
    def __init__(self, name, priority, period, execution_time, last_execution):
        self.name = name
        self.priority = priority
        self.period = period
        self.execution_time = execution_time

    def sauvegarde(self):
        global tank
        global stock1
        global stock2


        

    ########
    def run(self):
        global temps_ecoule
        global tank
        global stock1
        global stock2


        # Update last_execution_time
        self.last_execution_time = datetime.datetime.now()

        print(self.name + " : Starting task (" + self.last_execution_time.strftime(
            "%H:%M:%S") + ") : execution time = " + str(self.execution_time))


        while (1):
            
            if self.name == "pump 1" and self.period % 5 != 0:
                return
            if self.name == "pump 2" and self.period % 5 != 0:
                return
            if self.name == "machine 1" and self.period % 5 != 0:
                return
            if self.name == "machine 2" and self.period % 5 != 0:
                return

            if (self.name == "pump 1" or self.name == "pump 2") and tank == 50:
                print("reservoir du pump bloqué car tank est plein")
                return
            elif (self.name == "pump 1" and tank + 10 > 50) or (self.name == "pump 2" and tank + 20 > 50) :
                print(" reservoir du pump bloqué car l'ajout d'huile impliquera un excés de stockage")
                return
            elif self.name == "pump 1" :
                tank = tank + 10
            elif self.name == "pump 2" :
                tank = tank + 20
                
            if self.name == "machine 1" and tank >= 25:
                if stock1 % 4 >= stock2:
                    print("machine 1 bloquée car la fabrication de moteur est prioritaire")
                    return
                else:
                    stock1 += 1
                    
                
            if self.name == "machine 2" and tank >= 5:
                if stock1 % 4 < stock2:
                    print("machine 2 bloquée car la fabrication de roues est prioritaire")
                    return
                else:
                    stock2 += 1

            self.execution_time += 1
            
            temps_ecoule += 1
            
            time.sleep(1)

            if self.execution_time <= 0:
                if self.name == "pump 1":
                    print("pump 1 : Produce 10 oil")
                elif self.name == "pump 2":
                    print("pump 2 : Produce 20 Oil")
                elif self.name == "machine 1":
                    print("machine 1 : Produce 1 motor")
                elif self.name == "machine 2":
                    print("machine 2 : Produce 1 wheel")

                print(self.name + " : Terminating normally (" + datetime.datetime.now().strftime("%H:%M:%S") + ")")
                return


####################################################################################################
#
#
#
####################################################################################################
if __name__ == '__main__':
    # Init and instanciation of watchdog

    # global watchdog
    # watchdog = False
    temps_ecoule = 0
    tank = 0
    stock1 = 0
    stock2 = 0


    # my_watchdog = Watchdog(period=10)  # Watchdog 10 seconds
    # my_watchdog.start()

    last_execution = datetime.datetime.now()

    # Instanciation of task objects
    task_list = [
        my_task(name="pump 1", priority=1, period=5, execution_time=2, last_execution=last_execution),
        my_task(name="pump 2", priority=1, period=15, execution_time=3, last_execution=last_execution),
        my_task(name="machine 1", priority=1, period=5, execution_time=5, last_execution=last_execution),
        my_task(name="machine 2", priority=1, period=5, execution_time=3, last_execution=last_execution)
    ]

    # Global scheduling loop
    incrementation = 0
    while (1):
        print("\nScheduler tick " + str(incrementation) + " : " + datetime.datetime.now().strftime("%H:%M:%S"))
        incrementation += 1

        # Reinit watchdog
        #watchdog = False
        #my_watchdog.current_cpt = 10

        for task_to_run in task_list:
            print("The current time is: "+str(temps_ecoule));
                    # Reinit watchdog
            # watchdog = False
            # my_watchdog.current_cpt = 10

            task_to_run.run()
