# Job Alert Bot

### About
Job Alert "Bot" is a Python script that scrapes job links from LinkedIn job alert emails. Currently, this script is being utilized by a personal Discord bot that posts jobs almost daily. This was a personal project to help friends and colleagues with their job hunt during their busy schedules. Since this script was intended for use by a Discord bot, there are no functions to export the job links to a file.

### How does it work
This script uses Python's email and imaplib library to connect to an email specifically created to receive LinkedIn job alert emails. Then it takes in all available emails in the inbox and parses the HTML page using BeautifulSoup. 

### Future Plans
Previous versions of this script used to be able to grab the job title, company, and location alongside the link. Due to latency issues with the Discord bot, the script does not search for those fields. In future updates, the script will be able to grab more information.

- [ ] Automate script to scrape emails at 11:50PM everyday
- [ ] Implement export function to save job information
- [ ] Work with getting Indeed, Glassdoor, and Handshake emails to scrape properly
- [ ] Figure out how to automate job alert creation
