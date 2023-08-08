import os


def get_list():
  list_imges = []

  curent_dir = os.getcwd()
  img_file_dir = curent_dir + "/static/all_imgs"

  folders = os.listdir(img_file_dir)

  for folder in range(len(folders)):
    files = os.listdir(img_file_dir + "/" + folders[folder])
    for file in files:
      path = "static/all_imgs/" + folders[folder] + "/" + file
      list_imges.append(path)

  return list_imges


#for x in get_list(): print(x)

get_list()
