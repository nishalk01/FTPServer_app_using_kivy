# FTPServer_app_using_kivy
<h4>is an application built using kivy and kivymd for UI all the app does is setup ftpserver on the device so that u can use it transfer files</h4>



| Home page                                                                                                     | Settings page |
| ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------|
| ![image](https://github.com/nishalk01/FTPServer_app_using_kivy/blob/master/screenshots/ftpserverv0.1.0.jpeg)  | ![image](https://github.com/nishalk01/FTPServer_app_using_kivy/blob/master/screenshots/ftpserver2.jpeg)  |


<h2>You can find already built apk file <a href="https://github.com/nishalk01/FTPServer_app_using_kivy/blob/master/screenshots/ftpserver2.jpeg">here</a></h2>
<h4>How to use the app</h4>
<h4>Lets say you want to transfer file between mobile and a computer,Make sure You have both connected through hotspot(from mobile)</h4>
  
<h3>Step1:</h3>:Open App(on mobile phone) and click on the switch button to turn on ftpServer
<h3>Step2:</h3>:Check your Notification to see if there is a notification from the app<br>

![image](https://github.com/nishalk01/FTPServer_app_using_kivy/blob/master/screenshots/Notification.jpeg)

<h3>Step3:</h3>Type that out in your computer browser(in my case it was ftp://192.168.43.1:1024) and enter it should show something like this in your browser<br>


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
<h4>To build the app use buildozer you can refer to buildozer.spec file in the repo and also make sure uncomment code present in <code>main.py</code></h4>


    



