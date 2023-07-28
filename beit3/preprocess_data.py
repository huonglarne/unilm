from datasets import ImageNetDataset

ImageNetDataset.make_dataset_index(
    train_data_path = "/nas/common_data/imagenet_100cls/train",
    val_data_path = "/nas/common_data/imagenet_100cls/val",
    index_path = "/nas/common_data/imagenet_100cls/"
)