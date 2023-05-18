class Movie(object):
    def __init__(self, title, genre, runtime, lead):
        self.title=title
        self.genre=genre
        self.runtime=runtime
        self.lead=lead
    
    def showMovie(self):
        print(f"Title: {self.title}\nGenre: {self.genre}\nRuntime: {self.runtime}\nLead: {self.lead}")
    
movie_list=[]

while True:
    title=input("Enter movie title: ")
    runtime=int(input("Enter movie runtime: "))
    genre=input("Enter movie genre: ")
    lead=input("Enter movie lead: ")
    obj=Movie(title, genre, runtime, lead)
    movie_list.append(obj)
    print("Movie added")
    ans=input("Do yo wish to continue? y/n]: ").lower()
    if ans!='y':
        break

print("All movies in the list: ")
for obj in movie_list:
    obj.showMovie()