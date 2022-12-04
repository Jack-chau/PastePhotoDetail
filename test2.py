from path import Sorting

path = "./Photo/"

path = Sorting ( path ).sortByName()

for key, value in path.items() :
    print ( key )
    print ( value )