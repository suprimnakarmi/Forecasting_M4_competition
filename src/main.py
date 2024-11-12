from data_loader import read_csv
from torch.utils.data import DataLoader
from torch.utils.data import Dataset 

def main():
    file_path = "../M4-methods-master/Dataset/Train/Daily-train.csv"
    df = read_csv(file_path)
    print(df.head(5))


if __name__ == "__main__":
    main()