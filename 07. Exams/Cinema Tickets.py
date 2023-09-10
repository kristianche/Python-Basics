standard_count = 0
kid_count = 0
student_count = 0
type_of_ticket = 0
total_tickets = 0
seats = 1
while seats != total_tickets:
      movie_name = input()
      if movie_name == "Finish":
         break
      seats = int(input())
      type_of_ticket = input()
      total_tickets += 1
      while type_of_ticket != "End":
          type_of_ticket = input()
          total_tickets += 1
          if type_of_ticket == "kid":
              kid_count += 1
          elif type_of_ticket == "standard":
              standard_count += 1
          elif type_of_ticket == "student":
              student_count += 1




