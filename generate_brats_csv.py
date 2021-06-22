import os
import argparse
from tqdm import tqdm


def main():
    print("Parsing Arguments...")

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-input_dir",
        type=str,
        help="Input data directory which contains images in specified format",
        required=True,
    )

    parser.add_argument(
        "-output_csv",
        type=str,
        help="Output csv file name",
        required=True,
    )

    args = parser.parse_args()

    base_dir = os.path.abspath(args.input_dir)
    output_csv = os.path.abspath(args.output_csv)

    print("Finding all patients...")

    patients = os.listdir(base_dir)

    print("Writing to CSV...")
    f = open(output_csv, "w+")
    f.write("SubjectID,Channel_0,Channel_1,Channel_2,Channel_3,Label\n")

    for patient in tqdm(patients):
        t1_path = os.path.join(base_dir, patient, patient + "_t1.nii.gz")
        t2_path = os.path.join(base_dir, patient, patient + "_t2.nii.gz")
        t1ce_path = os.path.join(base_dir, patient, patient + "_t1ce.nii.gz")
        flair_path = os.path.join(base_dir, patient, patient + "_flair.nii.gz")
        mask_path = os.path.join(base_dir, patient, patient + "_wt.nii.gz")
        f.write(
            patient
            + ","
            + t1_path
            + ","
            + t2_path
            + ","
            + t1ce_path
            + ","
            + flair_path
            + ","
            + mask_path
            + "\n"
        )

    f.close()

    print("Finished.")


if __name__ == "__main__":
    main()
