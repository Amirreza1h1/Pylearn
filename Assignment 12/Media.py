import pytube

class Media:
    def __init__(self,n,dir,imdb,ur,dur,cas,reda,lang,t):
        self.name = n
        self.director = dir
        self.IMDBscore = imdb
        self.url = ur
        self.duration = dur
        self.casts = cas
        self.release_date = reda  # Release date of the media
        self.language = lang  # Language of the media
        self.time=t # Time of the Media

    @staticmethod
    def showinfo(c):
        for obj in c:
            print(type(obj).__name__)
            properties = ", ".join([f"{key}: {value}" for key, value in vars(obj).items()])
            print(properties)
            print()
    
    @staticmethod
    def download(u):
        first_stream=pytube.Youtube(u).streams.first()
        first_stream.download(output_path='./',filename='file.mp4')
    
    @staticmethod
    def show_menu(self):
        print("1- Add")
        print("2- Edit")
        print("3- remove")
        print("4- Search")
        print("5- Show List")
        print("6- download")
        print("7- Exit")
