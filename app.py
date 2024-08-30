from tkinter import *
from mydatabase import Database
from tkinter import messagebox
class NLPApp:
    
    def __init__(self):
        #creating a database object
        self.dbo = Database()
        #load the login Gui
        self.root = Tk()
        self.root.title('NLPApp')
        self.root.iconbitmap('Resources/favicon.ico')
        self.root.geometry('350x600')
        self.root.configure(bg='#0e1411')
        
        self.login_Gui()
        self.root.mainloop() # holds the gui 
        
    def login_Gui(self):
        # heading
        heading = Label(self.root, text = 'NLPApp', bg = '#0e1411', fg = '#e6ece9')
        heading.pack(pady=(30, 30))
        heading.configure(font = ('San Francisco', 24, 'bold'))
        
        #email
        label1 = Label(self.root, text = 'Enter Email: ')
        label1.pack(pady=(10, 10))
        self.email_input_login = Entry(self.root, width=30)
        self.email_input_login.pack(pady=(5, 10), ipady=4)
        
        #password
        label2 = Label(self.root, text = 'Enter Password: ')
        label2.pack(pady=(10, 10))
        self.password_input_login = Entry(self.root, width=30, show = '*')
        self.password_input_login.pack(pady=(5, 10), ipady=4)
        
        #login button
        login_btn = Button(self.root, text = 'login', width=30, height=2, command=self.perfor_login)
        login_btn.pack(pady=(10,10))
        
        # not a member text
        label3 = Label(self.root, text = 'Not a member ?')
        label3.pack(pady=(10, 20))
        
        #redirect button
        redirect_btn = Button(self.root, text = 'Register now', command = self.register_gui)
        redirect_btn.pack(pady=(0,0))     
        
    
    def register_gui(self):
        self.clear()
        # heading
        heading = Label(self.root, text = 'NLPApp', bg = '#0e1411', fg = '#e6ece9')
        heading.pack(pady=(30, 30))
        heading.configure(font = ('San Francisco', 24, 'bold'))
        
        #name
        label0 = Label(self.root, text = 'Enter Name: ')
        label0.pack(pady=(10, 10))
        self.name_input = Entry(self.root, width=30)
        self.name_input.pack(pady=(5, 10), ipady=4)
        
        #email
        label1 = Label(self.root, text = 'Enter Email: ')
        label1.pack(pady=(10, 10))
        self.email_input = Entry(self.root, width=30)
        self.email_input.pack(pady=(5, 10), ipady=4)
        
        #password
        label2 = Label(self.root, text = 'Enter Password: ')
        label2.pack(pady=(10, 10))
        self.password_input = Entry(self.root, width=30, show = '*')
        self.password_input.pack(pady=(5, 10), ipady=4)
        
        #register button
        register_btn = Button(self.root, text = 'Register', width=30, height=2, command= self.perform_registration)
        register_btn.pack(pady=(10,10))
        
        # already a member text
        label3 = Label(self.root, text = 'Already a Member ?')
        label3.pack(pady=(10, 20))
        
        #redirect button
        redirect_btn = Button(self.root, text = 'Login now', command = self.login_Gui)
        redirect_btn.pack(pady=(0,0))     
        
           
        
    
    def clear(self):
        #clearing the existing gui
        for i in self.root.pack_slaves():
            i.destroy()
            
    def perform_registration(self):
        #fetching data from the gui
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
    
        response = self.dbo.add_data(name, email, password)
        if response:
            messagebox.showinfo('Success', 'Registration Successful, you can login now')
        else:
            messagebox.showerror('Error', 'Email already exists')
            
    def perform_login(self):
        email = self.email_input_login.get()
        password = self.password_input_login.get() 
        response = self.dbo.search(email, password)
        if response:
            messagebox.showinfo('Success', 'Login Successful')
            self.home_gui()
        else:
            messagebox.showerror('Error', 'Incorrect email/password') 
    
    def home_gui(self):
        self.clear()
        heading = Label(self.root, text = 'NLPApp', bg = '#0e1411', fg = '#e6ece9')
        heading.pack(pady=(30, 30))
        heading.configure(font = ('San Francisco', 24, 'bold'))
        
        sentiment_btn = Button(self.root, text = 'Sentiment Analysis', width=30, height=4, command= self.sentiment_gui)
        sentiment_btn.pack(pady=(10,10))
        
        ner_btn = Button(self.root, text = 'Name Entity Emotion', width=30, height=4, command= self.perform_registration)
        ner_btn.pack(pady=(10,10))
        
        emotion_btn = Button(self.root, text = 'Emotion Prediction', width=30, height=4, command= self.perform_registration)
        emotion_btn.pack(pady=(10,10))
        
        #logout button
        redirect_btn = Button(self.root, text = 'Logout', command = self.login_Gui)
        redirect_btn.pack(pady=(0,0))
        
    # creating a sentiment gui function
    def sentiment_gui(self):
        self.clear()
        
        heading = Label(self.root, text = 'NLPApp', bg = '#0e1411', fg = '#e6ece9')
        heading.pack(pady=(30, 30))
        heading.configure(font = ('San Francisco', 24, 'bold'))
        
        heading2 = Label(self.root, text = 'Sentiment Analysis', bg = '#0e1411', fg = '#e6ece9')
        heading.pack(pady=(10, 20))
        heading.configure(font = ('San Francisco', 20))
        
        label1 = Label(self.root, text = 'Enter the Text')
        label1.pack(pady=(10, 10))
        
        self.sentiment_input = Entry(self.root, width=30)
        self.sentiment_input.pack(pady=(5, 10), ipady=4)
        
        sentiment_btn = Button(self.root, text = 'Analyse Sentiment', command = self.login_Gui)
        sentiment_btn.pack(pady=(10,10))
          
        self.sentiment_result = Label(self.root, text = '', bg ='#0e1411', fg = 'white')
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.configure(font = ('San Francisco', 16))

        
        goback_btn = Button(self.root, text = 'go back', command = self.home_gui)
        goback_btn.pack(pady=(10,10))
        
        
nlp = NLPApp()

