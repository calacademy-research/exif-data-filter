import argparse

def get_parser():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i",
                        "--input_path",
                        metavar="",
                        required=True,
                        type=str,
                        help="relative path to input directory")

    parser.add_argument("-o",
                        "--output_path",
                        metavar="",
                        default=".",
                        type=str,
                        help="relative path to output directory where csv_file will be generated or replaced.")

    parser.add_argument("-c",
                        "--collection_id",
                        metavar="",
                        required=True,
                        type=str,
                        help="collection_id to label all photos with.")

    parser.add_argument("-d",
                        "--debug",
                        metavar="",
                        choices=[True, False],
                        default=False,
                        type=bool,
                        help="argument describing whether it should print debugging and progress messages. Has deafult value of False.")
    return parser


def get_args():
    parser = get_parser()
    args = parser.parse_args()

    return args
