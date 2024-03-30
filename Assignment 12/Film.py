import Media
import Actor

actors = []
awards = []


class Film(Media):
    def __init__(self, na, dir, imd, ur, dur, actors, reda, lang,time, g, b, p, a):
        super().__init__(na, dir, imd, ur, dur, actors, reda, lang,time)
        self.type = "Film"
        self.genre = g  # Genre of the film (e.g., action, comedy, drama)
        self.box_office = b  # Box office earnings of the film
        self.production_company = p  # The main production company of the film
        self.awards = a  # []  # List of awards won by the film

    def add(self):
        na = input("please give me the name of the Film: ")
        dir = input("please give me the name of director of the Film: ")
        imd = input("please give me the IMDB score of the Film: ")
        ur = input("please give me the url of the Film: ")
        dur = input("please give me the duration of the Film: ")
        while True:
            cas = input(
                "please give me the name , age , nationality and height of the casts: //insert 0 to break! ")
            if cas == 0:
                break
            else:
                result = cas.strip().split(",")
                x = Actor(result[0], result[1], result[2], result[3])
            actors.append(x)
        reda = input("please give me the release date of the Film: ")
        lang = input("please give me the language of the Film: ")
        time = input("please give me the time(minute) of the Film: e.p. 120")
        g = input("please give me the genre of the Film: ")
        b = input("please give me the box office of the Film: ")
        p = input("please give me the production company of the Film: ")
        while True:
            a = input(
                "please give me the name of awards of the Film: // insert 0 to quit!")
            if a == 0:
                break
            awards.append(a)
        self(na, dir, imd, ur, dur, actors, reda, lang,time, g, b, p, awards)
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
        print("9- language")
        print("10- genre")
        print("11- box office")
        print("12- production company")
        print("13- awards")
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
                        obj[0] = result[0]
                        obj[1] = result[1]
                        obj[2] = result[2]
                        obj[3] = result[3]
                        break
                else:
                    print("there is no such an actor!")

            elif flag == 2:
                self.showinfo(self.casts)
                cas = input(
                    "please give me the name of actor you want to remove:"+"\n")
                for obj in self.casts:
                    i = 0
                    if cas == obj.name:
                        del self.casts[i]
                        break
                    else:
                        i += 1
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
            new_topic = input("what's the new genre?"+"\n")
            self.genre = new_topic
            print("👍")
            return
        elif flag == 11:
            new_source = input("what's the new box office?"+"\n")
            self.box_office = new_source
            print("👍")
            return
        elif flag == 12:
            new_source = input("what's the new production company?"+"\n")
            self.production_company = new_source
            print("👍")
            return
        elif flag == 13:
            print("Do you wanna change an award or remove?")
            print("1- change")
            print("2- remove")
            flag = int(input(""))
            if flag == 1:
                for a in self.awards:
                    print(a)
                cgn_name = input("write the wrong name compeletly:"+"\n")
                for name in self.awards:
                    if name == cgn_name:
                        new_name = input("what's its new name?"+"\n")
                        name = new_name
                        print("change succesfully")
                        break
                else:
                    print("there is no such a name in awards!")
                return
            elif flag == 2:
                for a in self.awards:
                    print(a)
                cgn_name = input("write the name compeletly:"+"\n")
                j = 0
                for name in self.awards:
                    if name == cgn_name:
                        del self.awards[j]
                        print("delete succesfully")
                        break
                    else:
                        j += 1
                else:
                    print("there is no such a name in awards!")
            else:
                print("your input is not correct!!")
            return
        else:
            print("your input is not correct!!")
        return
