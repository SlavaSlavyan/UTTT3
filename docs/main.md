For now, everything I've written here will be in one file. Later, of course, I'll scatter it all and probably completely rewrite it. 

### **THE INFORMATION IN THIS DOCUMENTATION MAY NO LONGER BE UP-TO-DATE**.

## **Project structure**

```text
root/                 
├── data/             # Additional data
├── scene/            # Scenes
├── src/              # Main folder
│   ├── display.py    # Displaying information on the screen
│   ├── event.py      # Event handling
│   └── program.py    # Main class
├── util/             # Utilities
│   ├── log.py        # Log handler
│   ├── mouse.py      # Mouse handler
│   └── scene.py      # Scene loader
├── .gitignore        # Git exceptions
├── README.md         # You are here!
└── start.py          # Entry point
```

I'll say right away that I didn't describe the scenes, because firstly, I'm lazy asf :), and secondly, each scene contains at least 4 files and a folder with another bunch of files.

I will definitely write all of this in the future when at least one scene is completely ready.

**Well, now briefly about each file and their methods.**

## **start.py**

Needed to start ¯\\\_(ツ)\_/¯. Currently does not contain any methods or classes EXCEPT an instance of the main Program class.

`Program("version").main()`


This is literally how the main class is initialized inside this file :P

## **program.py**

The main class of the program, essentially the root. Most functions or classes have a reference to it (mainself). This allows you to reach from any point in the code to another. It is **LITERALLY** not safe ASFF, but unfortunately it is too convenient to refuse.

This class also loads most utilities, as well as the **Display** and **Event** classes.

Currently contains:
- Display
- Event
- Log
- Scene

It also has important variable - <span style="color:#e06c75">**status**</span> <span style="color:gray">*(string)*</span>. It's responsible for displaying all scenes and their logic. Classes Display and Event define their work using this variable.

Well, there are two main methods, `start()` and `stop()`, which begin and end the program's operation, respectively.

---

uhh... I understand everything of course, but damn, I'm so tired of writing this fucking documentation. It's almost one in the morning and I'm actually doing some kind of bullshit. I will continue writing all this in the next few days, as I have already spent TOO much effort on it. I'm starting to lose faith that using AI to write documentation is bad...

Oh well, I can whine forever. Bye everyone!

---

<span style="color:gray">*doc version 1.0 for UTTT version 3.0.2*</span>