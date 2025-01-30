# Py-learn-assignment-22
تمرین جلسه بیست و دوم
## Python-GUI(Qt)

![GUI](assets/GUI.jpg)

### Session 22

<p>In this session, we're going to be more engage with database and an ui which is a To-Do List.</p>

#### database

<p>Database is a sqlite and has {id,title, description, time, date, is_done, priority} attribute which according to the different part of the code, our job is vary.</p>

#### ui

<p>it has two layer on itself which one of them is for showing the database information and another one for adding the new work to database.</p>

![pic](assets/ui.jpg)

##### different method

<p>1- we have delete which is obvious that will remove the data from the database, second the priority is that change the style of the object to tell user more important job or work haven't done yet according to the priority, title is a push_button and is for showing its details to come up with a clue for your purpose of your job and the last one is for checking that you have done it or not!</p>

<p>2- on the bottom of the page you see the inputs of the to-do list which gets the inputs of the programme, all of them considered as a Text.</p>

---

### pyinstaller

#### installation

easy to install and use


 ```
pip install pyinstaller
 ```

the main file of your project will be execute as a one file with the code below 

```
pyinstaller main.py --onefile
```

<p>I hope, you will learn something from my repo!</p> 
<p>good luck</p>