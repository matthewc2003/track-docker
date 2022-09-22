"""
This script should be placed in the root of a WoWS installation.
It will generate and populate res_extract.

Make sure you have the unpacker:
https://forum.worldofwarships.eu/topic/113847-all-wows-unpack-tool-unpack-game-client-resources/
"""

import argparse
import os
import shutil
import subprocess

OUTPUT_NAME = "res_extract"
UNPACK_LIST = (
    "content/GameParams.data",
    "gui/ship_silhouettes/*",
)


def main(bin_num):
    bin_path = rf"bin\{bin_num}"
    idx_path = rf"{bin_path}\idx"
    pkg_path = r"..\..\..\res_packages"
    include = []
    for pattern in UNPACK_LIST:
        include.append("-I")
        include.append(pattern)

    subprocess.run(
        ["wowsunpack.exe", "-x", idx_path, "-p", pkg_path, "-o", OUTPUT_NAME, *include]
    )

    texts_src = rf"{bin_path}\res\texts"
    texts_dest = rf"{OUTPUT_NAME}\texts"
    shutil.copytree(texts_src, texts_dest)

    print("Extraction complete.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extracts game resources.")
    parser.add_argument(
        "--bin", default=max(os.listdir("bin/")), help="The game version to use."
    )
    args = parser.parse_args()

    main(args.bin)
