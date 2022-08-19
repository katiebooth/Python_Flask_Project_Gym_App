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
member10 = Member("Kirsty Black", False, True)

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

class1 = GymClass("Yoga", "01/09/2022", 5, 5, premium=False)
class2 = GymClass("HIIT", "02/09/2022", 7, 8, premium=False)
class3 = GymClass("Kettlebells", "03/09/2022", 6, 8, premium=False)
class4 = GymClass("Weightlifting", "04/09/2022", 8, 10, premium=False)
class5 = GymClass("Run Club", "04/09/2022", 3, 20, premium=False)
class6 = GymClass("Yoga", "05/09/2022", 5, 5, premium=False)
class7 = GymClass("HIIT", "06/09/2022", 7, 8, premium=False)
class8 = GymClass("Kettlebells", "07/09/2022", 6, 8, premium=False)
class9 = GymClass("Weightlifting", "07/09/2022", 8, 10, premium=False)
class10 = GymClass("Run Club", "08/09/2022", 3, 20, premium=False)

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








