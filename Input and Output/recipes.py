# updating data stored in a shelve
import shelve

# blt = ["bacon", "lettuce", "tomatoe", "bread"]
# beans_on_toast = ["beans", "Bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
# soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

with shelve.open('recipes') as recipes:
    #    Already written to the database

    # recipes["blt"] = blt
    # recipes["beans on toast"] = beans_on_toast
    # recipes["scrambled eggs"] = scrambled_eggs
    # recipes["pasta"] = pasta
    # recipes["soup"] = soup

    for snack in recipes:
        print(snack, recipes[snack])
