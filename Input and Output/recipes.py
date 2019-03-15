# updating data stored in a shelve
import shelve

# blt = ["bacon", "lettuce", "tomatoe", "bread"]
# beans_on_toast = ["beans", "Bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
# soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

with shelve.open('recipes') as recipes:

    #   Already written to the database

    # recipes["blt"] = blt
    # recipes["beans on toast"] = beans_on_toast
    # recipes["scrambled eggs"] = scrambled_eggs
    # recipes["pasta"] = pasta
    # recipes["soup"] = soup

    temp_list = recipes["blt"]
    temp_list.append("butter")
    recipes["blt"] = temp_list

    temp_list = recipes["pasta"]
    temp_list.append("tomato")
    recipes["pasta"] = temp_list

    for snack in recipes:
        print(snack, recipes[snack])

# using writeback method
# using the sync() method

# when it will be appropriate to use it before getting into the challenge now that we've mentioned that the keys must
# be strings but the values can be just about any Python objects and can be really literally just as complex as you need
# so dictionaries containing lists for example can be use as values in the shelves the value are pickled before being
# stored in the underlying data base fields so the same for pickle applies to shelve values because of that now this
# makes shelves really convenient and simple way to store programs data unless you have persistent storage yet continue
# to use the usual Python syntax without having to learn SQL which is Structured Query Language a way to access data
# bases so you don't really need to use the use that SQL to interrogate database here rather use the usual Python syntax
#  in the last few video however with that said the shelve module does have some drawbacks and I mean it's not suitable
# for some applications so as a few examples for example because values are pickled before being stored and are
# unpickled by the value when it went back if your values are really complex this pickling and unpickling may impose
# significant overhead and affect performance so in other words slow down your application and the we mentioned that
# different systems may use different underlying database technology for storing the shelve so that data is platform
# agnostic so if an application is likely to be moved to a new system and must take its data starting with it then
# shelves aren't probably the best solution because they may or may not work properly or at  all in that environment or
# system and of course this also leads to another  potential issue and that's data from untrusted sources so deploying
# an  application that uses shelves for essentially Data necessary for the program to run as such as the location of the
#  maps from our adventure game would be deploying the shelve files  with the program as well as the previous issue that
#  the shelves may not be usable in some systems if the application is deployed over the internet and of course is that
# real possibility that the files can be tampered with and that would ultimately expose potentially user's to security
# threats also concurrent access can also be a problem with shelves although concurrent read accesses are safe if a
# program is writing to the shelve and no other programs should have it open or attempt to open it so the bottom line
# here is although shelves are very useful in the right place it may be preferable to store data in a database rather
# than using shelves now we are gonna be covering data bases later in the course and you'll be able to choose which
# persistent mechanism that best suit your needs after seeing how database work.
