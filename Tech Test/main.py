import time
# to genrante the schedule
class TrainIndicator:
    def __init__(self,schedule,current_time=0) -> None:
        self.schedule = {
            key:self.generateSchedule(*args)
        for key , args in schedule.items()
        }
        self.current_time = current_time
    # get next arrival time 
    def getNextArrival(self,train_schedule, current_time):
        for arrival in train_schedule:
            if arrival >= current_time:
                return arrival
        return train_schedule[0] + 1440 # add next day
    def generateSchedule(self,starttime:str, interval:int,endtime:str):
        '''
        eg: starttime=12:30
        eg: endtime=12:30
        '''
        Shour,Smin = [int(t) for t in starttime.split(":")]
        Ehour,Emin = [int(t) for t in endtime.split(":")]
        start = (Shour*60)+Smin
        end = (Ehour*60)+Emin
        if end<start:end+=1440 # add next day
        print(start,end,interval)
        schedule =[(i%1440) for i in range(start,end,interval)]
        schedule.sort()
        return schedule
    def checkTraninInNext(self,n=15):  # n=15 for next 15 VT mins
        # creating empty list for next trains
        nextTrains = []
        for destination,scheduleTime in self.schedule.items():
            arrival = self.getNextArrival(scheduleTime,self.current_time)
            if arrival-self.current_time <=n:
                nextTrains.append((destination,(arrival-self.current_time)))
        nextTrains.sort(key=lambda x: x[1])
        messege = f"Current Virtual Time: {self.current_time // 60:02d}:{self.current_time % 60:02d}\n"
        count = 1
        for train in nextTrains[:2]:
            messege  += f"{count}. Destination: {train[0]}, Arrival in {train[1]} VT minutes\n"
            count +=1
            
        # clear the screen 
        print("\033c", end="")
        print(f"{messege}")
    # display the screen infiniry
    def display(self):
        while True:
            self.checkTraninInNext()
            time.sleep(1)
            self.current_time = (self.current_time+1)%1440
        
if __name__== "__main__":
    schedule = {
        "Central" : ("00:00",20,"23:59") , # Station Every 20mins
        "Circular" : ("00:00",60,"23:59") , # Station Every hour on the hour
        "North Square" : ("07:00",12,"22:00") , # Station Every 12mins from 07:00 until 22:00
        "West Market" : ("05:30",6,"01:30")  # 6mins from 05:30 until 01 :30
    }
    currenttime = 5*60 # 05:00
    indicator = TrainIndicator(schedule,current_time=currenttime)
    indicator.display()
    