import os
import argparse

class Searcher:

    def __init__(self):
        self.found_files = []

    def search(self , path , target):

        files = os.listdir(path)

        for current_file in files:
            current_path = os.path.join(path , current_file)
            print("[=]Searching {}".format(current_path))

            if current_file == target:
                print("[*]{} found.".format(target))
                self.found_files.append(current_path)


            if os.path.isdir(current_path):
                self.search(current_path , target)

        return self.found_files







def main():


    parser = argparse.ArgumentParser()
    parser.add_argument("-p" , dest = "path" , required = True , type = str , help = "The path to start the search")
    parser.add_argument("-t" , dest = "target" , required = True , type = str , help = "The target that needs to be found")
    args = parser.parse_args()


    searcher = Searcher()
    found_paths = searcher.search(path = args.path  , target = args.target)

    print("Found paths")

    for path in found_paths:
        print(path)


if __name__ == "__main__":
    main()



