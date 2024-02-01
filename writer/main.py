import pymongo
import os

def main():

    # Connect to the MongoDB server running locally. You can customize the connection URL as needed.
    mongo_uri = os.environ.get("MONGO_URI")
    client = pymongo.MongoClient(mongo_uri)

    # Specify the name of the database and collection you want to use.
    db = client["test-database"]
    collection = db["test-collection"]

    # Define a mock document to insert into the collection.
    mock_entry = {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "age": 30
    }
    
    # Insert the mock entry into the collection.
    inserted_document = collection.insert_one(mock_entry)

    # Print the inserted document's ID.
    print(f"Inserted document ID: {inserted_document.inserted_id}")

    # Close the MongoDB connection.
    client.close()

if __name__ == "__main__":
    main()
