#!/usr/bin/env python3

from importlib.metadata import version, PackageNotFoundError


def get_req_packages(file: str) -> list:
    req = []
    line = 1
    with open(file) as f:
        for line in f:
            req.append(line.strip())
    return req


def check_dependencies(req: list) -> int:
    valid_state = 1
    print("\nChecking dependencies:")
    for package_name in req:
        try:
            print(f"✔ Found {package_name} ({version(package_name)})")
        except PackageNotFoundError:
            valid_state = 0
            print(f"🗙 Package not found: {package_name}. "
                  f"Install with 'pip install {package_name}'")
    return valid_state


def analyze_data() -> None:
    import pandas
    import numpy
    import matplotlib.pyplot as plt

    output_path = "matrix_analysis.png"
    n = 100

    print("\nAnalyzing Matrix data...")
    print(f"Processing {n} data points...")

    data_points = numpy.random.rand(n)
    dates = pandas.date_range("1999-10-01", periods=n, freq="W")
    data_frame = pandas.DataFrame({"Dates": dates, "Data points": data_points})

    print("Generating visualization...")

    plt.figure(figsize=(12, 5))
    plt.plot(
        data_frame["Dates"],
        data_frame["Data points"],
        label="Daily data",
        color="red",
        linestyle="--")
    plt.xlabel("Data")
    plt.ylabel("Value")
    plt.title("Matrix Analysis")
    plt.savefig(output_path)

    return output_path


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...")

    req = get_req_packages("requirements.txt")

    if check_dependencies(req):
        output_path = analyze_data()
        print("\nAnalysis complete!")
        print(f"Results saved to: {output_path}")
