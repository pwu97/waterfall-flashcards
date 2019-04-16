# Updated Animation Starter Code
# Starter code from 15-112 Lecture Notes
# https://quizlet.com/subject/8th-edition-biology-campbell/
# https://blog.prepscholar.com/the-best-way-to-study-sat-vocab-words
# https://apps.ankiweb.net/

from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    # load data.xyz as appropriate
    data.timerDelay = 1000 # 100 millisecond == 0.1 seconds
    data.timerCalls = 0
    data.rows = 10
    data.startRow = 2
    data.redWidth = 2
    data.currentTerm = 0
    data.terms = ['Biology', 'Organelles', 'Cells', 'Prokaryotics Cells',
        'Eukaryotic Cells', 'Tissue', 'Organ', 'Organ System']
    data.termDefs = [
    'The study of life or all that lived', 'Parts of a cell that perform    specific functions for it', 'Smallest unit of life functional units of life', 'Cells that lack a nuclear envelope around their DNA', 'Cells that have DNA enclosed by a nuclear envelope', 'A group of cells that perform the same function', 'A group of tissue that perform a function for an organism', 'A group of organs that generally perform the same function or are related to each other in function']
    data.showDef = False
    data.username = 'Peter'
    data.level = 1
    data.progress = 0
    data.page = 'Home'
    

def mousePressed(event, data):
    # Cards, Start, Stats boxes variables
    boxLength = .20
    boxLeft1 = .15
    boxLeft2 = .40
    boxLeft3 = .65
    
    # Navigate to Stats page
    if (event.x > (boxLeft3) * data.width and event.x < 
    (boxLeft3 + boxLength) * data.width and event.y > 
    (boxLeft3) * data.height and event.y < (boxLeft3 + boxLength) *     
    data.height and data.page == 'Home'):
        data.page = 'Stats'
    
    # Navigate to Game
    if (event.x > (boxLeft2) * data.width and event.x < 
    (boxLeft2 + boxLength) * data.width and event.y > (boxLeft3) * 
    data.height and event.y < (boxLeft3 + boxLength) * 
    data.height and data.page == 'Home'):
        data.page = 'Game'
        
    # Navigate to Cards
    if (event.x > (boxLeft1) * data.width and event.x < 
    (boxLeft1 + boxLength) * data.width and event.y > (boxLeft3) 
    * data.height and event.y < (boxLeft3 + boxLength) * 
    data.height and data.page == 'Home'):
        data.page = 'Cards'
    

def keyPressed(event, data):
    # use event.char and event.keysym
    
    if (event.keysym == 'Up' and data.currentTerm < 
    len(data.termDefs) - 1):
        data.currentTerm += 1
        data.showDef = False
        data.timerCalls = 0
    if (event.keysym == 'Down' and data.currentTerm > 0):
        data.currentTerm -= 1
        data.showDef = False
        data.timerCalls = 0
    if (event.keysym == 's'):
        data.showDef = True
        

def timerFired(data):
    data.timerCalls += 1

def redrawAll(canvas, data):
    homeButtonLeft = .85
    homeButtonRight = .93
    
    
    # Draw red line
    canvas.create_line(0, data.height // data.rows, data.width, 
        data.height // data.rows, fill = 'red', width = data.redWidth)
        
    # Draw black lines
    for i in range(data.startRow, data.rows):
        canvas.create_line(0, i * (data.height // data.rows), data.width,
            i * (data.height // data.rows), fill = 'dodgerblue')
    
    # Username info
    canvas.create_text(data.width, 0, text = "User: %s" % data.username, 
        anchor = NE, font = "Helvetica %d" % 
        (data.height // data.rows))
        
    # Home button
    canvas.create_rectangle((homeButtonLeft) * data.width, 
        (homeButtonRight) * data.height, data.width, data.height, 
        fill = None, width = 3)
    canvas.create_text(data.width, data.height, text = "Home Page", 
        anchor = SE, font = "Helvetica %d bold" % 
        (data.height // data.rows * .5))
    
    # Level info
    canvas.create_text(0, 0, text = "Level %d: %d/20" % 
        (data.level, data.progress), anchor = NW, font = 
        "Helvetica %d" % (data.height // data.rows))
        
    # User dashboard page (called 'Stats')
    if (data.page == 'Stats'):
        pass
        
    
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
            text = "Card %d/%d" % (data.currentTerm + 1, len(data.terms)), font =       
            "Helvetica 30")
        canvas.create_rectangle((5.5/7) * data.width, 0, data.width, (1/data.rows) * 
            data.height, fill = None, width = 2)
        canvas.create_text((6.3/7) * data.width, (1) * .5 *         
            (data.height // data.rows), text = "View Stats", font = 
            "Helvetica 30 bold")
            
        canvas.create_text(data.width * .9, data.height * .3, text="Time" +
            str(data.timerCalls), width = data.width // 6, font = 
            "Helvetica 50 bold")
    

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
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(800, 400)
run(1200, 600)