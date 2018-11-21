# from player import Player  # syntax not recommended
#
# thomas = Player("Thomas")
#
# print(thomas.name)
# print(thomas.lives)
#
# # print(thomas.get_name())
# # thomas.set_live(200)
#
# thomas.lives -= 1
# print(thomas)
#
# thomas.lives -= 1
# print(thomas)
#
# thomas._lives = 9  # still works even if you hide
# print(thomas)
#
# thomas.level = 8
# print(thomas)
#
# thomas.level = 6
# print(thomas)
#
# print(thomas)
# thomas.level = 12
# print(thomas)
#
# from enemy import Enemy, Troll, Vampire, VampireKing
#
# # random_monster = Enemy("Basic Enemy", 12, 1)
# # print(random_monster)
# #
# # random_monster.take_damage(4)
# # print(random_monster)
# #
# # random_monster.take_damage(8)
# # print(random_monster)
# #
# # random_monster.take_damage(9)
# # print(random_monster)
# #
# # ugly_troll = Troll("Pugh")
# # print(ugly_troll)
# #
# # another_troll = Troll("Ug")
# # print(another_troll)
# #
# # brother_troll = Troll("Urgh")
# # print(brother_troll)
# #
# # ugly_troll.grunt()
# # brother_troll.grunt()
# # another_troll.grunt()
# #
# # a_vampire = Vampire("Voldamot")
# # another_vampire = Vampire("Dracula")
# #
# # another_vampire.take_damage(2)
# # print(another_vampire)
# #
# # while another_vampire._alive:
# #     another_vampire.take_damage(1)
# #     print(another_vampire)
#
# print("********* Vampire King ************")
# the_king = VampireKing("The King")
# print(the_king)
#
# while the_king._alive:
#     the_king.take_damage(3)
#     print(the_king)


a = 9
b = "lkj"
c = 1, 2, 3  # tuple
print(type(c))
encoder = [None] * 26
print(encoder)
