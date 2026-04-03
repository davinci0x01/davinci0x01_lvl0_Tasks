import shutil

mode = input("zip/unzip: ").lower()

if mode == "zip":
    folder = input("Folder path: ")
    out = input("Output zip name (without .zip): ")
    shutil.make_archive(out, "zip", folder)
    print("Zipped")

else:
    zipf = input("Zip file path (.zip): ")
    out = input("Extract to folder: ")
    shutil.unpack_archive(zipf, out)
    print("Unzipped")