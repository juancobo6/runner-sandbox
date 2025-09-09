"""Main runner file."""

import datetime

import pandas as pd

if __name__ == "__main__":
    sample_data = {
        "name": ["John", "Jane", "Jim", "Jill"],
        "age": [25, 30, 35, 40],
        "city": ["New York", "Los Angeles", "Chicago", "Houston"],
    }
    sample_df = pd.DataFrame(sample_data)
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    sample_df.to_csv(
        f"C:/Users/JuanCobo/Documents/runner-sandbox/data/sample_data_{timestamp}.csv",
        index=False,
    )
