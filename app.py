from tkinter import *
class NLPApp:
    
    def __init__(self):
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
        self.email_input = Entry(self.root, width=30)
        self.email_input.pack(pady=(5, 10), ipady=4)
        
        #password
        label2 = Label(self.root, text = 'Enter Password: ')
        label2.pack(pady=(10, 10))
        self.password_input = Entry(self.root, width=30, show = '*')
        self.password_input.pack(pady=(5, 10), ipady=4)
        
        #login button
        login_btn = Button(self.root, text = 'login')
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
        register_btn = Button(self.root, text = 'Register', command= self.perform_registration)
        register_btn.pack(pady=(10,10))
        
        # already a member text
        label3 = Label(self.root, text = 'Already a Member ?')
        label3.pack(pady=(10, 20))
        
        #redirect button
        redirect_btn = Button(self.root, text = 'Login now', command = self.register_gui)
        redirect_btn.pack(pady=(0,0))     
        
           
        
    
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
            
nlp = NLPApp()

