# Submission for UBC LHD Build Day (Theme: "diversity, inclusivity, and accessibility")
## The Problem
In the USA, there are 250 000 to 500 000 individuals who know ASL. Out of the total population, that is .2%. Most of these indivudals are deaf or hard of hearing, and in order to interact with the world, must rely on observing mouth patterns, which can be difficult due to each indivudals unique speech pattern. 


### Our Solution 
Our solution is a web app that quickly translates speech to ASL. Users can either type or speak directly to the webapp, and in return, are given a translation of their speech in ASL. A Google cloud API that utilizes neural networks is able to translate speech with astounding accuracy. The app is easy to use, and more efficent than searching up commands. This creates a pathway for those hard of hearing and those who have never been introduced to ASL.

### How we built it
0. **Installing Python**  <br>
We will be using `Python 3.6.5` for this workshop. If you have another version of Python, it should still work but you may run into dependency issues. Here's the link to the [download for Python 3.](https://www.python.org/downloads/release/python-365/) Check if you've installed it properly by making sure you can run `python` and `pip` in the terminal.

1. **Installing Git** <br>
Git is a version control tool. You'll use this to download the repository and switch between branches! You can download the command line version here https://git-scm.com/downloads or if you prefer the GUI, https://www.gitkraken.com/

2. **Project setup** <br>
Clone this project somewhere convenient. You can do this by opening your command prompt and navigating to a convenient folder. <br><br>
e.g. `cd ~/Documents` <br><br>
Then `git clone https://github.com/jackyzha0/lhd-build-python-webapp` and change directory into the folder `cd lhd-build-python-webapp`.

3. **Installing dependencies** <br><br>
There are a few Python libraries we will be using today that will help us build today's app. <br> <br>
`pip install flask requests`

4. **API Keys** <br><br>
Near the end of the workshop, we'll be integrating our app with the Google Maps API. Go ahead and get that key here: https://developers.google.com/places/web-service/get-api-key. Follow the 5 steps to get your API key. Create a file called `secrets.txt` with your API key and put that in this folder. You'll need it later!

### 1. The Backend
**What is a backend?**

"Backend" code is the stuff that powers everything on the internet from behind the scenes.

**What is Flask?**

Flask is a *web framework* written in python. Basically, it gives you the basic tools to build a web application, meaning you can serve websites and other cool stuff.

**Getting started**

Great, so how do I get started? If you've set up the project properly, you should find the `main.py` file in the folder. Open it up with your editor of choice. We've provided 3 examples in the file. We can get our `Flask` server up and running by executing `python main.py`.
