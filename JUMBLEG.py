from tkinter import *
from tkinter import messagebox as mb
import random
import winsound as ws
import time
import os
import sys

root = Tk()
root.geometry('660x490+250+120')
root.title("Welcome To The Game Of Jumbled Words - RSP")
root.resizable(FALSE,FALSE)
#root.iconbitmap('Icon.ico')
root.config(bg='#f26712')

ans1 = ['apple', 'banana', 'grapes', 'orange', 'pear', 'bear', 'ball', 'cow', 'bull', 'dogs', 'try', 'good', 'bad',
        'cool', 'bush']
words1 = ['ppale', 'nabaan', 'sepgar', 'ageorn', 'earp', 'areb', 'labl', 'ocw', 'llub', 'sdog', 'yrt', 'odgo', 'abd',
          'oloc', 'shub']
ans2 = ['company', 'leverage', 'kitchen', 'burger', 'hello', 'synonym', 'aggresive', 'tunnel', 'blasted', 'druggist',
        'property', 'bungalow', 'heroistic', 'blogger', 'developer']
words2 = ['anycpom', 'agerevel', 'kenchit', 'urgeub', 'hloel', 'onymnys', 'siveregag', 'nutlen', 'adlbest', 'strugigd',
          'tryoprpe', 'nlowubga', 'shitroice', 'globerg', 'eproveled']
ans3 = ['asteroid', 'flowers', 'fruits', 'basket', 'song', 'college', 'random', 'jumbled', 'bitter', 'powder',
        'headache', 'stadium', 'beach', 'lover', 'friends']
words3 = ['roidestar', 'slowrefw', 'ritsuf', 'skateb', 'nosg', 'lecogel', 'modran', 'jemdlub', 'britet', 'wpored',
          'hdecheaa', 'tadisum', 'cheab', 'rolve', 'drienfs']
ans4 = ['electronics', 'glacier', 'pressure', 'communication', 'evolution', 'childhood', 'imagination', 'ambulance',
        'international', 'instagram', 'facebook', 'gambler', 'phenomenal', 'paranoid', 'champion']
words4 = ['setroncecil', 'algrice', 'spureser', 'cationmonicum', 'luvoteion', 'idocholod', 'natimanigio', 'malbumace',
          'rationlatenin', 'ramgistan', 'bacekofo', 'bagrlem', 'manophenol', 'danapoin', 'panmioch']
ans5 = ['migration', 'environment', 'microscope', 'temperature', 'elephant', 'continental', 'experiment', 'nucleus',
        'molecule', 'platinum', 'skeleton', 'metamorphism', 'photosynthesis', 'eclipse', 'astronaut']
words5 = ['imrtginaoi', 'evrntoenmni', 'ircspmeoco', 'erettarpuem', 'hnlaptew', 'tnnnletacio', 'pxmtianleere',
          'cesnuleu', 'ouellcme', 'lmutnpia', 'ktnlose', 'tearhmspmiom', 'ohtytspseinhso', 'cleespi', 'stoutananr']

ws.PlaySound('mp3/bg-game.wav',ws.SND_FILENAME|ws.SND_ASYNC|ws.SND_ALIAS)

def resource_path(relative_path):
    if hasattr(sys,'_MEIPASS'):
        return os.path.join(sys._MEIPASS,relative_path)
    return os.path.join(os.path.abspath("."),relative_path)


def bg_sound():
    ws.PlaySound('mp3/bg-game.wav',ws.SND_FILENAME|ws.SND_ASYNC|ws.SND_ALIAS)
    pass

score = 0
curr_level = 1
num = int(random.randrange(0, 15))


intro_frame = Frame(root,width=350,height=200,bd=13,bg='#784512')
intro_text = "Hello, Friends! \n Are you ready to play this game."
intro_label = Label(intro_frame,text=intro_text,bg="#ffffff",fg="#000000",font=('Arial Bold', 20))

intro_frame.place(x=90,y=15)
intro_label.pack()

rules_frame = Frame(root,width=350,height=130,bd=13,bg='#784512')
r1="Rules are quite simple. \n"
r2 =" You have to guess the correct word from the jumbled one,\n"
r3=" that will be displayed on your screen.\n"
r4=" There will only be 15 seconds time for you to guess it \n"
r5=" You have to guess and write it in text field given \n"
r6=" And Then Click on check Button. \n"
r7=" NOTE: Sometimes same jumbled words can be repeated \n"
r8=" 5 Levels - 50 Points \n"
r9=" Click on start button to start. \n"
r10=" Once clicked, Timer will automatically start. "
rules_text = r1  + r2 + r3 + r4 + r5 + r6 + r7 + r8 + r9 + r10
rules_label = Label(rules_frame,text=rules_text,bg="#ffffff",fg="#000000",font=('Arial Bold', 15))

rules_frame.place(x=30,y=130)
rules_label.pack()

def st():
    global words1, ans1, words2, ans2, num, score, words3, ans3, words4, ans4, words5, ans5 , uni_num,jum_label
    if score <= 10:
        jum_label.config(text=words1[num])
        uni_num = num
    elif 10 < score <= 20:
        jum_label.config(text=words2[num])
        uni_num = num
    elif 20 < score <= 30:
        jum_label.config(text=words3[num])
        uni_num = num
    elif 30 < score <= 40:
        jum_label.config(text=words4[num])
        uni_num = num
    else:
        jum_label.config(text=words5[num])
        uni_num = num

def check():
    global words1, ans1, num, score, words2, ans2, words3, ans3, words4, ans4, words5, ans5, uni_num,e,curr_level,root,ws
    var = e.get().lower()
    if score < 10:
        if var == ans1[num]:
            ws.PlaySound('mp3/right.wav',ws.SND_FILENAME|ws.SND_ALIAS)
            bg_sound()
            mb._show("Answer", str((words1[num])) + " has correct value " + str((ans1[num])))
            mb.showinfo("Success", "Next")
            score += 1
            reset()
            start_window()
        else:
            ws.PlaySound('mp3/fail.wav',ws.SND_FILENAME|ws.SND_ASYNC|ws.SND_ALIAS)
            bg_sound()
            mb.showerror("Game Over", "Retry")
            qt()
            e.delete(0, END)
    elif score == 10:
        if var == ans1[num]:
            ws.PlaySound('mp3/cp.wav',ws.SND_FILENAME|ws.SND_ASYNC|ws.SND_ALIAS)
            bg_sound()
            mb._show("Answer", str((words1[num])) + " has correct value " + str((ans1[num])))
            mb.showinfo("Level 2 starts now", "Ohh, You are playing well Your score is now 10")
            score += 1
            curr_level += 1
            reset()
            start_window()
        else:
            ws.PlaySound('mp3/fail.wav',ws.SND_FILENAME|ws.SND_ASYNC|ws.SND_ALIAS)
            bg_sound()
            mb._show("Answer", str((words1[num])) + " has correct value " + str((ans1[num])))
            mb.showerror("Game Over", "Try Again . Don't Worry")
            e.delete(0, END)
    elif 11 <= score < 20:
        if var == ans2[num]:
            ws.PlaySound('mp3/right.wav',ws.SND_FILENAME|ws.SND_ASYNC|ws.SND_ALIAS)
            bg_sound()
            mb._show("Answer", str((words2[num])) + " has correct value " + str((ans2[num])))
            mb.showinfo("Level 2", "Words Coming")
            score += 1
            reset()
            start_window()
        else:
            ws.PlaySound('mp3/fail.wav',ws.SND_FILENAME|ws.SND_ASYNC|ws.SND_ALIAS)
            bg_sound()
            mb._show("Answer", str((words2[num])) + " has correct value " + str((ans2[num])))
            mb.showerror("Game Over", "Try Again . Don't Worry")
            e.delete(0, END)
    elif score == 20:
        if var == ans2[num]:
            ws.PlaySound('mp3/cp.wav',ws.SND_FILENAME|ws.SND_ASYNC|ws.SND_ALIAS)
            bg_sound()
            mb._show("Answer", str((words2[num])) + " has correct value " + str((ans2[num])))
            mb.showinfo("Level 3 starts ", "Good job...\n Your Current score is 20")
            score += 1
            curr_level += 1
            reset()
            start_window()
        else:
            ws.PlaySound('mp3/fail.wav',ws.SND_FILENAME|ws.SND_ASYNC|ws.SND_ALIAS)
            bg_sound()
            mb._show("Answer", str((words2[num])) + " has correct value " + str((ans2[num])))
            mb.showerror("Game Over", "Retry")
            e.delete(0, END)
    elif 20 < score < 30:
        if var == ans3[num]:
            ws.PlaySound('mp3/right.wav',ws.SND_FILENAME|ws.SND_ASYNC|ws.SND_ALIAS)
            bg_sound()
            mb._show("Answer", str((words3[num])) + " has correct value " + str((ans3[num])))
            mb.showinfo("Level 3", "Next one Please.")
            score += 1
            reset()
            start_window()
        else:
            ws.PlaySound('mp3/fail.wav',ws.SND_FILENAME|ws.SND_ASYNC|ws.SND_ALIAS)
            bg_sound()
            mb._show("Answer", str((words3[num])) + " has correct value " + str((ans3[num])))
            mb.showerror("Game Over", "Good Performance")
            e.delete(0, END)
    elif score == 30:
        if var == ans3[num]:
            ws.PlaySound('mp3/cp.wav',ws.SND_FILENAME|ws.SND_ASYNC|ws.SND_ALIAS)
            bg_sound()
            mb._show("Answer", str((words3[num])) + " has correct value " + str((ans3[num])))
            mb.showinfo("Level 4 starts ", "Brilliant...Lets see how far you can go.\n Your Current score is 30")
            score += 1
            curr_level += 1
            reset()
            start_window()
        else:
            ws.PlaySound('mp3/fail.wav',ws.SND_FILENAME|ws.SND_ASYNC|ws.SND_ALIAS)
            bg_sound()
            mb._show("Answer", str((words3[num])) + " has correct value " + str((ans3[num])))
            mb.showerror("Game Over", "Retry")
            e.delete(0, END)
    elif 30 < score < 40:
        if var == ans4[num]:
            ws.PlaySound('mp3/right.wav',ws.SND_FILENAME|ws.SND_ASYNC|ws.SND_ALIAS)
            bg_sound()
            mb._show("Answer", str((words4[num])) + " has correct value " + str((ans4[num])))
            mb.showinfo("Level 4", "Finish this quickly")
            score += 1
            reset()
            start_window()
        else:
            ws.PlaySound('mp3/fail.wav',ws.SND_FILENAME|ws.SND_ASYNC|ws.SND_ALIAS)
            bg_sound()
            mb._show("Answer", str((words4[num])) + " has correct value " + str((ans4[num])))
            mb.showerror("Game Over", "You were almost there...")
            e.delete(0, END)
    elif score == 40:
        if var == ans4[num]:
            ws.PlaySound('mp3/cp.wav',ws.SND_FILENAME|ws.SND_ASYNC|ws.SND_ALIAS)
            bg_sound()
            mb._show("Answer", str((words4[num])) + " has correct value " + str((ans4[num])))
            mb.showinfo("The final Level ", "Can you finish off in style ? \n Your Current score is 40")
            score += 1
            curr_level += 1
            reset()
            start_window()
        else:
            ws.PlaySound('mp3/fail.wav',ws.SND_FILENAME|ws.SND_ASYNC|ws.SND_ALIAS)
            bg_sound()
            mb._show("Answer", str((words4[num])) + " has correct value " + str((ans4[num])))
            mb.showerror("Game Over", "Retry")
            e.delete(0, END)
    elif 40 < score < 50:
        if var == ans5[num]:
            ws.PlaySound('mp3/right.wav',ws.SND_FILENAME|ws.SND_ASYNC|ws.SND_ALIAS)
            bg_sound()
            mb._show("Answer", str((words5[num])) + " has correct value " + str((ans5[num])))
            mb.showinfo("Level", "Get me the next one I'm Hungry to win")
            score += 1
            reset()
            start_window()
        else:
            ws.PlaySound('mp3/fail.wav',ws.SND_FILENAME|ws.SND_ASYNC|ws.SND_ALIAS)
            bg_sound()
            mb._show("Answer", str((words5[num])) + " has correct value " + str((ans5[num])))
            mb.showerror("Game Over", "So Far So Close...")
            e.delete(0, END)
    else:
        if var == ans5[num]:
            ws.PlaySound('mp3/winner.wav',ws.SND_FILENAME|ws.SND_ASYNC|ws.SND_ALIAS)
            bg_sound()
            mb._show("Answer", str((words5[num])) + " has correct value " + str((ans5[num])))
            mb.showinfo("WINNER", "Congratulations from RSP!!!\n $$$ You are a champion $$$")
            root.destroy()
        else:
            ws.PlaySound('mp3/fail.wav',ws.SND_FILENAME|ws.SND_ASYNC|ws.SND_ALIAS)
            ws.PlaySound('mp3/cp.wav',ws.SND_FILENAME|ws.SND_ASYNC|ws.SND_ALIAS)
            bg_sound()
            mb._show("Answer", str((words5[num])) + " has correct value " + str((ans5[num])))
            mb.showerror("Game Over", "Last One missed, You are a great Player.")
            e.delete(0, END)
            root.destroy()

def reset():
    global words1, ans1, words2, ans2, words3, ans3, words4, ans4, words5, ans5, num,score,jum_label
    num = random.randrange(0, 15)
    if score <= 10:
        jum_label.config(text=words1[num])
        e.delete(0, END)
    elif 10 < score <= 20:
        jum_label.config(text=words2[num])
        e.delete(0, END)
    elif 20 < score <= 30:
        jum_label.config(text=words3[num])
        e.delete(0, END)
    elif 30 < score <= 40:
        jum_label.config(text=words4[num])
        e.delete(0, END)
    else:
        jum_label.config(text=words5[num])
        e.delete(0, END)

def n_reset():
    global words1, ans1, words2, ans2, words3, ans3, words4, ans4, words5, ans5, num,score,jum_label
    num = random.randrange(0, 15)
    mb.showwarning("Reset game",' All your progress has been resetted.')
    if score <= 10:
        jum_label.config(text=words1[num])
        score=0
        e.delete(0, END)
    elif 10 < score <= 20:
        jum_label.config(text=words2[num])
        score = 0
        e.delete(0, END)
    elif 20 < score <= 30:
        jum_label.config(text=words3[num])
        score = 0
        e.delete(0, END)
    elif 30 < score <= 40:
        jum_label.config(text=words4[num])
        score = 0
        e.delete(0, END)
    else:
        jum_label.config(text=words5[num])
        score = 0
        e.delete(0, END)
    
def qt():
    global score,root
    if score <=10:
        if score <=10:
            mb._show("Answer",str((words1[num])) + " has correct value " + str((ans1[num])))
        else:
             None
        root.quit()
    elif score <=40:
            if 10 < score <= 20:
                  mb._show("Answer", str((words2[num])) + " has correct value " + str((ans2[num])))
            elif 20 < score <= 30:
                mb._show("Answer", str((words3[num])) + " has correct value " + str((ans3[num])))
            elif 30 < score <= 40:
                mb._show("Answer", str((words4[num])) + " has correct value " + str((ans4[num])))
            else:
                None
            mb.showinfo("WELL DONE", " Your Score is " + str(score) + " . ")
            root.quit()

    mb.showinfo("Score", " Your Score is " + str(score) + " . ")
    score=0
    root.quit()

def time_up():
    ws.PlaySound('mp3/timeup.wav',ws.SND_FILENAME|ws.SND_ASYNC)
    mb.showwarning("TIME UP","Oops, 15 seconds are over. Your Score is " + str(score) + " .  ")
    if score <= 10:
        mb._show("Answer", str((words1[num])) + " has correct value " + str((ans1[num])))
    elif 10 < score <= 20:
        mb._show("Answer", str((words2[num])) + " has correct value " + str((ans2[num])))
    elif 20 < score <= 30:
        mb._show("Answer", str((words3[num])) + " has correct value " + str((ans3[num])))
    elif 30 < score <= 40:
        mb._show("Answer", str((words4[num])) + " has correct value " + str((ans4[num])))
    else:
        mb._show("Answer", str((words5[num])) + " has correct value " + str((ans5[num])))

def timer():
    global tlb,game_window ,jum_label,e
    st()
    tlb.config(bg='yellow')
    tlb.config(height=3)
    for k in range(15, 0, -1):
        tlb["text"] = k
        game_window.update()
        time.sleep(1)
        if k <= 10:
            tlb.config(bg="orange", fg="white")
            if k <= 5:
                tlb.config(bg='red', fg='white')
                if k <=1:
                    tlb.config(bg='black', fg='red')
                    tlb["text"] = "Time up"
                    time_up()
                else:
                    continue
            else:
                continue
        else:
            continue

def start_window():
    global tlb
    global game_window
    global jum_label
    global e
    game_window = Toplevel(root)
    game_window.geometry('660x490+250+120')
    game_window.title('Jumbled Words Game')
    game_window.resizable(False, False)
    game_window.config(bg='#f19066')
   # game_window.iconbitmap('Icon.ico')

    f1 = Frame(game_window, bg='#ffc048', width=350, height=200, bd=10)

    jum_label = Label(f1, text="Start", width=25, font=('Arial Bold', 20), bg='#febfaf', fg='#000000')
    f1.place(x=70, y=70)
    jum_label.pack()

    a1 = StringVar()
    e = Entry(f1, textvariable=a1, bd=5, width=25, font=('Arial Black', 20))
    e.pack(pady=20, ipadx=5)

    f2 = Frame(game_window, bg='#ff3f34', width=200, height=200, bd=5, padx=50)

    ch_b = Button(f2, text="Show", width=10, bg='#ab6532', fg='#0f0ea7', relief=RAISED, font=('Sitka Heading', 20),command=check)
    ch_b.pack(pady=10)

    r_b = Button(f2, text="Reset", bg='black', fg='#99336b', relief=SUNKEN, font=('Rockwell Condesed', 20),command=n_reset)
    r_b.pack()

    q_b = Button(f2, text="Quit", bg='#eeffac', fg='#4C4B4B', relief=SUNKEN, font=('Rockwell Condesed', 20), command=qt)
    q_b.pack(pady=10)
    f2.place(x=310, y=240)

    f3 = Frame(game_window, bg='#ffff99', width=100, height=30, bd=5)

    status = " Current Level: {cl} \n Current Score: {cs}".format(cl=curr_level, cs=score)
    status_label = Label(f3, text=status, height=10, font=('Tahoma', 14), width=15, bg="sky blue")
    status_label.pack(ipadx=20)
    f3.place(x=65, y=240)

    t_label = Label(game_window,height=3, text="Time remaining: ",font=('Open Sans',8),bg='#45ff43',fg='red')
    t_label.place(x=450,y=11)
    tlb = Label(game_window,height=1,width=10)
    tlb.place(x=550,y=10)
    e.focus_set()
    timer()

def start():
    start_window()

start_button = Button(root,text ="START",width=10, bg='black', fg='#888888', relief=RAISED, font=('Sitka Heading', 20),
              command=start)
start_button.place(x=250,y=410)

root.mainloop()
