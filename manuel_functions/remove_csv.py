import os
from _socket import gethostname, gethostbyname
from datetime import datetime


def remove_csv(folder: str) -> None:
    for filename in os.listdir(folder):
        current_time = datetime.now().strftime("%H-%M-%S")
        file_path = os.path.join(folder, filename)
        if file_path.endswith(".csv") and current_time not in file_path:
            os.unlink(file_path)


if __name__ == "__main__":
    remove_csv("../")
