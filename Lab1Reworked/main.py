from storage_manager import StorageManager
from user_storage import UserStoragePreference


def main():
    storage_manager = StorageManager()
    user_preferences = UserStoragePreference()

    user_id = "JustUserOfAmazon"

    user_preferences.set_user_storage(user_id, "s3")

    storage_type = user_preferences.get_user_storage(user_id)
    storage = storage_manager.get_storage(storage_type)

    if storage:
        storage.connect()

        files = storage.list_files()
        print(f"📁 Файлы в хранилище: {files}")

        storage.upload_file("my_document.txt")

        storage.download_file("cloud_doc.txt", "/downloads/")


if __name__ == "__main__":
    main()