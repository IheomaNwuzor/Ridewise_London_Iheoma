import pandas as pd


def load_data(input_path):
    data = pd.read_csv(input_path)
    return data


def clean_data(data):
    data = data.copy()

    # Put the same preprocessing steps from your notebook here
    data.columns = data.columns.str.strip().str.lower().str.replace(" ", "_")
    data = data.drop_duplicates()

    return data


def save_data(data, output_path):
    data.to_csv(output_path, index=False)


def main():
    input_path = "data/raw/sessions.csv"
    output_path = "data/processed/preprocessed_sessions.csv"

    data = load_data(input_path)
    data = clean_data(data)
    save_data(data, output_path)

    print("Preprocessing complete")


if __name__ == "__main__":
    main()



    