#this script helps you to to create a new cover letter without having to manually
#copy and paste the job details; think of it as a professional version of a Mad Lib 

import datetime


filename = input('enter an appropriate name for the file (wihtout extension)\n')
job_title = input('enter the specific title of the position (e.g. new grad software engineer - linux kernel)\n')
generic_title = ('enter a generic term for the position(e.g. software engineer)\n')
company = input('enter the name of the company\n')
job_field = input('enter the field the job is in (e.g. software engineering)\n')
contribution = input('enter the kind of contribution you would make in the field (e.g. meaningful, timely)\n')
team_name = input('name of the team/dept you are applying to\n')
today = datetime.datetime.now()
today = today.strftime("%d %B %Y")
found_on = input('did you find this job on LinkedIn (y/n)')
if found_on == 'y':
    found_on = 'LinkedIn'
else:
    found_on = input('Where did you find the job posting')


with open('coverlettertemplate.txt') as tmp:
    template = tmp.read()

template = template.replace('SOURCE',found_on)
template = template.replace('TODAY',today)
template = template.replace('JOBTITLE',job_title)
template = template.replace('GENERICTITLE',generic_title)
template = template.replace('COMPANY',company)
template = template.replace('ADJ',contribution)
template = template.replace('TEAM',team_name)
template = template.replace('FIELD',job_field)


with open((filename)+'.txt','w') as f:
    f.write(template)

    