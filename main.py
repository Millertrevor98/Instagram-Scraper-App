'''import these 3 modules through pip for this to run'''
import requests
from bs4 import BeautifulSoup
import tkinter as tk

'''creates the function of username and targets throught the url'''
def get_followers(username):
    url = 'https://www.instagram.com/' + username
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    try:
        follower_count = soup.find('meta', property='og:description')['content']
        follower_count = follower_count.split()[0]
        return follower_count
    except:
        return 'Error'

def display_followers():
    username = username_entry.get()
    followers = get_followers(username)
    followers_label.configure(text=followers)

'''tkinter window pop up'''
window = tk.Tk()
window.title('Instagram Follower Count')

username_label = tk.Label(window, text='Enter Instagram Username:')
username_label.pack()

username_entry = tk.Entry(window)
username_entry.pack()

'''targets follower count of an instagram account'''
get_followers_button = tk.Button(window, text='Get Followers', command=display_followers)
get_followers_button.pack()

followers_label = tk.Label(window, text='')
followers_label.pack()

window.mainloop()
