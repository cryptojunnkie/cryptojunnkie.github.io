# cryptojunnkie.github.io
always cd into the main file before running it

Polynomial Reversion Chart

Clone the repository
Go to the folder where you want to store your project, and clone the new repository:

git clone https://github.com/cryptojunnkie/cryptojunnkie.github.io

Hello World
Enter the project folder and add an index.html file:

cd username.github.io

echo "Hello World" > index.html

# Push it
# Add, commit, and push your changes
# commit and push changes to github :

git add --all

git commit -m "Initial commit"

git push -u origin main

…and you're done!
# website to see the chart
Fire up a browser and go to https://cryptojunnkie.github.io

# cron times and how they work

*     *     *     *     *
-     -     -     -     -
|     |     |     |     |
|     |     |     |     +----- Day of the week (0 - 7) (Sunday is 0 or 7, Monday is 1, etc.)
|     |     |     +------- Month (1 - 12)
|     |     +--------- Day of the month (1 - 31)
|     +----------- Hour (0 - 23)
+------------- Minute (0 - 59)

# If you decide to change the scheduled time:

Modify the hour field to the desired UTC hour in 24-hour format, and update the minute field if necessary.
Confirm that the current time and time zone conversion align with the schedule you intend based on your local time.

#user
The time difference between UTC (Coordinated Universal Time) and New York time varies depending on the time of year due to Daylight Saving Time (DST) adjustments. New York follows Eastern Time Zone (ET), which is either UTC-5 hours or UTC-4 hours during DST.

As a general guideline:

Standard Time (Fall/Winter):

The time difference between Eastern Standard Time (EST) and UTC is UTC-5 hours.
Daylight Saving Time (Spring/Summer):

The time difference between Eastern Daylight Time (EDT) and UTC is UTC-4 hours.