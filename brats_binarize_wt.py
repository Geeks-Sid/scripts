import os
import argparse
import nibabel as nib
from tqdm import tqdm
import numpy as np


def main():
    print("Parsing Arguments...")

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-input_dir",
        type=str,
        help="Input data directory which contains images in specified format",
        required=True,
    )

    args = parser.parse_args()

    base_dir = os.path.abspath(args.input_dir)

    print("Finding all patients...")

    patients = os.listdir(base_dir)

    print("Converting...")

    for patient in tqdm(patients):
        mask_path = os.path.join(base_dir, patient, patient + "_seg.nii.gz")
        to_save_path = os.path.join(base_dir, patient, patient + "_wt.nii.gz")
        mask_nib = nib.load(mask_path)
        mask_data = (mask_nib.get_fdata() > 0).astype(np.int8)
        to_save_nib = nib.Nifti1Image(mask_data, affine=mask_nib.affine)
        nib.save(to_save_nib, to_save_path)

    print("Finished.")


if __name__ == "__main__":
    main()
