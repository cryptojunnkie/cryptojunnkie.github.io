# Polynomial Reversion Chart

## Website Link
Explore the chart at [cryptojunnkie.github.io](https://cryptojunnkie.github.io)

## How to Run the Code
1. Navigate to your desired folder in the terminal.
   IN THE TERMINAL TYPE THE BELOW REFERENCE:
   cd foldername  # Replace foldername with your folder name

Clone the repository:
IN THE TERMINAL TYPE THE BELOW REFERENCE:
git clone https://github.com/cryptojunnkie/cryptojunnkie.github.io

Access the project folder:
IN THE TERMINAL TYPE THE BELOW REFERENCE:
cd cryptojunnkie.github.io

Save and run the code to generate index.html:
IN THE TERMINAL TYPE THE BELOW REFERENCE:
python price_chart.py

Once you run the main code it will generate the index.html doc for you. After the index.html is created, ensure to save it.

To visualize the chart, run it on a live server: Right-click on index.html and run it in a live server to confirm proper functionality.

Once validated, push your changes to github, ensure you have saved the .py and html code before pushing to github:
IN THE TERMINAL TYPE THE BELOW REFERENCE:
git add --all
git commit -m "Initial commit"
git push -u origin main
Explore the chart @ cryptojunnkie.github.io

# Cron Time Settings and Adjustments
The following illustrates the cron time configuration:


*     *     *     *     * 
-     -     -     -     - 
|     |     |     |     | 
|     |     |     |     +----- Day of the week (0 - 7) (Sunday is 0/7, Monday is 1, etc.)
|     |     |     +------- Month (1 - 12)
|     |     +--------- Day of the month (1 - 31)
|     +----------- Hour (0 - 23)
+------------- Minute (0 - 59)
Adjusting the Scheduled Time
To modify the scheduled time, follow these steps:

Update the hour field to your desired UTC hour in 24-hour format.
If necessary, adjust the minute field.
Verify that the current time and time zone conversion align with your intended schedule based on your local time.
Time zone considerations
The time difference between Eastern Standard Time (EST) and UTC is UTC-5 hours. During Daylight Saving Time (EDT), the difference is adjusted to UTC-4 hours. This information is particularly relevant for converting cron schedules to local time.



