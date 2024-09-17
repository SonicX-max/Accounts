class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    @property
    def user_id(self):
        return self._user_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def access_level(self):
        return self._access_level

    def __str__(self):
        return f"ID: {self._user_id}, Name: {self._name}, Access Level: {self._access_level}"

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'

    def add_user(self, users_list, name):
        new_id = max(user.user_id for user in users_list) + 1 if users_list else 1
        new_user = User(new_id, name)
        users_list.append(new_user)
        print(f"User '{name}' added.")

    def remove_user(self, users_list, user_id):
        for user in users_list:
            if user.user_id == user_id:
                users_list.remove(user)
                print(f"User with ID '{user_id}' removed.")
                return
        print(f"No user found with ID '{user_id}'.")

def main():
    users = []
    admin = Admin(0, "Admin")  # Создаем администратора

    while True:
        print("\nOptions:")
        print("1. Add User")
        print("2. Remove User")
        print("3. List Users")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the name of the user to add: ")
            admin.add_user(users, name)
        elif choice == '2':
            user_id = int(input("Enter the ID of the user to remove: "))
            admin.remove_user(users, user_id)
        elif choice == '3':
            if not users:
                print("No users available.")
            else:
                print("Current Users:")
                for user in users:
                    print(user)
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()