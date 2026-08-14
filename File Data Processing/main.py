from ucimlrepo import fetch_ucirepo

# Fetching the dataset (ID-53 for Iris)
iris_info = fetch_ucirepo(id=53)

# Separating data into features (X) and targets (y)
X = iris_info.data.features
y = iris_info.data.targets


#  Metadata and Variable Information 

print("--- METADATA ---")
print(iris_info.metadata)

print("\n--- VARIABLE INFO ---")
print(iris_info.variables)


# Calculating the required info 
total_records = len(y)
unique_flowers_list = y['class'].unique()
different_flowers_numbers = len(unique_flowers_list)

print("\n--- DATA PROCESSING RESULTS ---")
print(f"Total number of records: {total_records}")
print(f"Total number of different flowers: {different_flowers_numbers}")
print(f"Names of all different flowers: {list(unique_flowers_list)}")