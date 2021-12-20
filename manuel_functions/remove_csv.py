import os


def remove_csv(folder: str) -> None:
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if file_path.endswith(".csv"):
            os.unlink(file_path)


if __name__ == "__main__":
    remove_csv("../")
