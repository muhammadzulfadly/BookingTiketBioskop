# Step 1: Define the available movies
movies = {
    1: "The Matrix Resurrections",
    2: "Spider-Man: No Way Home",
    3: "Encanto",
    4: "Dune"
}

# Step 2: Define the available showtimes for each movie
showtimes = {
    1: ["12:00", "15:00", "18:00", "21:00"],
    2: ["10:00", "13:00", "16:00", "19:00"],
    3: ["11:00", "14:00", "17:00", "20:00"],
    4: ["12:30", "15:30", "18:30", "21:30"]
}

# Step 3: Define the seating layout (rows and columns)
seating = {
    'A': [1, 2, 3, 4, 5],
    'B': [1, 2, 3, 4, 5],
    'C': [1, 2, 3, 4, 5],
    'D': [1, 2, 3, 4, 5]
}

# Step 4: Function to display movies


def display_movies():
    print("Available Movies:")
    for key, movie in movies.items():
        print(f"{key}. {movie}")

# Step 5: Function to display showtimes for selected movie


def display_showtimes(movie_id):
    print(f"\nShowtimes for {movies[movie_id]}:")
    for idx, time in enumerate(showtimes[movie_id], 1):
        print(f"{idx}. {time}")

# Step 6: Function to display seating layout


def display_seating():
    print("\nAvailable Seats:")
    for row, seats in seating.items():
        print(f"{row}: {['X' if s == 'booked' else s for s in seats]}")

# Step 7: Function to book a seat


def book_seat(row, seat_num):
    if seating[row][seat_num - 1] != 'booked':
        seating[row][seat_num - 1] = 'booked'
        return True
    else:
        print("Seat is already booked. Please choose another.")
        return False

# Step 8: Function to simulate payment process


def process_payment(total_amount):
    print(f"\nTotal amount to pay: ${total_amount}")
    payment = input("Proceed with payment? (yes/no): ")
    if payment.lower() == 'yes':
        print("Payment successful! Your booking is confirmed.")
    else:
        print("Payment failed. Please try again.")

# Step 9: Main function for booking process


def book_ticket():
    display_movies()
    movie_id = int(input("\nSelect a movie (enter movie number): "))

    if movie_id in movies:
        display_showtimes(movie_id)
        showtime_choice = int(input("\nSelect a showtime (enter number): "))

        if showtime_choice in range(1, len(showtimes[movie_id]) + 1):
            selected_time = showtimes[movie_id][showtime_choice - 1]
            print(f"\nYou selected {movies[movie_id]} at {selected_time}.")

            display_seating()
            row = input("\nSelect a row (A-D): ").upper()
            seat_num = int(input("Select a seat number (1-5): "))

            if row in seating and 1 <= seat_num <= 5:
                if book_seat(row, seat_num):
                    total_amount = 10  # Example ticket price
                    print(f"\nSeat {row}{seat_num} booked successfully.")
                    process_payment(total_amount)
                else:
                    print("Booking failed.")
            else:
                print("Invalid seat selection.")
        else:
            print("Invalid showtime selection.")
    else:
        print("Invalid movie selection.")


# Running the booking system
book_ticket()
