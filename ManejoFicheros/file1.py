import file2


print(f"File2__name__ = {file2.__name__}")

if __name__ == "__main__":
    print("File2__name__ = %s" % __name__)
else:
    print("File2 has been imported")
