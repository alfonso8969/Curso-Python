import file1


print(f"File1__name__ = {file1.__name__}")
print("File2__name__ = %s" % __name__)

if __name__ == "__main__":
    print("File2__name__ = %s" % __name__)
else:
    print("File2 is being imported")
