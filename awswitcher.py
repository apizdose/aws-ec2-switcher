import boto3
from datetime import datetime
import pytz
import time

#Your credentials here
Access_key_ID = '***********************'
Secret_access_key = '*************************'
#Your availability zone
region = '***********************'
#Instance id here
instance = '*********************'
#Hours activity
work_hours="9:00-17:00"
#Set timezone
timezone='Europe/Kiev'

work_hours = work_hours.split('-')
ec2 = boto3.client('ec2',region, aws_access_key_id=Access_key_ID, aws_secret_access_key=Secret_access_key)
#Return current machine time
def timer(timezone):
    tzinfo = pytz.timezone(timezone)
    clock = datetime.now().astimezone(tzinfo)
    current_time = clock.strftime("%H:%M")
    return current_time

#On\Off insance
def switcher(current_time):
    global runningState
    if current_time == work_hours[0]:
        try:
            #Starting instance
            print('Starting')
            ec2.start_instances(InstanceIds=[instance])
        except Exception as e2:
            error2 = "Error2: %s" % str(e2)
            print(error2)
        #Waitin a min, to not repeat func
        time.sleep(60)
    elif current_time == work_hours[1]:
        try:
            #Stop instance
            print('Stopping')
            ec2.stop_instances(InstanceIds=[instance])
        except Exception as e2:
            error2 = "Error2: %s" % str(e2)
            print(error2)
        time.sleep(60)
      

def main():        
    while True:
        switcher(timer(timezone))
        time.sleep(5)       
        
        
if __name__ == '__main__':
    main()

    
