#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import LineString
from tqdm import tqdm
import os
import argparse
import sys


def parse_gmt_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    coordinates = []
    segment = []

    for line in lines:
        if line.strip() == '>':  # Start of a new segment
            if segment:
                coordinates.append(segment)
                segment = []
        else:
            lon, lat = map(float, line.split())
            segment.append((lon, lat))

    if segment:  # Add the last segment if exists
        coordinates.append(segment)

    return coordinates

def convert_to_shp(input_gmt, output_shp_base, crs, verbose=False):
    if verbose:
        print(f"Converting {input_gmt} to Shapefile with CRS {crs}")
    
    coordinates = parse_gmt_file(input_gmt)

    gdf_list = []
    for segment in tqdm(coordinates, desc="Processing segments"):
        line = LineString(segment)
        gdf_list.append(gpd.GeoDataFrame({'geometry': [line]}))

    gdf = pd.concat(gdf_list, ignore_index=True)
    try:
        gdf.crs = crs
    except ValueError as e:
        sys.exit(f"Error: Invalid CRS provided. {e}")

    output_shapefile_path = output_shp_base + '.shp'
    gdf.to_file(output_shapefile_path)

    if verbose:
        print(f"Shapefile saved to {output_shapefile_path}")

    shapefile_extensions = ['.shp', '.shx', '.dbf', '.prj', '.cpg']
    shapefile_paths = [output_shp_base + ext for ext in shapefile_extensions]
    existing_files = [f for f in shapefile_paths if os.path.exists(f)]
    print(f"Shapefiles created: {existing_files}")

def main():
    parser = argparse.ArgumentParser(description='Convert GMT format to Shapefile.')
    parser.add_argument('input_gmt', help='Input GMT file path')
    parser.add_argument('output_shp_base', help='Base name for output Shapefile')
    parser.add_argument('--crs', default='EPSG:4326', help='Coordinate Reference System (default: EPSG:4326)')
    parser.add_argument('--verbose', action='store_true', help='Increase output verbosity')

    args = parser.parse_args()

    convert_to_shp(args.input_gmt, args.output_shp_base, args.crs, args.verbose)

if __name__ == '__main__':
    main()
