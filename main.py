from args import get_args
from filter import extract_exif_data_from_dir

def main():
    args = get_args()
    if args.debug:
        print("Got arguments "+args.input_path+", "+args.collection_id+", "+args.output_path)

    extract_exif_data_from_dir(args.input_path, args.collection_id, args.output_path)


if __name__ == '__main__':

    main()
