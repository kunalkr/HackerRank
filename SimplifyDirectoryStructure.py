def simplify(path_str):
  dir_stack = []

  dir_list = path_str.split('/')

  for dir_string in dir_list:
    if dir_string in ['.', '']:
      continue
    elif dir_string == "..":
      if dir_stack:
        dir_stack.pop()
    else:
      dir_stack.append(dir_string)

  res_path = '/' + '/'.join(dir_stack)
  return res_path


# absolute path which we have to simplify. 
path_str_list = ["/a/./b/../../c", "/../../../../../a", "/home/", "/a/..", "/a/../", "/a/./b/./c/./d/", "/a/../.././../../.", "/a//b//c//////d"]
for path_str in path_str_list:
  res = simplify(path_str)
  print(res) 
