import random,os

#for local test purpose only. Comment b4 building
home_dir = '.\\randomdive\\icons\\'

#for executable purpose. Uncomment b4 building
# home_dir = resource_path('\\icons\\')

# def roll_stratagems(warbonds):
#     choose_count = 4
#     stratagems = []
#     stratagem_path = f'{home_dir}/stratagems'

#     for item in warbonds:
#         for root, dirs, files in os.walk(f'{stratagem_path}/{item}'):
#             for file in files:
#                 stratagems.append(os.path.join(root, file))

#     chosen_files = random.sample(stratagems, min(choose_count, len(stratagems)))
#     return chosen_files

# def roll_armor(warbonds):
#     num_files_to_choose = 1
#     armor = []
#     armor_path = f'{home_dir}/armor'

#     for item in warbonds:
#         for root, dirs, files in os.walk(f'{armor_path}/{item}'):
#             for file in files:
#                 armor.append(os.path.join(root, file))

#     chosen_files = random.sample(armor, min(num_files_to_choose, len(armor)))
#     return chosen_files

# def roll_passive(warbonds):
#     num_files_to_choose = 1
#     passive = []
#     passive_path = f'{home_dir}/passives'

#     for item in warbonds:
#         for root, dirs, files in os.walk(f'{passive_path}/{item}'):
#             for file in files:
#                 passive.append(os.path.join(root, file))

#     chosen_files = random.sample(passive, min(num_files_to_choose, len(passive)))

#     return chosen_files

# def roll_primary(warbonds):
#     num_files_to_choose = 1
#     weapons = []
#     weapon_path = f'{home_dir}/weapons'

#     for item in warbonds:
#         for root,dirs,files in os.walk(f'{weapon_path}/{item}/primary'):
#             for file in files:
#                 weapons.append(os.path.join(root, file))

#     chosen_primary = random.sample(weapons, min(num_files_to_choose, len(weapons)))

#     return chosen_primary

# def roll_secondary(warbonds):
#     num_files_to_choose = 1
#     weapon_path = f'{home_dir}/weapons'
#     weapons = []
    
#     for item in warbonds:
#         for root,dirs,files in os.walk(f'{weapon_path}/{item}/secondary'):
#             for file in files:
#                 weapons.append(os.path.join(root, file))

#     chosen_secondary = random.sample(weapons, min(num_files_to_choose, len(weapons)))

#     return chosen_secondary

# def roll_grenade(warbonds):
#     num_files_to_choose = 1
#     weapon_path = f'{home_dir}/weapons'
#     weapons = []

#     for item in warbonds:
#         for root,dirs,files in os.walk(f'{weapon_path}/{item}/grenade'):
#             for file in files:
#                 weapons.append(os.path.join(root, file))

#     chosen_grenade = random.sample(weapons, min(num_files_to_choose, len(weapons)))

#     return chosen_grenade

def roll_item(path,which_item,how_many,packs):

    #luck = random.randint(1,100)

    # for num in range(0,how_many-1):
    #     if luck != 100:
    #         chosen_items[num] = f'{home_dir}/luck.png'

    whole_path = f'{home_dir}\\{path}'
    all_items = []
    for item in packs:
        for root,dirs,files in os.walk(f'{whole_path}\\{which_item}\\{item}'):
            for file in files:
                all_items.append(os.path.join(root, file))

    chosen_items = random.sample(all_items, min(how_many, len(all_items)))

    return chosen_items
