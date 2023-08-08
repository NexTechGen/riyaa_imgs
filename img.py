import os

list_imges = []

curent_dir = os.getcwd()

img_file_dir = curent_dir + "/all_imgs"

img_file_dir_list = os.listdir(img_file_dir)

for i in range(len(img_file_dir_list)):
  get_folder = img_file_dir + "/" + img_file_dir_list[i]
  listOf_get_folder = os.listdir(get_folder)
  for s in range(len(listOf_get_folder)):
    get_file = listOf_get_folder[s]
    imgs = get_folder + "/" + get_file
    list_imges.append(imgs)

print(list_imges)