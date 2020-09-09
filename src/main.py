from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.list import TwoLineAvatarIconListItem
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.textfield import MDTextField
import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import ThreadedFTPServer,FTPServer
import threading
import netifaces as ni
import logging 
import plyer
#  buildozer android debug deploy run |  buildozer android logcat

def get_wl_ip():
 try:
    try:
      wl_ip=ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
      proceed=True
    except KeyError:
        toast("Turn on hotspot")
        proceed=False
        wl_ip=None
        

 except ValueError:
  try:
   wl_ip=ni.ifaddresses('wlo1')[ni.AF_INET][0]['addr']
   proceed=True
  except KeyError:
    wl_ip=None
    proceed=False
 return proceed,wl_ip


KV = '''
<TogglePage>:
    GridLayout:
        cols:1
        size: root.width, root.height
        MDToolbar:
            title: "FTPServer"
            anchor_title: 'center'
            left_action_items: [["rss", lambda x:'']]
            right_action_items:[["settings", lambda x:app.change()]]
        
    
        FloatLayout:
            MDSwitch:
                id:switch
                label:"its in"
                pos_hint: {'center_x': 0.5, 'center_y':0.9}
                on_active:app.start_server() if switch.active else app.stop_server()
            MDLabel:
                pos_hint: {'center_x': 0.90, 'center_y':0.80}
                text:"Server running" if switch.active else ''
            

<SettingsPage>:
    GridLayout:
        cols:1
        MDToolbar:
            title: "Settings"
            anchor_title: 'center'
            left_action_items: [["rss", lambda x: '']]
            right_action_items: [["chevron-left", lambda x:app.change_()]]

        TwoLineAvatarIconListItem:
            text: "Port"
            secondary_text: "Port used by ftp server"
            on_press:app.show_alert_dialog_port()

            IconLeftWidget:
                icon: "nature"
        
        TwoLineAvatarIconListItem:
            text: "Passive Port"
            tertiary_text:"Passive Port used by ftp server"
            on_press:app.show_alert_dialog_passive_port()

            IconLeftWidget:
                icon: "account"

            
        TwoLineAvatarIconListItem:
            text: "User name"
            secondary_text: "User name(empty to disable user log in)"
            on_press:app.show_alert_dialog_username()

            IconLeftWidget:
                icon: "account"




        TwoLineAvatarIconListItem:
            text: "User password"
            secondary_text: "User password"
            on_press:app.show_alert_dialog_password()

            IconLeftWidget:
                icon: "key"



        
    
'''

def run_(server,port_number=1024):
        toast("Running server at "+str(port_number))
        server.serve_forever()

def stop_(server,proceed,port_number=1024):
    if(proceed==True):
      toast("Stopped server running at "+str(port_number))
      server.close_all()


  
class TogglePage(Screen):
    pass

class SettingsPage(Screen):
    pass



class Test(MDApp):
    dialog = None
    def build(self):
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.theme_style = "Light" 
        # from android.permissions import request_permissions, Permission
        # request_permissions([Permission.READ_EXTERNAL_STORAGE],Permission.READ_EXTERNAL_STORAGE)
        # from android.storage import primary_external_storage_path
        # self.path_sd=primary_external_storage_path()
        Builder.load_string(KV)
        self.sm=ScreenManager()
        self.sm.add_widget(TogglePage(name="toggle_page"))
        self.sm.add_widget(SettingsPage(name="settings_page"))
        return  self.sm
    
    def change(self):
        self.sm.transition.direction = 'left'
        self.sm.current="settings_page"
    def change_(self):
        self.sm.transition.direction = 'right'
        self.sm.current="toggle_page"
    
    def start_server(self):
        logging.info("started")
        try:
         if(self.port_number):
            print(self.port_number)
        except:
          self.port_number=1024

        authorizer = DummyAuthorizer()
        try: 
            try:
             authorizer.add_user(str(self.username),str(self.password),'.', perm='elradfmwMT')
            
            except AttributeError:
                try:
                 authorizer.add_user(str(self.username),'12345','.', perm='elradfmwMT')
                
                except:
                 authorizer.add_user('user',str(self.password),'.', perm='elradfmwMT')
                 


        except AttributeError :
            authorizer.add_user('user', '12345', '.', perm='elradfmwMT')
        self.proceed,self.wl_ip=get_wl_ip() 
        if(self.proceed==True):
            logging.info("passed")
            # authorizer.add_anonymous(os.path.join(self.path_sd))###for android
            authorizer.add_anonymous(os.getcwd())# for desktop mention path
            # logging.info(os.listdir(self.path_sd))
            handler = FTPHandler
            handler.authorizer = authorizer
            handler.banner = "pyftpdlib based ftpd ready."
            try:
             handler.passive_ports = range(self.range1,self.range2)
             logging.info("changed passive ports")
            except:
             handler.passive_ports=range(2300,2399)
             logging.info("default passive ports")
            logging.info(self.wl_ip)
            logging.info(self.port_number)
            address = (self.wl_ip, self.port_number)
            self.server = ThreadedFTPServer(address, handler)
            logging.info(self.server)
            self.server.max_cons = 256
            self.server.max_cons_per_ip = 5
            logging.info("passed that max_cons")
            t1=threading.Thread(target=run_,args=(self.server,self.port_number))
            logging.info("thread assigned")
            t1.start()
            self.show_notification()
            logging.info("Thread started")
        else:
            toast("Try turning on hotspot and try again")
        
    def show_alert_dialog_port(self):       
            self.dialog = MDDialog(
                title="Port:",
                type="custom",
                content_cls=MDTextField(),
                buttons=[
                    MDFlatButton(
                        text="Ok", text_color=self.theme_cls.primary_color,on_press=self.outport
                    ),
                    MDFlatButton(
                        text="Cancel", text_color=self.theme_cls.primary_color,on_press=self.dialog_close
                    ),
                ],
                size_hint=(0.9,1)
            )
            try:
                #setting port number that is saved
                self.dialog.content_cls.text=str(self.port_number)
            except AttributeError:
                #setting default if no value is set
                self.dialog.content_cls.text="1024"
            
            self.dialog.open()

    def show_notification(self):#for showing notification when server starts
        plyer.notification.notify(title='FTPServer', message="Server ready at "+"ftp://"+str(self.wl_ip)+":"+str(self.port_number))

    def show_alert_dialog_username(self):
            self.dialog = MDDialog(
                title="Change Username?",
                type="custom",
                content_cls= MDTextField(hint_text="color_mode = 'custom'"),
                buttons=[
                    MDFlatButton(
                        text="save", text_color=self.theme_cls.primary_color,on_press=self.outusername
                    ),
                    MDFlatButton(
                        text="close", text_color=self.theme_cls.primary_color,on_press=self.dialog_close
                    ),
                ],
                size_hint=(0.9,1)
            )
            try:
                #setting port number that is saved
                self.dialog.content_cls.text=str(self.username)
            except AttributeError:
                #setting default if no value is set
                self.dialog.content_cls.text="user"
            self.dialog.open()
    
    def show_alert_dialog_password(self):
            self.dialog = MDDialog(
                title="Change Password?",
                type="custom",
                content_cls= MDTextField(helper_text_mode="on_error"),
                buttons=[
                    MDFlatButton(
                        text="save", text_color=self.theme_cls.primary_color,on_press=self.outpassword
                    ),
                    MDFlatButton(
                        text="close", text_color=self.theme_cls.primary_color,on_press=self.dialog_close
                    ),
                ],
                size_hint=(0.9,1)
                
            )
            try:
                #setting port number that is saved
                self.dialog.content_cls.text=str(self.password)
            except AttributeError:
                #setting default if no value is set
                self.dialog.content_cls.text="12345"
            self.dialog.open()
        
    def show_alert_dialog_passive_port(self):
            self.dialog = MDDialog(
                title="Change Passive Port?",
                type="custom",
                content_cls= MDTextField(),
                buttons=[
                    MDFlatButton(
                        text="save", text_color=self.theme_cls.primary_color,on_press=self.passive_port_range
                    ),
                    MDFlatButton(
                        text="close", text_color=self.theme_cls.primary_color,on_press=self.dialog_close
                    ),
                ],
                size_hint=(0.9,1)
                
            )
            try:
                #setting passive port number that is saved
                self.dialog.content_cls.text=str(self.range1)+"-"+str(self.range2)
            except AttributeError:
                #setting default if no value is set
                self.dialog.content_cls.text="2300-2399"
            
            self.dialog.open()
        


    def outport(self,val):
        try:
            self.port_number=int(self.dialog.content_cls.text)
            self.dialog.content_cls.text=str(self.port_number)
            
        except:
            toast("enter valid port")
            self.dialog.content_cls.text=""
        
        self.dialog_close()

    def outusername(self,val):
        self.username=self.dialog.content_cls.text
        self.dialog_close()

    def outpassword(self,val):
        self.password=self.dialog.content_cls.text
        self.dialog_close()

    def passive_port_range(self,val):
     try:
        ranges=self.dialog.content_cls.text
        range_=ranges.split('-')
        self.range1=int(range_[0])
        self.range2=int(range_[1])
     except:
         toast("enter in valid format \n eg:1200-1299")
       
     self.dialog_close()


    def dialog_close(self, *args):
        self.dialog.dismiss(force=True)


    def stop_server(self):
     print(self.proceed)
     logging.info("stopping server")
     try:
        t2=threading.Thread(target=stop_,args=(self.server,self.proceed,self.port_number))
        t2.start()
     except AttributeError:
         pass

        
Test().run()

