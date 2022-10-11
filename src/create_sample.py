import argparse
import pandas as pd

def create_sample(file):
    df = pd.read_csv(file)
    samples = df[['structureNumber',
                  'yearBuilt',
                  'age',
                  'adtCategory',
                  'material',
                  'lengthOfMaximumSpan',
                  'structureLength',
                  'operatingRating',
                  'deckNumberIntervention',
                  'supNumberIntervention',
                  'subNumberIntervention',
                ]]
    return samples

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inputfile', help='input filename')
    parser.add_argument('-o', '--outputfile', help='outputfile filename')

    args = parser.parse_args()
    path = args.inputfile
    output_file = args.outputfile
    samples = create_sample(path)
    samples.to_csv(output_file, index=False)

if __name__ == '__main__':
    main()
