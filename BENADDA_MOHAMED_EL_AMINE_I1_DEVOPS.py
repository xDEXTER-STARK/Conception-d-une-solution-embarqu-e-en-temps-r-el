
import datetime
import time
import threading
import random



################################################################################
#   Watchdog to stop tasks
################################################################################
class Watchdog(threading.Thread):

	period = -1
	current_cpt = -1

    	############################################################################
	def __init__(self, period):

		self.period = period
		
		threading.Thread.__init__(self)


    	############################################################################
	def run(self):

		print(" : Starting watchdog")

		self.current_cpt = self.period

		while (1):

			if(self.current_cpt >= 0):

				self.current_cpt -= 1
				time.sleep(1)
				
			else :
				print("!!! Watchdog stops tasks.")
				global watchdog
				watchdog = True
				self.current_cpt = self.period



################################################################################
#   Handle all connections and rights for the server
################################################################################
class my_task():


	name = None
	priority = -1
	period = -1
	execution_time = -1
	last_deadline = -1
	last_execution_time = None


    	############################################################################
	def __init__(self, name, priority, period, execution_time, last_execution):

		self.name = name
		self.priority = priority
		self.period = period
		self.execution_time = execution_time
		self.last_execution_time = last_execution


	############################################################################
	def run(self):

		# Update last_execution_time
		self.last_execution_time = datetime.datetime.now()

		global watchdog
		
		execution_time = random.randint(2, 30)

		print(self.name + " : Starting task (" + self.last_execution_time.strftime("%H:%M:%S") + ") : execution time = " + str(execution_time))

		while (watchdog == False):

			execution_time -= 1

			time.sleep(1)

			if (execution_time <= 0):
				print(self.name + " : Terminating normally (" + datetime.datetime.now().strftime("%H:%M:%S") + ")")
				return
		

		print(self.name + " : Pre-empting task (" + datetime.datetime.now().strftime("%H:%M:%S") + ")")

	

####################################################################################################
#
#
#
####################################################################################################
if __name__ == '__main__':
	
	tank = {"full":True}
	pump_1 = []
	pump_2 = []
	stock_1=[]
	stock_2=[]
	Machine_1 = {"nb_wheels":4,"nb_motors":2,"priority":0}
	Machine_2 = {"nb_wheels":4,"nb_motors":2,"priority":0}

	if tank["full"]==True:
		pump_1 = "Low Priority"
		pump_2 = "Low Priority"
	else:
		pump_2 = " High priority"
		pump_1 = "High priority"
		stock_1 = "oil"
		stock_2 = "oil"
	if (Machine_1["nb_wheels"]/4 > Machine_1["nb_motors"]):
		Machine_1["priority"]=2
		Machine_1["priority"]=1
		stock_1 = "oil"
		stock_2 = "oil"
	elif(Machine_2["nb_wheels"]/4 < Machine_2["nb_motors"]):
		Machine_2["priority"]=2
		Machine_2["priority"]=1
		stock_1 = "oil"
		stock_2 = "oil"
	else:
		pass
	# Init and instanciation of watchdog
	print("\nResults are :\ntank = {}\npump 1 = {}\npump 2 = {} \nstock 1 = {}\nstock 2 = {}\nMachine 1 = {}\nMachine 2 = {}\n".format(tank,pump_1,pump_2,stock_1,stock_2,Machine_1,Machine_2))

	global watchdog
	watchdog = False

	my_watchdog = Watchdog(period = 10)		# Watchdog 10 seconds
	my_watchdog.start()


	last_execution = datetime.datetime.now()
	
	# Instanciation of task objects
	task_list = []
	task_list.append(my_task(name="thread_1", priority = 1, period = 15, execution_time = 10, last_execution = last_execution))
	task_list.append(my_task(name="thread_2", priority = 1, period = 30, execution_time = 5, last_execution = last_execution))
	task_list.append(my_task(name="thread_3", priority = 1, period = 60, execution_time = 30, last_execution = last_execution))



	# Global scheduling loop
	while(1):

		print("\nScheduler tick : " + datetime.datetime.now().strftime("%H:%M:%S"))
		
		# Reinit watchdog
		watchdog = False
		my_watchdog.current_cpt = 10
	
		for task_to_run in task_list :
		
			# Reinit watchdog
			watchdog = False
			my_watchdog.current_cpt = 10
		
			task_to_run.run()
			
			
			
		
		
		



