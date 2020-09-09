# FTPServer_app_using_kivy
<h4>is an application built using kivy and kivymd for UI all the app does is setup ftpserver on the device so that u can use it transfer files</h4>



| Home page                                                                                                     | Settings page |
| ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------|
| ![image](https://github.com/nishalk01/FTPServer_app_using_kivy/blob/master/screenshots/ftpserverv0.1.0.jpeg)  | ![image](https://github.com/nishalk01/FTPServer_app_using_kivy/blob/master/screenshots/ftpserver2.jpeg)  |


<h2>You can find already built apk file <a href="https://drive.google.com/file/d/1Upq-P3JjLySYnxHBVO4kb9poUQTsx4fA/view?usp=sharing">here</a></h2>
<h4>How to use the app</h4>
<h4>Lets say you want to transfer file between mobile and a computer,Make sure You have both connected through hotspot(from mobile)</h4>
  
<h3>Step1:</h3>Open App(on mobile phone) and click on the switch button to turn on ftpServer
<h3>Step2:</h3>Check your Notification to see if there is a notification from the app<br>

![image](https://github.com/nishalk01/FTPServer_app_using_kivy/blob/master/screenshots/Notification.jpeg)

<h3>Step3:</h3>Type that out in your computer browser(in my case it was ftp://192.168.43.1:1024) and enter it should show something like this in your browser<br>

<h3>You can also write your own ftpclient like the one i use you can refer to that code <a href="https://github.com/nishalk01/automating_anime_video_transfer_using_ftplib">Here</a>
  
![image](https://github.com/nishalk01/FTPServer_app_using_kivy/blob/master/screenshots/browser.png)


<h3>How to run the code</h3><br>
<h2>Step1:Installation</h2>
<h4>Assuming you have pip3 and python3 installed in your system install the following packages</h4>
<ul>
  <li><code>pip3 install kivy</code></li>
  <li><code>pip3 install kivymd</code></li>
  <li><code>pip3  install netifaces</code></li>
  <li><code>pip3  install pyftpdlib</code></li>
  <li><code>pip3  install plyer</code></li>
</ul>

<h4>Now that you have all the dependencies run the program that will open up app window</h4>
<h4>To build the app use buildozer you can refer to <code>src/buildozer.spec</code> file in the repo and also <h3>make sure uncomment code present in<h3> <code>src/main.py</code> and comment the desktop ones</h4>
  
# References:
<ul>
  <li>https://kivymd.readthedocs.io/en/latest/</li>
  <li>https://pyftpdlib.readthedocs.io/en/latest/tutorial.html#a-base-ftp-server</li>
</ul>


    



