from . import user_seeder as UserSeeder


class DatabaseSeeder:
    def run(self):
        UserSeeder.run()


if __name__ == "__main__":
    db = DatabaseSeeder()
    db.run()
