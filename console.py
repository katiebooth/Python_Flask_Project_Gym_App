from models.gym_class import GymClass
from models.member import Member
from models.booking import Booking
import repositories.class_repository as class_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as bookings_repository

member_repository.delete_all()
class_repository.delete_all()
bookings_repository.delete_all()

member1 = Member("Katie Smith", False, True)
member2 = Member("Joe Bloggs", False, True)
member3 = Member("Mike McDonald", False, True)
member4 = Member("Sarah Jones", False, True)
member5 = Member("Will Brown", False, True)
member6 = Member("Hannah Green", False, True)
member7 = Member("Sam Whitehouse", False, True)
member8 = Member("Liz King", False, True)
member9 = Member("Tom Johnson", False, True)
member10 = Member("Finn Russel", True, False)
member11 = Member("Greg Laidlaw", True, True)
member12 = Member("Stuart Hogg", False, False)
member13 = Member("Blair Kinghorn", False, False)
member14 = Member("John Barclay", False, True)
member15 = Member("Gaving Hastings", False, True)


member_repository.save(member1)
member_repository.save(member2)
member_repository.save(member3)
member_repository.save(member4)
member_repository.save(member5)
member_repository.save(member6)
member_repository.save(member7)
member_repository.save(member8)
member_repository.save(member9)
member_repository.save(member10)
member_repository.save(member11)
member_repository.save(member12)
member_repository.save(member13)
member_repository.save(member14)
member_repository.save(member15)

class1 = GymClass("Yoga", "09/01/2022", "10:00", 5, 5, False)
class2 = GymClass("HIIT", "09/02/2022","12:00", 7, 8, True)
class3 = GymClass("Kettlebells", "09/03/2022","17:00", 6, 8, False)
class4 = GymClass("Weightlifting", "09/03/2022","18:00", 8, 10, False)
class5 = GymClass("Run Club", "09/04/2022", "19:00", 3, 20, False)
class6 = GymClass("Yoga", "09/05/2022","21:00", 5, 5, False)
class7 = GymClass("HIIT", "09/06/2022","15:00", 7, 8, True)
class8 = GymClass("Kettlebells", "09/06/2022","12:00", 6, 8, False)
class9 = GymClass("Weightlifting", "09/07/2022","09:00", 8, 10, False)
class10 = GymClass("Run Club", "09/08/2022","17:00", 3, 20, False)

class_repository.save(class1)
class_repository.save(class2)
class_repository.save(class3)
class_repository.save(class4)
class_repository.save(class5)
class_repository.save(class6)
class_repository.save(class7)
class_repository.save(class8)
class_repository.save(class9)
class_repository.save(class10)

booking1 = Booking(member1, class1)
booking2 = Booking(member1, class2)
booking3 = Booking(member2, class1)
booking4 = Booking(member2, class5)
booking5 = Booking(member3, class1)
booking6 = Booking(member4, class2)
booking7 = Booking(member5, class4)
booking8 = Booking(member5, class5)
booking9 = Booking(member6, class2)
booking10 = Booking(member7, class3)
booking11 = Booking(member8, class6)

bookings_repository.save(booking1)
bookings_repository.save(booking2)
bookings_repository.save(booking3)
bookings_repository.save(booking4)
bookings_repository.save(booking5)
bookings_repository.save(booking6)
bookings_repository.save(booking7)
bookings_repository.save(booking8)
bookings_repository.save(booking9)
bookings_repository.save(booking10)
bookings_repository.save(booking11)

print(member_repository.select_all())
print(class_repository.select_all())
print(member_repository.select(member1.id))
print(class_repository.select(class1.id))









