from concert_methods import (
    get_band_for_concert, get_venue_for_concert, get_concerts_for_venue, 
    get_bands_for_venue, is_hometown_show, get_introduction, 
    play_in_venue, get_all_introductions, get_most_performances, 
    get_concert_on_date, get_most_frequent_band
)


print(get_band_for_concert(1))  
print(get_venue_for_concert(1))  
print(get_concerts_for_venue(1))  
print(get_bands_for_venue(1))  
print(is_hometown_show(1))  
print(get_introduction(1))  
play_in_venue('Band A', 'Venue 1', '2024-09-15')  
print(get_all_introductions('Band A'))  
print(get_most_performances())  
print(get_concert_on_date('Venue 1', '2024-09-15'))  
print(get_most_frequent_band('Venue 1'))  
