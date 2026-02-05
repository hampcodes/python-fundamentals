people = {
    "Person1": {"name": "Henry", "age": 29, "city": "Lima, Peru"},
    "Person2": {"name": "Brenda", "age": 26, "city": "Trujillo, Peru"},
    "Person3": {"name": "Estela", "age": 50, "city": "Arequipa, Peru"}
}


print("=== People Information ===")

for person_id, person_info in people.items():
    print(f"\n{person_id}:")

    for field, data in person_info.items():
        print(f"  {field}: {data}")
