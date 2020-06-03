# NameMC Friend Bot ! [![Python 3.x](https://img.shields.io/badge/PYTHON-3.X-blueviolet?style=for-the-badge)](http://www.python.org/download/)

Feeling lonely ? Get some friends !

## Built with ❤️ by

* [portalthree](https://github.com/portalthree) - The creator of the script

### 🤔 But how does it work ?

Its really easy ! 
It uses [![Selenium](https://img.shields.io/badge/SELENIUM-yellow?style=flat-square)](https://www.selenium.dev/downloads/) and [![Requests](https://img.shields.io/badge/REQUESTS-gray?style=flat-square)](https://requests.readthedocs.io/en/master/). 
Its basicly logging in your NameMC account, going to search people from [CoderTim](https://fr.namemc.com/profile/CoderTim.1) friend list (which is one of the people that has the most friends on the platform), get their username and then its going to bring you to the user in question NameMC profile and click a simple button to add them as a friend !

#  ⚠️ BE CAREFUL YOU CAN ONLY HAVE 50 FRIEND REQUESTS AT THE SAME TIME

### 📚 Ok but how do i install it ?
(search for tutorials on how to install python before doing this)
First of all, find your google chrome version.
You found it ? Ok cool
>If you are using Chrome version 84, please download [ChromeDriver 84.0.4147.30](https://chromedriver.storage.googleapis.com/index.html?path=84.0.4147.30/)
>If you are using Chrome version 83, please download [ChromeDriver 83.0.4103.39](https://chromedriver.storage.googleapis.com/index.html?path=83.0.4103.39/)
>If you are using Chrome version 81, please download [ChromeDriver 81.0.4044.138](https://chromedriver.storage.googleapis.com/index.html?path=81.0.4044.138/)
>

You will have something like this
![You will have something like this](https://cdn.discordapp.com/attachments/612940686077198346/717813044675084449/unknown.png)
Download the win32 version on windows, linux64 on linux ect...

Now you will need to extract the .zip file.
Once you extracted the .zip file, at line 5 if the code, you will have something like this
> driver = webdriver.Chrome(executable_path=r'C:\Users\User\Documents\chromedriver_win32\chromedriver.exe')
>
You will want to modify the C:\Users\User\Documents\chromedriver_win32\ and put the folder where you extracted the chromedriver.exe 

Did it ? Awesome ! :)

You will now see at line 13 this
> driver.find_element_by_id("email").send_keys("EMAIL@domain.com")
>
You will want to replace the "EMAIL@domain.com" with your own email adress. DO NOT REMOVE THE "" ONLY THE EMAIL PART

Its going to be the same with the password, at line 17
>driver.find_element_by_id("password").send_keys("ENTER YOUR PASSWORD HERE")
>
Modify it with your namemc password.

Once you did all of this, you are almost done ! 
You only need to install the requirements !

You will need to open a command prompt in the folder you were in, just search how to do this on google its really simple.

Once you got your command prompte type pip install -r requirements.txt

and Voila!