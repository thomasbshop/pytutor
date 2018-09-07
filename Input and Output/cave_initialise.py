import shelve
# import copy

# locations_dict = {
#     "zero": {"desc": "You are sitting in-front of a computer learning python",
#              "exits": {},
#              "namedExits": {}},
#     "one": {"desc": "You are standing at the end of the road before a small brick building.",
#             "exits": {"W": 2,  "E": 3, "N": 5, "S": 4, "Q": 0},
#             "namedExits": {"2": 2, "3": 3, "5": 5, "4": 4}},
#     "two": {"desc": "You are at the top of a hill",
#             "exits": {"N": 5, "Q": 0},
#             "namedExits": {"5": 5}},
#     "three": {"desc": "You are inside a building, a well house for a small stream",
#               "exits": {"W": 1, "Q": 0},
#               "namedExits": {"1": 1}},
#     "four": {"desc": "You are in the valley beside a stream.",
#              "exits": {"N": 1, "W": 2, "Q": 0},
#              "namedExits": {"1": 1, "2": 2}},
#     "five": {"desc": "You are in the forest",
#              "exits": {"W": 2, "S": 1, "Q": 0},
#              "namedExits": {"2": 2, "1": 1}}
# }


locations = shelve.open("LocationsData")

locations["0"] = {"desc": "You are sitting in-front of a computer learning python",
                  "exits": {}, "namedExits": {}
                  }
locations["1"] = {"desc": "You are standing at the end of the road before a small brick building.",
                  "exits": {"W": "2",  "E": "3", "N": "5", "S": "4", "Q": "0"}, "namedExits": {"2": "2", "3": "3", "5": "5", "4": "4"}
                  }
locations["2"] = {"desc": "You are at the top of a hill",
                  "exits": {"N": "5", "Q": "0"}, "namedExits": {"5": "5"}
                  }
locations["3"] = {"desc": "You are inside a building, a well house for a small stream",
                  "exits": {"W": "1", "Q": "0"}, "namedExits": {"1": "1"}}
locations["4"] = {"desc": "You are in the valley beside a stream.",
                  "exits": {"N": "1", "W": "2", "Q": "0"}, "namedExits": {"1": "1", "2": "2"}
                  }
locations["5"] = {"desc": "You are in the forest",
                  "exits": {"W": "2", "S": "1", "Q": "0"}, "namedExits": {"2": "2", "1": "1"}
                  }

# locations['locationsDict'] = copy.deepcopy(locations_dict)
locations.close()


vocabulary = shelve.open("VocabularyData")

# vocabulary["QUIT"] = "Q"
# vocabulary["NORTH"] = "N"
# vocabulary["EAST"] = "E"
# vocabulary["WEST"] = "W"
# vocabulary["SOUTH"] = "S"
# vocabulary["ROAD"] = "1"
# vocabulary["HILL"] = "2"
# vocabulary["BUILDING"] = "3"
# vocabulary["VALLEY"] = "4"
# vocabulary["FOREST"] = "5"

vocabulary['vocabularyDict'] = {"QUIT": "Q",
                                "NORTH": "N",
                                "EAST": "E",
                                "WEST": "W",
                                "SOUTH": "S",
                                "ROAD": "1",
                                "HILL": "2",
                                "BUILDING": "3",
                                "VALLEY": "4",
                                "FOREST": "5"}
# vocabulary['vocabularyDict'] = copy.deepcopy(vocabulary_dict)
vocabulary.close()
