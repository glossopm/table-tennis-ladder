import requests

new_num = 1

for i in range(1000000):
    new_num += 1
    requests.post("http://ateam.iw-c.co.uk/", data= {"leaderboard_name":"j" + str(new_num)})
    #requests.post("http://team1.iw-c.co.uk/", data={"new_lb_name": "james" + str(new_num)})
