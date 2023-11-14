import argparse
import os


def simple_progress_bar(iterable_func):
    total = len(iterable_func)
    bar_length = 30
    result = ""
    for i, item in enumerate(iterable_func):
        progress = (i + 1) / total
        block = int(round(bar_length * progress))
        progress_bar = "#" * block + "-" * (bar_length - block)
        print(f"\r[{progress_bar}] {int(progress * 100)}%", end="")
        if "ATOM" in item.split()[0] or "TER" in item.split()[0] or "HETATM" in item.split()[0]:
            result += item

    print()  # Move to the next line after the progress bar
    return result


def reconstruct_pdb(het_atm, prot):
    combined = het_atm + prot
    return simple_progress_bar(combined)


def extract_models(data):
    second_model = False
    model_1 = []
    model_2 = []
    for datum in data:

        if "MODEL" in datum.strip():
                if "2" in datum.strip():
                    second_model = True
        else:
            if second_model:
                model_2.append(datum)
            else:
                model_1.append(datum)
    return model_1, model_2


def main(args):
    print("Reading pdb file at {}".format(args.file_path))
    with open(args.file_path, "r") as f:
        data = f.readlines()
    model_1, model_2 = extract_models(data)


    # Path validation
    # Check if the output path is a full path or just a file name
    if os.path.isabs(args.output_path):
        output_path = args.output_path
    else:
        # If it's just a file name, prepend the current working directory
        output_path = os.path.join(os.getcwd(), args.output_path)
    with open(output_path, "w") as f:
        f.write(reconstruct_pdb(model_1,model_2))
    print(f"Reconstructed pdb file is saved at {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", type=str, help="path to pdb file")
    parser.add_argument("--output_path", type=str, help="path to output pdb file.\
                        If just a file name, will save in current working directory"
                        , default="diffdocked.pdb", required=False)
    args = parser.parse_args()
    main(args)



