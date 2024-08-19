from lib.data_utils import download_mit_ecg_dataset, download_man_ahl_dataset

def download_sigWGAN_datasets():
    download_mit_ecg_dataset()
    download_man_ahl_dataset()


if __name__ == "__main__":
    download_sigWGAN_datasets()