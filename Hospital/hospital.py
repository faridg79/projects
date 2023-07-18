class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

    def __str__(self):
        return f"نام دکتر: {self.name}\nتخصص: {self.specialty}"


class Patient:
    def __init__(self, name, condition):
        self.name = name
        self.condition = condition

    def __str__(self):
        return f"نام بیمار: {self.name}\nوضعیت: {self.condition}"


class Room:
    def __init__(self, number):
        self.number = number
        self.patient = None

    def assign_patient(self, patient):
        if self.patient:
            print("اتاق قبلاً به یک بیمار اختصاص داده شده است.")
        else:
            self.patient = patient
            print(f"بیمار {patient.name} به اتاق شماره {self.number} منتقل شد.")

    def discharge_patient(self):
        if self.patient:
            discharged_patient = self.patient
            self.patient = None
            print(f"بیمار {discharged_patient.name} از اتاق شماره {self.number} ترخیص شد.")
        else:
            print("هیچ بیماری در این اتاق نیست.")

    def __str__(self):
        if self.patient:
            return f"اتاق شماره {self.number}: دارای بیمار {self.patient.name}"
        else:
            return f"اتاق شماره {self.number}: خالی"


class Hospital:
    def __init__(self):
        self.doctors = []
        self.patients = []
        self.rooms = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        print(f"دکتر {doctor.name} به بیمارستان اضافه شد.")

    def remove_doctor(self, doctor):
        if doctor in self.doctors:
            self.doctors.remove(doctor)
            print(f"دکتر {doctor.name} از بیمارستان حذف شد.")
        else:
            print("این دکتر در بیمارستان وجود ندارد.")

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"بیمار {patient.name} به بیمارستان اضافه شد.")

    def remove_patient(self, patient):
        if patient in self.patients:
            self.patients.remove(patient)
            print(f"بیمار {patient.name} از بیمارستان حذف شد.")
        else:
            print("این بیمار در بیمارستان وجود ندارد.")

    def add_room(self, room):
        self.rooms.append(room)
        print(f"اتاق شماره {room.number} به بیمارستان اضافه شد.")

    def remove_room(self, room):
        if room in self.rooms:
            self.rooms.remove(room)
            print(f"اتاق شماره {room.number} از بیمارستان حذف شد.")
        else:
            print("این اتاق در بیمارستان وجود ندارد.")

    def get_num_doctors(self):
        return len(self.doctors)

    def get_num_patients(self):
        return len(self.patients)

    def get_num_rooms(self):
        return len(self.rooms)

    def get_doctors(self):
        print("لیست دکترها:")
        for doctor in self.doctors:
            print(doctor)
            print("-----------")

    def get_patients(self):
        print("لیست بیماران:")
        for patient in self.patients:
            print(patient)
            print("-----------")

    def get_rooms(self):
        print("لیست اتاق‌ها:")
        for room in self.rooms:
            print(room)
            print("-----------")


# مثال استفاده از کلاس‌ها و توابع آنها
hospital = Hospital()

doctor1 = Doctor("دکتر محمدی", "جراحی")
doctor2 = Doctor("دکتر علوی", "داخلی")
hospital.add_doctor(doctor1)
hospital.add_doctor(doctor2)

patient1 = Patient("علی احمدی", "سرماخوردگی")
patient2 = Patient("زهرا میرزایی", "آنفولانزا")
hospital.add_patient(patient1)
hospital.add_patient(patient2)

room1 = Room(101)
room2 = Room(102)
hospital.add_room(room1)
hospital.add_room(room2)

room1.assign_patient(patient1)
room2.assign_patient(patient2)

hospital.get_num_doctors()
hospital.get_num_patients()
hospital.get_num_rooms()

hospital.get_doctors()
hospital.get_patients()
hospital.get_rooms()

room1.discharge_patient()
room2.discharge_patient()

hospital.remove_patient(patient1)
hospital.remove_room(room2)

hospital.get_patients()
hospital.get_rooms()