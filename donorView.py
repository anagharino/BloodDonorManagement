from mysql import connector
from datetime import datetime


class BloodDonorManager:

    def __init__(self):
        self.connection = connector.connect(
            user="root",
            host="localhost",
            password="Anagha1710@",
            database="blood_db_aug26"
        )
        print("Connected Successfully....!")

    # Get one record using ID
    def get_object(self, id=None):
        try:
            self.cursor = self.connection.cursor()

            query = "SELECT * FROM donor WHERE id = %s"
            values = (id,)

            self.cursor.execute(query, values)

            record = self.cursor.fetchone()

            return record

        except Exception as e:
            print(e)

    # Insert new donor
    def post(self, **kwargs):
        try:
            self.cursor = self.connection.cursor()

            query = """
            INSERT INTO donor
            (name, blood_group, phone, city, last_donation)
            VALUES (%s, %s, %s, %s, %s)
            """

            values = [v for v in kwargs.values()]

            self.cursor.execute(query, values)
            self.connection.commit()

            print("Data inserted Successfully....!")

        except Exception as e:
            print(e)

    # View all records
    def get(self):
    
            self.cursor = self.connection.cursor()

            query = "SELECT * FROM donor"

            self.cursor.execute(query)

            records = self.cursor.fetchall()
            return records

       

    # Get one donor by ID and display it
    def retrieve(self, id=None):
        try:
            record = self.get_object(id=id)

            if record is None:
                print("No donor found")
            else:
                print(record)

        except Exception as e:
            print(e)

    # Update donor
    def put(self, id=None, **kwargs):
        try:
            record = self.get_object(id=id)

            if record != None:

                self.cursor = self.connection.cursor()

                placeholder = ""

                for k in kwargs.keys():
                    placeholder += k + "=%s, "
                placeholder = placeholder.rstrip(", ")

                query = f"UPDATE donor SET {placeholder} WHERE id=%s"

                values = [v for v in kwargs.values()]
                values.append(id)

                self.cursor.execute(query, values)

                self.connection.commit()

                return True,"Donor updated Sucessfully...!"

            else:
                return False,"No donors found"

        except Exception as e:
            print(e)

    # Delete donor
    def delete(self, id=None):
        try:
            record = self.get_object(id=id)

            if record is not None:

                query = "DELETE FROM donor WHERE id=%s"

                self.cursor.execute(query, (id,))

                self.connection.commit()

                print("Donor deleted successfully....!")

            else:
                print("No donor found")

        except Exception as e:
            print(e)


donor_instance = BloodDonorManager()
#donor_instance.post(name = "Rahul",blood_group ="b+",phone="7654567000",city = "kochi",last_donation = datetime.today())
donor_instance.get()
#donor_instance.retrieve(id=1)
#donor_instance.delete(id=4)
#donor_instance.put(id = 2,name = "Anagha",blood_group ="b+",phone="7654567800",city = "kochi",last_donation = datetime.today())
#self.connection.close()




