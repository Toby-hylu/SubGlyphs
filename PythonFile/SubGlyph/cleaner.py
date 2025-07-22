import os

"""
Provide functions: 
# --------------------------------------#------------------------------------- #
clean_tmp_files                         # clean the files in the set below
# --------------------------------------#------------------------------------- #
"""
# --------------------------------------#------------------------------------- #
extensions_to_remove = {
  '.log', '.aux', '.out', '.gz', '.synctex(busy)'
}
# --------------------------------------#------------------------------------- #
# --------------------------------------#------------------------------------- #
def clean_tmp_files(                    # clean temporary files in tmp/
  base_dir  : str='./'                , # base directory
  extra_set : list=None               , # other file extensions to be removed
):
  tmp_path = os.path.join(base_dir, "tmp")
  if not os.path.isdir(tmp_path): 
    print(f'Invalid path {tmp_path}')
    return
  for filename in os.listdir(tmp_path): 
    file_path = os.path.join(tmp_path, filename)
    # print(f"checking file {filename}")
    if os.path.isfile(file_path): 
      file_ext = os.path.splitext(filename)[1].lower()
      # print(f"extension name is {file_ext}")
      if file_ext in extensions_to_remove: 
        try: 
          os.remove(file_path)
        except OSError as e: 
          print('Unable to remove file {filename}')
      if extra_set is not None: 
        if file_ext in extra_set: 
          try: 
            os.remove(file_path)
          except OSError as e: 
            print('Unable to remove file {filename}')
# --------------------------------------#------------------------------------- # 