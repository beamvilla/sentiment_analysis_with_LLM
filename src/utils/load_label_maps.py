from typing import Mapping
import yaml


def load_label_maps(label_maps_path: str) -> Mapping[str, int]:
    with open(label_maps_path, "r") as file:
        label_maps = yaml.safe_load(file)
        return label_maps