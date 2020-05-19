In this project, I tested whether there was a statistically significant difference in preventative care options for low income Americans after the Affordable Care Act (ACA) was implemented. I scraped data from the Behavioral Risk Factor Surveillance System (BRFSS), which is the largest continuously-conducted health survey in the world, for 5 New England states (Rhode Island, Massachusetts, Connecticut, New Hampshire, and Vermont). I tested if the ACA increased low-income residents' access to preventative care using the following metrics: healthcare coverage, cost barrier to seeking medical help, self-reported health, and checkup frequency.


The health data files (2011-2014.rds and 2015-2018.rds) are a collection of phone polls from the Behavioral Risk Factor Surveillance System. Each row represents a voluntary participant in the phone poll that asked an upwards of 450 questions. The participant could end the call at any time or opt out of a question. These files are filtered to only look at the columns of interest.

Statistical tests are in stats jupyter notebook. A summary of the results are detailed in the results pdf.

—————————————————————————————————————————————
Variable naming conventions:


Columns filtered in the dataset: 'xstate', 'genhlth', 'hlthpln1', 'numadult', 'race', 'income2', 'physhlth', 'poorhlth', 'persdoc2', 'checkup1', 'exerany2', 'sex', 'educa', 'numadult.1', 'children', 'employ', 'flushot5', 'howlong', 'lastpap2', 'lastsig3', 'hadsigm3', 'xhcvu651', 'medcost', 'year', 'drvisits', 'medscost'

Variables tested:

Each line in the file contains one participant in the phone interview. 

a. xstate - the state the interviewee is from (1= Alabama, 2 = Alaska, 3 = Arizona, etc.)

b. genhlth - general health of the participant (integer value 1-7,9 where 1 is excellent and 5 is poor, 7 is not sure and 9 is refused)

c. hlthpln1 - health plan: do you have any health care coverage? (1 = yes, 2 = no, 7 = not sure, 9 = refused)

d. numadult - number of adults in household

e. race - race of participant

f. income2 - income range

g. physhlth- physical health : for how many days in the past 30 days was your health not good (integer between 1-30, 88 = None, 77 = not sure, 99 = refused)

h. poorhlth- poor physical or mental health: how many days did your poor physical or mental keep you from doing your usual activities (integer between 1 and 30, 88 = None, 77 = not sure, 99 = refused )

i. persdoc2- personal doctor: Do you have one person you think of as your personal doctor or health care provider? (1= yes, one, 2= more than one, 3 = no, 7 = not sure, 9 = refused)

j. checkup1- length of time between last checkup (1 = less than 12 months ago, 2 = over 1 year but less than 2, 3= over 2 years but less than 5 years, 4 = 5 or more years, 7 = not sure, 8 = never, 9 = refused)

k. exerany2- exercise: did you participate in any physical activity besides your job in the past month?(1= yes, one, 2= more than one, 3 = no, 7 = not sure, 9 = refused)

l. sex- what is your sex: (1 = male, 2 = female, 7 = not sure, 9 = refused)

m. educa- education level: What is the highest grade or year of school you completed? ( 1 = never attended school, 2 = elementary/middle school(grades 1 -8), 3 = high school (grades 9-11), 4 = high school graduate(12 or GED), 5 = college (1-3 years), 6 = college ( 4 years or more), 9 = refused)

n. children - number of children

o. employ- employent status: what is your current employment status? (1 = employed for wages, 2 = self-employed, 3 = out of work for 1 year or more, 4 = out of work for less than 1 year, 5 = a homemaker, 6 = a student, 7 = retired, 8 = unable to work, 9 = refused)

p. flushot5- adult flu shot: During the past 12 months, have you had either a flu shot or a flu vaccine that was sprayed in your nose? (1 = yes, 2 = no, 7 = not sure, 9 = refused)

q. Howlong: mammogram: how long has it been since your last mammogram? ( 1 = less than 12 months, 2 = within past 2 years, 3 = within past 3 years, 4 = within the past 5 years, 5 = 5 or more years ago, 7 = not sure, 9 = refused)

r. lastpap2: How long has it been since your last Pap test? (1 = within 12 months, 2 = within the past 2 years, 3 = within the past 3 years, 4 = within the past 5 years, 5 = 5 or more years ago, 7 = not sure, 9 = refused)

s. lastsig3: sigmoidoscopy/colonoscopy: How long has it been since your last sigmoidoscopy to colonoscopy? ( 1 = less than 12 months, 2 = within past 2 years, 3 = within past 3 years, 4 = within the past 5 years, 5 = within past 10 years, 6 = 10 or more years ago, 7 = not sure, 9 = refused)

t. hadsigm3: sigmoidoscopy/colonoscopy: Have you ever had a sigmoidoscopy or colonoscopy? (1 = yes, 2 = no, 7 = not sure, 9 = refused)

u. hlthcvr1- Primary Health Care Coverage: What is the primary source of your health care coverage? (1 = plan through employer, 2 = a plan bought by you or another family member, 3 = medicare, 4 = medicaid or other state program, 5 = tricare, VA, or Military, 6 = Alaska Native, Indian Health Service. Tribal Health Services, 7 = some other source, 8 = no coverage, 77 = not sure, 99 = refused)

v. medcost- could not see doctor because of cost: Was there a time in the past 12 months when you needed to see a doctor but could not because of cost? (1 = yes, 2 = no, 7 = not sure, 9 = refused)

w. Year- a column we created that indicates the year the participant answered the phone survey (integer between 2014 and 2018)

x. drvisits- How many times have you been to a doctor, nurse, or other health professional in the past 12 months? (Integer 1- 76, 88 = None, 77 = not sure)

y. medscost- Not including over-the-counter (OTC) medications, was there a time in the past 12 months when you did not take your medication as prescribed because of cost?( 1 = yes, 2 = no, 3 = no medication was prescribed, 7 = not sure, 9 = refused)

