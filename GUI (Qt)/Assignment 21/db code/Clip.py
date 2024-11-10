from Media import Media
import Actor

actors = []


class Clip(Media):
    def __init__(self, na, dir, imd, ur, dur, actors, reda, lang,time, t, s, q):
        super().__init__(na, dir, imd, ur, dur, actors, reda, lang,time)
        self.type = "Clip"
        self.topic = t  # The main topic or subject of the clip
        self.source = s  # Source of the clip (e.g., website, TV channel)
        self.quality = q  # Quality of the clip (e.g., HD, SD)

    def add(self):
        na = input("please give me the name of the Clip: ")
        dir = input("please give me the name of director of the Clip: ")
        imd = input("please give me the IMDB score of the Clip: ")
        ur = input("please give me the url of the Clip: ")
        dur = input("please give me the duration of the Clip: ")
        while True:
            cas = input(
                "please give me the name , age , nationality and height of the casts: //insert 0 to break! ")
            if cas == 0:
                break
            else:
                result = cas.strip().split(",")
                x = Actor(result[0], result[1], result[2], result[3])
            actors.append(x)
        reda = input("please give me the release date of the Clip: ")
        lang = input("please give me the language of the Clip: ")
        time = input("please give me the time of the Clip: ")
        t = input("please give me the topic of the Clip: ")
        s = input("please give me the source of the Clip: ")
        q = input("please give me the quality of the Clip: ")
        self(na, dir, imd, ur, dur, actors, reda, lang,time, t, s, q)
        return (self)

    def edit(self):
        print("what parameter do you want to change?")
        print("1- name")
        print("2- director")
        print("3- IMDB score")
        print("4- url")
        print("5- duration")
        print("6- casts")
        print("7- release_date")
        print("8- language")
        print("9- time")
        print("10- topic")
        print("11- source")
        print("12- quality")
        flag = int(input(""))
        if flag == 1:
            new_name = input("what's the new name?"+"\n")
            self.name = new_name
            print("👍")
            return
        elif flag == 2:
            new_director = input("what's the new director?"+"\n")
            self.director = new_director
            print("👍")
            return
        elif flag == 3:
            new_imdb = input("what's the new IMDB score?"+"\n")
            self.IMDBscore = new_imdb
            print("👍")
            return
        elif flag == 4:
            new_url = input("what's the new url?"+"\n")
            self.url = new_url
            print("👍")
            return
        elif flag == 5:
            new_duration = input("what's the new time?"+"\n")
            self.duration = new_duration
            print("👍")
            return
        elif flag == 6:
            print("Do you wanna change an actor or remove?")
            print("1- change")
            print("2- remove")
            flag = int(input(""))
            if flag == 1:
                self.showinfo(self.casts)
                cas = input(
                        "please give me the name of actor you want to change:"+"\n")
                for obj in self.casts:
                    if cas == obj.name:
                        c = input(
                            "please give me the name , age , nationality and height of the new actor:"+"\n")
                        result = c.strip().split(",")
                        obj[0]=result[0]
                        obj[1]=result[1]
                        obj[2]=result[2]
                        obj[3]=result[3]
                        break
                else:
                    print("there is no such an actor!")
                    
            elif flag == 2:
                self.showinfo(self.casts)
                cas = input(
                        "please give me the name of actor you want to remove:"+"\n")
                for obj in self.casts:
                    i =0
                    if cas == obj.name:
                        del self.casts[i]
                        break
                    else:
                        i+=1
                else:
                    print("there is no such an actor!")
                return
            else:
                print("your input is not correct!!")
            return
        elif flag == 7:
            new_date = input("what's the new date?"+"\n")
            self.release_date = new_date
            print("👍")
            return
        elif flag == 8:
            new_lang = input("what's the new language?"+"\n")
            self.language = new_lang
            print("👍")
            return
        elif flag == 9:
            new_time = input("what's the new time?"+"\n")
            self.time = new_time
            print("👍")
            return
        elif flag == 10:
            new_topic = input("what's the new topic?"+"\n")
            self.topic = new_topic
            print("👍")
            return
        elif flag == 11:
            new_source = input("what's the new source?"+"\n")
            self.source = new_source
            print("👍")
            return
        elif flag == 12:
            new_quality = input("what's the new quality?"+"\n")
            self.quality = new_quality
            print("👍")
            return
        else:
            print("your input is not correct!!")
        return
