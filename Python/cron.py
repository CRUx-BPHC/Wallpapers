from crontab import CronTab
cron = CronTab(user='username')

def defineJob(hour):
    job = cron.new(command='python getWallpapers.py',comment='getWallpapers')
    job.hour.every(hour)
    cron.write()
    print (job.enable())

def printJobs():
    for job in cron:
        print(job)

def remove():
    cron.remove_all(comment='getWallpapers')


defineJob(11)
printJobs()