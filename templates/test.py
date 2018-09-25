import requests

new_num = 1

for i in range(100):
    new_num += 1
    requests.post("http://teamgold.iw-c.co.uk/add-player", data={"player_name": "j" + str(new_num)})


#requests.post("http://ateam.iw-c.co.uk/", data= {"leaderboard_name":"j" + str(new_num)})
#requests.post("http://team1.iw-c.co.uk/leaderboard", data={"new_lb_name": "TEST" + str(new_num)})