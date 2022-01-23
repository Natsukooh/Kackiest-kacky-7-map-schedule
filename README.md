# Kackiest Kacky 7 map schedule

## Intro
When I am writing these lines, the date is january the 23rd, 2022.  
  
Kackiest kacky 7 is currently happening, and will end in 8 days. Right now we have 3 players at 74 maps finished (ninion, simo and tres), and none at 75.  
I like to open [simo's stream](twitch.tv/simo_900) when the one map he hasn't finished yet is being played, but due to the constant map rotation on the kacky servers, it only happens every 6 hours approximatly.  
The [kackiest kacky map schedule](https://kacky.dingens.me/) website is a great website which can tell you when will be played a specific map. It is very useful to know when to open the stream or to open the game and spectate a specific player you want to see. But I thought it would be good to have a command-line tool that would do the same, just to be able to see it quickly, without having to go to the site and type the multiple maps you're interested in.  
  
So I created this little tool in a few minutes to satisfy my need.
  
This script makes requests to the [kackiest kacky map schedule](https://kacky.dingens.me/) website I mentionned earlier ; thanks to them for this amazing website. You can go check their work [here](https://github.com/dremerb/kacky_maptimes).

## Usage
```bash
./kacky.py MAP_NUMBERS...
```

where MAP_NUMBERS are any number of kkackiest kacky 7 maps names. You can type as much map numbers as you want.
  
The fact that the script can be executed without specifying a python interpreter is because of the first line of the program, specifying a standard path of the python interpreter, which is /usr/bin/python3 ; if you get an error saying :
```bash
-bash: ./kacky.py: /usr/bin/python3: bad interpreter: No such file or directory
```
then you need to specify the python interpreter when running the script ; assuming you have a <code>python</code> command in your environment (can also be python3 or something like that), try this :
```bash
python kacky.py MAP_NUMBERS...
```

## Requirements
You can probably tell it : the script of course needs a python 3 interpreter to run.
Moreover, the python packages used are : sys, re and requests. I think sys and re are part of the python standard library, but requests is not (I'm not sure) ; make sure it is installed running
```bash
pip install requests
```
Last, you need to be connected to internet to run the script, since it works by making requests to the [kackiest kacky map schedule](https://kacky.dingens.me/) website.

## Contribution
This is only a quick one-shot utilitary script. However, if you think about some feature to add, feel free to clone the repo to add it.

## Contact
Feel free to DM me on Discord : Natsuko#4825
