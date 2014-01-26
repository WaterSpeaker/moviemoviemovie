import codecs 
import sys 
import re 
  
filename = "movie_lens.csv"
count_line = 0
voc_user = set() #number of user 
voc_movie = set() #number of movie

#change by Chen strat
std_sum = 0 
sta_dev = 0
#change by Chen end

oldest_movie_year = None
latest_movie_year = None

rate_sum = 0 # NOTE: sum is a Reserved word. you cannot use it as variable name 
  
with codecs.open(filename,"rt") as my_file: 
    for line in my_file: 
        userid, movie, rate = line.split('|') 
          
        count_line += 1 # count movie number 
  
        rate_sum += int(rate) # your method is right. just a naming problem
        std_sum += int(rate)*int(rate)
        for word in userid.strip().split(): 
            voc_user.add(word) 
  
        for word in movie.strip().split(): 
            voc_movie.add(word) 
          
        years = re.findall(r'\(\d{4}\)$', movie) # find data of year 
        movie = re.sub(r'\(\d{4}\)$', '',movie).strip() # delete year from name 

        for year in years: # travel in list of years and keep the last element 
            year = year.strip('()') # cut the year as number 

        # oldest movie and year 
        if oldest_movie_year == None or int(year) < oldest_movie_year: # compare year 
            oldest_movie_year = int(year) 
            oldest_movie_name = movie 

        # latest 
        if latest_movie_year == None or int(year) > latest_movie_year: # compare year 
            latest_movie_year = int(year) 
            latest_movie_name = movie 
                
    averange_rate = rate_sum / count_line # calculate averange rate)
    sta_dev = ( (std_sum + count_line*averange_rate*averange_rate -2*averange_rate*rate_sum) /count_line) ** 0.5

    #change by Chen start
    for line in my_file:
        std_sum += (int(rate) - averange_rate)**2
        print ( std_sum )
    sta_dev = ( std_sum / count_line )**0.5
    #change by Chen end
        
    # print results 
    print ('movie number is:') # line number is the number of movies 
    print (count_line) 
    print ('\n')

    print ("user number:" + len(voc_user))      

    print ('oldest movie is:') # oldest movie and the name 
    print (oldest_movie_name) 
    print (' in ') 
    print (oldest_movie_year) 
    print ('\n') 
  
    print ('averange rage is:') # averange rate 
    print (averange_rate) 
    print ('\n') 

    print ('rate standard deviation is:') # averange rate 
    print (sta_dev) 
    print ('\n') 
  
