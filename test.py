from git import Repo
import os
import tarfile

repo = Repo(".")
file="tmp.tar"
with open(file, "w") as tar: repo.archive(tar, prefix=".tags/c001/", path=".generated/") 
                                           def is_within_directory(directory, target):
                                               
                                               abs_directory = os.path.abspath(directory)
                                               abs_target = os.path.abspath(target)
                                           
                                               prefix = os.path.commonprefix([abs_directory, abs_target])
                                               
                                               return prefix == abs_directory
                                           
                                           def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
                                           
                                               for member in tar.getmembers():
                                                   member_path = os.path.join(path, member.name)
                                                   if not is_within_directory(path, member_path):
                                                       raise Exception("Attempted Path Traversal in Tar File")
                                           
                                               tar.extractall(path, members, numeric_owner=numeric_owner) 
                                               
                                           
                                           safe_extract(tar)
os.remove(file)

