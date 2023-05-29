# DEFCON'23 Quals Scoreboard

## Usage
run `./crontab.sh` to fetch new scores and stores log in a pickle file `logs.p`, the output html will be written to `~/htdocs/defcon_quals/scoreboard.html`, change the path in the code to your destination

Demo: https://www.csie.ntu.edu.tw/~jason/defcon_quals/scoreboard.html

## Set up automatic fetch 
run `crontab -e`
```crontab
* * * * * /home/dept/ta/jason/scoreboard/crontab.sh
```