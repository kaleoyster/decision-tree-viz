import pandas as pd

def create_sample(file):
    df = pd.read_csv(file)
    sample_1 = df['structureNumber']
    return sample_1

def main():
    path = 'nebraska_gravel.csv'
    samples = create_sample(path)
    samples.to_csv('samples.csv', index=False)

main()
