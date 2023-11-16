
# gmt2shp Tool

## Purpose
The `gmt2shp` tool is designed to convert geographical data from the GMT (Generic Mapping Tools) format to ESRI's Shapefile format. It provides a simple and efficient command-line interface for geospatial data conversion, supporting customization of the Coordinate Reference System (CRS).

## Description
This Python-based tool takes a GMT file as input and generates a corresponding Shapefile. It allows users to specify the output file's base name and the desired CRS. The tool is equipped with features like verbose output and a progress bar for enhanced user experience.

## Installation

### Prerequisites
- Python 3
- pip (Python package installer)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/okaragoz/gmt2shp.git
   ```
2. Navigate to the cloned directory:
   ```sh
   cd gmt2shp
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the tool from the command line:

```sh
gmt2shp <input_gmt_file> <output_shapefile_base> [--crs CRS] [--verbose]
```

- `<input_gmt_file>`: Path to the input GMT file.
- `<output_shapefile_base>`: Base name for the output Shapefile.
- `--crs CRS`: (Optional) Specify the Coordinate Reference System. Defaults to "EPSG:4326".
- `--verbose`: (Optional) Enable verbose output.

Example:

```sh
gmt2shp example.gmt example_output --crs "EPSG:4326" --verbose
```

## Dependencies
- geopandas
- shapely
- tqdm (for progress bar functionality)
- argparse (for command-line interface handling)

## Contributing
Contributions to the `gmt2shp` tool are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
