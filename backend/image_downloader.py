from bing_image_downloader import downloader

male_celebrities = [
    'Leonardo DiCaprio', 'Brad Pitt', 'Tom Hanks', 'Johnny Depp', 'George Clooney',
    'Robert Downey Jr.', 'Denzel Washington', 'Will Smith', 'Chris Hemsworth', 'Ryan Reynolds',
    'Shah Rukh Khan', 'Salman Khan', 'Amitabh Bachchan', 'Ranbir Kapoor', 'Hrithik Roshan',
    'Akshay Kumar', 'Aamir Khan', 'Varun Dhawan', 'Ranveer Singh', 'Shahid Kapoor',
    'Christian Bale', 'Matt Damon', 'Dwayne Johnson', 'Hugh Jackman', 'Vin Diesel',
    'Chris Evans', 'Mark Wahlberg', 'Keanu Reeves', 'Tom Cruise', 'Daniel Craig',
    'Jake Gyllenhaal', 'Michael B. Jordan', 'Joaquin Phoenix', 'Chris Pratt', 'Eddie Redmayne',
    'Idris Elba', 'Ryan Gosling', 'Ben Affleck', 'Jared Leto', 'Kit Harington',
    'Zac Efron', 'Chris Pine', 'Jamie Foxx', 'Mahesh Babu', 'Prabhas',
    'Ajay Devgn', 'John Abraham', 'Shahid Afridi', 'Fawad Khan', 'Siddharth Malhotra',
    'Adam Driver', 'Daniel Radcliffe', 'Seth Rogen', 'Bradley Cooper', 'Robert Pattinson',
    'Tobey Maguire', 'Orlando Bloom', 'James Franco', 'Channing Tatum', 'Liam Hemsworth',
    'Jason Momoa', 'Rami Malek', 'Russell Crowe', 'Jim Carrey', 'Ben Stiller',
    'Colin Farrell', 'Shia LaBeouf', 'Joseph Gordon-Levitt', 'Jeremy Renner', 'Tom Hardy',
    'Hugh Grant', 'Owen Wilson', 'James McAvoy', 'Gerard Butler', 'Jamie Dornan',
    'Michael Fassbender', 'Andrew Garfield', 'Jon Hamm', 'Chris Rock', 'Daniel Kaluuya',
    'Eddie Murphy', 'Steve Carell', 'Ben Kingsley', 'Denzel Curry', 'Jesse Eisenberg',
    'Paul Rudd', 'Seth MacFarlane', 'Aziz Ansari', 'Donald Glover', 'Jake Johnson',
    'Martin Freeman', 'John Krasinski', 'Jason Bateman', 'Dev Patel', 'Adrien Brody',
    'Adam Sandler', 'Casey Affleck', 'Charlie Hunnam', 'Dave Franco', 'Edward Norton'
]

female_celebrities = [
    'Angelina Jolie', 'Jennifer Lawrence', 'Scarlett Johansson', 'Meryl Streep', 'Nicole Kidman',
    'Julia Roberts', 'Natalie Portman', 'Charlize Theron', 'Emma Stone', 'Sandra Bullock',
    'Deepika Padukone', 'Priyanka Chopra', 'Alia Bhatt', 'Kareena Kapoor Khan', 'Aishwarya Rai Bachchan',
    'Kangana Ranaut', 'Anushka Sharma', 'Katrina Kaif', 'Sonam Kapoor', 'Gal Gadot',
    'Anne Hathaway', 'Cate Blanchett', 'Margot Robbie', 'Emma Watson', 'Jennifer Aniston',
    'Reese Witherspoon', 'Kristen Stewart', 'Cameron Diaz', 'Mila Kunis', 'Rachel McAdams',
    'Keira Knightley', 'Blake Lively', 'Halle Berry', 'Jessica Chastain', 'Emily Blunt',
    'Saoirse Ronan', 'Viola Davis', 'Emma Thompson', 'Lupita Nyong\'o', 'Salma Hayek',
    'Emily Ratajkowski', 'Kate Winslet', 'Naomi Watts', 'Gwyneth Paltrow', 'Brie Larson',
    'Penélope Cruz', 'Zoe Saldana', 'Alicia Vikander', 'Julianne Moore', 'Olivia Wilde',
    'Jessica Biel', 'Eva Green', 'Milla Jovovich', 'Emilia Clarke', 'Jessica Alba',
    'Amber Heard', 'Jennifer Garner', 'Amanda Seyfried', 'Rachel Weisz', 'Diane Kruger',
    'Lily Collins', 'Sarah Jessica Parker', 'Liv Tyler', 'Naomi Campbell', 'Jessica Lange',
    'Natalie Dormer', 'Carey Mulligan', 'Emma Roberts', 'Chloe Grace Moretz', 'Dakota Johnson',
    'Hailee Steinfeld', 'Rooney Mara', 'Lily James', 'Rose Byrne', 'Michelle Rodriguez',
    'Shailene Woodley', 'Dakota Fanning', 'Rachel Bilson', 'Julia Stiles', 'Isla Fisher',
    'Kristen Bell', 'Amanda Bynes', 'Drew Barrymore', 'Winona Ryder', 'Sarah Michelle Gellar',
    'Christina Ricci', 'Kirsten Dunst', 'Jessica Simpson', 'Hilary Duff', 'Scarlett Johansson',
    'Jennifer Love Hewitt', 'Alicia Silverstone', 'Ashley Judd', 'Angelina Jolie'
]

# Combine both lists into one
celebrities = male_celebrities + female_celebrities

for i in celebrities:

    query = i + ' face frontal shot'
    downloader.download(query, limit=1,  output_dir='static/images', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)