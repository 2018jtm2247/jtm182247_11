#application for students and admin of a college
#Created by: Priyanshu Aggarwal

import kivy 
kivy.require('1.10.1')

import operator
import matplotlib.pyplot as plt 
import numpy as np

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from systemd import login
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp
from kivy.core.image import Image as CoreImage
from kivy.graphics import Color, Rectangle
#for popup
from kivy.uix.popup import Popup
from kivy.uix.button import Button
#from kivy.uix.listview import ListItemButton
#Global variables
login_successfull = False
first_entry = True
E_number = ''
user = ''
login =''


###################################################################################################
#Initial page ...select Admin or Student
class WelcomePage(Screen):
    def login_as(self,argc):
        global user
        user = argc
        self.manager.current = "login_page"   #go to login_page
         
######################################################################################################        
    


class LoginPage(Screen):
    checkbox_is_active = ObjectProperty(False)
    
    def verify_credentials(self):
        global login_successfull
        login_successfull = False
        global login
        login = self.ids["login"].text
        print("user is" + user)
        if user == 'student':                    
            std =open("student.txt", 'r')
            #a = std.readlines()
            for i in std:
                i = i.split()
                if self.ids["login"].text == i[0] and self.ids["pass"].text == i[1]:     #Verify login id and password for user
                    self.manager.current = "user_page"
                    if self.ids["checkbox"].active is True:                              #Check is checkbox selected
            #no action
                        print("checkbox ok")
                        self.ids["checkbox"].active is False            
        
                    else:
                        self.ids["login"].text = ''
                        self.ids["pass"].text = '' 
                    
                    login_successfull = True                
                    print(login_successfull)
                    break
            
            if login_successfull != True:                                                    #Come here if login is not successfull
                #error
                print("Error student login")
                #Switch to wrong credentials screen
                #self.manager.current = "wrong_credentials"
                self.ids["login"].text = ""
                self.ids["pass"].text  = "" 
               # self.ids["error"].text  = "user name or passord not matched" 
                content=Button(text='You Have Entered Invalid Credentials!')
                popup = Popup(title='Oops!!', content=content, size_hint=(None, None), size=(400, 200),auto_dismiss=False)
                content.bind(on_press=popup.dismiss)
                popup.open() 
                
        elif user == 'admin':                                                        #user is admin
            std =open("admin.txt", 'r')
        
            #std = std.readlines()
            for i in std:
                i = i.split()
                if self.ids["login"].text == i[0] and self.ids["pass"].text == i[1]:
                    self.manager.current = "admin_page"
                    if self.ids["checkbox"].active is True:
            #no action
                        print("checkbox ok")  
                        self.ids["checkbox"].active is False           
        
                    else:
                        self.ids["login"].text = ''
                        self.ids["pass"].text = '' 
                    # global login_successfull
                    login_successfull = True                
                    print(login_successfull)
                    break
                
            if login_successfull != True:
                #error
                print("Error admin login")
                #Switch to wrong credentials screen
                #self.manager.current = "wrong_credentials" 
                self.ids["login"].text = ""
                self.ids["pass"].text  = "" 
                #self.ids["error"].text  = "user name or password not matched"   
                content=Button(text='You Have Entered Invalid Credentials!')
                popup = Popup(title='Oops!!', content=content, size_hint=(None, None), size=(400, 200),auto_dismiss=True)  #auto_dismiss = True i.e popup dismiss after click anywhere
                content.bind(on_press=popup.dismiss)
                popup.open() 
                
           
                    
###################################################################################################3
              

#####################################################################################################


class UserPage(Screen):
    def user_details(self,name,entry_no,branch,year_of_passing,address,subject1,subject2,subject3,subject4,subject5):
        global first_entry
        first_entry = True
        global E_number
        E_number = entry_no.text
        print("in user" + E_number)
        print("user detail reached")  
        #Check is subject1 are matched 
        if E_number is not '':
             #Entry is not empty   
            db = open("data_base.txt", 'r')
            for i in db:         #get one line
                #one time loop for heading matching  
               #one time loop to check subject1
                
                if first_entry == True:
                    first_entry = False   #make it False so that it will never come in this loop
                    heading = ''
                    heading = i.split(',')       #make list heading
                    
                        
                marks = i.split(',')
                if entry_no.text in marks:       #get marks acc to entry no
                    #we got the marks of student 
                   # print(marks)
                    break
                
                
            marks_1 = marks_2 = marks_3 =marks_4 =marks_5 =''
            #now get the marks acco. to subject1
            for i in range(len(heading)):
                if subject1.text == heading[i]:
                    marks_1 = marks[i]
                   # print(subject1.text)
                    
                elif subject2.text == heading[i]:
                    marks_2 = marks[i] 
                    #print(marks_2) 
                    #print(address.text)  
                elif subject3.text == heading[i]:
                    marks_3 = marks[i] 
                    
                elif subject4.text == heading[i]:
                    marks_4 = marks[i] 
                    
                elif subject5.text == heading[i]:
                    marks_5 = marks[i]                               
            
               
               
            if marks[0] == entry_no.text and entry_no.text == login:  
                #correct entry no..now check subjects
                
                if subject1.text and subject2.text and subject3.text and subject4.text and subject5.text is not '':  
                    if (subject1.text in heading) and (subject2.text in heading) and (subject3.text in heading)  and (subject4.text in heading)  and (subject5.text in heading) :
                    #if subject1.text and subject2.text and subject3.text and subject4.text and subject5.text  in heading:  # Error if write Tele
                        if subject1.text != subject2.text and subject1.text != subject3.text and subject1.text != subject4.text and subject1.text != subject5.text and \
                        subject2.text != subject3.text and subject2.text != subject4.text and subject2.text != subject5.text and \
                        subject3.text != subject4.text and subject3.text != subject5.text and \
                        subject4.text != subject5.text:
                        
                               # print(heading)
                            if ((' ' != marks_1) and (' ' !=marks_2) and (' ' != marks_3) and (' ' !=marks_4) and (' ' !=marks_5) ) :
                            
                                #subject1 matched...now get the marks of student
                                try:                      
                                    fh= open( 'student_info//' + entry_no.text,'w') 
                                    fh.write("name: " + "," + name.text + "," +  "\n" + \
                                             "Entry_no: " + "," + entry_no.text + "," +  "\n" + \
                                             "Branch: " + "," + branch.text + "\n" + \
                                             "Year_of_passing: " + "," + year_of_passing.text + "," +  "\n" + \
                                             "Address: " + "," + address.text + "," +  "\n" + \
                                             "Subject1: " + "," + subject1.text +"," + "marks:" + "," + marks_1  +  "\n" +\
                                             "Subject2: " + "," + subject2.text +"," + "marks:" + "," + marks_2 + "\n" + \
                                             "Subject3: " + "," + subject3.text +"," + "marks:" + "," + marks_3 + "\n" + \
                                             "Subject4: " + "," + subject4.text +"," + "marks:" + "," + marks_4 + "\n" + \
                                             "Subject5: " + "," + subject5.text +"," + "marks:" + "," + marks_5  )  
                                    #move to next screen WatchWindow
                                    fh.close()
                                    
                                    self.manager.current = "watch_window"
                                    #blank all values
                                    self.ids["name"].text = ""
                                    self.ids["entry_no"].text = ""
                                    self.ids["branch"].text = ""
                                    self.ids["year_of_passing"].text = ""
                                    self.ids["address"].text = ""
                                    self.ids["subject1"].text = ""
                                    self.ids["subject2"].text = ""
                                    self.ids["subject3"].text = ""
                                    self.ids["subject4"].text = ""
                                    self.ids["subject5"].text = ""            
                                                            
                                            
                                             
                                                     
                                except:
                                #Blank entry no
                                    content=Button(text='Error in file handling!')
                                    popup = Popup(title='Error...!!', content=content, size_hint=(None, None), size=(400, 200),auto_dismiss=True)  #auto_dismiss = True i.e popup dismiss after click anywhere
                                    content.bind(on_press=popup.dismiss)
                                    popup.open()               
                                
                            elif marks_1 is ' ' :
                                content=Button(text='Subject 1 has no marks!')
                                popup = Popup(title='Oops!!', content=content, size_hint=(None, None), size=(400, 200),auto_dismiss=True)  #auto_dismiss = True i.e popup dismiss after click anywhere
                                content.bind(on_press=popup.dismiss)
                                popup.open()
                            elif marks_2 is ' ':
                                content=Button(text='Subject 2 has no marks!')
                                popup = Popup(title='Oops!!', content=content, size_hint=(None, None), size=(400, 200),auto_dismiss=True)  #auto_dismiss = True i.e popup dismiss after click anywhere
                                content.bind(on_press=popup.dismiss)
                                popup.open()
                            elif marks_3 is ' ':
                                content=Button(text='Subject 3 has no marks!')
                                popup = Popup(title='Oops!!', content=content, size_hint=(None, None), size=(400, 200),auto_dismiss=True)  #auto_dismiss = True i.e popup dismiss after click anywhere
                                content.bind(on_press=popup.dismiss)
                                popup.open()
                            elif marks_4 is ' ':
                                content=Button(text='Subject 4 has no marks!')
                                popup = Popup(title='Oops!!', content=content, size_hint=(None, None), size=(400, 200),auto_dismiss=True)  #auto_dismiss = True i.e popup dismiss after click anywhere
                                content.bind(on_press=popup.dismiss)
                                popup.open()
                            elif marks_5 is ' ':
                                content=Button(text='Subject 5 has no marks!')
                                popup = Popup(title='Oops!!', content=content, size_hint=(None, None), size=(400, 200),auto_dismiss=True)  #auto_dismiss = True i.e popup dismiss after click anywhere
                                content.bind(on_press=popup.dismiss)
                                popup.open()                
                                 
                        else:
                            #same subjects enter
                            content=Button(text='You have entered same sub!')
                            popup = Popup(title='Oops!!', content=content, size_hint=(None, None), size=(400, 200),auto_dismiss=True)  #auto_dismiss = True i.e popup dismiss after click anywhere
                            content.bind(on_press=popup.dismiss)
                            popup.open()     
                        
                                        
                    else:
                        #error
                        print("Error in Sub")
                        content=Button(text='You Have Entered Invalid Subjects!')
                        popup = Popup(title='Oops!!', content=content, size_hint=(None, None), size=(400, 200),auto_dismiss=True)  #auto_dismiss = True i.e popup dismiss after click anywhere
                        content.bind(on_press=popup.dismiss)
                        popup.open()                      
                else:
                    content=Button(text='Please fill all the Subjects!')
                    popup = Popup(title='Blank Entry!!', content=content, size_hint=(None, None), size=(400, 200),auto_dismiss=True)  #auto_dismiss = True i.e popup dismiss after click anywhere
                    content.bind(on_press=popup.dismiss)
                    popup.open()                 
                
                    
                                       
            else:
                #entry no not matched
                content=Button(text='Invalid Entry No!')
                popup = Popup(title='Oops!!', content=content, size_hint=(None, None), size=(400, 200),auto_dismiss=True)  #auto_dismiss = True i.e popup dismiss after click anywhere
                content.bind(on_press=popup.dismiss)
                popup.open() 
            db.close()    
                
        else:
            content=Button(text='Please fill Entry No!')
            popup = Popup(title='Blank Entry!!', content=content, size_hint=(None, None), size=(400, 200),auto_dismiss=True)  #auto_dismiss = True i.e popup dismiss after click anywhere
            content.bind(on_press=popup.dismiss)
            popup.open()         
            
                       
                         #print(argc)
            
            
        #print(str(argc))
         
        first_entry = True
        #empty data
        
       #     
        
#####################################################################################################
class WatchWindow(Screen):
    def show_data(self):  
      
        fd = open('student_info//' + E_number, 'r')
        fd = fd.readlines()
        #fd = fd.split("\n")    
        
        i = fd[0].split(',')
        self.ids["name_h"].text = i[0]                   
        self.ids["name"].text = i[1]
        
        i = fd[1].split(',')
        self.ids["entry_no_h"].text = i[0]                  
        self.ids["entry_no"].text = i[1]
        
        i = fd[2].split(',')
        self.ids["branch_h"].text = i[0]                    
        self.ids["branch"].text = i[1]
        
        i = fd[3].split(',')
        self.ids["year_of_passing_h"].text = i[0]                  
        self.ids["year_of_passing"].text = i[1]
        
        i = fd[4].split(',')
        self.ids["address_h"].text = i[0]                    
        self.ids["address"].text = i[1]
        
        i = fd[5].split(',')
        self.ids["subject1_h"].text = i[0]                    
        self.ids["subject1"].text = i[1]
        self.ids["marks1"].text = i[2] + '  ' + i[3]
        
        i = fd[6].split(',')
        self.ids["subject2_h"].text = i[0]                    
        self.ids["subject2"].text = i[1]
        self.ids["marks2"].text = i[2] + '  ' + i[3]
        
        i = fd[7].split(',')
        self.ids["subject3_h"].text = i[0]                    
        self.ids["subject3"].text = i[1]
        self.ids["marks3"].text = i[2] + '  ' + i[3]
        
        i = fd[8].split(',')
        self.ids["subject4_h"].text = i[0]                    
        self.ids["subject4"].text = i[1]
        self.ids["marks4"].text = i[2] + '  ' + i[3]
        
        i = fd[9].split(',')
        self.ids["subject5_h"].text = i[0]                    
        self.ids["subject5"].text = i[1]
        self.ids["marks5"].text = i[2] + '  ' + i[3]
        
        
    def exit(self):
        self.ids["name_h"].text = ''                  
        self.ids["name"].text = ''        
        self.ids["entry_no_h"].text = ''                 
        self.ids["entry_no"].text = ''        
        self.ids["branch_h"].text = ''                  
        self.ids["branch"].text = ''        
        self.ids["year_of_passing_h"].text = ''                 
        self.ids["year_of_passing"].text = ''        
        self.ids["address_h"].text = ''                   
        self.ids["address"].text = ''        
        self.ids["subject1_h"].text = ''                  
        self.ids["subject1"].text = ''
        self.ids["marks1"].text = ''        
        self.ids["subject2_h"].text = ''                  
        self.ids["subject2"].text =''
        self.ids["marks2"].text = ''        
        self.ids["subject3_h"].text = ''                    
        self.ids["subject3"].text = ''
        self.ids["marks3"].text = ''        
        self.ids["subject4_h"].text = ''                    
        self.ids["subject4"].text = ''
        self.ids["marks4"].text = ''        
        self.ids["subject5_h"].text = ''                 
        self.ids["subject5"].text = ''
        self.ids["marks5"].text = ''  
        self.manager.current = "login_page"
        

    
####################################################################################################
class AdminPage(Screen):
    def show_details(self):
        try:
            
            file_name =self.ids["entry_no_enter"].text
            sh = open('student_info//' + file_name,'r')
            sh =sh.readlines()
            
            i = sh[0].split(',')
            self.ids["name_h"].text = i[0]                   
            self.ids["name"].text = i[1]
            
            
            i = sh[1].split(',')
            self.ids["entry_no_h"].text = i[0]                  
            self.ids["entry_no"].text = i[1]
            
            i = sh[2].split(',')
            self.ids["branch_h"].text = i[0]                    
            self.ids["branch"].text = i[1]
            
            i = sh[3].split(',')
            self.ids["year_of_passing_h"].text = i[0]                  
            self.ids["year_of_passing"].text = i[1]
            
            i = sh[4].split(',')
            self.ids["address_h"].text = i[0]                    
            self.ids["address"].text = i[1]
            
            i = sh[5].split(',')
            self.ids["subject1_h"].text = i[0]                    
            self.ids["subject1"].text = i[1] 
            self.ids["marks1"].text = i[2] +  '  ' + i[3]
            
            i = sh[6].split(',')
            self.ids["subject2_h"].text = i[0]                    
            self.ids["subject2"].text = i[1] 
            self.ids["marks2"].text = i[2] +  '  ' + i[3]
            
            i = sh[7].split(',')
            self.ids["subject3_h"].text = i[0]                    
            self.ids["subject3"].text = i[1] 
            self.ids["marks3"].text = i[2] +  '  ' + i[3]
            
            i = sh[8].split(',')
            self.ids["subject4_h"].text = i[0]                    
            self.ids["subject4"].text = i[1] 
            self.ids["marks4"].text = i[2] +  '  ' + i[3]
            
            i = sh[9].split(',')
            self.ids["subject5_h"].text = i[0]                    
            self.ids["subject5"].text = i[1] 
            self.ids["marks5"].text = i[2] +  '  ' + i[3]
            
        except :
            #file not found
            content=Button(text='File not found!')
            popup = Popup(title='Oops!!', content=content, size_hint=(None, None), size=(400, 200),auto_dismiss=True)  #auto_dismiss = True i.e popup dismiss after click anywhere
            content.bind(on_press=popup.dismiss)
            popup.open()    



    def plot_graph(self):
        try:            
            file_name =self.ids["entry_no_enter"].text
            sh = open('student_info//' + file_name,'r')
            sh =sh.readlines()
            x =['1','','','','']
            y =[0,0,0,0,0]       
                                
            i = sh[5].split(',')
            x[0] = i[1] 
            y[0]= int(i[3])
            
            i = sh[6].split(',')
            x[1] = i[1] 
            y[1]= int(i[3])
            
            i = sh[7].split(',')
            x[2] = i[1] 
            y[2]= int(i[3])
            
            i = sh[8].split(',')
            x[3] = i[1] 
            y[3]= int(i[3])
            
            i = sh[9].split(',')
            x[4] = i[1] 
            y[4]= int(i[3])
            
            #Plot graph
            index = np.arange(len(x))
            plt.bar(index, y)
            plt.xlabel('Subjects', fontsize=15)
            plt.ylabel(' Marks', fontsize=15)
            plt.xticks(index, x, fontsize=15, rotation=0)
            plt.title(file_name)
            plt.show()    
         #   sh.close() 
           
        except IOError:
            #file not found
            content=Button(text='File not found in plot!')
            popup = Popup(title='Oops!!', content=content, size_hint=(None, None), size=(400, 200),auto_dismiss=True)  #auto_dismiss = True i.e popup dismiss after click anywhere
            content.bind(on_press=popup.dismiss)
            popup.open()    

        #now plot graph
    def analysis(self):
        self.ids["entry_no_enter"].text = ''
        self.ids["name_h"].text = ''
        self.ids["name"].text = ''   
        self.ids["entry_no_h"].text = ''   
        self.ids["entry_no"].text = '' 
        self.ids["branch_h"].text = ''   
        self.ids["branch"].text = ''
        self.ids["year_of_passing_h"].text = ''   
        self.ids["year_of_passing"].text = ''
        self.ids["address_h"].text = ''   
        self.ids["address"].text = ''     
        self.ids["subject1_h"].text = ''    
        self.ids["subject1"].text = '' 
        self.ids["marks1"].text = ''
        
        self.ids["subject2_h"].text = ''    
        self.ids["subject2"].text = '' 
        self.ids["marks2"].text = ''
        
        self.ids["subject3_h"].text = ''    
        self.ids["subject3"].text = '' 
        self.ids["marks3"].text = ''
        
        self.ids["subject4_h"].text = ''    
        self.ids["subject4"].text = '' 
        self.ids["marks4"].text = ''
        
        self.ids["subject5_h"].text = ''    
        self.ids["subject5"].text = '' 
        self.ids["marks5"].text = ''
        
        self.manager.current = "analysis_page"
    
    def admin_home(self): 
        self.ids["entry_no_enter"].text = ''
        self.ids["name_h"].text = ''
        self.ids["name"].text = ''   
        self.ids["entry_no_h"].text = ''   
        self.ids["entry_no"].text = '' 
        self.ids["branch_h"].text = ''   
        self.ids["branch"].text = ''
        self.ids["year_of_passing_h"].text = ''   
        self.ids["year_of_passing"].text = ''
        self.ids["address_h"].text = ''   
        self.ids["address"].text = ''     
        self.ids["subject1_h"].text = ''    
        self.ids["subject1"].text = '' 
        self.ids["marks1"].text = ''
        
        self.ids["subject2_h"].text = ''    
        self.ids["subject2"].text = '' 
        self.ids["marks2"].text = ''
        
        self.ids["subject3_h"].text = ''    
        self.ids["subject3"].text = '' 
        self.ids["marks3"].text = ''
        
        self.ids["subject4_h"].text = ''    
        self.ids["subject4"].text = '' 
        self.ids["marks4"].text = ''
        
        self.ids["subject5_h"].text = ''    
        self.ids["subject5"].text = '' 
        self.ids["marks5"].text = ''
        
        self.manager.current = "Welcome_page"   

##################################################################################################


##################################################################################################
class AnalysisPage(Screen):
    def show_toppres(self):
        #data =[]
        db = open("data_base.txt", 'r')
        dict ={'' :''}
        data=[]
        addi =0
        #for i in db:
           # line = i.split(',')   #line by line
           # data = data.append(line)
           # print(data)
       # data = [[i.split(',') for i in j] for j in db]
        for i in db:
            i = i.split(',')
            data.append(i)
            #print(data)
            
        
        for i in range(len(data) -1):
            for j in range(len(data[0]) -1):
                #raw element
                if j ==0: # first element
                    print("escape")
                    #dict.keys(i) = data[i+1][j]
                elif data[i+1][j] != ' ' and data[i+1][j] != '':
                    addi = addi + int(data[i+1][j]) 
                    #print(int(data[i+1][j]))
                    #print(data[i+1][j])
                    
            dict[data[i+1][0]] = addi   
            addi =0
        del dict['']            
        #print(dict)   
        #s = sorted((value,key) for (key,value) in dict.items() )
        #q = s.reverse()
        #print(s)
        
       # p = sorted(dict.items(), key=operator.itemgetter(0), reverse =True)
       # print(p)
       # q=""
        toppers = sorted(dict.items(), key=lambda x:x[1], reverse = True)           
            
         #headings
        self.ids["sn"].text = 'SN'
        self.ids["entry_no_h"].text = 'Entry_no'
        self.ids["name_h"].text = 'Name'
        self.ids["marks_h"].text = 'Marks'
        
        #values
        self.ids["sn1"].text = '1'
        self.ids["entry_no1"].text = toppers[0][0]
        f = open('student_info//' + self.ids["entry_no1"].text,'r')
        for i in f:
            i = i.split(',')
            self.ids["name1"].text = i[1]
            break            
        self.ids["marks1"].text = str(toppers[0][1])
        
        self.ids["sn2"].text = '2'
        self.ids["entry_no2"].text = toppers[1][0]
        f = open('student_info//' + self.ids["entry_no2"].text,'r')
        for i in f:
            i = i.split(',')
            self.ids["name2"].text = i[1]
            break
        self.ids["marks2"].text = str(toppers[1][1])
        
        self.ids["sn3"].text = '3'
        self.ids["entry_no3"].text = toppers[2][0]
        f = open('student_info//' + self.ids["entry_no3"].text,'r')
        for i in f:
            i = i.split(',')
            self.ids["name3"].text = i[1]
            break
        self.ids["marks3"].text = str(toppers[2][1])
        
        self.ids["sn4"].text = '4'
        self.ids["entry_no4"].text = toppers[3][0]
        f = open('student_info//' + self.ids["entry_no4"].text,'r')
        for i in f:
            i = i.split(',')
            self.ids["name4"].text = i[1]
            break
        self.ids["marks4"].text = str(toppers[3][1])
        
        self.ids["sn5"].text = '5'
        self.ids["entry_no5"].text = toppers[4][0]
        f = open('student_info//' + self.ids["entry_no5"].text,'r')
        for i in f:
            i = i.split(',')
            self.ids["name5"].text = i[1]
            break
        self.ids["marks5"].text = str(toppers[4][1])
        
        
        
        
    def plot_graph_avg(self): 
        #data =[]
        db = open("data_base.txt", 'r')
        dict ={'' :''}
        data=[]
        addi =0       
        for i in db:
            i = i.split(',')
            data.append(i)
            #print(data)
            
        
        for i in range(len(data) -1):
            for j in range(len(data[0]) -1):
                #raw element
                if j ==0: # first element
                    print("escape")
                    #dict.keys(i) = data[i+1][j]
                elif data[i+1][j] != ' ' and data[i+1][j] != '':
                    addi = addi + int(data[i+1][j]) 
                    #print(int(data[i+1][j]))
                    #print(data[i+1][j])
                    
            dict[data[i+1][0]] = addi / 5  
            addi =0
        del dict['']   
      
        q=""
        cd = sorted(dict.items(), key=lambda x:x[1], reverse = True)   
        #toppers.update((x, y/5) for x, y in toppers.items())
        subjects =[]
        marks = []
        for i in range(len(cd)):
            subjects.append(cd[i][0])
            marks.append(cd[i][1])
        
        
        index = np.arange(len(subjects))
        plt.bar(index, marks)
        plt.xlabel('Subject', fontsize=15)
        plt.ylabel(' Marks', fontsize=15)
        plt.xticks(index, subjects, fontsize=15, rotation=0)
        plt.title(' Avg Marks of Students ')
        plt.savefig('bar.png')
                    
        plt.show()
        
        
        
        
                     
    def home(self):
        #Clear all fields
        self.ids["sn"].text = ''     
        self.ids["sn1"].text = ''
        self.ids["sn2"].text = ''
        self.ids["sn3"].text = '' 
        self.ids["sn4"].text = ''
        self.ids["sn5"].text = ''
        
        self.ids["entry_no_h"].text = ''
        self.ids["entry_no1"].text = ''
        self.ids["entry_no2"].text = ''
        self.ids["entry_no3"].text = ''
        self.ids["entry_no4"].text = ''
        self.ids["entry_no5"].text = ''
        
        self.ids["name_h"].text = ''
        self.ids["name1"].text = ''
        self.ids["name2"].text = ''
        self.ids["name3"].text = ''
        self.ids["name4"].text = ''
        self.ids["name5"].text = ''
        
        self.ids["marks_h"].text = ''
        self.ids["marks1"].text = ''
        self.ids["marks2"].text = ''
        self.ids["marks3"].text = ''
        self.ids["marks4"].text = ''
        self.ids["marks5"].text = ''
        
        self.manager.current = "Welcome_page" 
        
            
      
              
##############################################################################################
class ScreenManagement(ScreenManager):
    pass

###################################################################################################
kv_file = Builder.load_file('login.kv')

class LoginApp(App):
    def builder(self):
        return kv_file


LoginApp().run()