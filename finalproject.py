# Updated Animation Starter Code
# Starter code from 15-112 Lecture Notes
# https://quizlet.com/subject/8th-edition-biology-campbell/
# https://blog.prepscholar.com/the-best-way-to-study-sat-vocab-words
# https://apps.ankiweb.net/

from tkinter import *
import tkinter.messagebox as tm
import random

USERNAMES = ['Peter', 'Esther']
user = 'Peter'
loggedIn = False

# Log-In
class LoginFrame(Frame):
    def __init__(self, master, data):
        super().__init__(master)

        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        self.checkbox = Checkbutton(self, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)

        self.pack()
        

    def _login_btn_clicked(self):
        # print("Clicked")
        username = self.entry_username.get()
        password = self.entry_password.get()

        # print(username, password)
        # print(data.usernames)
        
        if username in USERNAMES and password == "a":
            tm.showinfo("Login info", "Welcome %s" % username)
            loggedIn = True
            user = username
            print(user, 'dddddd')
            # print(data.username)
            # data.logIn = True
        else:
            tm.showerror("Login error", "Incorrect username")
            

####################################
# customize these functions
####################################

def init(data):
    data.logIn = loggedIn
    data.timerDelay = 1000 # 100 millisecond == 0.1 seconds
    data.timerCalls = 0
    data.rows = 10
    data.startRow = 2
    data.redWidth = 2
    data.currentTerm = 0
    data.terms = ['Biology', 'Organelles', 'Cells', 'Prokaryotics Cells',
        'Eukaryotic Cells', 'Tissue', 'Organ', 'Organ System', 'Organism',
        'Population', 'Community', 'Ecosystem', 'Biosphere', 'Entropy', 
        'Abiotic Factors', 'Reproduction', 'Growth and Development', 'Growth', 'Development', 'Energy Processing', 'Metabolism', 'Catabolic', 'Anabolic']
    data.termDefs = [
    'The study of life or all that lived', 'Parts of a cell that perform    specific functions for it', 'Smallest unit of life functional units of life', 'Cells that lack a nuclear envelope around their DNA', 'Cells that have DNA enclosed by a nuclear envelope', 'A group of cells that perform the same function', 'A group of tissue that perform a function for an organism', 'A group of organs that generally perform the same function or are related to each other in function', 'An individual living thing made up of organ systems', 'Groups of the same organism', 'Groups of different populations that live in the same general area', 'All of the organisms in an area, along with biotic and abiotic factors', 'The global sum of all ecosystems', 'Chaos; disorder', 'Any non-living factor such as terrain, weather, geography, etc.', 'The ability of organisms to reproduce their own kind', 'Consistent growth and development controlled by inherited DNA', 'To increase in size (early stages of mitosis, etc)', 'Changing phases of life (puberty, etc)', 'Ability of an organism to do chemical reactions to power the cell', 'The sum or rate of all catabolic and anabolic reactions', 'A reaction in which things are broken down', 'A reaction in which things are built/synthesized']
    data.pickThree = random.sample(range(len(data.termDefs)), 3)
    data.showDef = False
    data.clicked = False
    data.usernames = ['Peter', 'Esther']
    data.username = user
    print(data.username)
    data.timeData = []
    data.level = 1
    data.progress = 0
    data.page = 'Home'
    data.fontSize = 0.75 * (data.height // data.rows)
    data.numCorrect = 0
    data.pause = False
    data.gameType = "Regular"
    if (data.gameType == 'Regular'):
        data.gameColor1 = "Helvetica %d" % data.fontSize
        data.gameColor2 = "Helvetica %d bold" % data.fontSize
    if (data.gameType == 'Test'):
        data.gameColor1 = "Helvetica %d bold" % data.fontSize
        data.gameColor2 = "Helvetica %d" % data.fontSize
    

def mousePressed(event, data):
    # Cards, Start, Stats boxes variables
    boxLength = .20
    boxLeft1 = .15
    boxLeft2 = .40
    boxLeft3 = .65
    homeBox = 5/7
    homeBoxUnit = 1/7
    
    # Navigate to Stats page
    if (event.x > (boxLeft3) * data.width and event.x < 
    (boxLeft3 + boxLength) * data.width and event.y > 
    (boxLeft3) * data.height and event.y < (boxLeft3 + boxLength) *     
    data.height and data.page == 'Home'):
        data.page = 'Stats'
    
    # Navigate to Game Regular Mode
    if (event.x > (boxLeft2) * data.width and event.x < 
    (boxLeft2 + boxLength) * data.width and event.y > (boxLeft3) * 
    data.height and event.y < (boxLeft3 + boxLength) * 
    data.height and data.page == 'Home' and data.gameType == 'Regular'):
        data.page = 'Game'
        data.currentTerm = 0
    
    # Navigate to Game Test Mode
    if (event.x > (boxLeft2) * data.width and event.x < 
    (boxLeft2 + boxLength) * data.width and event.y > (boxLeft3) * 
    data.height and event.y < (boxLeft3 + boxLength) * 
    data.height and data.page == 'Home' and data.gameType == 'Test'):
        data.page = 'Test'
        
    # Navigate to Cards
    if (event.x > (boxLeft1) * data.width and event.x < 
    (boxLeft1 + boxLength) * data.width and event.y > (boxLeft3) 
    * data.height and event.y < (boxLeft3 + boxLength) * 
    data.height and data.page == 'Home'):
        data.page = 'Cards'
    
    # Navigate to Home Screen
    if (event.x > (homeBox) * data.width and event.x < 
    (homeBox + homeBoxUnit) * data.width and event.y > 
    (data.rows - 1) * (data.height // data.rows) and 
    event.y < (data.rows) * data.height // data.rows):
        data.page = 'Home'
    
    # Edit term
    if (event.x > (6/7) * data.width and event.x < data.width 
    and event.y > (int(.25*data.rows)) * (data.height // data.rows)
    and event.y < (int(.25*data.rows) + 1) * (data.height // data.rows)
    and data.page == 'Cards'):
        print(data.level)
        newTerm = input("What is your new term?")
        data.terms[data.currentTerm] = newTerm
    
    # Edit definition
    if (event.x > (6/7) * data.width and event.x < data.width 
    and event.y > (int(.6*data.rows)) * (data.height // data.rows)
    and event.y < (int(.6*data.rows) + 1) * (data.height // data.rows)
    and data.page == 'Cards'):
        print(data.level)
        newDef = input("What is your new definition?")
        data.termDefs[data.currentTerm] = newDef
    
    # Add new card
    if (event.x > 0 and event.x < (1/7) * data.width and 
    event.y > (int(.5*data.rows)) * (data.height // data.rows) and event.y < (int(.5*data.rows) + 1) * (data.height // data.rows) and 
    data.page == 'Cards'):
        newTerm = input("What is the new term you want to add?")
        data.terms.append(newTerm)
        newDef = input("What is the new definition for this term?")
        data.termDefs.append(newDef)
        
    # Button for Regular mode
    if (event.x > .4 * data.width and event.x < .6 * data.width and event.y > .15 * data.height and event.y < .35 * data.height and data.page == 'Home'):
        data.gameType = 'Regular'
        if (data.gameType == 'Regular'):
            data.gameColor1 = "Helvetica %d" % data.fontSize
            data.gameColor2 = "Helvetica %d bold" % data.fontSize
        if (data.gameType == 'Test'):
            data.gameColor1 = "Helvetica %d bold" % data.fontSize
            data.gameColor2 = "Helvetica %d" % data.fontSize
            
    # Button for Test mode
    if (event.x > .6 * data.width and event.x < .85 * data.width and event.y > .15 * data.height and event.y < .35 * data.height and data.page == 'Home'):
        data.gameType = 'Test'
        print(data.gameType)
        if (data.gameType == 'Regular'):
            data.gameColor1 = "Helvetica %d" % data.fontSize
            data.gameColor2 = "Helvetica %d bold" % data.fontSize
        if (data.gameType == 'Test'):
            data.gameColor1 = "Helvetica %d bold" % data.fontSize
            data.gameColor2 = "Helvetica %d" % data.fontSize
    
    # Hard
    if (event.x > (2/7) * data.width and event.x < (3/7) * data.width and event.y > (data.rows - 1) * (data.height // data.rows) and event.y < (data.rows) * (data.height // data.rows) and data.page == "Game" and data.gameType == "Regular" and data.clicked == False):
        data.progress += 1
        data.showDef = True
        data.pause = True
        data.clicked = True
        data.timeData.append([data.username, data.page, data.gameType, data.timerCalls, data.currentTerm])
        print(data.timeData)
        print('hi')
        print(data.page)
    # 
    # Good    
    if (event.x > (3/7) * data.width and event.x < (4/7) * data.width and event.y > (data.rows - 1) * (data.height // data.rows) and event.y < (data.rows) * (data.height // data.rows) and data.page == "Game" and data.gameType == "Regular" and data.clicked == False):
        data.progress += 3
        data.showDef = True
        data.pause = True
        data.clicked = True
        print('hi')
        print(data.page)
        print(data.pause)

    # Easy    
    if (event.x > (4/7) * data.width and event.x < (5/7) * data.width and event.y > (data.rows - 1) * (data.height // data.rows) and event.y < (data.rows) * (data.height // data.rows) and data.page == "Game" and data.gameType == "Regular" and data.clicked == False):
        data.progress += 5
        data.showDef = True
        data.clicked = True
        data.pause = True
        print('hi')
        print(data.page)

def keyPressed(event, data):
    if (data.logIn == True):
        if (event.keysym == 'Up' and data.currentTerm < 
        len(data.termDefs) - 1 and data.page != 'Test'):
            data.pickThree = random.sample(range(len(data.termDefs)), 3)
            data.currentTerm += 1
            data.showDef = False
            data.pause = False
            data.clicked = False
            data.timerCalls = 0
        if (event.keysym == 'Down' and data.currentTerm > 0 and data.page != 'Test'):
            data.pause = False
            data.pickThree = random.sample(range(len(data.termDefs)), 3)
            data.currentTerm -= 1
            data.clicked = False
            data.showDef = False
            data.timerCalls = 0
        if (event.keysym == 's'):
            data.showDef = True
        if (event.keysym == 't'):
            data.page = 'Test'
        if (data.page == 'Test' and (event.keysym == 'a' or event.keysym == 'b' or event.keysym == 'c' or event.keysym == 'd') and data.page == 'Test'):
            if (event.keysym == 'a' and data.page == 'Test' and data.termDefs[data.pickThree[0]] == data.termDefs[data.currentTerm]):
                data.progress += 1
                data.numCorrect += 1
    
            elif (event.keysym == 'b' and data.page == 'Test' and data.termDefs[data.pickThree[1]] == data.termDefs[data.currentTerm]):
                data.progress += 1
                data.numCorrect += 1
    
            elif (event.keysym == 'c' and data.page == 'Test' and data.termDefs[data.pickThree[2]] == data.termDefs[data.currentTerm]):
                data.progress += 1
                data.numCorrect += 1
    
            elif (event.keysym == 'd' and data.page == 'Test' and data.termDefs[data.pickThree[0]] != data.termDefs[data.currentTerm] and data.termDefs[data.pickThree[1]] != data.termDefs[data.currentTerm] and data.termDefs[data.pickThree[2]] != data.termDefs[data.currentTerm]):
                data.progress += 1
                data.numCorrect += 1
    
            if (data.currentTerm < len(data.termDefs) - 1):
                data.currentTerm += 1
            else:
                data.page = 'Congrats'
                data.currentTerm = 0

def timerFired(data):
    if ((data.page == 'Game' or data.page == 'Test') and data.pause == False):
        data.timerCalls += 1

def redrawAll(canvas, data):
    homeButtonLeft = .85
    homeButtonRight = .93
    homeWidth = 5/7
    homeWidthRight = 6/7
    homeAvg = 5.5
    
    # Draw red line
    canvas.create_line(0, data.height // data.rows, data.width, 
        data.height // data.rows, fill = 'red', width = data.redWidth)
        
    # Draw black lines
    for i in range(data.startRow, data.rows):
        canvas.create_line(0, i * (data.height // data.rows), data.width,
            i * (data.height // data.rows), fill = 'dodgerblue')
    
    # Username info
    canvas.create_text(data.width, 0, text = "User: %s" % user, 
            anchor = NE, font = "Helvetica %d" % 
            data.fontSize)
        
    # Home button
    canvas.create_rectangle(homeWidth * data.width, (data.rows - 1) * 
        (data.height // data.rows), homeWidthRight*data.width, (data.rows) *       
        (data.height // data.rows), fill = None, width = 2)
    canvas.create_text((homeAvg/7) * data.width, (2 * data.rows - 1) * .5 *         
        (data.height // data.rows), text = "Home", font = "Helvetica %d bold" %
        data.fontSize)
    
    # Level info
    canvas.create_text(0, 0, text = "Level %d: %d/20" % 
            (data.level, data.progress), anchor = NW, font = 
            "Helvetica %d" % data.fontSize)
        
    # User dashboard page (called 'Stats')
    if (data.page == 'Stats'):
        pass
        
    if (data.page == 'Test'):
        canvas.create_rectangle((0) * data.width, (data.rows - 1) *
            (data.height // data.rows), (1/7) * data.width, (data.rows) *
            (data.height // data.rows), fill = None, width = 2)
        canvas.create_text((0.5/7) * data.width, (2 * data.rows - 1) * .5 *         
            (data.height // data.rows), text = "Prev", font = "Helvetica 30 bold")
            
        canvas.create_rectangle((6/7) * data.width, (data.rows - 1) * 
            (data.height // data.rows), data.width, (data.rows) *       
            (data.height // data.rows), fill = None, width = 2)
        canvas.create_text((6.5/7) * data.width, (2 * data.rows - 1) * .5 *         
            (data.height // data.rows), text = "Next", font = "Helvetica 30 bold")
            
        canvas.create_text(data.width // 2, (.25) * data.height, 
            text = data.terms[data.currentTerm], font = "Helvetica 50 bold")
        if (data.showDef == True):
            canvas.create_text(data.width // 2, (.65) * data.height, 
                text = data.termDefs[data.currentTerm], font = "Helvetica 30",
                width = data.width // 2)
            
        canvas.create_text(data.width // 2, (0.5/data.rows) * data.height, 
            text = "Card %d/%d" % (data.currentTerm + 1, len(data.terms)), font =  "Helvetica 30")
            
        canvas.create_text(data.width * .9, data.height * .3, text="Time: " +
            str(data.timerCalls), width = data.width // 6, font = 
            "Helvetica %d bold" % data.fontSize)
        
        defnList = []
        for defn in data.pickThree:
            print(data.termDefs[defn])
            defnList.append(data.termDefs[defn])
        
        canvas.create_text(data.width / 2, data.height * .4, text = "A) %s" % defnList[0], font = "Helvetica %d" % (data.height * .05), width = data.width * .7)
        canvas.create_text(data.width / 2, data.height * .55, text = "B) %s" % defnList[1], font = "Helvetica %d" % (data.height * .05), width = data.width * .7)
        canvas.create_text(data.width / 2, data.height * .7, text = "C) %s" % defnList[2], font = "Helvetica %d" % (data.height * .05), width = data.width * .7)
        canvas.create_text(data.width / 2, data.height * .85, text = "D) None of the above", font = "Helvetica %d" % (data.height * .05), width = data.width * .7)
        
    if (data.page == 'Cards'):
        canvas.create_rectangle((0) * data.width, (data.rows - 1) *
            (data.height // data.rows), (1/7) * data.width, (data.rows) *
            (data.height // data.rows), fill = None, width = 2)
        canvas.create_text((0.5/7) * data.width, (2 * data.rows - 1) * .5 *         
            (data.height // data.rows), text = "Prev", font = "Helvetica %d bold" % data.fontSize)
            
        canvas.create_rectangle((6/7) * data.width, (data.rows - 1) * 
            (data.height // data.rows), data.width, (data.rows) *       
            (data.height // data.rows), fill = None, width = 2)
        canvas.create_text((6.5/7) * data.width, (2 * data.rows - 1) * .5 *         
            (data.height // data.rows), text = "Next", font = "Helvetica %d bold" % data.fontSize)
            
        canvas.create_text(data.width // 2, (.25) * data.height, 
            text = data.terms[data.currentTerm], font = "Helvetica %d bold" % (1.6 * data.fontSize))
        
        canvas.create_text(data.width // 2, (.65) * data.height, 
                text = data.termDefs[data.currentTerm], font = "Helvetica %d" % data.fontSize,
                width = data.width // 2)
            
        canvas.create_text(data.width // 2, (0.5/data.rows) * data.height, 
            text = "Card %d/%d" % (data.currentTerm + 1, len(data.terms)), font
            = "Helvetica %d" % data.fontSize)
        
        canvas.create_rectangle((6/7) * data.width, (int(.25*data.rows)) * 
            (data.height // data.rows), data.width, (int(.25*data.rows) + 1) *       
            (data.height // data.rows), fill = None, width = 2)
        canvas.create_text((6.5/7) * data.width, (2 * int(.25*data.rows) + 1) * .5 * (data.height // data.rows), text = "Edit", font = "Helvetica %d bold" % data.fontSize)  
        
        canvas.create_rectangle((6/7) * data.width, (int(.6*data.rows)) * 
            (data.height // data.rows), data.width, (int(.6*data.rows) + 1) *       
            (data.height // data.rows), fill = None, width = 2)
        canvas.create_text((6.5/7) * data.width, (2 * int(.6*data.rows) + 1) * .5 * (data.height // data.rows), text = "Edit", font = "Helvetica 30 bold") 
        
        canvas.create_rectangle(0, (int(.5*data.rows)) * 
            (data.height // data.rows), (1/7) * data.width, (int(.5*data.rows) + 1) *       
            (data.height // data.rows), fill = None, width = 2)
        canvas.create_text((0.5/7) * data.width, (2 * int(.5*data.rows) + 1) * .5 * (data.height // data.rows), text = "New", font = "Helvetica %d bold" % data.fontSize)

        # newCard = input("What is your new term?")
        # print(newCard)
    
    # Waterfall Flashcard home page
    if (data.page == 'Home'):
        canvas.create_text(data.width // 2, data.height // 2, 
            text = "Waterfall Flashcards", font = "Helvetica 50 bold")
        
        # Stats box
        canvas.create_rectangle((.65) * data.width, (.65) * data.height,
            (.85) * data.width, (.85) * data.height, fill = None,
            width = 3)
        canvas.create_text(data.width * (.75), data.height * (.75),
            text = "Stats", font = "Helvetica 40 bold", fill = "blue")
            
        # Test box
        canvas.create_rectangle((.65) * data.width, (.15) * data.height,
            (.85) * data.width, (.35) * data.height, fill = None,
            width = 3)
        canvas.create_text(data.width * (.75), data.height * (.25),
            text = "Test", font = data.gameColor1)
            
        # Regular box
        canvas.create_rectangle((.4) * data.width, (.15) * data.height,
            (.6) * data.width, (.35) * data.height, fill = None,
            width = 3)
        canvas.create_text(data.width * (.5), data.height * (.25),
            text = "Regular", font = data.gameColor2)
        
        # Start box
        canvas.create_rectangle((.4) * data.width, (.65) * data.height,
            (.6) * data.width, (.85) * data.height, fill = None,
            width = 3)
        canvas.create_text(data.width * (.5), data.height * (.75),
            text = "Start", font = "Helvetica 40 bold", fill = "green")
        
        # Cards box
        canvas.create_rectangle((.15) * data.width, (.65) * data.height,
            (.35) * data.width, (.85) * data.height, fill = None,
            width = 3)
        canvas.create_text(data.width * (.25), data.height * (.75),
            text = "Cards", font = "Helvetica 40 bold", fill = "indigo")
    
    if (data.page == 'Game'):
        canvas.create_rectangle((0) * data.width, (data.rows - 1) *
            (data.height // data.rows), (1/7) * data.width, (data.rows) *
            (data.height // data.rows), fill = None, width = 2)
        canvas.create_text((0.5/7) * data.width, (2 * data.rows - 1) * .5 *         
            (data.height // data.rows), text = "Prev", font = "Helvetica 30 bold")
            
        canvas.create_rectangle((2/7) * data.width, (data.rows - 1) *
            (data.height // data.rows), (3/7) * data.width, (data.rows) *
            (data.height // data.rows), fill = 'red')
        canvas.create_text((2.5/7) * data.width, (2 * data.rows - 1) * .5 *
            (data.height // data.rows), text = "Hard", font = 
            "Helvetica 30 bold")
        canvas.create_rectangle((3/7) * data.width, (data.rows - 1) * 
            (data.height // data.rows), (4/7) * data.width, (data.rows) *                   
            (data.height // data.rows), fill = 'yellow')
        canvas.create_text((3.5/7) * data.width, (2 * data.rows - 1) * .5 *
            (data.height // data.rows), text = "Good", font = "Helvetica 30 bold")
        canvas.create_rectangle((4/7) * data.width, (data.rows - 1) * 
            (data.height // data.rows), (5/7) * data.width, (data.rows) *       
            (data.height // data.rows), fill = 'green')
        canvas.create_text((4.5/7) * data.width, (2 * data.rows - 1) * .5 *         
            (data.height // data.rows), text = "Easy", font = "Helvetica 30 bold")
            
        canvas.create_rectangle((6/7) * data.width, (data.rows - 1) * 
            (data.height // data.rows), data.width, (data.rows) *       
            (data.height // data.rows), fill = None, width = 2)
        canvas.create_text((6.5/7) * data.width, (2 * data.rows - 1) * .5 *         
            (data.height // data.rows), text = "Next", font = "Helvetica 30 bold")
            
        canvas.create_text(data.width // 2, (.25) * data.height, 
            text = data.terms[data.currentTerm], font = "Helvetica 50 bold")
        if (data.showDef == True):
            canvas.create_text(data.width // 2, (.65) * data.height, 
                text = data.termDefs[data.currentTerm], font = "Helvetica 30",
                width = data.width // 2)
            
        canvas.create_text(data.width // 2, (0.5/data.rows) * data.height, 
            text = "Card %d/%d" % (data.currentTerm + 1, len(data.terms)), font =  "Helvetica 30")
            
        canvas.create_text(data.width * .9, data.height * .3, text="Time: " +
            str(data.timerCalls), width = data.width // 5, font = 
            "Helvetica %d bold" % data.fontSize)
    
    if (data.page == 'Congrats'):
        canvas.create_text(data.width / 2, data.height / 2, 
        text = "Congrats! You got %d correct out of %d" % (data.numCorrect, 
        len(data.termDefs)))
    

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    lf = LoginFrame(root, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(800, 400)
run(1200, 600)